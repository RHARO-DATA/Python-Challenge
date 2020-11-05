# PyPoll challenge

import csv
import os

# Path to file
election_csv = os.path.join("..", "Resources","election_data.csv")

votes = []   #List to count the votes
khan = 0     #Variable to count Khan Votes     
correy = 0   #Variable to count Correy Votes     
li = 0       #Variable to count Li Votes     
toley = 0    #Variable to count O'Tooley Votes    



with open(election_csv,'r', newline= "") as csvfile:
    # Create the csv reader object
    csvreader = csv.reader(csvfile, delimiter = ',')    


    for row in csvreader:

        votes.append(row[0])      #add Votes to the List

        if row[2] == "Khan":
            khan = khan + 1       #count votes for Khan

        elif row[2] == "Correy":
            correy = correy + 1   #count votes for Correy

        elif row[2] == "Li":
            li = li + 1           #count votes for Li

        elif row[2] == "O'Tooley":
            toley = toley + 1      #count votes for O'Tooley


# Total Votes
total_votes = int(len(votes))


total_khan =round( (khan * 100) / total_votes)        #Total votes for Kham
total_correy = round( (correy * 100) / total_votes)   #Total votes for Correy
total_li =round( (li * 100) / total_votes)            #Total votes for Li
total_toley =round( (toley * 100) / total_votes)      #Total votes for O'Tooley


# Analysis Print
print("Election Results")
print("--------------------------------------")
print(f"Total Votes:  {total_votes}  ")
print("--------------------------------------")
print(f"Khan:     {total_khan}%  ({khan}) ")
print(f"Correy:   {total_correy}%  ({correy}) ")
print(f"li:       {total_li}%  ({li}) ")
print(f"O'Tooley: {total_toley}%  ({toley}) ")
print("--------------------------------------")
print("Winner: Khan")
print("--------------------------------------")






            





