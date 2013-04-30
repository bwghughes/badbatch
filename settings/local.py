from .base import *

DATABASE = {
    'name': 'badbatch',
    'engine': 'peewee.PostgresqlDatabase',
    'host': '127.0.0.1',
    'user': 'ben'
}
SECRET_KEY = 'devkey'
RECAPTCHA_PUBLIC_KEY = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'