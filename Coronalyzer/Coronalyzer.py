#!/bin/python
import time
import os
import csv
import sys
from datetime import datetime
import dload
import matplotlib.pyplot as plt


# Default Output format
def log(text):
    line = '---->'
    print(line, text)


# load data from repo
try:
    log('getting data')
    dload.save('https://covid.ourworldindata.org/data/owid-covid-data.csv', 'COVID-19.csv')
except:
    log('data exists already')

# pass arguments
args = sys.argv


# gives value of Country namme
def getCountrydata(countryname):
    with open('./COVID-19.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        data = []
        for row in readcsv:
            if countryname in row[2]:
                if len(countryname) == len(row[2]):
                    d = str(row[2]), str(row[5])
                    data.append(d)
    return data[len(data) - 1]


def gethistoricalCountrydata(countryname):
    with open('./COVID-19.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        date = []
        newcases = []
        for row in readcsv:
            if countryname in row[2]:
                if len(countryname) == len(row[2]):
                    d = str(row[2]), str(row[5])
                    date.append(str(row[3]))
                    newcases.append(str(row[5]))
        plt.plot(date,newcases,'r')
        plt.xlabel('Date')
        plt.ylabel('Infected')
        plt.savefig('graph.png')
        # plt.show()
    return newcases

# Dynamic HTML

def dynhtml(country=[]):
    dynindex = open("/var/www/html/Corona.html", "w")
    page = """
<!DOCTYPE html>
<html lang="de">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="/index.css" media="screen" />
<title>Raspberry Pi</title>
<link rel="icon" href="https://img.icons8.com/carbon-copy/2x/instagram-new.png">
</head>
<body class="background">
<div class="navbar" width="5000px" background-color=green>
        <a href="/">Home</a>
        <a href="/nextcloud">Nextcloud</a>
        <a href="https://flexonmyex.de:4200">Shell</a>
        <a href="/access_log.html">Access Log</a>
</div>
<div>
<p>Updatet at: {}</p>
<table style="color:white; width:100% ;font-family:Arial ; font-size:200%">
{}
</table>
</div>

</body>
"""

    blank_entry = """<tr> <th>{}</th>  <th><i>{}</i></th>  <th><i>{}</i></th>  <th><i>{}<i></th> </tr>"""
    blank_entry_headline = """<tr> <th>{}</th>  <th>{}</th>  <th>{}</th>  <th>{}</th> </tr>"""

    data = getCountrydata(country[0])
    entry = blank_entry_headline.format("Country", "New_cases")

    for i in range(0, len(country)):
        data = getCountrydata(country[i])
        entry = entry + blank_entry.format(data[0], data[1])
    page = page.format(datetime.now(), entry)

    dynindex.write(page)
    print("Corona HTML created")
    dynindex.close()


###########################################
# end of definition block

for i in range(1, len(args)):
    print(getCountrydata(args[i]))
print(gethistoricalCountrydata("Germany"))

# fuctions need to be worked on

# print(top3())
# print(getdata('Germany'))

# sum of people who died

countries = sys.argv
countries[0] = "Germany"

# dynhtml(countries)
# print(str(totaldeaths())+' <-- people have died')
