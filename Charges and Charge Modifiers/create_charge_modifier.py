import sys
import webbrowser
from os.path import abspath, dirname

from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()
#19330, 19331, 19332, 19333,
charge_id = [19330]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')

    util.login(page)

    print("Enter Vehicle Model Source: ")
    vehicle_model_source = input()
    print("How many iterations: ")
    iterations = int(input())

    for index in range(0, iterations):
        id = charge_id[index]
        print("Charge ID: ", id)

        if index == 0:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'
            webbrowser.get(chrome_path).open(f'https://www.eaglerider.com/activeadmin/charge_modifiers?utf8=%E2%9C%93&q%5Bmodifiable_source_id_equals%5D={id}&commit=Filter&order=id_desc')
            print("Enter 1-3 Amount: ")
            onetothree = input()
            print("Enter 4-6 Amount: ")
            fourtosix = input()
            print("Enter 7-13 Amount: ")
            seventothirteen = input()
            print("Enter 14-20 Amount: ")
            fourteentotwenty = input()
            print("Enter 21+ Amount: ")
            twentyoneplus = input()

        page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')
        page.fill("input[name=\"charge_modifier[description]\"]", f"{vehicle_model_source} | 1 - 3 Days Discount")
        page.fill("input[name=\"charge_modifier[modifiable_source_id]\"]", f"{id}")
        page.fill("input[name=\"charge_modifier[start_date]\"]", "2023-01-01")
        page.fill("input[name=\"charge_modifier[end_date]\"]", "2025-12-31")
        page.fill("input[name=\"charge_modifier[min_days]\"]", "1")
        page.fill("input[name=\"charge_modifier[max_days]\"]", "3")
        page.locator("select[name=\"charge_modifier[calculation_method_id]\"]").select_option(value="2")
        page.click("input[name=\"charge_modifier[adjustment_amount]\"]")
        page.fill("input[name=\"charge_modifier[adjustment_amount]\"]", onetothree)
        page.click("input[name=\"commit\"]")

        page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')
        page.fill("input[name=\"charge_modifier[description]\"]", f"{vehicle_model_source} | 4 - 6 Days Discount")
        page.fill("input[name=\"charge_modifier[modifiable_source_id]\"]", f"{id}")
        page.fill("input[name=\"charge_modifier[start_date]\"]", "2023-01-01")
        page.fill("input[name=\"charge_modifier[end_date]\"]", "2025-12-31")
        page.fill("input[name=\"charge_modifier[min_days]\"]", "4")
        page.fill("input[name=\"charge_modifier[max_days]\"]", "6")
        page.locator("select[name=\"charge_modifier[calculation_method_id]\"]").select_option(value="2")
        page.click("input[name=\"charge_modifier[adjustment_amount]\"]")
        page.fill("input[name=\"charge_modifier[adjustment_amount]\"]", fourtosix)
        page.click("input[name=\"commit\"]")

        page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')
        page.fill("input[name=\"charge_modifier[description]\"]", f"{vehicle_model_source} | 7 - 13 Days Discount")
        page.fill("input[name=\"charge_modifier[modifiable_source_id]\"]", f"{id}")
        page.fill("input[name=\"charge_modifier[start_date]\"]", "2023-01-01")
        page.fill("input[name=\"charge_modifier[end_date]\"]", "2025-12-31")
        page.fill("input[name=\"charge_modifier[min_days]\"]", "7")
        page.fill("input[name=\"charge_modifier[max_days]\"]", "13")
        page.locator("select[name=\"charge_modifier[calculation_method_id]\"]").select_option(value="2")
        page.click("input[name=\"charge_modifier[adjustment_amount]\"]")
        page.fill("input[name=\"charge_modifier[adjustment_amount]\"]", seventothirteen)
        page.click("input[name=\"commit\"]")

        page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')
        page.fill("input[name=\"charge_modifier[description]\"]", f"{vehicle_model_source} | 14 - 20 Days Discount")
        page.fill("input[name=\"charge_modifier[modifiable_source_id]\"]", f"{id}")
        page.fill("input[name=\"charge_modifier[start_date]\"]", "2023-01-01")
        page.fill("input[name=\"charge_modifier[end_date]\"]", "2025-12-31")
        page.fill("input[name=\"charge_modifier[min_days]\"]", "14")
        page.fill("input[name=\"charge_modifier[max_days]\"]", "20")
        page.locator("select[name=\"charge_modifier[calculation_method_id]\"]").select_option(value="2")
        page.click("input[name=\"charge_modifier[adjustment_amount]\"]")
        page.fill("input[name=\"charge_modifier[adjustment_amount]\"]", fourteentotwenty)
        page.click("input[name=\"commit\"]")

        page.goto('https://www.eaglerider.com/activeadmin/charge_modifiers/new')
        page.fill("input[name=\"charge_modifier[description]\"]", f"{vehicle_model_source} | 21+ Days Discount")
        page.fill("input[name=\"charge_modifier[modifiable_source_id]\"]", f"{id}")
        page.fill("input[name=\"charge_modifier[start_date]\"]", "2023-01-01")
        page.fill("input[name=\"charge_modifier[end_date]\"]", "2025-12-31")
        page.fill("input[name=\"charge_modifier[min_days]\"]", "21")
        page.fill("input[name=\"charge_modifier[max_days]\"]", "999")
        page.locator("select[name=\"charge_modifier[calculation_method_id]\"]").select_option(value="2")
        page.click("input[name=\"charge_modifier[adjustment_amount]\"]")
        page.fill("input[name=\"charge_modifier[adjustment_amount]\"]", twentyoneplus)
        page.click("input[name=\"commit\"]")

    browser.close()
