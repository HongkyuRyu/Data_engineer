from decouple import config

def get_api_key():
    return config('SECRET_KEY')