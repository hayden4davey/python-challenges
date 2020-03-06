import os
import csv

pybank_csv = os.path.join("../resources", "budget_data.csv")
pybank_report = "PyBankReport.txt"

dates = []
monthly_profit = []
changes = []

with open (pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
    
        dates.append(row[0])
        total_months = len(dates)
        
        monthly_profit.append(int(row[1]))
        net_profit = sum(monthly_profit)
   
    for i in range(1, len(monthly_profit)):
    
        changes.append(monthly_profit[i] - monthly_profit[i-1])
        average_change = round(sum(changes)/len(changes), 2)
        
        greatest_increase = max(changes)
        greatest_increase_month = dates[changes.index(greatest_increase) + 1]
        
        greatest_decrease = min(changes)
        greatest_decrease_month = dates[changes.index(greatest_decrease) + 1]

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

with open(pybank_report, "a") as txt_file:
    txt_file.write(output)
    
