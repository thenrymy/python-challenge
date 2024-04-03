# Import operating system and csv module
import os
import csv

# Read from the file
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv 
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Set initial values
    total_votes = 0

    # Dictionary or list to store date
    candidate_counts = {}

    # Read through each row of data after the header
    for row in csv_reader:

        # Count the total number of votes cast
        total_votes += 1

        # Complete list of candidate who received votes
        candidate = row[2]
        if candidate in candidate_counts:
            candidate_counts[candidate] += 1
        else:
            candidate_counts[candidate] = 1

# Candidate with the biggest votes
winner = max(candidate_counts, key=candidate_counts.get)

# Print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Print a list of cendidates and their votes
for candidate, count in candidate_counts.items():
    percentage = (count / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({count})")
print("-------------------------")

# Print winner
print(f"Winner: {winner}")

# Set variable for output file
output_file = os.path.join("analysis", "election_data_analysis.txt")

# Open the output file
with open(output_file, 'w') as f:
    
    # Output header
    print("Election Results", file=f)
    print("----------------------------", file=f)
    
    # Output results
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------")
    for candidate, count in candidate_counts.items():
        percentage = (count / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({count})",file=f)
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("-------------------------", file=f)