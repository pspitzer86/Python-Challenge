
import csv

myList = []

Total_months = 0
Net_Total = 0
Greatest_Profit = 0
Greatest_Loss = 0
Profits = 0
Losses = 0

bank_data = "C:\\Python-Challenge\\PyBank\\Resources\\budget_data.csv"

with open(bank_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        Total_months = Total_months + 1
        Net_Total = Net_Total + int(row[1])

        if int(row[1]) > Greatest_Profit:
            Greatest_Profit = int(row[1])
            Great_Month = row[0]
        elif int(row[1]) < Greatest_Loss:
            Greatest_Loss = int(row[1])
            Bad_Month = row[0]

print(f'In {Great_Month} we gained {Greatest_Profit}')
print(f'In {Bad_Month} we lost {Greatest_Loss}')
        

# Set variable for output file
output_file = "C:\\Python-Challenge\\PyBank\\Analysis\\bank_analysis.txt"

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.writelines(myList)
