import datetime
import os
import sys
from os.path import abspath, dirname

import pandas as pd
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print("File Name(exclude .csv): ")
file = input() or 'location-vehicle-models-2022-09-12'
print("Enter Location ID")
location_id = input()

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path, encoding='utf-8')

# for i in df.index:
#     location_vehicle_model_id = df['Id'][i]
#     start_date = pd.to_datetime(df['Start date'][i])
#     end_date = pd.to_datetime(df['End date'][i])

#     print(location_vehicle_model_id)

#     print(start_date)
#     print(end_date)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto(f'https://www.eaglerider.com/activeadmin/soldouts/new?location_id={location_id}')

    util.login(page)

    for i in df.index:
        location_vehicle_model_id = df['Id'][i]
        start_date = pd.to_datetime(df['Start date'][i]).strftime('%Y-%m-%d')
        end_date = pd.to_datetime(df['End date'][i]).strftime('%Y-%m-%d')

        print(location_vehicle_model_id)

        page.locator("select[name=\"soldout[location_vehicle_model_id]\"]").select_option(value=str(location_vehicle_model_id))
        page.fill("input[name=\"soldout[start_date]\"]", start_date)
        page.fill("input[name=\"soldout[end_date]\"]", end_date)
        page.check("#soldout_products_1")
        page.check("#soldout_products_2")
        page.check("#soldout_products_3")
        page.check("#soldout_products_4")

        page.check("#soldout_sales_channels_1")
        page.check("#soldout_sales_channels_2")

        page.wait_for_timeout(1000)
        page.click("input[name=\"commit\"]")
        page.goto(f'https://www.eaglerider.com/activeadmin/soldouts/new?location_id={location_id}')

    browser.close()
