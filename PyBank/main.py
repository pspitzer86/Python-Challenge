# import csv module
import csv

# Defining variables, some set to 0 for later arguments
# Setting flag in order to skip first entry for average change calculation
Total_Months = 0
Net_Total = 0
Total_Change = 0
Greatest_Up = 0
Greatest_Down = 0
First_Read = True

# Defining our csv Resource from Resources folder for reading

bank_data = "C:\\Python-Challenge\\PyBank\\Resources\\budget_data.csv"

# Reading csv file data, delimiting by commas, utf-8 needed for windows
# Used Next(csvreader) to skip first row of data which were headers

with open(bank_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # For each row in the csv, defining the first row as the month
    # and the second row as the current profit for each month

    for row in csvreader:

        Month = row[0]
        curr_profit = int(row[1])

        # Found Flag, used to skip the first entry for average change
        # calculation, every other row calculates the change between 
        # consecutive months and adds them to get the total

        if First_Read == True:
            First_Read = False
        else:
            Change = curr_profit - prev_profit
            Total_Change = Total_Change + Change

            # Comparing the change between each consecutive pair of months
            # in order to find which months had the greatest increase in
            # profit and the greatest decrease in profit

            if Change > Greatest_Up:
                Greatest_Up = Change 
                Great_Month = Month
            elif Change < Greatest_Down:
                Greatest_Down = Change
                Bad_Month = Month

        # After each change calculation and comparison, set the current profit
        # to the previous profit to be used for next calculation.  Also counting
        # each month and adding together the total profit for all months
        
        prev_profit = curr_profit
        Total_Months += 1
        Net_Total = Net_Total + curr_profit

# After all changes calculated, find the average of the changes.
# Subtract one from total months since we did not need to find the change
# for the first month

Average = Total_Change/(Total_Months - 1)

# Printing in the format requested, print all calculations made.

print("\nFinancial Analysis")
print("--------------------------")
print(f'Total Months: {Total_Months}')
print(f'Total: ${Net_Total}')
print(f'Average Change: ${round(Average,2)}')
print(f'Greatest Increase in Profits: {Great_Month} (${Greatest_Up})')
print(f'Greatest Decrease in Profits: {Bad_Month} (${Greatest_Down})')        

# Set variable for output file

output_file = "C:\\Python-Challenge\\PyBank\\Analysis\\bank_analysis.txt"

#  Open the output file in the same format as printed in terminal

with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Total Months: {Total_Months}\n')
    text_file.write(f'Total: ${Net_Total}\n')
    text_file.write(f'Average Change: ${round(Average,2)}\n')
    text_file.write(f'Greatest Increase in Profits: {Great_Month} (${Greatest_Up})\n')
    text_file.write(f'Greatest Decrease in Profits: {Bad_Month} (${Greatest_Down})\n') 