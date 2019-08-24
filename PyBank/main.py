# Import modules
import os 
import csv

# Create file path
csv_file = os.path.join("budget_data.csv")

# Create lists for months and revenue
months = []
revenue = []

# Open csv 
with open(csv_file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

# Total Months
total_months = len(months)

# Loop through revenue to determine greatest increase and decrease of revenue
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0

for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        max_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        min_month = months[r]
    total_revenue += revenue[r]

# Calculate the average change
avg_change = round(total_revenue/total_months, 2)

# set path for output file
output_file = os.path.join('output.txt')

# open file in write mode and print summary
with open(output_file, 'w') as writefile:
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("Total Months: " + str(total_months) + "\n")
    writefile.writelines("Total Revenue: " + "$" + str(total_revenue) + "\n")
    writefile.writelines("Average Revenue Change: " + "$" + str(avg_change) + "\n")
    writefile.writelines("Greatest Increase in Revenue: " + max_month + "$" + str(greatest_increase) + "\n")
    writefile.writelines("Greatest Decrease in Revenue: " + min_month+ "$" + str(greatest_decrease) + "\n")

# Open file in r mode, print to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())



