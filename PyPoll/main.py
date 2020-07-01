#Homework 3 - PyPoll

import os
import csv

# Set path for the Budget Data CSV file
csvpath = os.path.join("..", "PyPoll", "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
results = os.path.join("..", "PyPoll", "analysis", "output.txt")


#Find the Total Number of Votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_votes = len(list(csvreader)) - 1

#Set the variables
candidates = []
candidate_counter = []

#Find out who the candidates are
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        
        if (str(row[2])) not in candidates:
            candidates.append (str(row[2]))

    #Name the variables for the candidates name
    candidate_1 = candidates[0]
    candidate_2 = candidates[1]
    candidate_3 = candidates[2]
    candidate_4 = candidates[3]

#Find out how many votes each candidate got
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        candidate_counter.append(str(row[2]))

    candidate_1_votes = 0
    candidate_2_votes = 0
    candidate_3_votes = 0
    candidate_4_votes = 0
    
    for people in candidate_counter: 
        if people == candidate_1: 
            candidate_1_votes = candidate_1_votes + 1
        if people == candidate_2: 
            candidate_2_votes = candidate_2_votes + 1   
        if people == candidate_3: 
            candidate_3_votes = candidate_3_votes + 1
        if people == candidate_4: 
            candidate_4_votes = candidate_4_votes + 1   

#Calculate the percentage of votes each candidate got

candidate_1_percentage = candidate_1_votes / total_votes * 100
candidate_2_percentage = candidate_2_votes / total_votes * 100
candidate_3_percentage = candidate_3_votes / total_votes * 100
candidate_4_percentage = candidate_4_votes / total_votes * 100

#Find out who the winner is

if candidate_1_votes > candidate_2_votes and candidate_1_votes > candidate_3_votes and candidate_1_votes > candidate_4_votes:
    winner = candidate_1

elif candidate_2_votes > candidate_3_votes and candidate_2_votes > candidate_4_votes:
    winner = candidate_2

elif candidate_3_votes > candidate_4_votes:
    winner = candidate_3

else:
    winner = candidate_4


output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"{candidate_1}: {candidate_1_percentage:.3f}% ({candidate_1_votes})\n"
    f"{candidate_2}: {candidate_2_percentage:.3f}% ({candidate_2_votes})\n"
    f"{candidate_3}: {candidate_3_percentage:.3f}% ({candidate_3_votes})\n"
    f"{candidate_4}: {candidate_4_percentage:.3f}% ({candidate_4_votes})\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")

print(output)

# Export the results to text file
with open(results, "w") as txt_file:
    txt_file.write(output)