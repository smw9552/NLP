from urllib import request
from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize

# Dealing with HTML
url = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=24964572"
#url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')

#BeautifulSoup library 활용
raw = BeautifulSoup(html, 'html.parser').get_text()

tokens = word_tokenize(raw)

#Tokenization된 결과로부터 특정 키워드 (예시: garlic)를 바탕으로 관련된 문장 추출
#Concordance (용어, 색인)
text = nltk.Text(tokens)

temp_list = []


temp_list.append(str(text.concordance('Garlic', 100, 100)))

print(len(temp_list))


print("$$$$$$$$$")

print(temp_list)
#text.concordance('Cancer', 100, 100)

#Keywords = ['Garlic', 'Cancer']

##Keyword 하나씩 정리하는 것
#for key in Keywords:
#    print(key)
#    text.concordance(str(key), 100, 100)