import random
import secrets
import requests

from string import ascii_lowercase, ascii_letters, digits
from configparser import ConfigParser


def get_config_data(path='bot_settings.ini'):
    config = ConfigParser()
    config.read(path)
    return {
        'number_of_users': config.get("Settings", "number_of_users"),
        'max_posts_per_user': config.get("Settings", "max_posts_per_user"),
        'max_likes_per_user': config.get("Settings", "max_likes_per_user"),
    }


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for _ in range(length))


def generate_users_data(nb, domains, letters, length=10):
    alphabet = ascii_letters + digits
    data_list = []
    for num in range(nb):
        data_list.append({
            'email': f'{get_random_name(letters, length)}@{get_random_domain(domains)}',
            'password': ''.join(secrets.choice(alphabet) for _ in range(length)),
        })
    return data_list


def create_users(users_data):
    for user in users_data:
        response = requests.post('http://127.0.0.1:8000/users/create/',
                                 json=user)
        print('Create user:', response.status_code,
              response.reason, response.json())


def login_users(users_data):
    user_token_list = []
    for user in users_data:
        response = requests.post('http://127.0.0.1:8000/users/login/',
                                 json=user)
        json_response = response.json()
        user_token_list.append(json_response.get('token'))
    return user_token_list


def create_posts(users_token_list, max_posts_per_user, letters):
    post_ids = []
    for token in users_token_list:
        header = {
            'Authorization': f'Bearer {token}'
        }
        max_posts = random.choice([x for x in range(1, max_posts_per_user)])
        for i in range(max_posts):
            data = {"post_body": get_random_name(letters, 30)}
            response = requests.post('http://127.0.0.1:8000/posts/create/',
                                     json=data, headers=header)
            json_response = response.json()
            print('Create post:', response.status_code,
                  response.reason, json_response)
            post_ids.append(json_response.get('id'))
    return post_ids


def like_posts(users_token_list, post_ids, max_likes_per_user):
    for token in users_token_list:
        header = {
            'Authorization': f'Bearer {token}'
        }
        max_likes = random.choice([x for x in range(1, max_likes_per_user)])
        for i in range(max_likes):
            random_post = random.choice(post_ids)
            response = requests.get(
                f'http://127.0.0.1:8000/posts/like/{random_post}/',
                headers=header
            )
            print('Like:', f'post_id: {random_post}', response.text)


def main():
    domains = ["hotmail.com", "gmail.com", "i.ua", "mail.com", "yahoo.com"]
    letters = ascii_lowercase
    config_data = get_config_data()
    number_of_users = int(config_data.get('number_of_users'))
    max_posts_per_user = int(config_data.get('max_posts_per_user'))
    max_likes_per_user = int(config_data.get('max_likes_per_user'))
    users_data = generate_users_data(number_of_users, domains, letters)
    create_users(users_data)
    users_token_list = login_users(users_data)
    post_ids = create_posts(users_token_list, max_posts_per_user, letters)
    like_posts(users_token_list, post_ids, max_likes_per_user)


if __name__ == "__main__":
    main()
