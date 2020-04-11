# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:04:14 2020

@author: NARAYANA REDDY DATA SCIENTIST
"""
# IMPORT LIBRARIES

import nltk
import urllib
import bs4 as bs
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

# GETTING THE DATA SOURCE
source=urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

# PARSING THE DATA/CREATING BEAUTIFUL SOUP
soup=bs.BeautifulSoup(source,'lxml')

# FETCHING THE DATA
text=""
for paragraph in soup.find_all('p'):
    text+=paragraph.text
    
# PRE PROCESSING DATA
text=re.sub(r'\[[0-9]*\]',' ',text)
text=re.sub(r'\s+',' ',text)
text=re.sub(r'\d',' ',text)
text=text.lower()

# PREPARINH THE DATASET 
sentences=nltk.sent_tokenize(text)
words=[nltk.word_tokenize(sentence) for sentence in sentences]
