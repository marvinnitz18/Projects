

import sys
args = sys.argv

f = open("input.txt","rt")

def find(name):
    lines = f.readlines()
    Datum = []
    Name = []
    
    for line in lines:
        
        line = line[:-1]

        if line.isalpha() == True:
            line = line.lower()
            line = line.capitalize()
            
            Name.append(str(line))
        else:
            Datum.append(str(line))
    
    search = Name.index(name) 
    
#    for Vorname in Name:
        


    return Name[int(search)] +' : '+ Datum[int(search)]
    
try:
    print(find(args[1]))
except:
    print('Error!')
