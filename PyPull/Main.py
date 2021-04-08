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
    
    for row in csv_reader:
        votes.append((row[0]))
        print(votes)
        county.append(row[1])
        candidates.append(row[2])
        
        # Total # of votes 
        total_votes = (len(votes))
        print(total_votes)
        
  
        
        # Votes per person 
        for candidate in candidates: 
            if candidate == "khan":
                khan.append(candidates)
                total_khan_votes = len(khan)
                
            elif candidate == "correy":
                correy.append(candidates)
                total_correy_votes = len(correy)
                
            elif candidate == "li":
                li.append(candidates)
                total_li_votes = len(li)
                
            else:
                otooley.append(candidates)
                total_otooley_votes = len(otooley)
                
         
                      #Percentage of Votes 
        khan_percent = round(((total_khan_votes / total_votes) * 100), 2)
        correy_percent = round(((total_correy_votes / total_votes) * 100), 2)
        li_percent = round(((total_li_votes / total_votes) * 100), 2)
        otooley_percent = round(((total_otooley_votes / total_votes) * 100), 2)
    print(khan_percent)
    print(correy_percent)
    print(li_percent)
    print(otooley_percent)
                
    #Winner 
                
                
                
        
      