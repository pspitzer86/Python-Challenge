# Comment for citing source of dict

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Import needed modules

import csv

Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

employee_data = "C:\\Python-Challenge\\PyBoss\\Resources\\employee_data.csv"

with open(employee_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    
    for row in csvreader:
        
        emp_id = row[0]
        name = row[1]
        date = row[2]
        social = row[3]
        states = row[4]

        Emp_ID.append(emp_id)

        name.split()
        print(name)
        First_Name.append(name[0])
        Last_Name.append(name[1])

        date.split("-")
        DOB.append(date[1] + "/" + date[2] + "/" + date[0])

        social.split("-")
        SSN.append("***-**-" + social[2])

        State.append(us_state_abbreviation[states])










#cleaned_csv = zip(Emp_Id, First_Name, Last_Name, DOB, SSN, State)
       

#output_file = "C:\\Python-Challenge\\PyBoss\\Analysis\\employee_info.txt"

#with open(output_file, "w") as csv_file:
    #writer = csv.writer(csv_file)

    # Write the header row
    #writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
    #                 "SSN", "State"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)
