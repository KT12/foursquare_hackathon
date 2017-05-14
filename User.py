####
# Python3
# class to create vector of words

# -*- coding: utf-8 -*-
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

        #twitterDataFile.write(simplejson.dumps(simplejson.loads(output), indent=4, sort_keys=True))


    def get_venue_history(self, download=True):
        # Set the API request url
        url="https://api.foursquare.com/v2/users/self/venuehistory?oauth_token={}&v=20161016".format(self.foursquare_oauth_token)
        results = requests.get(url).json()["response"]['venues']
        if download==True:
            with open('four_square_'+self.userid+'.txt', 'w') as f:
                f.write(json.dumps(results, indent=2))
        print(results)

    def keep_only_this_category(self):
        pass

    def get_all_categories(self):
                # define URL for categories
        url = "https://api.foursquare.com/v2/venues/categories?client_id={}&client_secret={}&v={}".format(self.foursq_client, self.foursq_secret, 20170513)

        # send call request and get categories
        results = requests.get(url).json()
        categories = results["response"]["categories"]

        with open('categories_data.txt','w') as f:
            f.write(json.dumps(categories, indent=2))

        #with open('categories_data.txt') as f:
        #    categories = json.load(f)

        #return categories

        self.set_of_food_cats = set()
        for cat in categories:
            
            #print(cat[0])
            #print(cat['name'])
            if cat['name'] == 'Food':
                #return(cat)
                for subcat in cat['categories']:
                    #print(subcat)
                    #return(subcat)
                    #print('adding:{}'.format(subcat['id']))
                    self.set_of_food_cats.add(subcat['id'])

        print(self.set_of_food_cats)
        return(self.set_of_food_cats)

    def list_all_cat_visits(self, category):
        pass





if __name__ == '__main__':
    Test = Users('a')
    Test.get_all_categories()
    #Test.get_venue_history()
