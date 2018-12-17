import csv
import os
import collections as ct


voteList = []
candidatelist = []


pollcsv = os.path.join( "election_data.csv" )
    
with open (pollcsv,"r") as file: 
    reader = csv.reader(file,delimiter=',') 
    
    votes = ct.Counter()
    header = next(reader)
    #c = Counter(votes)
    
    for row in reader:
        voteList.append(1) #appends 1 to the end of each row        
        candidatelist.append(row[2]) #adds candidates to candidatelist
        candidate = row[-1] #counts votes by candidate, not sure exactly how, found this option by googling
        votes[candidate] += 1
        

        
        
    totalvotes = sum(voteList) #counts all the 1's to get a total of votes
    percent = {key: value/totalvotes * 100 for key, value in votes.items()}
    winner = max(percent, key=percent.get)
    summary = ([(totalvotes, str(round(count / sum(votes.values()) * 100.0, 3)) + '%') for totalvotes, count in votes.most_common()])
   
    
        
    
    
#myset = set(candidatelist) #using set to get a unique list of candidates 
#print(myset)
#votes.most_common() #provides totals for each candidate
#print(winner)

print("Election Results")
print("Total Votes: " + str(totalvotes))
print("Total votes per candidate: " + str(votes.most_common())) #I cannot figure out how to concatenate the votes and percent
print("Percent of total votes: " + str(summary))
print("Winner: " + winner)

file = open("PyPoll_Summary.txt","w")
    
file.write("Election Results"+"\n")
file.write("Total Votes: " + str(totalvotes)+"\n")
file.write("Total votes per candidate: " +  str(votes.most_common())+"\n")
file.write("Percent of total votes: " + str(summary)+"\n")
file.write("Winner: "+ winner + "\n")
   
      
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
    
  