import os
import csv

pyboss_csv = os.path.join("../resources", "employee_data.csv")
pyboss_output = "PyBossOutput.csv"

# State abbreviation dictionary
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

new_employee_data = []

# Read CSV and loop through rows
with open (pyboss_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    
    for row in csvreader:
    
        # Split into first and last name columns
        first_name, last_name = row[1].split(" ")
        row.insert(1, first_name)
        row.insert(2, last_name)
        row.pop(3)
        
        # Reconfigure date layout
        row[3] = row[3].replace("-","/") + "/"
        row[3] = row[3][5:] + row[3][:4]
        
        # Hide SSN digits
        row[4] = "***-**" + row[4][6:]
        
        # Replace state names with abbreviations
        state_name = row[5]
        for key in us_state_abbrev.keys():
            if state_name == key:
                row[5] = state_name.replace(key, us_state_abbrev[key])

        new_employee_data.append(row)

# Reconfigure header and add to new data list        
csv_header[1] = csv_header[1].replace("Name", "First Name")
csv_header.insert(2, "Last Name")
new_employee_data.insert(0, csv_header)

# Output to CSV
with open(pyboss_output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for data in new_employee_data:
            writer.writerow(data)
