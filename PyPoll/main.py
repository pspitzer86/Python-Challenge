# import csv module
import csv

# Create two empty lists to append candidates and their vote counts
# Defining variables set to zero for later arguments/comparisons

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

    # For each row in the csv, defining the 3rd entry in esch row as Candidate

    for row in csvreader:

        Candidate = row[2]

        # Checking if candidate is in the list, if not in the list
        # add into list and start their vote count with 1 so indecies 
        # are associated between the two lists.  If already in list
        # add another vote to the appropriate index in list.  Then count
        # each row to get the total amount of votes

        if Candidate not in Candidate_List:
            Candidate_List.append(Candidate)
            Vote_Count.append(1)
        else:
            Vote_Count[Candidate_List.index(Candidate)] += 1
        
        Votes += 1


# Printing in the format requested, print header and total votes counted.

print("\nElection Results")
print("--------------------------")
print(f'Total Votes: {Votes}')
print("--------------------------")

# Looping through the candidate list and checking the associated vote count
# Comparing the vote counts to see who has the most and is therefore the
# winna-mon like cinnamon.  Percent vote calculated by taking the Vote count
# from list associated with each candidate and divide by the total votes.
# The print line is alos included in the loop to print all necessary values.
# Format the percents to correct decimal places.

for can in Candidate_List:
    Total_Votes = Vote_Count[Candidate_List.index(can)]
    if Total_Votes > Most_Votes:
        Most_Votes = Total_Votes
        Winner = can
    Percent_Vote = format((Vote_Count[Candidate_List.index(can)]/Votes) * 100, ".3f")

    print(f'{can}:{Percent_Vote}% ({Vote_Count[Candidate_List.index(can)]})')

# Print the winner and format lines    
         
print("--------------------------")
print(f'Winner: {Winner}')
print("--------------------------")

# Set variable for output file

result_file = "C:\\Python-Challenge\\PyPoll\\Analysis\\election_analysis.txt"

# Open the output file in the same format as printed in terminal, loop
# needed again for Percent Change lines.

with open(result_file, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Total Votes: {Votes}\n')
    text_file.write("--------------------------\n")

    for can in Candidate_List:
        Total_Votes = Vote_Count[Candidate_List.index(can)]
        if Total_Votes > Most_Votes:
            Most_Votes = Total_Votes
            Winner = can
        Percent_Vote = format((Vote_Count[Candidate_List.index(can)]/Votes) * 100, ".3f")

        text_file.write(f'{can}:{Percent_Vote}% ({Vote_Count[Candidate_List.index(can)]})\n')
     
    text_file.write("--------------------------\n")
    text_file.write(f'Winner: {Winner}\n')
    text_file.write("--------------------------\n")