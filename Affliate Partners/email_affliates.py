import os
from datetime import datetime, timedelta
from doctest import script_from_examples

import win32com.client

outlook = win32com.client.Dispatch('outlook.application').GetNamespace("MAPI")

folder = outlook.Folders("jlee@eaglerider.com")
affiliate = folder.Folders.Item('Affiliate')
messages = affiliate.Items

contacts = []
emails = []
for message in messages:
    if message.UnRead == True:
        message.UnRead = False
        for item in message.body.splitlines():
            if 'Contact Name:' in item:
                split_name = item.split(" ")
                name = split_name[2]
                contacts.append(name)
                # print(name)
            if 'Contact Email:' in item:
                split_name = item.split(" ")
                email = split_name[2]
                emails.append(email)
                # print(email)

outlook_create = win32com.client.Dispatch('outlook.application')
for index in range(len(contacts)):
    print("Preparing to send email to: "+contacts[index]+"("+emails[index]+")")
    mail = outlook_create.CreateItem(0)
    mail.To = emails[index]
    mail.Subject = 'New Affiliate Program Partner Request'
    mail.Body = "Hi "+contacts[index]+",\n\nThanks for your interest in our White Label Integration Program. With the White Label Integration, you would be placing our motorcycle reservation widget onto your webpage, which will allow your viewers to book their own motorcycle rental based on date and location. The commission structure is 10 % of the time and mileage on reservations.For more information regarding the process of white label integration, please visit the link below:\nhttps://sites.google.com/a/eaglerider.com/partners/white-label-widget-information-request\n\nPlease let me know if you are unable to access the links or have any questions or concerns."
    mail.Send()
    print("Email sent")
