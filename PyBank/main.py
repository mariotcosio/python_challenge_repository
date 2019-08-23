# Import modules
import os 
import csv
# Write a function that does:
# names a variable as csv
def gethestuff(csv):
    # defining variables
    months=0
    total=0
    maxrevenue=0
    minrevenue=0
    avgchange=0
    # "" indicates a string
    maxmonth = ""
    minmonth = ""
    # row is located in csv, looping through row
    for row in csv:
        current_month = row[0]
        pnl = row[1]
        total += pnl
        #Number of months
        months += 1
       # if something is > something else:
            #do something
        # this makes the highest amount of revenue as the max while it goes through the loop
        if pnl > maxrevenue:
            maxrevenue = pnl
            maxmonth = current_month
    return [months, total, maxrev, minrev, avgchange]
# print(total) will show total revenue
 

# Greatest profit and month


# Greatest Loss and month
# Average Change
# Greatest Month
#set input file path
#Open the file
# Read Source file
with open(path) as file:
    csvreader = csv.reader(file, delimiter = ',')
    header = next(csvreader)
    analysis = getthestuff(csvreader)
print(analysis[0])

# set output file path
# Print answer    
print(total)
# Save to text file