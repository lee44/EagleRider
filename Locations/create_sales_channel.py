import sys
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()


def create_sales_channels(location):
    sales_channels = ['Retail', 'Wholesale']

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
    context = browser.new_context(
        viewport={
            "width": 2550, "height": 1300}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/location_sales_channels/new?location_sales_channel%5Blocation_id%5D=")

    util.login(page)

    page.wait_for_timeout(1000)

    for sales_channel in sales_channels:
        page.goto("https://www.eaglerider.com/activeadmin/location_sales_channels/new?location_sales_channel%5Blocation_id%5D=")
        page.locator("select[name=\"location_sales_channel[location_id]\"]").select_option(label=location)
        page.locator("select[name=\"location_sales_channel[sales_channel_id]\"]").select_option(label=sales_channel)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)


create_sales_channels('Mieming')
