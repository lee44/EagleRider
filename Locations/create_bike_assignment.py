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
    245, 244, 243, 242, 241, 240, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220, 219, 218, 217, 216, 215, 214, 213, 212, 211, 210, 209, 208, 207,
    206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168,
    167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129,
    128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87,
    86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38,
    37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, ]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--window-position=0,0"])
    context = browser.new_context(
        viewport={
            "width": 2500, "height": 1300}
    )
    page = context.new_page()

    page.goto('https://www.eaglerider.com/activeadmin/location_fleet_configurations')

    util.login(page)

    for id in location_id:
        page.goto(f'https://www.eaglerider.com/activeadmin/location_fleet_configurations/{id}/edit')
        page.fill("input[name=\"location_fleet_configuration[yielding_up_threshold_percentage]\"]", "100")
        page.fill("input[name=\"location_fleet_configuration[turn_around_time_in_minutes]\"]", "60")
        page.fill("input[name=\"location_fleet_configuration[location_fleet_department_email]\"]", "jlee@eaglerider.com")
        page.locator("#location_fleet_configuration_enable_automatic_vehicle_assignment").check()
        page.locator("select[name=\"location_fleet_configuration[automatic_vehicle_assignment_mileage_strategy_type_id]\"]").select_option(value="1")
        page.locator("#location_fleet_configuration_reassign_vehicle_assignments_made_by_system").check()
        page.fill("input[name=\"location_fleet_configuration[automatic_vehicle_assignment_turn_around_time_in_minutes]\"]", "120")
        page.fill("input[name=\"location_fleet_configuration[automatic_vehicle_assignment_lead_days]\"]", "14")
        page.fill("input[name=\"location_fleet_configuration[w1_vehicle_reservation_product_preference_weight]\"]", "5")
        page.fill("input[name=\"location_fleet_configuration[w1_1_vehicle_reservation_product_preference_guided_tour_sub_weight]\"]", "3")
        page.fill("input[name=\"location_fleet_configuration[w1_2_vehicle_reservation_product_preference_self_drive_tour_sub_weight]\"]", "2")
        page.fill("input[name=\"location_fleet_configuration[w1_3_vehicle_reservation_product_preference_rental_sub_weight]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w2_vehicle_reservation_motorcycle_model_guaranteed_preference_weight]\"]", "4")
        page.fill("input[name=\"location_fleet_configuration[w3_vehicle_reservation_sales_channel_preference_weight]\"]", "3")
        page.fill("input[name=\"location_fleet_configuration[w3_1_vehicle_reservation_sales_channel_preference_retail_sub_weight]\"]", "6")
        page.fill("input[name=\"location_fleet_configuration[w3_2_vehicle_reservation_sales_channel_preference_club_sub_weight]\"]", "5")
        page.fill("input[name=\"location_fleet_configuration[w3_3_vehicle_reservation_sales_channel_preference_wholesale_travel_agent_sub_weight]\"]", "4")
        page.fill("input[name=\"location_fleet_configuration[w3_4_vehicle_reservation_sales_channel_preference_wholesale_travel_wholesaler_sub_weight]\"]", "3")
        page.fill("input[name=\"location_fleet_configuration[w3_5_vehicle_reservation_sales_channel_preference_wholesale_mc_travel_specialist_sub_weight]\"]", "2")
        page.fill("input[name=\"location_fleet_configuration[w3_6_vehicle_reservation_sales_channel_preference_wholesale_other_company_types_sub_weight]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w4_vehicle_reservation_deal_reservation_preference_weight]\"]", "2")
        page.fill("input[name=\"location_fleet_configuration[w5_vehicle_reservation_longer_rentals_preference_weight]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w6_1_vehicle_assignment_to_one_way_same_dropoff_location_and_owning_location_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w6_2_vehicle_assignment_to_one_way_same_dropoff_location_type_and_owning_location_type_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w6_3_vehicle_assignment_to_one_way_defleet_dropoff_location_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w6_4_vehicle_assignment_to_one_way_service_dropoff_location_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w7_1_vehicle_assignment_to_returning_defleet_mileage_strategy_type_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w7_2_vehicle_assignment_to_returning_remaining_mileage_before_next_service_preference]\"]", "1")
        page.fill("input[name=\"location_fleet_configuration[w7_3_vehicle_assignment_to_returning_remaining_duration_between_planned_transactions]\"]", "1")
        page.click("input[name=\"commit\"]")

    browser.close()
