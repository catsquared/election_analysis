# In this project, our final Python script will need to be able to deliver
# the following information when the script is run: 


# Need to get the total number of rows? Or can just cycle through the data one by one
# Check if the Ballot ID id has duplicates?

# Use Python's built in module called csv
import csv
import os

# Name the file to load
# file_to_load = "Resources/election_results.csv"

# Alternatively, name the file using the os module
file_to_load = os.path.join("Resources", "election_results.csv")

# Declare a file to write to
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Declare a file object
# election_data = open(file_to_load, 'r')

# Total number of votes cast
#   Equals total rows
#   Can count while the next row is not empty
# Every time the .py file is run, total votes should be 0
total_votes = 0

# Declare a variable to capture list of candidates
candidates = list()

# Declare a variable to capture dictionary of candidate names and their votes
candidate_dict = dict()

# Use with function instead of open() and close()
with open(file_to_load) as election_data:
    # Use the reader function from the csv module
    file_reader = csv.reader(election_data)

    # Read the header row
    header = next(file_reader)
    
    # Print each row in the file
    for row in file_reader:
        # Use a counter to get total number of votes
        total_votes += 1
        candidate_name = row[2]

        # Add the Candidate to a list
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            # Add the vote for the candidate to the dictionary candidate_dict
            candidate_dict[candidate_name] = 0
        
        # Add the vote to the correct candidate in candidate_dict
        candidate_dict[candidate_name] += 1

# Print total_votes in console
print(f"The total number of votes cast is {total_votes}.")

# Print all Candidates
print(f"The List of Candidates are {candidates}.")

# Print the dictionary of Candidates and their votes
print(f"The candidates and their votes are {candidate_dict}")

# Calculate the pct of votes for each Candidate
# Divide each candidate's vote by total_votes
# Use a dictionary to keep the candidates and their pct
pct_dict = dict()
for c in candidates:
    # Get the candidate votes from candidate_dict
    candidate_vote = candidate_dict.get(c)
    # Calculate the percentage and assign it to the value
    # Format it such that only 2 decimals are present
    pct_dict[c] = f"{candidate_vote / total_votes * 100 :.2f}%"

# Print the dictionary of Candidates and their votes in pct
print(f"The candidates and pct of votes they received are {pct_dict}")

# # Declare a file object
# with open(file_to_save, 'w') as txt_file:

    # Test on writing to outfile
    # txt_file.write("Counties in the election\n----------\nArapahoe\nDenver\nJefferson")

# Store information in a dictionary, or a list of dictionaries:
# {Candidate_name: Candidate_votes}



# Or Store information as
# ({Candidate_name: Name, No_of_Votes: Votes})

# A complete list of candidates who received votes
#   If the Candidate name is not in a list of Candidates already, add the Candidate name to the list
#   
# Total number of votes each candidate received
#   For each ballot ID, add 1 to the count for that candidate
#
# Percentage of votes each candidate won
#   For each candidate, calculate total votes he/she received divided by total ballots
#
# The winner of the election based on popular vote
#   The Candidate with the highest percentage of votes wins



# Close the file object after analysis is complete
# election_data.close()

# Close the file where analysis is performed
# outfile.close()
