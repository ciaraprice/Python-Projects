#!/usr/bin/python
hyphens = ""
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#add a line of hyphens the same length of Belgium string
for iteration in range(len(Belgium)): #can also just use Belgium no need for range or len
    #hyphens = hyphens + "-"
    print("-", end="")
print()

#add the string with the comma seperators replaced by colons ':'
print(Belgium.replace("," , ":"))

#followed by the population of Belgium plus the population of capital city

belgiumArray = Belgium.split(",") #spilt returns an array
#print (belgiumArray)

totalPop = int(belgiumArray[1]) + int(belgiumArray[3])
print (totalPop)