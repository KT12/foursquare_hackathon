####
# Python3
# class to create vector of words

# -*- coding: utf-8 -*-
import json
import time
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
from Venues import Venues
from statistics import median, mean


tone_analyzer = ToneAnalyzerV3(
   username=os.environ.get("TONE_USERNAME"),
   password=os.environ.get("TONE_PASSWORD"),
   version='2016-05-19')

#191252
#https://api.foursquare.com/v2/users/191252/venuehistory?v=20170513&client_id=EIRSNTE1TNTRTTX51TOBCDMCPIXQ3CVXK3YNXURU5C5TH3BZ&client_secret=EBW0D5N2YEML5CXXYQNNQIONECPG51MRMGXFCVOTKBPHHJRL

#https://api.foursquare.com/v2/users/self/venuehistory?oauth_token=3H1A0NYWAIJ3ZIIPAIC1TVDH5IBL4XLIEX2LG2TJPBIWBM52&v=20170513



class Users:
    def __init__(self, userid, category):
        self.userid = userid
        self.category = category
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.foursq_client = os.environ.get("FOURSQUARE_CLIENT_ID")
        self.foursq_secret = os.environ.get("FOURSQUARE_CLIENT_SECRET")
        self.foursquare_oauth_token = os.environ.get("FOURSQUARE_OAUTH_TOKEN")
        self.dict_of_subcats = {'Food':set(), 'Nightlife':set()}
        self.list_of_cat_visited = []
        
    def eval_user(self):
        # get the users complete history
        self.get_venue_history()
        # get all main and sub categories from Foursquare
        self.get_all_categories()
        # filter their venue history based on the desired category
        self.list_all_cat_visits()        

    def get_venue_history(self, fromfile=True):
        # hit the api and return a list of venues that a user has visited
        # note this has to be authorized at an user level not with the api key

        if fromfile==True:
            with open('four_square_'+self.userid+'.txt', 'r') as f:
                results = json.load(f)

        else:
            url="https://api.foursquare.com/v2/users/self/venuehistory?oauth_token={}&v=20161016".format   (self.foursquare_oauth_token)
            results = requests.get(url).json()["response"]['venues']


        self.venue_history = results
        

    def keep_only_this_category(self, category):
        # return a list of venueIDs that match one of these categories
        FOOD = '4d4b7105d754a06374d81259'
        NIGHTLIFE = '4d4b7105d754a06376d81259'
        return(list_of_venues)
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
       
        for cat in categories:
            if cat['shortName'] in self.dict_of_subcats.keys():
                #return(cat)
                for subcat in cat['categories']:
                    #return(subcat)
                    #print('adding:{}'.format(subcat['id']))
                    self.dict_of_subcats[cat['shortName']].add(subcat['id'])


    def list_all_cat_visits(self):
    # loop through every venue in history and return a list of only the venue ID where it mataches
    # a subcategory in the main category defined in the class creation


        for venue in self.venue_history['items']:

            if venue['venue']['categories'][0]['id'] in self.dict_of_subcats[self.category]:
                print('here')
                self.list_of_cat_visited.append(venue['venue']['id'])

    def concepts_for_all_relevant_visits(self):
        dict_of_relevant_visits = dict()
        
        for v in self.list_of_cat_visited:
            time.sleep(1.3)
            V = Venues(v)
            c = V.analyize_venue()
            dict_of_relevant_visits[v] = c

        self.dict_of_relevant_visits = dict_of_relevant_visits

        
    def all_concepts(self):
        set_of_all_concepts = set()
        for venue in self.dict_of_relevant_visits:
            for c in self.dict_of_relevant_visits[venue].keys():
                set_of_all_concepts.add(c)
        self.set_of_all_concepts = set_of_all_concepts

    def pool_concepts(self):
        dict_of_pooled = dict()
        for c in self.set_of_all_concepts:
            dict_of_pooled[c] = list()

        for c in dict_of_pooled:
            for venue in self.dict_of_relevant_visits:
                if c in self.dict_of_relevant_visits[venue].keys():
                    dict_of_pooled[c].append(self.dict_of_relevant_visits[venue][c])
                else:
                    dict_of_pooled[c].append(0)
        return dict_of_pooled

    def mean_concepts(self, dict_of_pooled):
        dict_of_mean = dict()
        
        for c in dict_of_pooled:
            
            dict_of_mean[c] = mean(dict_of_pooled[c])
        
        return dict_of_mean
            
                    



if __name__ == '__main__':
    A = Users('a', 'Food')
    A.eval_user()
    A.concepts_for_all_relevant_visits()
    A.all_concepts()
    ra = A.pool_concepts()
    ma = A.mean_concepts(ra)

    Y = Users('y', 'Food')
    Y.eval_user()
    Y.concepts_for_all_relevant_visits()
    Y.all_concepts()
    ry = Y.pool_concepts()
    my = Y.mean_concepts(ry)

    
    #Test.get_venue_history()
