import os
import sys
from datetime import date
from os.path import abspath, dirname

import pandas as pd
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

print('\n*In excel, ensure the following columns: Email, Amount, Expired, Res')
print('*Convert all dates to short date, make sure there exists an Expired column, and no empty cells')
print("File Name(exclude .csv): ")
file = input()

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path, encoding="ISO-8859-1", parse_dates=["Expired"])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/store_credits/new")

    util.login(page)

    page.wait_for_timeout(1000)
    for i in df.index:
        email = df['Email'][i]
        amount = df['Amount'][i]
        res_number = df['Res #'][i]
        expired_datetime = df['Expired'][i]
        extension = df['Extension'][i]

        extension_value = extension.split()[0]
        extension_unit = extension.split()[1]

        res_url = 'https://www.eaglerider.com/agent/vehicle_reservations?rentalapp_reservation_number=' + res_number + '&reservation_identifier=&third_party_reservation_number='
        response = requests.get(res_url, headers=util.get_headers())
        soup = BeautifulSoup(response.content, features="lxml")
        anchors = soup.select('.has-tip.top')

        res_id = anchors[0]['href'].split("/")[3]
        customer_id = anchors[1]['href'].split("/")[3]

        print('\nCreating for: ', email, " -> ", amount, " -> ", customer_id, " -> ", res_id)

        store_credit_url_search = 'https://www.eaglerider.com/activeadmin/store_credits?utf8=%E2%9C%93&q%5Bvehicle_reservation_id_equals%5D=' + res_id + '&commit=Filter&order=id_desc'
        response = requests.get(store_credit_url_search, headers=util.get_headers())
        soup = BeautifulSoup(response.content, features="lxml")
        anchors = soup.select('td:nth-of-type(1)')

        reference_id = anchors[0].get_text()

        if(customer_id == "" or res_id == "" or reference_id == ""):
            print('Skipped because customer_id, res_id, or reference_id are empty')
            continue

        page.goto("https://www.eaglerider.com/activeadmin/store_credits/new")

        page.fill("input[name=\"store_credit[issued_for_customer_id]\"]", customer_id)
        page.fill("input[name=\"store_credit[vehicle_reservation_id]\"]", res_id)
        page.fill("input[name=\"store_credit[amount]\"]", str(amount))
        page.fill("input[name=\"store_credit[remaining_amount]\"]", str(amount))

        if extension_unit == 'year':
            page.locator("select[name=\"store_credit[expiration_time(1i)]\"]").select_option(value=str(int(expired_datetime.year) + int(extension_value)))
            page.locator("select[name=\"store_credit[expiration_time(2i)]\"]").select_option(value=str(expired_datetime.month))
        else:
            if int(expired_datetime.month) + int(extension_value) == 12:
                page.locator("select[name=\"store_credit[expiration_time(1i)]\"]").select_option(value=str(date.today().year))
                page.locator("select[name=\"store_credit[expiration_time(2i)]\"]").select_option(value="12")
            else:
                page.locator("select[name=\"store_credit[expiration_time(1i)]\"]").select_option(value=str(date.today().year))
                page.locator("select[name=\"store_credit[expiration_time(2i)]\"]").select_option(value=str((int(expired_datetime.month) + int(extension_value)) % 12))

        page.locator("select[name=\"store_credit[expiration_time(3i)]\"]").select_option(value=str(expired_datetime.day))
        page.locator("select[name=\"store_credit[expiration_time(4i)]\"]").select_option(value="12")
        page.locator("select[name=\"store_credit[expiration_time(5i)]\"]").select_option(value="00")
        page.fill("input[name=\"store_credit[reference_id]\"]", str(reference_id))

        page.wait_for_timeout(2000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1500)
    browser.close()
