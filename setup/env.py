import os

os.environ['SECRET_KEY'] = 'your project secret key'
os.environ['DEBUG'] = '1' # if '' is False, else is True
os.environ['ALLOWED_HOSTS'] = f'["127.0.0.1", "localhost"]'
os.environ['USE_SQLITE'] = '1' # if '' is False, else is True
os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'
os.environ['AUTHOR'] = 'your name or email'

# aws keys
os.environ['AWS_ACCESS_KEY_ID'] = f'*******'
os.environ['AWS_SECRET_ACCESS_KEY'] = '*******'
os.environ['AWS_STORAGE_BUCKET_NAME'] = 'your bucket name'
os.environ['USE_S3'] = '' # if '' is False, else is True

# aws parameters to save files
os.environ['AWS_STATIC_LOCATION'] = 'static'
os.environ['STATICFILES_STORAGE'] = 'setup.storage_backends.StaticStorage'

os.environ['AWS_PUBLIC_MEDIA_LOCATION'] = 'media/public'
os.environ['DEFAULT_FILE_STORAGE'] = 'setup.storage_backends.PublicMediaStorage'

os.environ['AWS_PRIVATE_MEDIA_LOCATION'] = 'media/private'
os.environ['PRIVATE_FILE_STORAGE'] = 'setup.storage_backends.PrivateMediaStorage'
