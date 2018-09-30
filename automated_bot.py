import random
import secrets
import requests

from string import ascii_lowercase, ascii_letters, digits
from configparser import ConfigParser

domains = ["hotmail.com", "gmail.com", "i.ua", "mail.com", "yahoo.com"]
letters = ascii_lowercase


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


def generate_users_data(nb, domains, length=10):
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
        if response.status_code != 200:
            json_response = response.json()
            user_token_list.append(json_response['token'])
    return user_token_list
