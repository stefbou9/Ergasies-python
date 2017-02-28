#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
from tweepy import OAuthHandler
consumer_key = 'rpJCHW14GqdEGEEKGcxHi1sJf'
consumer_secret = 'udluTBT7HPQOv6aarhAm1J0sy2EEBNVHt1kekYlIsVR62rJPbA'
access_token = '4593369735-HTF8ErW5yP2Oo7i9wDZvNnKhaVUHFxZchRqLAqV'
access_secret = '4bHBSgRLKfnWTUPNo85H4Z9lbi7FW0rUkMGKOHtQZlcp4'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
print "Dwse to prwto onoma xrhsth"
xrhsths1=raw_input()
print "Dwse to deutero onoma xrhsth"
xrhsths2=raw_input()
fids1=api.followers_ids(xrhsths1)
fids2=api.followers_ids(xrhsths2)
megethos1=len(fids1)
megethos2=len(fids2)
p=0
for i in range(0,megethos1):
    for j in range(0,megethos2):
        if fids1[i]==fids2[j]:
            p=p+1
            s=api.get_user(fids1[i])
            print p, ".", s.screen_name
