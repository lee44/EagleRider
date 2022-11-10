import os
import urllib
import webbrowser

import pandas as pd

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'
urls = ['https://www.eaglerider.com/',
        'https://www.eaglerider.com/losangeles',
        'https://www.eaglerider.com/losangeles/rental',
        'https://www.eaglerider.com/losangeles/electra-glide',
        'https://www.eaglerider.com/motorcycle-rental',
        'https://www.eaglerider.com/harley-rentals',
        'https://www.eaglerider.com/harley-rentals/electra-glide?page=1',
        'https://www.eaglerider.com/motorcycle-rental/las-vegas-nevada-united-states?page=1',
        'https://www.eaglerider.com/harley-rentals/las-vegas-nevada-united-states?page=1',
        'https://www.eaglerider.com/harley-rentals/road-glide/las-vegas-nevada-united-states?page=1',
        'https://www.eaglerider.com/guided-motorcycle-tours',
        'https://www.eaglerider.com/guided-motorcycle-tours/route-66-motorcycle-tour',
        'https://www.eaglerider.com/self-drive-motorcycle-tours',
        'https://www.eaglerider.com/self-drive-motorcycle-tours/route-66-self-guided-motorcycle-tour',
        'https://www.eaglerider.com/motorcycle-tours',
        'https://www.eaglerider.com/motorcycle-trips',
        'https://www.eaglerider.com/route-66-motorcycle-tours',
        'https://www.eaglerider.com/motorcycle-deals',
        'https://www.eaglerider.com/motorcycle-deals/active-police-fire-and-military-10-off-motorcycle-rental-732',
        'https://www.eaglerider.com/motorcycle-events',
        'https://www.eaglerider.com/motorcycle-events/las-vegas-bikefest',
        'https://www.eaglerider.com/locations',
        'https://www.eaglerider.com/motorcycle-club',
        'https://www.eaglerider.com/motorcycle-rental-gift-cards',
        'https://www.eaglerider.com/motorcycle-club-gift-cards/buy',
        'https://www.eaglerider.com/motorcycle-rental-gift-cards/buy',
        'https://www.eaglerider.com/rent-my-motorcycle',
        'https://www.eaglerider.com/motorcycle-club/sign-up?membership_id=6',
        'https://www.eaglerider.com/siteindex',
        'https://www.eaglerider.com/check-in',
        'https://www.eaglerider.com/motorcycle-rides',
        'https://www.eaglerider.com/motorcycle-rides/pacific-coast-highway',
        'https://www.eaglerider.com/motorcycle-touring',
        'https://www.eaglerider.com/motorcycle-touring/motorcycle-touring-tips',
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
