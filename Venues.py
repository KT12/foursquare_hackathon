import json
from watson_developer_cloud import ToneAnalyzerV3
import requests

# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# END of python-dotenv section

from watson_scoring import calc_concepts


class Venues:
    def __init__(self, venue_id, category=''):
        self.venue_id = venue_id
        #self.category = category
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.foursq_client = os.environ.get("FOURSQUARE_CLIENT_ID")
        self.foursq_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")
        self.foursquare_oauth_token = os.environ.get("FOURSQUARE_OAUTH_TOKEN")
        
    def analyize_venue(self):
        self.get_venue_data(False)
        self.get_list_of_tips()
        r = self.return_concepts()
        return r

    def get_venue_data(self, from_file=True):

         # take venue id and get a a response of all the tips
        if from_file ==True:
            with open('venue_data.json','r') as f:
                results = json.load(f)
        else:
            url = "https://api.foursquare.com/v2/venues/{}/tips?sort=recent&client_id={}&client_secret={}&v=20170513".format(self.venue_id,self.foursq_client, self.foursq_secret)
            results = requests.get(url).json()

        self.venue_data = results


    def get_list_of_tips(self):
        response = self.venue_data['response']
        response = response['tips']
        response = response['items']

        self.list_of_responses = []
        for item in response:
            tip = item['text']
            self.list_of_responses.append(tip)

        return self.list_of_responses

    def return_concepts(self):
        concat_tips = ' '.join(self.list_of_responses)
        concepts = calc_concepts(concat_tips)
        return concepts

if __name__ == '__main__':
    T = Venues('40a55d80f964a52020f31ee3')
    c = T.analyize_venue()
