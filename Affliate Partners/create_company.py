def create_company(page, company_name, company_code, billing_email, email, phone):

    page.fill("input[name=\"company[name]\"]", company_name+" White Label")
    page.fill("input[name=\"company[code]\"]", company_code)
    page.locator("select[name=\"company[company_type_id]\"]").select_option("11")
    page.locator("select[name=\"company[interface_type_id]\"]").select_option("3")
    page.locator("select[name=\"company[sales_channel_id]\"]").select_option("1")
    page.locator("select[name=\"company[invoice_delivery_method_id]\"]").select_option("1")
    page.fill("input[name=\"company[billing_email]\"]", billing_email)
    page.fill("input[name=\"company[email]\"]", email)
    page.locator("select[name=\"company[country_id]\"]").select_option(label='United States')

    page.fill("input[name=\"company[phone]\"]", phone)
    page.click("xpath=//html/body/div/div[4]/div/div/form/fieldset[1]/ol/li[23]/label/input")
    page.click("xpath=//html/body/div/div[4]/div/div/form/fieldset[1]/ol/li[24]/label/input")

    print("5 seconds to check")
    page.wait_for_timeout(5000)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)
