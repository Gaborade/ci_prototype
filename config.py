import os

class Config:
    START_NGROK = os.environ.get('START_NGROK', default=True)