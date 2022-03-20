import sys
from datetime import date
from os.path import abspath, dirname

import requests
import win32com.client
from bs4 import BeautifulSoup

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from Utilities.util import Util

util = Util()


def email_affiliate_code_snippet(email):

    print("Referral #: ")
    referral = input()
    print("Enter contact name: ")
    contact = input()

    url = 'https://www.eaglerider.com/activeadmin/referrals/' + referral

    response = requests.get(url, headers=util.get_headers())

    soup = BeautifulSoup(response.content, features="lxml")

    company = soup.select(".row.row-name > td")[0].find(text=True, recursive=False)
    # email = soup.select(
    #     ".row.row-email > td > a")[0].find(text=True, recursive=False)
    code_snippet = soup.select(
        ".row.row-code_snippet > td")[0].find(text=True, recursive=False)

    utm_company = company.replace(" ", "+")
    utm_code_snippet = code_snippet.replace("<a href='http://www.eaglerider.com/", "<a href='http://www.eaglerider.com/?utm_source=affiliate&utm_medium=whitelabel&utm_campaign=" + utm_company)

    outlook_create = win32com.client.Dispatch('outlook.application')

    # New Draft emails are put under Unread
    mail = outlook_create.CreateItem(0)
    mail.To = email
    mail.Subject = 'New Affiliate Program Partner Request'
    mail.Body = "Hi " + contact + ",\n\nYour code snippet is ready, please give the code below to your web developers:\n\n" + utm_code_snippet + \
        "\n\nThe anchor tag that links to EagleRider is mandatory so please do not remove it.\n\nIf you have any questions, let me know."
    mail.Send()
    # mail.Save()
    print("Email sent to: " + contact + " with email: " + email)
