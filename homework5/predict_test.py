#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://192.168.50.162:9696/predict'

# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()
print(response)
