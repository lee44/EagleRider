def create_referral(page, company_name, company_code, email):
    page.goto("https://www.eaglerider.com/activeadmin/referrals/new")

    page.fill("input[name=\"referral[name]\"]", company_name)
    page.fill("input[name=\"referral[company_name]\"]", company_name+" White Label")
    page.fill("input[name=\"referral[company_code]\"]", company_code)
    page.fill("input[name=\"referral[email]\"]", email)
    page.fill("input[name=\"referral[commission]\"]", "10")
    page.fill("input[name=\"referral[widget_height]\"]", "460")
    page.fill("input[name=\"referral[widget_width]\"]", "395")
    page.fill("input[name=\"referral[parent_div_id]\"]", "divWidget")
    page.locator("select[name=\"referral[company_id]\"]").select_option(label=company_name+" White Label")
    page.click("xpath=//html/body/div/div[4]/div/div/form/fieldset[1]/ol/li[22]/label/input")

    print("5 seconds to check")
    page.wait_for_timeout(5000)
    page.click("input[name=\"commit\"]")
    page.wait_for_timeout(1000)
