# -*- coding: utf-8 -*-
import tweepy, json, csv, gspread, re, string, wordlists
import numpy as np
from tweepy import Stream, OAuthHandler
from pythainlp.word_vector import thai2vec
from pythainlp.rank import rank
from sklearn.metrics.pairwise import cosine_similarity
from pythainlp.tokenize import word_tokenize, WhitespaceTokenizer, sent_tokenize
from oauth2client.service_account import ServiceAccountCredentials
from tweepy.streaming import StreamListener
from pythainlp.collation import collation
from pythainlp.sentiment import sentiment


api_key = 'XXX'
api_secret = 'XXX'
access_token = 'XXX'
access_secret = 'XXX'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_persona.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url('XXXX')


# OCEAN_O is Dictionary of mood
# lookup is word from ex-message
def search_emotoins(OCEAN_O, lookup):

    for key, value in OCEAN_O.items():
        for word in value:
            if lookup in word:
                return value
