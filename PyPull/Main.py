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
        
        # number of votes
        total_votes = (len(votes))
        print(total_votes)
        
        