import sys
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()


def create_products(location):
    products = ['Bike', 'Guided Tour', 'Self Drive Tour']

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
        context = browser.new_context(
            viewport={
                "width": 2550, "height": 1300}
        )
        page = context.new_page()

        page.goto("https://www.eaglerider.com/activeadmin/location_products/new?location_product%5Blocation_id%5D=")

        util.login(page)

        page.wait_for_timeout(1000)

        for product in products:
            page.goto("https://www.eaglerider.com/activeadmin/location_products/new?location_product%5Blocation_id%5D=")
            page.locator("select[name=\"location_product[location_id]\"]").select_option(label=location)
            page.locator("select[name=\"location_product[product_id]\"]").select_option(label=product)
            page.click("input[name=\"commit\"]")
            page.wait_for_timeout(1000)


create_products('Mieming')
