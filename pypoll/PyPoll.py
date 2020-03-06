import os 
import csv

pypoll_csv = os.path.join("../resources", "election_data.csv")
pypoll_report = "PyPollReport.txt"

votes = []
poll_dict = {}

with open (pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
    
        votes.append(row[2])
        total_votes = len(votes)
    
    for candidate in votes:
        if candidate in poll_dict:
            poll_dict[candidate] += 1
        else:
            poll_dict[candidate] = 1
            
winner = max(poll_dict, key=poll_dict.get)

print(
    f"Election Results \n"
    f"--------------------------------- \n"
    f"Total Votes: {total_votes} \n"
    f"---------------------------------")
for key, val in poll_dict.items():
    print( f"{key}: {round((val/total_votes*100.000), 3)}% ({val})")
print(
    f"--------------------------------- \n"
    f"Winner: {winner} \n"
    f"--------------------------------- \n")    

final = open(pypoll_report, "a")

print(
    f"Election Results \n"
    f"--------------------------------- \n"
    f"Total Votes: {total_votes} \n"
    f"---------------------------------", file=final)
for key, val in poll_dict.items():
    print( f"{key}: {round((val/total_votes*100.000), 3)}% ({val})", file=final)
print(
    f"--------------------------------- \n"
    f"Winner: {winner} \n"
    f"--------------------------------- \n", file=final)