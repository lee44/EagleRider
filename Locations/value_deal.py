import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

file = 'Location_Vehicle_Model_Value_Deal'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin")

    util.login(page)

    for i in df.index:
        location_vehicle_model_id = df['id'][i]
        location_id = df['location_id'][i]
        vehicle_model_id = df['vehicle_model_id'][i]

        if int(vehicle_model_id) == 546:
            vehicle_model = "Harley-Davidson® Street Glide® Touring Edition"
        else:
            vehicle_model = "Harley-Davidson® Road Glide® Touring Edition"

        print(f"Checking Value Deal for: {vehicle_model}({location_id})")

        page.goto(f"https://www.eaglerider.com/activeadmin/location_vehicle_models/{location_vehicle_model_id}/edit")

        if int(vehicle_model_id) == 546:
            page.uncheck("#location_vehicle_model_value_deal")
        else:
            if not page.is_checked("#location_vehicle_model_value_deal"):
                page.check("#location_vehicle_model_value_deal")

        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)

    browser.close()
