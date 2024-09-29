import os
from dotenv import load_dotenv
from django.conf import settings

BASE_DIR = settings.BASE_DIR
load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'env', 'id'))

SECRET_KEY = os.getenv('SECRET_KEY')