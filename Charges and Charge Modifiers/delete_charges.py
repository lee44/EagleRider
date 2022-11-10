import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
    context = browser.new_context(
        viewport={
            "width": 2525, "height": 1325}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin')

    util.login(page)

    page.on("dialog", lambda dialog: dialog.accept())

    for id in range(22724, 22753):
        page.goto(f'https://www.eaglerider.com/activeadmin/charges/{id}')
        page.locator('a:has-text("Delete Charge")').click()

    browser.close()
