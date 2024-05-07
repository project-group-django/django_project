SECRET_KEY = 'your_secret_key_here'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mydatabase',  # Название вашей базы данных MongoDB
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://lapik.wot:lapa@cluster0.76q9wp8.mongodb.net:27017/Personal_Assistant',
            # Укажите ваши реальные данные для подключения к MongoDB
        }
    }
}
