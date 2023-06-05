#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

r = requests.get('https://proxyway.com/reviews')

print(r)

print(r.content)


# In[3]:


import requests

r = requests.get('https://proxyway.com/reviews')

print(r.url)

print(r.status_code)


# In[4]:


import requests
from bs4 import BeautifulSoup

r = requests.get('https://proxyway.com/reviews')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)


# In[19]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://proxyway.com/reviews')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='grid')
content = s.find_all('p')

print(content)


# In[22]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://proxyway.com/reviews')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Finding by id
s = soup.find('div', id= 'main')

# Getting the leftbar
leftbar = s.find('row', class_='archive-list')

# All the li under the above ul
content = leftbar.find_all('row')

print(content)


# In[16]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')

lines = s.find_all('p')

for line in lines:
    print(line.text)


# In[29]:


import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://proxyway.com/reviews'

titles_list = []
title_page9 = []

for page in range(1,10):
    req = requests.get(URL + str(page) + '/')
    soup  = bs(req.text, 'html.parser')
    
    titles = soup.find_all('h3', attrs={'class', 'archive-list__title'})
    
    count = 1
    for title in titles:
        d = {}
        d['Page Number'] = f'page {page}'
        d['Title Number'] = f'Title {count}'
        d['Title Name'] = title.text
        count += 1
        titles_list.append(d)
    if page == 9 :
        count = 1
        for title in titles:
            e = {}
            e['Page Number'] = f'Page {page}'
            e['Title Number'] = f'Title {count}'
            e['Title Name'] = title.text
            count += 1
            title_page9.append(e)
            
titles_all = titles_list + title_page9

filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Page Number', 'Title Number', 'Title Name'])
    w.writeheader()
    
    w.writerows(titles_all)


# In[35]:


import csv
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

data = []

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")
        data.append({
            'Page Number': f'Page {page}',
            'Title Number': f'Title {i+1}',
            'Title Name': title.text
        })

# Menyimpan data ke dalam file CSV
filename = 'proxywaydata.csv'
fieldnames = ['Page Number', 'Title Number', 'Title Name']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data telah disimpan ke dalam file", filename)


# In[ ]:




