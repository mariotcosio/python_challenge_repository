# Import modules and set file path for csv
import os
import csv
csv_file = os.path.join("election_data.csv")

# Create a dictionary for candidates and votes
poll = {}
candidates = []
number_votes = []
total_votes = 0
vote_percentage = []

# Open csv file
with open(csv_file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    # Create a dictionary for votes
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] += 1
        else:
            poll[row[2]] = 1

# Put Dictionary keys into lists
for key, value in poll.items():
    candidates.append(key)
    number_votes.append(value)
for n in number_votes:
    vote_percentage.append(round(n/total_votes*100, 1))
# put dictionaries into tuples
poll_data = list(zip(candidates, number_votes, vote_percentage))

# create winner as a list
winner_list = []
for name in poll_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print to file then print to terminal
output_file = os.path.join("output.txt")
with open(output_file, 'w') as txtfile:
    txtfile.writelines("Election Results")
    txtfile.writelines("Total votes: " + str(total_votes))
    for entry in poll_data:
        txtfile.writelines(entry[0] +":" + str(entry[2]) + "% ("+ str(entry[1]) + ")\n")
    txtfile.writelines("Winner" + winner)

with open(output_file, 'r') as readfile:
    print(readfile.read())






