import sys
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

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
    page.wait_for_timeout(30000)

    page.locator('[aria-label="Clock Out"],[aria-label="Clock In"]').click()
    # page.locator("text=Clock Out").click()
    page.wait_for_timeout(30000)
    browser.close()
