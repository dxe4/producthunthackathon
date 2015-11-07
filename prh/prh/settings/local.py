from prh.settings.common import *

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Or path to database file if using sqlite3.
        'NAME': 'vagrant',
        # The following settings are not used with sqlite3:
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        # Empty for localhost through domain sockets or
        # '127.0.0.1' for localhost through TCP.
        'HOST': '192.168.33.3',
        # Set to empty string for default.
        'PORT': '',
    }
}
