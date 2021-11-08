# In this project, our final Python script will need to be able to deliver
# the following information when the script is run: 


# Need to get the total number of rows? Or can just cycle through the data one by one
# Check if the Ballot ID id has duplicates?

# Total number of votes cast
#   Equals total rows
#   Can count while the next row is not empty
# 
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