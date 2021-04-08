# import modules to load csv data
import os
import csv

with open('election_data.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter =",")