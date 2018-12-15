import csv

datelist[]
profitlosslist[]
total = []
    
with open ("data.csv","r") as file: 
    reader = csv.reader(file)  
    
    header = next(reader)
            
    for row in reader:
        profitlossList.append(float(row[1]))
        dateList.append(1)
        total.append(row)