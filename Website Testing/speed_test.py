import os
import urllib
import webbrowser

import pandas as pd

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'
urls = [
    'https://www.eagleshare.com/',
    'https://www.eagleshare.com/motorcycle-rental/los-angeles-california-united-states',
    'https://www.eagleshare.com/harley-rentals/street-glide-special/studio-city-california-united-states/14284',
    'https://www.eagleshare.com/rent-my-motorcycle',
    'https://www.eagleshare.com/commercial-host',
    'https://www.eagleshare.com/check-in',
    'https://www.eagleshare.com/siteindex',
]

# Mobile Score
for url in urls:
    webbrowser.get(chrome_path).open('https://pagespeed.web.dev/report?url=' + url)

# Desktop Score
for url in urls:
    webbrowser.get(chrome_path).open('https://pagespeed.web.dev/report?url=' + url + '&form_factor=desktop')
