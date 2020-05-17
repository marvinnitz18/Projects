

import sys

args = sys.argv

f = open("input.txt","r")
lines = f.readlines()

def find(name):
    
    Datum = []
    Name = []

    if len(Name) == 0:
        
        for line in lines:
            line = line[:-1]

            if line.isalpha() == True:
                line = line.lower()
                line = line.capitalize()
                Name.append(str(line))
            else:
                Datum.append(str(line))
    else:
        print("Name len is over 0")
    
    search = Name.index(name) 
    return Name[int(search)] +' : '+ Datum[int(search)]

######################################

#cleaning up args input

for i in range(0,len(args)):
    args[i] = str(args[i]).lower()
    args[i] = str(args[i]).capitalize()

#######################################

#call functions




try:
#    print(find(args[1]))

    for i in range(1,len(args)):
        arg = str(args[i])
        print(find(arg))


except:
    print('Error!')
