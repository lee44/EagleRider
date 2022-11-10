import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()
# 5335,
vehicle_id = [5348, 5352, 5396, 5399, 5405, 5423, 5464, 5473, 5476, 5630, 5677, 5688, 5689, 5723, 5735, 6007, 6256, 6257,
              6258, 6443, 6444, 6445, 6446, 6613, 6616, 6617, 6618, 6623, 6624, 6625, 6626, 6627, 6649, 6650, 6651, 6710, 6712, 6713, 6714, 6716, 6720, 6764]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=-5,0"])
    context = browser.new_context(
        viewport={
            "width": 2550, "height": 1300},
        http_credentials={"username": util.get_prelive_username(), "password": util.get_prelive_password()}
    )
    page = context.new_page()

    page.goto('https://prelive-www.eaglerider.com/agent/vehicles/find')

    util.login(page)

    for id in vehicle_id:
        page.goto(f'https://prelive-www.eaglerider.com/agent/vehicles/{id}/edit')
        page.click(".js-vehicleStatusDropdown")
        page.click("data-value=9")

        page.click(".js-vehicleStatusReasonDropdown")
        page.click("data-value=10")

        page.click(".js-submitTrigger")
