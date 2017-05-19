import json
from dotenv import load_dotenv
from os.path import join, dirname
import os
import requests
import pandas as pd
import numpy as np
from collections import Counter
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features

load_dotenv('.env') 

# Get credentials

username=os.environ.get('NLU_USERNAME')
password = os.environ.get('NLU_PASSWORD')

foursquare_client_id=os.environ.get('FOURSQUARE_CLIENT_ID')
foursquare_client_secret=os.environ.get('FOURSQUARE_CLIENT_SECRET')

# VERSION = "20170511"
# LIMIT = 30
# radius = 1000

def pull_foursquare_json(venue_id):
    VERSION = "20170511"
    foursquare_client_id=os.environ.get('FOURSQUARE_CLIENT_ID')
    foursquare_client_secret=os.environ.get('FOURSQUARE_CLIENT_SECRET')
    url="https://api.foursquare.com/v2/venues/{}/tips?client_id={}&client_secret={}&v={}&limit=150".format(venue_id, foursquare_client_id, foursquare_client_secret, VERSION)
    json_f = requests.get(url).json()
    return json_f

# Helper function to return list of tips from restaurant's JSON file
def tips_list(json_file):
    try:
        num_tips = json_file['response']['tips']['count']
        return [json_file['response']['tips']['items'][k]['text'] for k in range(num_tips)]
    except:
        return [""]

def combine_u_prefs(u1_dict, u2_dict, k):
    u1_counter = Counter(u1_dict)
    u2_counter = Counter(u2_dict)
    u_prefs = u1_counter + u2_counter
    # Pull k highest values
    u_prefs_top = dict(u_prefs.most_common(k))
    vallist = [val for val in u_prefs_top.values()]
    factor = np.median(vallist)
    normed_val = [val/factor for val in vallist]
    topic_idx = [key for key in u_prefs_top.keys()]
    pref_vec = pd.Series(data=normed_val, index=topic_idx)
    return pref_vec, topic_idx

def construct_matrix(venue_ids, topic_idx):
    empty_matrix = pd.DataFrame(index=venue_ids, columns=topic_idx)
    return empty_matrix

def sentiment(tips):
    # Helper function to return text sentiment analysis
    # Load Watson credentials
    username=os.environ.get('NLU_USERNAME')
    password = os.environ.get('NLU_PASSWORD')
    nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-02-27',
        username=username, password=password)
    output = nlu.analyze(text=tips, features=[features.Sentiment()])
    return output['sentiment']['document']['score']

def fill_sentiment_matrix(mat):
    for j in range(mat.shape[0]):
        venue_id = mat.index[j]
        json_f = pull_foursquare_json(venue_id)
        tips = tips_list(json_f)
        for k in range(mat.shape[1]):
            topic = mat.columns[k]
            score = np.median([sentiment(tip) for tip in tips if topic in tip])
            mat.loc[venue_id, topic] = score
    return mat.fillna(0)

def recommend(score_mat, user_vec, venues_ids, top_n):
    score_vec = pd.Series(np.dot(score_mat, user_vec), index=venues_ids)
    return score_vec.sort_values(ascending=False)[:top_n].index.values

