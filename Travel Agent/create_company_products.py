from datetime import datetime


def create_company_products(page, company_name):
    products = ['Bike', 'Guided Tour', 'Self Drive Tour']

    for product in products:
        page.goto("https://www.eaglerider.com/activeadmin/company_products/new")
        page.locator("select[name=\"company_product[company_id]\"]").select_option(label=company_name)
        page.locator("select[name=\"company_product[product_id]\"]").select_option(label=product)
        page.fill("input[name=\"company_product[start_date]\"]", datetime.today().strftime('%Y-%m-%d'))

        page.fill("input[name=\"company_product[end_date]\"]", "2050-12-31")
        if product == 'Bike':
            page.locator("select[name=\"company_product[commission_calculation_method_id]\"]").select_option(value="1")
        else:
            page.locator("select[name=\"company_product[commission_calculation_method_id]\"]").select_option(value="2")

        page.fill("input[name=\"company_product[commission_percentage]\"]", "10")
        page.locator("select[name=\"company_product[commission_currency_code]\"]").select_option(value="USD")

        page.click("xpath=//html/body/div[1]/div[2]/div[1]/h2")

        print("5 seconds to check")
        page.wait_for_timeout(5000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)
