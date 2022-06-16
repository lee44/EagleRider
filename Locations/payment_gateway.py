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
file = 'corp_locations'

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
        location = df['location'][i]

        print(f"Changing Payment Gateway for: {location} ({location_id})")

        page.goto(f"https://www.eaglerider.com/activeadmin/locations/{location_id}/edit")
        page.locator("select[name=\"location[payment_gateway_id]\"]").select_option(label="Accounting - CK")
        page.wait_for_timeout(1000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)

    browser.close()
