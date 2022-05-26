from datetime import datetime


def create_product_credit_terms(page):
    print("Enter the biggest Company Product ID for that company: ")
    company_product_id = int(input())

    for i in range(3):
        page.goto("https://www.eaglerider.com/activeadmin/company_product_credit_terms/new")
        page.fill("input[name=\"company_product_credit_term[company_product_id]\"]", str(company_product_id))

        if i != 1:
            page.fill("input[name=\"company_product_credit_term[due_days]\"]", "30")
        else:
            page.fill("input[name=\"company_product_credit_term[due_days]\"]", "60")

        page.locator("select[name=\"company_product_credit_term[calculation_method_id]\"]").select_option(label="Before Pickup")
        page.fill("input[name=\"company_product_credit_term[start_date]\"]", datetime.today().strftime('%Y-%m-%d'))
        page.fill("input[name=\"company_product_credit_term[end_date]\"]", "2050-12-31")
        print("5 seconds to check")
        page.wait_for_timeout(5000)
        page.click("input[name=\"commit\"]")
        page.wait_for_timeout(1000)
        company_product_id -= 1
