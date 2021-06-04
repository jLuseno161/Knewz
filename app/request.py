import urllib.request
import json
from .models import News

api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    # '''

    return

def process_results():
    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''

    return
