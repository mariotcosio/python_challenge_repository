# Import modules
import os 
import csv
# Set file path for csv file
with open("budget_data.csv") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter = ',')
    header = next(csvreader)
# defining variables
    total_months = 0
    total_rev = 0
    rev = []
    pre_rev = 0
    month_change = 0
    rev_change = 0
    greatest_increase = ["",0]
    greatest_decrease = ["",99999999]
    rev_change_list = []
    avg_rev = 0
#Total number of months and total revenue
    for row in csvreader:
        total_months += 1
        total_rev += int(row["Profit/Losses"])
#Average change in profits
        avgchange = int(row["Profit/Losses"]) - prevrev
        prevrev = int(row["Profit/Losses"])
        rev_change_list += [rev_change]
        month_change += [row["Date"]]
        # if something is > something else:
        if rev_change > greatest_increase[1]:
            greatest_increase[1] = rev_change
            greatest_increase[0] = row["Date"]
        if rev_change < greatest_decrease[1]:
            greatest_decrease[1] = rev_change
            greatest_decrease[0] = row["Date"]
    avg_rev = sum(rev_change_list)/len(rev_change_list)

# set output file path

# Print answer
print("Financial Analysis")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_rev))
print("Average Change: " + "$" + str(avg_rev))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) +")")
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) +")")
# Save to text file
with open(text, "w") as text_file
    text_file.write("Total Months: " + str(total_months))
    text_file.write("Total Revenue: " + "$" + str(total_rev))
    text_file.write("Average Change: " + "$" + str(avg_rev))
    text_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) +")")
    text_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) +")")

