#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import base64

email = input('Email: ')
password = input('Password: ')

s = requests.Session()
login = BeautifulSoup(s.get('https://www.hackerschool.com/login').text)
authenticity_token = login.find('input', attrs={"name": "authenticity_token"})['value']
s.post('https://www.hackerschool.com/sessions', {'utf8': '\xe2\x9c\x93',
    'authenticity_token': authenticity_token, 'email': email, 'password': password})
soup = BeautifulSoup(s.get('https://www.hackerschool.com/people').text)
batch = soup.find(id='batch9')

emails = []

links = batch.find_all('a')
start_index = len('mailto:')
for link in links:
    if link.get('href').find('mailto:') != -1:
        email = link.get('href')[start_index:]
        if email.find('@hackerschool.com') == -1:
            emails.append(email)
                

with open('emails.txt', 'w') as f: 
    for email in emails: 
        f.write(email + '\n')


