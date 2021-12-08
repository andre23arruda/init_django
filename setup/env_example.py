import os, json, socket


def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_allowed_hosts():
    '''Create a list of aloowed hosts'''
    hosts = ['127.0.0.1', 'localhost', get_ip_address()]
    return hosts


os.environ['SECRET_KEY'] = 'your project secret key'
os.environ['DEBUG'] = 'true' # Empty string is False, else is True
os.environ['ALLOWED_HOSTS'] = json.dumps(get_allowed_hosts())

## DATABASE
os.environ['USE_SQLITE'] = 'true' # Empty string is False, else is True

## djongo
os.environ['DATABASES'] = '''{
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'db-name',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb+srv://<user>:<password>@cluster0.i33sy.mongodb.net/<db-name>?retryWrites=true&w=majority',
        }
    }
}'''

## postgres
# 'default': {
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'database_name',
#     'USER': 'username',
#     'PASSWORD': 'password',
#     'HOST': 'localhost',
# }

os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'
os.environ['AUTHOR'] = 'your name or email'

# cors
os.environ['CORS_ALLOWED_ORIGINS'] = [
    'http://localhost:3000'
]

# cloudinary
os.environ['USE_CLOUDINARY'] = '' # Empty string is False, else is True
os.environ['CLOUD_NAME'] = 'your_cloud_name'
os.environ['API_KEY'] = 'your_api_key'
os.environ['API_SECRET'] = 'your_api_secret'

# aws keys
os.environ['USE_S3'] = '' # Empty string is False, else is True
os.environ['AWS_ACCESS_KEY_ID'] = f'*******'
os.environ['AWS_SECRET_ACCESS_KEY'] = '*******'
os.environ['AWS_STORAGE_BUCKET_NAME'] = 'your bucket name'

# aws parameters to save files
os.environ['AWS_STATIC_LOCATION'] = 'static'
os.environ['AWS_PUBLIC_MEDIA_LOCATION'] = 'media/public'
os.environ['AWS_PRIVATE_MEDIA_LOCATION'] = 'media/private'
os.environ['STATICFILES_STORAGE'] = 'setup.storage_backends.StaticStorage'
os.environ['DEFAULT_FILE_STORAGE'] = 'setup.storage_backends.PublicMediaStorage'
os.environ['PRIVATE_FILE_STORAGE'] = 'setup.storage_backends.PrivateMediaStorage'
