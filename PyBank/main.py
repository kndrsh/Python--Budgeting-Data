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
        
       
        
        
        # monthly change in profits ( c will represent change)
        # have to use for loop to iterate through the profits to get monthly change
        
        for c in range(len(total_profit)-1):
            monthly_profit_change.append(int(total_profit[c+1])- int(total_profit[c]))
            
            #Finding Greatest Increase & Greatest Decrease (Profits)
            # Can use the max & min function 
            
            max_greatest_increase = max(monthly_profit_change)
            max_greatest_decrease = min(monthly_profit_change)
            
            
            max_greatest_increase_month = monthly_profit_change.index(max(monthly_profit_change)) +1
            max_greatest_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) +1
            
            # Print Statements 
            print("Financial Analysis")
            print("---------------------------------")
            print(f"Total months: {len(total_months)}")
            print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
            print(f"Greatest Increase In Profits: {total_months[max_greatest_increase_month]} (${(str(max_greatest_increase))})") 
            print(f"Greatest Decrease In Profits: {total_months[max_greatest_decrease_month]} (${(str(max_greatest_decrease))})") 
            
            
       # Export the results to text file
budget_data_export = "analysis/budget_data.txt"
with open(budget_data_export, "w") as txt_file:
    txt_file.write()
            
       
        
    
    






    
    