import sys
from os.path import abspath, dirname

import pandas as pd
import requests
from bs4 import BeautifulSoup

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

# Source https://www.banjocode.com/post/python/scrape-authenticated/

print("Category #: ")
category = input()
url = 'https://prelive-www.eaglerider.com/translation_center/categories/' + category

# English (en)
# French (fr)
# Spanish (es)
# Italian (it)
# Portuguese (pt)

print("What language(en/fr/es/it/pt):")
language = input()

params = (
    ('lang_to', language),
)

response = requests.get(url, headers=util.get_prelive_headers, params=params)

content = response.content

soup = BeautifulSoup(content, features="lxml")

em_list = soup.select("a p b em")

# with open('Words_Needing_Translation.txt', 'w', encoding='utf-8') as f:
#     for element in em_list:
#         f.write(element.text.replace("\n", ""))
#         f.write('\n')
df = pd.DataFrame(em_list, columns=['Word'])
df.to_excel("output.xlsx", index=False)
