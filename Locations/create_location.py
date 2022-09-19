import os
import sys
from os.path import abspath, dirname

import pandas as pd
from playwright.sync_api import sync_playwright

from utils.getLongLat import getLongLat

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', 'Affiliate_Location_ Information_ Form_ER_ Mieming,Austria' + '.xlsx'))
df = pd.read_excel(abs_path, usecols='A:B', nrows=37)

print('Enter Description:')
description = input()

print('Enter Directions Text:')
directions = input()

print('Enter Email(Ask Kasun to generate ER email)')
email = input()

print('Enter Geography ID')
geography = input()

print('Enter Region')
region = input()

print('Enter Postal Code')
postal_code = input()

# print('Enter Longitude')
# longitude = input() or "10.9810202"

# print('Enter Latitude')
# latitude = input() or "47.29846"

print('Enter Timezone Name')
timezone = input()

print('Allow One Ways(y/n)')
allow_one_ways = input()

print('Currency Code(Default:EUR)')
currency_code = input()

print('Preferred Language(Default:English)')
preferred_language = input() or "English"

print('Payment Gateway(Default:BT - Euros)')
payment_gateway = input() or "BT - Euros"

contact_email = ''

for i, j in df.iterrows():
    if(j['Entity'] == 'Location Name'):
        display_name = j['Value']
    if(j['Entity'] == 'Location Code'):
        location_code = j['Value']
    if(j['Entity'] == 'Physical Address'):
        first_address = j['Value']
    if(j['Entity'] == 'Location Phone #'):
        phone = j['Value']
    if(j['Entity'] == 'Email Address' and contact_email == ''):
        contact_email = j['Value']
    if(j['Entity'] == 'Legal Entity'):
        legal_name = j['Value']
    if(j['Entity'] == 'Owner Principal'):
        contact_person_name = j['Value']
    if(j['Entity'] == 'Physical Address'):
        address = j['Value']
    if(j['Entity'] == 'City, State'):
        city_state = j['Value']

latitude, longitude = getLongLat(address)

country = display_name.split(',')[1].strip()
display_name = display_name.split(' ')[1].strip(',')
location_code = f'EA{location_code.strip()}01'

slug = display_name.lower()

city_name = display_name
website_url = f'https://www.eaglerider.com/{slug}'

zoom_level = '12'
location_type = 'Affiliate'
tier = 'A1'
location_group = 'INTERNATIONAL'
contact_person_phone = phone
contact_person_email = contact_email

fuel_rate = '15'
incoming_fleet_contingency_percentage = '0'
budgeted_free_sale_overridden_period = '0'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto("https://www.eaglerider.com/activeadmin/locations/new")

    util.login(page)

    page.wait_for_timeout(1000)

    page.fill("input[name=\"location[translations_attributes][0][display_name]\"]", display_name)
    page.fill("input[name=\"location[translations_attributes][0][slug]\"]", slug)
    # page.fill("input[name=\"location[translations_attributes][0][description]\"]", description)
    # page.fill("input[name=\"location[translations_attributes][0][directions_text]\"]", directions)
    page.fill("input[name=\"location[location_code]\"]", location_code)
    page.locator("select[name=\"location[preferred_language_id]\"]").select_option(label=preferred_language)
    page.locator("select[name=\"location[payment_gateway_id]\"]").select_option(label=payment_gateway)
    page.fill("input[name=\"location[email]\"]", email)
    page.locator("select[name=\"location[country_id]\"]").select_option(label=country)
    page.fill("input[name=\"location[geography_id]\"]", geography)
    page.locator("select[name=\"location[region_id]\"]").select_option(label=region)
    page.fill("input[name=\"location[region_name]\"]", region)
    page.fill("input[name=\"location[city_name]\"]", city_name)
    page.fill("input[name=\"location[address1]\"]", first_address)
    page.fill("input[name=\"location[postal_code]\"]", postal_code)
    page.fill("input[name=\"location[phone]\"]", phone)
    page.fill("input[name=\"location[website_url]\"]", website_url)
    page.fill("input[name=\"location[contact_email]\"]", contact_email)
    page.fill("input[name=\"location[longitude]\"]", longitude)
    page.fill("input[name=\"location[latitude]\"]", latitude)
    page.locator("select[name=\"location[timezone_name]\"]").select_option(label=timezone)
    page.fill("input[name=\"location[zoom_level]\"]", zoom_level)
    page.locator("select[name=\"location[location_type_id]\"]").select_option(label=location_type)
    page.locator("select[name=\"location[tier_id]\"]").select_option(label=tier)
    if(allow_one_ways == 'y'):
        page.click("input[name=\"location[allow_one_way_in]\"] >> visible=true")
    page.locator("select[name=\"location[currency_code]\"]").select_option(label=currency_code)
    page.locator("select[name=\"location[location_group_id]\"]").select_option(label=location_group)
    page.fill("input[name=\"location[legal_name]\"]", legal_name)
    page.fill("input[name=\"location[contact_person_name]\"]", contact_person_name)
    page.fill("input[name=\"location[contact_person_phone]\"]", contact_person_phone)
    page.fill("input[name=\"location[contact_person_email]\"]", contact_person_email)
    page.fill("input[name=\"location[fuel_rate]\"]", fuel_rate)
    page.locator("select[name=\"location[fleet_region_id]\"]").select_option('18')
    page.click("input[name=\"location[active]\"]")

    page.fill("input[name=\"location[incoming_fleet_contingency_percentage]\"]", incoming_fleet_contingency_percentage)
    page.fill("input[name=\"location[budgeted_free_sale_overridden_period]\"]", budgeted_free_sale_overridden_period)

    print("5 seconds to check")
    page.wait_for_timeout(20000)
    # page.click("input[name=\"commit\"]")
    # page.wait_for_timeout(1000)
    browser.close()

print('Make sure to add location image 1440x960px')
