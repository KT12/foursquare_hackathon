####
# Python3
# class to create vector of words

# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import ToneAnalyzerV3


# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# END of python-dotenv section


tone_analyzer = ToneAnalyzerV3(
   username=os.environ.get("TONE_USERNAME"),
   password=os.environ.get("TONE_PASSWORD"),
   version='2016-05-19')

#191252
#https://api.foursquare.com/v2/users/191252/venuehistory?v=20170513&client_id=EIRSNTE1TNTRTTX51TOBCDMCPIXQ3CVXK3YNXURU5C5TH3BZ&client_secret=EBW0D5N2YEML5CXXYQNNQIONECPG51MRMGXFCVOTKBPHHJRL

#https://api.foursquare.com/v2/users/self/venuehistory?oauth_token=3H1A0NYWAIJ3ZIIPAIC1TVDH5IBL4XLIEX2LG2TJPBIWBM52&v=20170513



class Users:
    def __init__(self, userid):
        self.userid = userid
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.foursq_client = os.environ.get("FOURSQUARE_CLIENT_ID")
        self.foursq_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")
        self.foursquare_oauth_token = os.environ.get("FOURSQUARE_OAUTH_TOKEN")



    def get_venue_history(self):
        # Set the API request url
        url="https://api.foursquare.com/v2/users/self/venuehistory?oauth_token={}&v=20161016".format(self.foursquare_oauth_token)
        results = requests.get(url).json()["response"]['venues']
        print(results)
