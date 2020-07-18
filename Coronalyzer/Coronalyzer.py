#!/bin/python
import time
import os
import csv
import sys
from datetime import datetime
import dload
import matplotlib.pyplot as plt
import numpy as np


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
            if str(countryname) in row[2]:
                toearly = ['2019-12-31', '2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19', '2020-01-20', '2020-01-21', '2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25', '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29', '2020-01-30', '2020-01-31', '2020-02-01', '2020-02-02', '2020-02-03', '2020-02-04', '2020-02-05', '2020-02-06', '2020-02-07', '2020-02-08', '2020-02-09', '2020-02-10', '2020-02-11', '2020-02-12', '2020-02-13', '2020-02-14', '2020-02-15', '2020-02-16', '2020-02-17', '2020-02-18', '2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22', '2020-02-23', '2020-02-24', '2020-02-25', '2020-02-26', '2020-02-27', '2020-02-28', '2020-02-29', '2020-03-01']

                if len(countryname) == len(row[2]) and row[3] not in toearly :
                    date.append(str(row[3]))

                    newcases.append(str(row[4]))
        newcases = [x[:-2] for x in newcases]

    return newcases,date


#Graphs and shit

def show(country):
    data = []
    for i in range(0, len(country)):
        data.append(gethistoricalCountrydata(country[i]))
        colour = ['b','g','r','y']
        plt.plot(data[i][1],data[i][0], colour[i])

    print(data[0][1])

    plt.ylabel('Cases')
    plt.xlabel('Date')
    #plt.savefig('graph.png')
    plt.show()






# Dynamic HTML

def dynhtml(country=[]):
    dynindex = open("/var/www/html/Corona.html", "w")
    page = """
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


countrys = ['Germany','France','Italy']
show(countrys)


for i in range(1, len(args)):
    print(getCountrydata(args[i]))





# fuctions need to be worked on

# print(top3())
# print(getdata('Germany'))

# sum of people who died

countries = sys.argv


# dynhtml(countries)
# print(str(totaldeaths())+' <-- people have died')
