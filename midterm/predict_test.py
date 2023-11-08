#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://192.168.0.152:9696/predict'

client = {"WineRating": "4.0", "RegionalVariety": "Riesling", "Winery": "Trimbach" , "Year": "2020"}
response = requests.post(url, json=client)
print(response)
print(response.json())
