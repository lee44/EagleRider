import sys
from datetime import datetime
from os.path import abspath, dirname

from playwright.sync_api import TimeoutError, sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Utilities.util import Util

util = Util()


def create_non_working_intervals(location):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={
                "width": 1875, "height": 975}
        )
        page = context.new_page()

        page.goto("https://www.eaglerider.com/activeadmin/location_non_working_intervals/new?location_non_working_interval%5Blocation_id%5D=")

        util.login(page)

        page.wait_for_timeout(1000)

        print('How many holidays?')
        holiday_count = input()

        for index in holiday_count:
            page.goto("https://www.eaglerider.com/activeadmin/location_non_working_intervals/new?location_non_working_interval%5Blocation_id%5D=")
            page.locator("select[name=\"location_non_working_interval[location_id]\"]").select_option(label=location)
            print("Finish entering holiday?(Press Enter)")
            is_finished = input()
            page.click("input[name=\"commit\"]")
            page.wait_for_timeout(1000)


create_non_working_intervals('Mieming')
