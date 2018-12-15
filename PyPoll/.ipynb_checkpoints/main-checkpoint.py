import csv
import os

voteList = []
candidatelist = []
total = []
    
with open ("data.csv","r") as file: 
    reader = csv.reader(file)  
    
    header = next(reader)
    
    for row in reader:
        voteList.append(1)
        candidatelist.append(1)
        total.append(row)
        
    totalvotes = sum(voteList)
    
    print(totalvotes)

