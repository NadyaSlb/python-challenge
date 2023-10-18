import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Print the header
    print("Election Results")
    print("----------------------------------------------------")

# Skip the header row
    next(csv_reader, None)

# Initialize variables
    total_votes=0
    candidates_votes={}

    # Loop through all the data in a file
    for row in csv_reader:
        # Count the total number of votes
        total_votes+=1

        #Add candidates to the dictionary
        candidate = row[2]
        if candidate in candidates_votes:
            candidates_votes[candidate]+=1
        else:
            candidates_votes[candidate]=1
    print(f"Total Votes: {total_votes}")
    print("----------------------------------------------------")

    #calculate the percentage of votes each candidate won and who is the winner
    winner = ""
    winner_votes = 0
    for candidate, votes in candidates_votes.items():
        percent_votes = round((votes/total_votes)*100,3)
        print(f"{candidate}: {percent_votes}% ({votes})")
        if votes>winner_votes:
            winner = candidate
            winner_votes=votes

    print("----------------------------------------------------")
    print(f"Winner: {winner}")
    print("----------------------------------------------------")

     # Create a text file to write the results
    output_file = os.path.join("analysis", "PyPoll_results.txt")
    with open(output_file, 'w') as textfile:
        textfile.write("Election Results\n")
        textfile.write("----------------------------------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("----------------------------------------------------\n")
        for candidate, votes in candidates_votes.items():
            textfile.write(f"{candidate}: {round((votes/total_votes)*100,3)}% ({votes})\n")
        textfile.write("----------------------------------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("----------------------------------------------------\n")
