from configparser import ConfigParser


def get_config_data(path='bot_settings.ini'):
    config = ConfigParser()
    config.read(path)
    return {
        'number_of_users': config.get("Settings", "number_of_users"),
        'max_posts_per_user': config.get("Settings", "max_posts_per_user"),
        'max_likes_per_user': config.get("Settings", "max_likes_per_user"),
    }
