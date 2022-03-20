import sys
from datetime import datetime
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

products = ['Bike', 'Guided Tour', 'Self Drive Tour']

print("Company Name: ")
company_name = input()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin")

    util.login(page)

    for product in products:
        page.goto("https://www.eaglerider.com/activeadmin/company_products/new")
        page.locator("select[name=\"company_product[company_id]\"]").select_option(label=company_name)
        page.locator("select[name=\"company_product[product_id]\"]").select_option(label=product)
        page.fill("input[name=\"company_product[start_date]\"]", datetime.today().strftime('%Y-%m-%d'))

        page.fill("input[name=\"company_product[end_date]\"]", "2050-12-31")
        if product == 'Bike':
            page.locator("select[name=\"company_product[commission_calculation_method_id]\"]").select_option(value="1")
        else:
            page.locator("select[name=\"company_product[commission_calculation_method_id]\"]").select_option(value="2")

        page.fill("input[name=\"company_product[commission_percentage]\"]", "10")
        page.locator("select[name=\"company_product[commission_currency_code]\"]").select_option(value="USD")

        page.click("xpath=//html/body/div[1]/div[2]/div[1]/h2")

        print("10 seconds to check")
        page.wait_for_timeout(10000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)

    browser.close()
