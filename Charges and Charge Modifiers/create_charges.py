import os
import sys
from cgitb import text
from os.path import abspath, dirname
from unicodedata import name

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

vehicle_class = ['Grand Touring', 'Touring', 'Classic', '3-Wheel']

print("Enter Location")
location = input()
print("Enter Charge Description")
charge_description = input()
print("Enter Start Date")
start_date = input()
print("Enter End Date")
end_date = input()
print("Enter Amount")
amount = input()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
    context = browser.new_context(
        viewport={
            "width": 2540, "height": 1300}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin')

    util.login(page)

    for className in vehicle_class:
        page.wait_for_timeout(2000)
        page.goto('https://www.eaglerider.com/activeadmin/charges/new')
        page.locator("select[name=\"charge[charge_description_id]\"]").select_option(label=charge_description)

        page.fill("input[name=\"charge[start_date]\"]", start_date)
        page.fill("input[name=\"charge[end_date]\"]", '')
        page.fill("input[name=\"charge[end_date]\"]", end_date)
        page.locator("select[name=\"charge[calculation_method_id]\"]").select_option(value="4")
        page.fill("input[name=\"charge[hourly_amount]\"]", amount)
        page.fill("input[name=\"charge[sun_amount]\"]", amount)
        page.fill("input[name=\"charge[mon_amount]\"]", amount)
        page.fill("input[name=\"charge[tue_amount]\"]", amount)
        page.fill("input[name=\"charge[wed_amount]\"]", amount)
        page.fill("input[name=\"charge[thu_amount]\"]", amount)
        page.fill("input[name=\"charge[fri_amount]\"]", amount)
        page.fill("input[name=\"charge[sat_amount]\"]", amount)
        page.locator("select[name=\"charge[currency_code]\"]").select_option(value="USD")
        page.locator("select[name=\"charge[location_source_type]\"]").select_option(value="Location")
        page.locator("select[name=\"charge[location_source_id]\"]").select_option(label=location)
        page.locator("select[name=\"charge[vehicle_model_source_type]\"]").select_option(value="VehicleClass")
        page.locator("select[name=\"charge[vehicle_model_source_id]\"]").select_option(label=className)
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

        # page.wait_for_timeout(10000)
        page.click("input[name=\"commit\"]")

    browser.close()
