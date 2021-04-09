# import modules to load csv data

import csv

with open('election_data.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter =",")
    
    # Declare your variables 
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []
    total_khan_votes = 0 
    total_correy_votes = 0
    total_li_votes = 0
    total_otooley_votes = 0
    candidate = 0
    
    for row in csv_reader:
        votes.append((row[0]))
        county.append(row[1])
        candidates.append(row[2])
        
        # Total # of votes 
        total_votes = (len(votes))
    
        
    
        # Votes per person 
        for candidate in candidates: 
           
            if candidate == "khan":
                #khan.append(candidates)
                total_khan_votes += 1
                
            elif candidate == "correy":
               # correy.append(candidates)
               total_correy_votes+= 1
                
            elif candidate == "li":
               # li.append(candidates)
                total_li_votes += 1
                
            else:
               # otooley.append(candidates)
                total_otooley_votes += 1
               

                      #Percentage of Votes 
khan_percent = round(((total_khan_votes / total_votes) * 100), 2)
correy_percent = round(((total_correy_votes / total_votes) * 100), 2)
li_percent = round(((total_li_votes / total_votes) * 100), 2)
otooley_percent = round(((total_otooley_votes / total_votes) * 100), 2)

    #Winner 
if khan_percent > max(correy_percent, li_percent, otooley_percent):
    winner = "Khan"
elif correy_percent > max(khan_percent, li_percent, otooley_percent):
    winner = "Correy"  
elif li_percent > max(correy_percent, khan_percent, otooley_percent):
    winner = "Li"
else:
    winner = "O'tooley"

                
print("Election Results}") 
print("-----------------------------------")     
print (f"Total Votes : {total_votes}")
print("winner : " + winner)  
print (f" Khan: {khan_percent} ({total_khan_votes}) ")
print(f"coorey : {correy_percent} ({total_correy_votes}) ")
print(f"Li : {li_percent} ({total_li_votes}) ")
print(f"O'tooley' : {otooley_percent} ({total_otooley_votes}) ")


print("Election Results}", file=open("output.txt","a")) 
print("-----------------------------------", file=open("output.txt","a"))     
print (f"Total Votes : {total_votes}", file=open("output.txt","a"))
print("winner : " + winner, file=open("output.txt","a"))  
print (f" Khan: {khan_percent} ({total_khan_votes}) ", file=open("output.txt","a"))
print(f"coorey : {correy_percent} ({total_correy_votes}) ", file=open("output.txt","a"))
print(f"Li : {li_percent} ({total_li_votes}) ", file=open("output.txt","a"))
print(f"O'tooley' : {otooley_percent} ({total_otooley_votes}) ", file=open("output.txt","a"))              
        
      