import csv
f=open("emp.csv",'r')
r=csv.reader(f) #returns csv reader object
data=list(r)
for line in data:
    if line[2]>"3500": print(line[0],line[1],line[2]) 
       
