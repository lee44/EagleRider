import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

# print("File Name(exclude .csv): ")
# file = input()
file = 'payment_gateway'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.csv'))
df = pd.read_csv(abs_path)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/users")

    util.login(page)

    for i in df.index:
        user_id = df['id'][i]
        agent_name = df['agent_name'][i]
        payment_gateway = 'Accounting - CK'

        print(f"Changing Payment Gateway for: {agent_name}")

        page.goto(f"https://www.eaglerider.com/activeadmin/users/{user_id}/edit")
        page.locator("select[name=\"user[admin_extended_profile_attributes][payment_gateway_id]\"]").select_option("158")
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)

    browser.close()
