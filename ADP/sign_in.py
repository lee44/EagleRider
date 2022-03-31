import sys
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright
import random
from util import Util

util = Util()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={
            "width": 1875, "height": 975}
    )
    page = context.new_page()

    page.goto("https://workforcenow.adp.com/workforcenow/login.html?")
    page.fill("id=login-form_username", util.get_email())
    page.locator("text=Next").click()
    page.wait_for_timeout(1000)
    page.fill("id=login-form_password", util.get_password())
    page.locator("text=Sign In").click()
    # Random wait time 0 - 15 minutes
    wait = float(random.randint(0, 10)*1000*60)
    page.wait_for_timeout(wait)
    page.locator('[aria-label="Clock Out"],[aria-label="Clock In"]').click()
    page.wait_for_timeout(5000)
    browser.close()