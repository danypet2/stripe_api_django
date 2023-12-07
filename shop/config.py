from dotenv import load_dotenv
import os
load_dotenv()
HOST = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
NAME = os.environ.get('DB_NAME')





STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_TEST_MODE = os.environ.get('STRIPE_TEST_MODE')