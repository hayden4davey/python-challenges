import os
import csv

pybank_csv = os.path.join("../resources", "budget_data.csv")
pybank_report = "PyBankReport.txt"

# Create empty lists to fill
dates = []
monthly_profit = []
changes = []

# Read csv file
with open (pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
    
        # Loop through dates, adding them to list and determine total time period
        dates.append(row[0])
        total_months = len(dates)
        
        # Loop through profits, adding them to monthly list and sum to determine net profit
        monthly_profit.append(int(row[1]))
        net_profit = sum(monthly_profit)
   
    for i in range(1, len(monthly_profit)):
    
        # Loop through monthly profit list to determine change and average change
        changes.append(monthly_profit[i] - monthly_profit[i-1])
        average_change = round(sum(changes)/len(changes), 2)
        
        # Determine max increase
        greatest_increase = max(changes)
        greatest_increase_month = dates[changes.index(greatest_increase) + 1]
        
        # Determine min increase
        greatest_decrease = min(changes)
        greatest_decrease_month = dates[changes.index(greatest_decrease) + 1]

# Report
output = (
    f"Financial Analysis \n"
    f"-------------------------------------------------\n"
    f"Total Months: {total_months} \n"
    f"Total: ${net_profit} \n"
    f"Average Change: ${average_change} \n"
    f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease}) \n"
    )
    
print(output)

# Output text file
with open(pybank_report, "a") as txt_file:
    txt_file.write(output)
    
