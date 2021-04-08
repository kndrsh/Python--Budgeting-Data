# -*- coding: utf-8 -*-
"""
Created on Wed March 31 17:24:26 2021

@author: kndrsh
"""
# import modules to read budget data csv file 
import os
import csv

# create empty lists to be able to iterate data 
total_months = []
total_profit = []
monthly_profit_change = []

with open('budget_data.csv','r') as csv_file :
    csv_reader = csv.reader(csv_file,delimiter =",")
    
    skip_header=(next(csv_reader))
   # total months 
    for row in csv_reader :
        total_months.append(row[0])
        total_profit.append(row[1])
        print(len(total_months))
       
        
    
    






    
    