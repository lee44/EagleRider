import sys
from cProfile import label
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print("Company Name: ")
company_name = input()
print("Company Code(6 Digits): ")
company_code = input()
print("Company Type:")
company_type = input()
print("Interface Type:")
interface_type = input()
print("Billing Email: ")
email = input()
print("Phone: ")
phone = input()
print("Country: ")
country = input()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/companies/new")

    util.login(page)

    page.fill("input[name=\"company[name]\"]", company_name)
    page.fill("input[name=\"company[code]\"]", company_code)
    page.locator("select[name=\"company[company_type_id]\"]").select_option(label=company_type)
    page.locator("select[name=\"company[interface_type_id]\"]").select_option(label=interface_type)
    page.locator("select[name=\"company[sales_channel_id]\"]").select_option("1")
    page.locator("select[name=\"company[invoice_delivery_method_id]\"]").select_option("1")
    page.fill("input[name=\"company[billing_email]\"]", email)
    page.fill("input[name=\"company[email]\"]", email)
    page.locator("select[name=\"company[country_id]\"]").select_option(label=country)

    page.fill("input[name=\"company[phone]\"]", phone)
    page.click("xpath=//html/body/div/div[4]/div/div/form/fieldset[1]/ol/li[23]/label/input")
    page.click("xpath=//html/body/div/div[4]/div/div/form/fieldset[1]/ol/li[24]/label/input")

    print("10 seconds to check")
    page.wait_for_timeout(10000)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)
    browser.close()
