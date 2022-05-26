def create_company_user(page, company_name):
    print("Enter company id: ")
    company_id = int(input())
    print("Enter user id: ")
    user_id = int(input())

    page.goto("https://www.eaglerider.com/activeadmin/user_companies/new")
    page.fill("select[name=\"user_company[user_id]\"]", company_id)
    page.fill("select[name=\"user_company[company_id]\"]", user_id)

    page.goto(f"https://www.eaglerider.com/activeadmin/users/{user_id}/edit")

    if not page.is_checked("#user_role_ids_39"):
        page.check("#user_role_ids_39")
    if not page.is_checked("#user_managed_location_ids_1"):
        page.check("#user_managed_location_ids_1")

    page.locator("select[name=\"user[admin_extended_profile_attributes][default_location_id]\"]").select_option(value="1")
    page.locator("select[name=\"user[admin_extended_profile_attributes][process_payment_location_id]\"]").select_option(value="1")
    page.locator("select[name=\"user[admin_extended_profile_attributes][payment_gateway_id]\"]").select_option(value="158")

    print("5 seconds to check")
    page.wait_for_timeout(5000)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)
