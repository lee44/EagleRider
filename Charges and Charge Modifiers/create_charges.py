import os
import sys
from cgitb import text
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

file = 'MMG (1)'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path, encoding="ISO-8859-1")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2540, "height": 1400}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin')

    util.login(page)

    for i in df.index:
        location = df['location_source'][i]
        vehicle_class = df['class'][i]

        print(location, vehicle_class)

        page.goto('https://www.eaglerider.com/activeadmin/charges/new')
        page.locator("select[name=\"charge[charge_description_id]\"]").select_option(value="9")

        page.fill("input[name=\"charge[end_date]\"]", "2050-12-31")
        page.fill("input[name=\"charge[start_date]\"]", "2023-01-01")
        page.locator("select[name=\"charge[calculation_method_id]\"]").select_option(value="3")
        page.fill("input[name=\"charge[hourly_amount]\"]", "99")
        page.fill("input[name=\"charge[sun_amount]\"]", "99")
        page.fill("input[name=\"charge[mon_amount]\"]", "99")
        page.fill("input[name=\"charge[tue_amount]\"]", "99")
        page.fill("input[name=\"charge[wed_amount]\"]", "99")
        page.fill("input[name=\"charge[thu_amount]\"]", "99")
        page.fill("input[name=\"charge[fri_amount]\"]", "99")
        page.fill("input[name=\"charge[sat_amount]\"]", "99")
        page.locator("select[name=\"charge[currency_code]\"]").select_option(value="USD")
        page.locator("select[name=\"charge[location_source_type]\"]").select_option(value="Location")
        page.locator("select[name=\"charge[location_source_id]\"]").select_option(label=location.strip())
        page.locator("select[name=\"charge[vehicle_model_source_type]\"]").select_option(value="VehicleClass")
        page.locator("select[name=\"charge[vehicle_model_source_id]\"]").select_option(label=vehicle_class.strip())
        page.locator("#charge_active").check()

        page.locator('a:has-text("Add New Charge product")').click()
        page.locator('a:has-text("Add New Charge product")').click()
        page.locator('a:has-text("Add New Charge product")').click()
        page.locator("select[name=\"charge[charge_products_attributes][0][product_id]\"]").select_option(value="1")
        page.locator("select[name=\"charge[charge_products_attributes][1][product_id]\"]").select_option(value="3")
        page.locator("select[name=\"charge[charge_products_attributes][2][product_id]\"]").select_option(value="4")

        page.locator('a:has-text("Add New Charge sales channel")').click()
        page.locator('a:has-text("Add New Charge sales channel")').click()
        page.locator("select[name=\"charge[charge_sales_channels_attributes][0][sales_channel_id]\"]").select_option(value="1")
        page.locator("select[name=\"charge[charge_sales_channels_attributes][1][sales_channel_id]\"]").select_option(value="2")

        page.click("input[name=\"commit\"]")

    browser.close()
