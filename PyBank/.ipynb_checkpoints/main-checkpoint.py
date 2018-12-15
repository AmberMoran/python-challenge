#import os
import csv

#csvpath = os.path.join("python-challenge"/"PyBank","03-Python_Homework_PyBank_Resources_budget_data.csv")

#with open(csvpath, newline="") as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
with open ("data.csv","r") as file: 
    reader = csv.reader(file) 
print(reader)
    
    #for row in csvreader:
     #   if row[0] == date:
      #    print(row(1))

#

    #months = 0
    
    #for row in reader:
      #date = row["date"]
      #print("date")
      