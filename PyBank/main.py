
import csv

Total_Months = 0
Net_Total = 0
Total_Change = 0
Greatest_Up = 0
Greatest_Down = 0
First_Read = True


bank_data = "C:\\Python-Challenge\\PyBank\\Resources\\budget_data.csv"

with open(bank_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:

        Month = row[0]
        curr_profit = int(row[1])

        if First_Read == True:
            First_Read = False
        else:
            Change = curr_profit - prev_profit
            Total_Change = Total_Change + Change

            if Change > Greatest_Up:
                Greatest_Up = Change 
                Great_Month = Month
            elif Change < Greatest_Down:
                Greatest_Down = Change
                Bad_Month = Month
        
        prev_profit = curr_profit
        Total_Months = Total_Months + 1
        Net_Total = Net_Total + curr_profit

Average = Total_Change/(Total_Months - 1)

print("\nFinancial Analysis")
print("--------------------------")
print(f'Total Months: {Total_Months}')
print(f'Total: ${Net_Total}')
print(f'Average Change: ${round(Average,2)}')
print(f'Greatest Increase in Profits: {Great_Month} $({Greatest_Up})')
print(f'Greatest Decrease in Profits: {Bad_Month} S({Greatest_Down})')        

# Set variable for output file
output_file = "C:\\Python-Challenge\\PyBank\\Analysis\\bank_analysis.txt"

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f'Total Months: {Total_Months}\n')
    text_file.write(f'Total: ${Net_Total}\n')
    text_file.write(f'Average Change: ${round(Average,2)}\n')
    text_file.write(f'Greatest Increase in Profits: {Great_Month} (${Greatest_Up})\n')
    text_file.write(f'Greatest Decrease in Profits: {Bad_Month} (${Greatest_Down})\n') 
