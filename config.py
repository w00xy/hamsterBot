import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# getting from .env file
TOKEN = os.getenv('TOKEN')
BOT_LINK = os.getenv('BOT_LINK')
SITE_URL = os.getenv('SITE_URL')
