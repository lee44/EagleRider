import os
import urllib
import webbrowser

import pandas as pd

file = 'store_credits'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path, encoding="ISO-8859-1", parse_dates=["Expired"])

url_list = []

for i in df.index:
    url_param = {'by_receiver_email_equals': df['Email'][i], 'commit': 'Filter', 'order': "id_desc"}
    url_list.append('https://www.eaglerider.com/activeadmin/store_credits?utf8=✓&q%5B' + urllib.parse.urlencode(url_param))

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'

for link in url_list:
    if link != '':
        webbrowser.get(chrome_path).open(link)
