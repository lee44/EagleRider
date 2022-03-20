import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

# Words needing translation in the translation center need to match the exact order of the csv file,
# otherwise script will get stuck on the missing word in the excel file

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', 'spanish.csv'))
df = pd.read_csv(abs_path, header=None)

# print(df[0].to_string(index=False))

# for index in df.index:
#     print(df[0][index], df[1][index])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username": util.get_prelive_username(), "password": util.get_prelive_password()}
    )
    page = context.new_page()
    page.set_viewport_size({"width": 1875, "height": 975})

    page.goto("https://prelive-www.eaglerider.com/translation_center")

    page.locator('.dropdown.pull-left').click()
    page.locator('a:has-text("Español")').click()

    page.locator(
        'a:has(div:has-text("Fe Er Tour Package Selector"))').click()

    for index in df.index:
        print('\nStarting to Enter: ', df[0][index], " -> ", df[1][index])
        page.locator(
            "div.tab-pane.active >> div.tabbable >> ul.nav.nav-tabs >> li >> nth=1").click()

        # Grabs the word to be translated
        word_to_be_translated = page.text_content(
            "div.tab-pane.active >> div.tabbable >> div.tab-content >> div.tab-pane.active >> em >> b")

        if(not(df[0][index].lower() in word_to_be_translated.lower())):
            print(
                "Failed because '" + df[0][index] + "' from excel doesn't match '" + word_to_be_translated.replace("\n", "") + "'")
            continue

        translated_input = page.locator(
            "div.tab-pane.active >> div.tabbable >> div.tab-content >> div.tab-pane >> div.user_translation.well.well-small.ltr")
        translated_input.click()
        translated_input.type(df[1][index])
        page.wait_for_timeout(2500)
        page.locator(
            "div.tab-content.translations_listing").click()
        page.wait_for_timeout(2500)

    page.wait_for_timeout(2500)
    browser.close()
