import sys
from datetime import datetime
from os.path import abspath, dirname

from dateutil.relativedelta import relativedelta
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()
print("Enter the biggest Company Product ID for that company: ")
company_product_id = input()

company_product_id = int(company_product_id)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin")

    util.login(page)

    for i in range(3):
        page.goto("https://www.eaglerider.com/activeadmin/company_product_credit_terms/new")
        page.fill("input[name=\"company_product_credit_term[company_product_id]\"]", str(company_product_id))

        if i != 1:
            page.fill("input[name=\"company_product_credit_term[due_days]\"]", "30")
        else:
            page.fill("input[name=\"company_product_credit_term[due_days]\"]", "60")

        page.locator("select[name=\"company_product_credit_term[calculation_method_id]\"]").select_option(label="Before Pickup")
        page.fill("input[name=\"company_product_credit_term[start_date]\"]", datetime.today().strftime('%Y-%m-%d'))
        page.fill("input[name=\"company_product_credit_term[end_date]\"]", "2050-12-31")
        print("5 seconds to check")
        page.wait_for_timeout(5000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)
        company_product_id -= 1

    browser.close()
