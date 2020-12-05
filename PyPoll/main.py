# import csv module
import csv

# Defining variables, some set to 0 for later arguments
# Setting flag in order to skip first entry for average change calculation

Candidate_List = []
Vote_Count = []
Votes = 0
Most_Votes = 0

# Defining our csv Resource from Resources folder for reading

poll_data = "C:\\Python-Challenge\\PyPoll\\Resources\\election_data.csv"

# Reading csv file data, delimiting by commas, utf-8 needed for windows
# Used Next(csvreader) to skip first row of data which were headers

with open(poll_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # For each row in the csv, defining the first row as the month
    # and the second row as the current profit for each month

    for row in csvreader:

        Candidate = row[2]

        # Found Flag, used to skip the first entry for average change
        # calculation, every other row calculates the change between 
        # consecutive months and adds them to get the total

        if Candidate not in Candidate_List:
            Candidate_List.append(Candidate)
            Vote_Count.append(1)
        else:
            Vote_Count[Candidate_List.index(Candidate)] += 1
        
        Votes += 1

            # Comparing the change between each consecutive pair of months
            # in order to find which months had the greatest increase in
            # profit and the greatest decrease in profit


        # After each change calculation and comparison, set the current profit
        # to the previous profit to be used for next calculation.  Also counting
        # each month and adding together the total profit for all months
        

# After all changes calculated, find the average of the changes.
# Subtract one from total months since we did not need to find the change
# for the first month

# Printing in the format requested, print all calculations made.

print("\nElection Results")
print("--------------------------")
print(f'Total Votes: {Votes}')
print("--------------------------")

for can in Candidate_List:
    Total_Votes = Vote_Count[Candidate_List.index(can)]
    if Total_Votes > Most_Votes:
        Most_Votes = Total_Votes
        Winner = can

#print(f'{Candidate}:{Percentage}% ({Vote_Count})')
#print(f'{Candidate}:{Percentage}% ({Vote_Count})')
#print(f'{Candidate}:{Percentage}% ({Vote_Count})')
#print(f'{Candidate}:{Percentage}% ({Vote_Count})')      
#print("--------------------------")
print(f'Winner: {Winner}')
print("--------------------------")

# Set variable for output file

output_file = "C:\\Python-Challenge\\PyPoll\\Analysis\\election_analysis.txt"

#  Open the output file in the same format as printed in terminal

with open(output_file, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Total Votes: {Votes}\n')
    text_file.write("--------------------------\n")
    #text_file.write(f'{Candidate}:{Percentage}% ({Vote_Count})\n')
    #text_file.write(f'{Candidate}:{Percentage}% ({Vote_Count})\n')
    #text_file.write(f'{Candidate}:{Percentage}% ({Vote_Count})\n')
    #text_file.write(f'{Candidate}:{Percentage}% ({Vote_Count})\n')      
    #text_file.write("--------------------------\n")
    text_file.write(f'Winner: {Winner}\n')
    text_file.write("--------------------------\n")