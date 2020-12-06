# PyBoss instructions had link to US State abbreviations dictionary
# Borrowed from GitHub user afhaque, file rogerallen/us_state_abbrev.py
# Dictionary for reading US State names as their abbreviations.

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

# Created empty lists to fill with data from employee_data.csv

Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

# Resource csv file path called and labeled
# Csv read through by comma delimiter, skipped header values

employee_data = "C:\\Python-Challenge\\PyBoss\\Resources\\employee_data.csv"

with open(employee_data, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Looping through each row in read csv file
    
    for row in csvreader:

        # Assigning each row index to a variable
        # Name, date, and social need to be split to return a list where
        # the index values of the returned list can be used for new format
        
        emp_id = row[0]
        name = row[1].split()
        date = row[2].split("-")
        social = row[3].split("-")
        state_name = row[4]

        # Appending all needed data into our empty lists.  Concatenating
        # needed values from split lists with strings in order to fit 
        # the new format for the employee info.  US State dict called to
        # grab the necessary state abbreviations.

        Emp_ID.append(emp_id)

        First_Name.append(name[0])
        Last_Name.append(name[1])

        DOB.append(date[1] + "/" + date[2] + "/" + date[0])

        SSN.append("***-**-" + social[2])

        State.append(us_state_abbrev[state_name])

# Zip command used to combine together all the created lists now filled
# with data in the correct format.  Creadted output file path and file type.

NewHR_csv = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)
       
output_file = "C:\\Python-Challenge\\PyBoss\\Analysis\\employee_info.csv"

# Writing output csv file

with open(output_file, "w") as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])

    # Write in zipped rows
    writer.writerows(NewHR_csv)
