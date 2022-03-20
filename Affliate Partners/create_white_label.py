import sys
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

from create_company import create_company
from create_company_products import create_company_products
from create_product_credit_terms import create_product_credit_terms
from create_referral import create_referral
from email_affliates_code_snippet import email_affiliate_code_snippet

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print("Company Name: ")
company_name = input()
print("Company Code(6 Digits): ")
company_code = input()
print("Billing Email: ")
billing_email = input()
email = billing_email
print("Phone: ")
phone = input()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/companies/new")

    util.login(page)

    create_company(page, company_name, company_code, billing_email, email, phone)
    create_company_products(page, company_name)
    create_product_credit_terms(page)

    create_referral(page, company_name, company_code, email)

    email_affiliate_code_snippet(email)

    browser.close()
