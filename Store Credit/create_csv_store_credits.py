import os
import re
from operator import index

import pandas as pd

# print("File Name(include .txt): ")
# file = input()

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', 'store_credits_v2.txt'))

strip_list = [line.rstrip('\n|') for line in open(abs_path)]
strip_list = list(filter(None, strip_list))
strip_list = list(filter(lambda text: not '|' in text, strip_list))

# print(strip_list)

store_credits = []
reservations = []
emails = []
claim_codes = []
amounts = []
expires = []
extensions = []

reservations_pattern = r'[A-Z]{0,9}[0-9]{12,12}'
emails_pattern = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
claim_codes_pattern = r'[A-Z0-9]{4,4}-[A-Z0-9]{4,4}-[A-Z0-9]{4,4}-[A-Z0-9]{4,4}'
amounts_pattern = r'\$?\s?[\d,]+(?:.(\d+))?'
expires_pattern = r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{3,4}'
extensions_pattern = r'[0-9]{1,2}\s*(mo|ye){1,1}'

# re.compile() method compiles a regex pattern into a regex object. It's mostly used for efficiency reasons, when we plan on matching the pattern more than once.
reservations_regex = re.compile(reservations_pattern)
email_regex = re.compile(emails_pattern)
claim_code_regex = re.compile(claim_codes_pattern)
amounts_regex = re.compile(amounts_pattern)
expires_regex = re.compile(expires_pattern)
extensions_regex = re.compile(extensions_pattern)

for index, value in enumerate(strip_list):
    match_reservation = re.search(reservations_regex, value)
    if(match_reservation):
        reservations.append(match_reservation.group())
        continue
    if(re.fullmatch(email_regex, value)):
        emails.append(value)
        continue
    if(re.fullmatch(claim_code_regex, value)):
        claim_codes.append(value)
        continue
    if(re.fullmatch(amounts_regex, value)):
        amounts.append(value[1:].replace(',', ''))
        continue
    if(re.fullmatch(expires_regex, value)):
        if(re.fullmatch(amounts_regex, strip_list[index - 1])):
            expires.append(value)
        continue
    if(re.fullmatch(extensions_regex, value)):
        extensions.append(value)
        continue

store_credits.append(reservations)
store_credits.append(emails)
store_credits.append(claim_codes)
store_credits.append(amounts)
store_credits.append(expires)
store_credits.append(extensions)

# print(store_credits)

df = pd.DataFrame(store_credits).transpose()
df.columns = ['Res #', 'Email', 'Claim Code', 'Amount', 'Expired', 'Extension']
df['Extension'].fillna(value='1 year', inplace=True)
# print(df)
print(strip_list)

store_credit_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', 'store_credits2.csv'))
df.to_csv(store_credit_path, index=False, header=True)
