import json

####
# Python3
# class to create vector of words

# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import requests

# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# END of python-dotenv section

def calc_concepts(text_input):
    import watson_developer_cloud.natural_language_understanding.features.v1 as features

    NLU = NaturalLanguageUnderstandingV1(
        username=os.environ.get("NLU_USERNAME"),
        password=os.environ.get("NLU_PASSWORD"),
        version='2016-05-19')

    #features = ['concepts', 'keywords']
    #tips = 'The IBM Watson™ AlchemyLanguage service is a collection of text analysis functions that derive semantic information from your content. You can input text, HTML, or a public URL and leverage sophisticated natural language processing techniques to get a quick high-level understanding of your content and obtain detailed insights such as sentiment for detected entities and keywords. See a video overview of the service here.'
    r = NLU.analyze(text=text_input, features=[features.Concepts()])
    concepts = r['concepts']
    dict_of_concepts = dict()
    for c in concepts:
        dict_of_concepts[c['text']] = c['relevance'] 
    #print(dict_of_concepts)    
    return dict_of_concepts

if __name__ == '__main__':
	pass

