import os
import webbrowser
from asyncore import read
from operator import index

import pandas as pd


def readXLSX(filename, column):
    path = os.path.join('C:\\Users\\Lee\\Downloads', filename+'.xlsx')
    data = pd.read_excel(path)
    df = pd.DataFrame(data, columns=[column])
    return df[column].tolist()


def readCSV(filename, column):
    path = os.path.join('C:\\Users\\Lee\\Downloads', filename+'.csv')
    data = pd.read_csv(path)
    df = pd.DataFrame(data, columns=[column])
    return df[column].tolist()


print("Is this a xlsx file(y/n):")
xlsx = input()
print("File Name(exclude file extension):")
filename = input()
print("Column Name:")
column = input()

if xlsx == 'y' or xlsx == 'Y':
    links = readXLSX(filename, column)
    print(links)
else:
    links = readCSV(filename, column)
    print(links)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  --profile-directory="Profile 4" %s'
for link in links:
    if link != '':
        webbrowser.get(chrome_path).open('https://www.eaglerider.com/agent/vehicle_reservations?rentalapp_reservation_number=' +
                                         link+'&reservation_identifier=&third_party_reservation_number=')
