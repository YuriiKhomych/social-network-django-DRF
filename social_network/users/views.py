from jwt import encode

from .models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler
from django.conf import settings
from django.contrib.auth.signals import user_logged_in


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            try:
                user = User.objects.get(email=email, password=password)
            except User.DoesNotExist:
                user = None
            if user:
                try:
                    payload = jwt_payload_handler(user)
                    token = encode(payload, settings.SECRET_KEY)
                    user_details = {
                        'name': f"{user.first_name} {user.last_name}",
                        'token': token
                    }
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)
                    return Response(user_details, status=status.HTTP_200_OK)

                except Exception as e:
                    raise e
            else:
                res = {
                    'Error': 'Can not authenticate with the given credentials '
                             'or the account has been deactivated'
                }
                return Response(res, status=status.HTTP_403_FORBIDDEN)
        except KeyError:
            res = {'Error': 'please provide a email and a password'}
            return Response(res)


class RetrieveUpdateUserAPI(RetrieveUpdateAPIView):
    """Single user endpoint"""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
