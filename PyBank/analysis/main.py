##Homework 3 - Pybank

import os
import csv

# Set path for the Budget Data CSV file
csvpath = os.path.join("..", "PyBank", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
results = os.path.join("..", "PyBank", "analysis", "output.txt")


#Find out how many months (rows) are in the CSV, subtracting the header row. Then, print Total Months.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    total_months = len(list(csvreader)) - 1


#Find the net total amount of "Profit/Losses"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Define variables and set to 0 to start
    total_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    spends = []
    dates = []
    dates_spends = []


    #Skip the first row in the CSV
    next(csvreader)

    #Find the sum of the Profit/losses
    for row in csvreader:
        total_profit = float((row[1])) + total_profit
        spends.append(float(row[1]))
        dates.append(str(row[0]))
    
#Find the average change

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    start = 0
    next_start = 1
    next_month_spend = []    

    for spend_list in range(next_start, total_months):
        next_month_spend.append (spends[spend_list])

    average_change = []

    zip_object = zip(spends, next_month_spend)
    for spends_i, next_month_spend_i in zip_object:
        average_change.append(next_month_spend_i-spends_i)


    #Use a mean function to find the average of the "average_change" list 
    from statistics import mean 
    
    def Average(average_change): 
        return mean(average_change) 
    
    average = Average(average_change)


    #Find the maximum & minimum of the "average_change" list
    greatest_increase = int(max(average_change))
    greatest_decrease = int(min(average_change))


    ######Loop through the CSV once again to find the dates that the greatest increase/decrease are associated to

    #Find what line the greatest increase happened on
    index = average_change.index(int(greatest_increase))

    #The average change line starts one row down, so add 1 to the index to find the date the increase occured on
    greatest_increase_date = dates[index + 1]

    #Find what line the greatest decrease happened on
    index = average_change.index(int(greatest_decrease))

    greatest_decrease_date = dates[index + 1]

output = (
    #Set the header for the Terminal output
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total_profit:.0f}\n"
    f"Average  Change: ${average:.2f}\n" 
    f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})")

print(output)


    # Export the results to text file
with open(results, "w") as txt_file:
    txt_file.write(output)


    


  