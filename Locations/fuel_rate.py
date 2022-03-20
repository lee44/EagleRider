import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

# print("File Name(exclude .csv): ")
# file = input()
file = 'active_locations'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/locations/225/edit")

    util.login(page)

    for i in df.index:
        location_id = df['id'][i]
        city_name = df['city_name'][i]

        print(f"Entering fuel rate for: {city_name}({location_id})")

        page.goto(f"https://www.eaglerider.com/activeadmin/locations/{location_id}/edit")
        page.fill("input[name=\"location[fuel_rate]\"]", '15')
        page.wait_for_timeout(2000)
        page.click("input[name=\"commit\"]")
        # page.wait_for_timeout(1500)

    browser.close()
