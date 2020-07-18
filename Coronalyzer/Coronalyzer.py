#!/bin/python
import time
import git
import os
import csv
import sys
from datetime import datetime


datarepo = "https://github.com/CSSEGISandData/COVID-19"
#https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports



#Default Output format
def log(text):
    line = '---->'
    print(line,text)



#load data from repo
#try:
#    log('getting data')
#    log('trying to clone')
#    git.Git().clone(datarepo)
#except: log('data exists already')



#pass arguments
args = sys.argv




#get the newest file in a path
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)




#open newest daily reort
dailyrepopath = newest('./COVID-19/csse_covid_19_data/csse_covid_19_daily_reports')



def gethistoricCountrydata(countryname):
    with open(dailyrepopath) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
             if countryname in row[11]:
                 if len(countryname) == len(row[11]):
                    return 'Date ','Infected ',row[7]



#gives value of Country namme
def getCountrydata(countryname):
    with open(dailyrepopath) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
             if countryname in row[11]:
                 if len(countryname) == len(row[11]):
                    percentage = int(row[8])/int(row[7])
                    return 'Country ',row[11],'Infected ',row[7],'Dead ',row[8] ,'ratio ',percentage


def getdata(countryname):
    
    basepath = './COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'
    country = []

    for file in os.listdir('./COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'):
        if file == 'README.md' or file == '.gitignore':
            continue
        else: 
            with open(basepath+file) as csvfile:
                readcsv = csv.reader(csvfile, delimiter=',')
                for row in readcsv:
                    try:
                        row[11]
                        if countryname in row[11]:
                            if len(countryname) == len(row[11]):
                                country.append(int(row[11]))
                    except:
                        log('Exceptionj')
    return len(country)





def top3():
    with open(dailyrepopath) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        i=0
        countrydata = [['test','test']]
        for row in readcsv:
            if row[8] == 0 or row[8] == 'Deaths':
                continue
            else:
                countrydata.append([[row[8],row[11]]])
    del countrydata[0]
    countrydata = sorted(countrydata,key=lambda x: x[0])
    return countrydata

# Dynamic HTML

def dynhtml(country =  []):
    dynindex = open("/var/www/html/Corona.html","w")
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
    entry = blank_entry_headline.format(data[0],data[2],data[4],data[6])
    
    for i in range(0,len(country)):
        data = getCountrydata(country[i])
        entry = entry + blank_entry.format(data[1],data[3],data[5],data[7])
    page = page.format(datetime.now(),entry)

    
    
    dynindex.write(page)
    print("Corona HTML created")
    dynindex.close()






#sums up deaths
def totaldeaths():
    with open(dailyrepopath) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        country = []
        total = 0
        for row in readcsv:
            country = row[8]
            try:
                total = total+int(row[8])
            except: continue
        return total

###########################################
# end of definition block

for i in range(1,len(args)):
    print(getCountrydata(args[i]))


#fuctions need to be worked on

#print(top3())
#print(getdata('Germany'))

#sum of people who died

countries = sys.argv
countries[0] = "Germany"

dynhtml(countries)
print(str(totaldeaths())+' <-- people have died')
