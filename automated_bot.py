import random

from string import ascii_lowercase
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
