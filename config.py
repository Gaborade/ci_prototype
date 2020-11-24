import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    START_NGROK = os.environ.get('START_NGROK') is not None and \
    os.environ.get('WERKZEUG_RUN_MAIN') != 'true'

