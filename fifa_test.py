# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 00:33:43 2018

@author: HP
"""
from __future__ import unicode_literals
"""
add your keys here <twitter API>
"""
#users = api.GetFriends()

#print([u.screen_name for u in users])
import pandas as pd
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
tweet_list = []
location_list = []
time_stamp_list=[]
class listener(StreamListener):
    
    def on_data(self, data):
        #print(data)
        tweet = data.split(',"text":"')[1].split('source')[0]
        print(tweet)
        #tweet_list.append(tweet)
        #location = data.split(',"location":')[1].split('url')[0]
        #location_list.append(location)
        #time_stamp=data.split(',"timestamp_ms:"')[1]
        #time_stamp_list.append(time_stamp)
        #x={'tweet':tweet_list,'location':location_list,'time_stamp':time_stamp_list}
        #print(time_stamp)
        #X = pd.DataFrame(x)
        #df.to_csv('C:/Users/HP/OneDrive/Python_Tut/FIFA_sentimap/df_tweet_location.csv')
        """
        saveFile = open('data_tweet_location.csv','a')
        saveFile.write(tweet)
        saveFile.write('\t')
        saveFile.write(location)
        saveFile.write('\n')
        saveFile.close()
        """
        return(True)
    
    def on_error(self, status):
        print(status)
#if _name__=="__main__":
auth=OAuthHandler(c_key,c_secret)
auth.set_access_token(a_key,a_secret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["#ENGCRO"])
#print(listener.df)
