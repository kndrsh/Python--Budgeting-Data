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
    
    for row in csv_reader:
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
        # Total # of votes 
        total_votes = (len(votes))
        print(total_votes)
        
        # Votes per person 
        for candidate in candidates: 
            if candidate == "Khan":
                khan.append(candidates)
                total_khan_votes = len(khan)
            elif candidate == "Correy":
                correy.append(candidates)
                correy_votes = len(correy)
            elif candidate == "Li":
                li.append(candidates)
                total_li_votes = len(li)
            else:
                otooley.append(candidates)
                total_otooley_votes = len(otooley)
                
                print(correy_votes)
                print(total_khan_votes)
                print(total_li_votes)
                print(total_otooley_votes)
                
                
                
                
        
      