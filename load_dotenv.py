import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
DEBUG = os.getenv('DEBUG')
DB_URI=os.getenv('DB_URI')