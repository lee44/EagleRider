import os
import urllib
import webbrowser

import pandas as pd

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'
urls = ['https://prelive-www.eaglerider.com/motorcycle-rental',
        'https://prelive-www.eaglerider.com/motorcycle-rental/las-vegas-nevada-united-states',
        'https://prelive-www.eaglerider.com/dirt-bike-rentals',
        'https://prelive-www.eaglerider.com/harley-rentals',
        'https://prelive-www.eaglerider.com/bmw-motorcycle-rental',
        'https://prelive-www.eaglerider.com/losangeles/rental',

        # 'https://prelive-www.eaglerider.com/washingtondc/rental',
        # 'https://prelive-www.eaglerider.com/vancouver/rental',
        # 'https://prelive-www.eaglerider.com/seattle/rental',
        # 'https://prelive-www.eaglerider.com/phoenix/rental',
        # 'https://prelive-www.eaglerider.com/fortlauderdale/rental',
        # 'https://prelive-www.eaglerider.com/daytona/rental',
        # 'https://prelive-www.eaglerider.com/nashville-airport/rental',
        # 'https://prelive-www.eaglerider.com/dallas/rental',
        # 'https://prelive-www.eaglerider.com/boston/rental',
        # 'https://prelive-www.eaglerider.com/motorrad-mieten/gefuhrte-motorradreisen',
        # 'https://prelive-www.eaglerider.com/alquiler-de-motos/tours-en-moto-con-guia',
        # 'https://prelive-www.eaglerider.com/noleggio-moto/viaggi-in-moto-guidati',
        # 'https://prelive-www.eaglerider.com/aluguel-de-motos/moto-tours-guiados',
        # 'https://prelive-www.eaglerider.com/motorcycle-tours',
        # 'https://prelive-www.eaglerider.com/guided-motorcycle-tours',
        # 'https://prelive-www.eaglerider.com/self-drive-motorcycle-tours',
        # 'https://prelive-www.eaglerider.com/route-66-motorcycle-tours',
        # 'https://prelive-www.eaglerider.com/location-moto/route-66-motorcycle-tours',
        # 'https://prelive-www.eaglerider.com/motorcycle-trips',
        # 'https://prelive-www.eaglerider.com/motorcycle-deals',
        # 'https://prelive-www.eaglerider.com/motorcycle-club',
        # 'https://prelive-www.eaglerider.com/faqs/motorcycle-rentals',
        # 'https://prelive-www.eaglerider.com/information',
        # 'https://prelive-www.eaglerider.com/rentals/rental-terms-and-conditions',
        # 'https://prelive-www.eaglerider.com/contact-us',
        # 'https://prelive-www.eaglerider.com/maui-lahaina/rental',
        # 'https://prelive-www.eaglerider.com/sturgis/rental',
        # 'https://prelive-www.eaglerider.com/sandiego/rental ',
        # 'https://prelive-www.eaglerider.com/neworleans/rental ',
        # 'https://prelive-www.eaglerider.com/austin/rental',
        ]

# Mobile Score
for url in urls:
    webbrowser.get(chrome_path).open(url)
