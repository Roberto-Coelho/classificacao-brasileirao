from flask import request_finished
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math
import numpy as np

req = requests.get(
    'https://www.academiadasapostasbrasil.com/stats/competition/brasil/26')


'''headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
'''

content = req.content
soup = BeautifulSoup(content, 'html.parser')

# pegando do o texto do titulo da tabela Classificação atual
brtabelaACD = soup.find('span', class_=re.compile('currenttable-group-0'))
brtabelatitulo = brtabelaACD.find(
    'span', class_=re.compile('boxed-title')).get_text().strip()
brtabelaACD_str = str(brtabelatitulo)
# pegando o titulo classificação atual


classifi = soup.find('span', class_=re.compile('currenttable-group-0'))
brclassifi = classifi.find_all(name='table')
brclassifi_str = str(brclassifi)

df = pd.read_html(brclassifi_str)
tbl = df[0]

tbl.to_excel('C:/Users/Roberto/Desktop/classifi.xlsx', index=False)
print(tbl)

request_finished