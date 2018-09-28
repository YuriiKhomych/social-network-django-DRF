from pyhunter import PyHunter

hunter = PyHunter('KEY')


def check_email(email):
    try:
        verify_email = hunter.email_verifier(email)
        if verify_email.get('webmail'):
            return True
        return False
    except:
        return False
