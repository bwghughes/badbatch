import os
from os import path
import json

from .base import *

if path.exists('/home/dotcloud/environment.json'):
    with open('/home/dotcloud/environment.json') as f:
        env = json.load(f)

DATABASE={
    'name': 'badbatch',
    'user': env['DOTCLOUD_DB_SQL_LOGIN'],
    'password': env['DOTCLOUD_DB_SQL_PASSWORD'],
    'engine': 'peewee.PostgresqlDatabase',
    'host': env['DOTCLOUD_DB_SQL_HOST'],
    'port': env['DOTCLOUD_DB_SQL_PORT'],
}
SECRET_KEY = 'devkey'
RECAPTCHA_PUBLIC_KEY = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'