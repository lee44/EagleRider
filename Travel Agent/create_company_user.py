import sys
from cProfile import label
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print("Enter company id: ")
company_id = input()
print("Enter user id: ")
user_id = input()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/user_companies/new")

    util.login(page)

    page.fill("input[name=\"user_company[user_id]\"]", user_id)
    page.fill("input[name=\"user_company[company_id]\"]", company_id)

    print("5 seconds to check")
    page.wait_for_timeout(2500)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)

    page.goto(f"https://www.eaglerider.com/activeadmin/users/{user_id}/edit")

    if not page.is_checked("#user_role_ids_39"):
        page.check("#user_role_ids_39")
    if not page.is_checked("#user_managed_location_ids_1"):
        page.check("#user_managed_location_ids_1")

    page.locator("select[name=\"user[admin_extended_profile_attributes][default_location_id]\"]").select_option(value="1")
    page.locator("select[name=\"user[admin_extended_profile_attributes][process_payment_location_id]\"]").select_option(value="1")
    page.locator("select[name=\"user[admin_extended_profile_attributes][payment_gateway_id]\"]").select_option(value="158")

    print("5 seconds to check")
    page.wait_for_timeout(2500)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)
