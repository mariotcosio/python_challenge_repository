# Import modules
import os
import csv

# Determine variables
total_votes = 0
khan = 0
correy = 0 
li = 0 
otooley = 0

# Open path for csv
with open(election_data.csv) as election_data
    csvreader = csv.reader(election_data, delimiter = ",")
    header = next(csvreader)
for row in csv reader:
# Count total and individual votes    
    total += 1
    if row [2] == "Khan":
        khan +=1
    elif row[2] == "Correy":
        correy += 1
    elif row[2] == "Li":
        li += 1
    elif row[2] == "O'Tooley":
        otooley +=1
 # Print percent votes
 khan_percent = (khan/total_votes) * 100
 correy_percent = (correy/total_votes) * 100
 li_percent = (li/total_votes) * 100
 otooley_percent = (otooley/total_votes) * 100


