import sys
from datetime import datetime
from os.path import abspath, dirname

from playwright.sync_api import TimeoutError, sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Utilities.util import Util

util = Util()


def create_operation_interval(location):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
        context = browser.new_context(
            viewport={
                "width": 2550, "height": 1300}
        )
        page = context.new_page()

        page.goto("https://www.eaglerider.com/activeadmin/location_operational_intervals/new?location_operational_interval%5Blocation_id%5D=")

        util.login(page)

        page.wait_for_timeout(1000)

        page.locator("select[name=\"location_operational_interval[location_id]\"]").select_option(label=location)
        page.fill("input[name=\"location_operational_interval[reason]\"]", "Default Schedule")

        # Default Operation Interval
        for i in range(0, 7):
            page.click(".has_many_add")
            page.wait_for_timeout(1000)

            page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{i}][day_of_the_week]\"]").select_option(value=str(i))
            page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{i}][start_period]\"]").select_option(value='09:00')
            page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{i}][end_period]\"]").select_option(value='17:00')

            page.click("input[name=\"commit\"]")
            page.wait_for_timeout(5000)

            # Actual Operation Interval
            page.goto("https://www.eaglerider.com/activeadmin/location_operational_intervals/new?location_operational_interval%5Blocation_id%5D=")
            page.locator("select[name=\"location_operational_interval[location_id]\"]").select_option(label=location)
            page.fill("input[name=\"location_operational_interval[start_date]\"]", datetime.today().strftime('%Y-%m-%d'))
            page.fill("input[name=\"location_operational_interval[end_date]\"]", "2050-12-31")
            page.fill("input[name=\"location_operational_interval[reason]\"]", "Location Schedule")

            Dict = {}
            days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

            print('Common Start Date(hh:mm)')
            common_start_date = input()
            print('Common End Date(hh:mm)')
            common_end_date = input()

            for day in days:
                print(f'Does {day} start date equal common start date(y/n, empty for Yes)?')
                is_start_date_common = input() or 'y'
                print(f'Does {day} end date equal common end date(y/n, empty for Yes)?')
                is_end_date_common = input() or 'y'

                if is_start_date_common == 'n':
                    print(f'What is {day} start date(hh:mm, blank for closed)')
                    start_date = input() or 0
                if is_end_date_common == 'n':
                    print(f'What is {day} end date(hh:mm, blank for closed)')
                    end_date = input() or 0

                Dict[day] = {'start_date': common_start_date if is_start_date_common == 'y' else start_date, 'end_date': common_end_date if is_end_date_common == 'y' else end_date}
            index = 0
            for day in days:
                if Dict[day]['start_date'] != 0:
                    page.click(".has_many_add")
                    page.wait_for_timeout(1000)

                    page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{index}][day_of_the_week]\"]").select_option(label=day)
                    page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{index}][start_period]\"]").select_option(value=str(Dict[day]['start_date']))
                    page.locator(f"select[name=\"location_operational_interval[operational_days_attributes][{index}][end_period]\"]").select_option(value=str(Dict[day]['end_date']))
                    index += 1
            page.wait_for_timeout(5000)
            page.click("input[name=\"commit\"]")


create_operation_interval('Mieming')
