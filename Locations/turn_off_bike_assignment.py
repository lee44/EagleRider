import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

location_id = [
    1, 2, 3, 4, 196, 5, 6, 7, 9, 10, 11, 14, 19, 22, 24, 35, 38, 40, 207, 45, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 208, 79,
    198, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 92, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 107, 105, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
    123, 124, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164,
    165, 167, 166, 168, 169, 170, 171, 172, 173, 174, 175, 179, 177, 178, 180, 181, 184, 185, 186, 188, 189, 192, 193, 197, 199, 200, 201, 204, 205, 206, 212, 226, 227, 229, 232]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
    context = browser.new_context(
        viewport={
            "width": 2550, "height": 1300}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin/location_fleet_configurations')

    util.login(page)

    for id in location_id:
        page.goto(f'https://www.eaglerider.com/activeadmin/location_fleet_configurations/{id}/edit')
        if page.locator("#location_fleet_configuration_reassign_vehicle_assignments_made_by_system").is_checked():
            print("reassign_vehicle_assignments_made_by_system is checked for ", id)
            page.locator("#location_fleet_configuration_reassign_vehicle_assignments_made_by_system").uncheck()
            page.wait_for_timeout(2000)
            page.click("input[name=\"commit\"]")

    browser.close()
