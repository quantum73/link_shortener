import random
import string

from flask import current_app

SYMBOLS = string.ascii_letters + string.digits


def id_generator(size: int = 12) -> str:
    return ''.join(random.choice(SYMBOLS) for _ in range(size))


def get_base_url() -> str:
    host = current_app.config.get('HOST')
    port = current_app.config.get('PORT')
    if port == 443:
        base_url = 'https://{}'.format(host)
    elif port == 80:
        base_url = 'http://{}'.format(host)
    else:
        base_url = 'http://{}:{}'.format(host, port)
    return base_url
