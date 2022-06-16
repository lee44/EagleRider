import sys
from cProfile import label
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

from create_company_products import create_company_products
from create_product_credit_terms import create_product_credit_terms

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print("Company Name: ")
company_name = input()
print("Company Code(6 Digits): ")
company_code = input()
print("Company Type:(Leave blank for Travel Agency)")
company_type = input() or "Travel Agency"
print("Sales Channel:(Leave blank for Retail)")
sales_channel = input() or "Retail"
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
            "width": 2500, "height": 1375}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/companies/new")

    util.login(page)

    page.fill("input[name=\"company[name]\"]", company_name)
    page.fill("input[name=\"company[code]\"]", company_code)
    page.locator("select[name=\"company[company_type_id]\"]").select_option(label=company_type)
    page.locator("select[name=\"company[interface_type_id]\"]").select_option(label="Agent Interface")
    page.locator("select[name=\"company[sales_channel_id]\"]").select_option(label=sales_channel)
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

    create_company_products(page, company_name)
    create_product_credit_terms(page)

    browser.close()
