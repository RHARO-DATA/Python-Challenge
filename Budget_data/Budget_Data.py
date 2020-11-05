# Budget Data

import os
import csv


# Path to file
budget_csv = os.path.join("..", "Resources","budget_data.csv")

date = []            # List for the dates
profit_losses = []   # List for Profit / Losses 
diferience = []      # List for the differiece between months  
total = 0            # Variable for Total amount
month2 = []          # List to copy elements from Profit / Losses




with open(budget_csv,'r', newline= "") as csvfile:

     # Create the csv reader object
    csvreader = csv.reader(csvfile, delimiter = ',')
    

    csv_header = next(csvreader)   

    # Read each row of data 
    for row in csvreader:

        date.append(row[0])             # add dates to the lis
        profit_losses.append(row[1])    # add profit / losses to the list
        total = total + int(row[1])     # Total amount



    month2 = profit_losses

    
    for i in range (len(date)-1):        # calculate diferience between months

        diferience.append(int(month2[i+1])-int(month2[i]))  # add diferience to the list 


   
    # Number of months
    num_months = len(date)      

    #calculate the average of Profit / Losses 
    average = round((sum(diferience)) / (num_months -1),2)

    # Get max increase in profits
    maxi = max(diferience)

    # Get decrease in losses
    mini = min(diferience)
    

    # Print Analysis
    
    print(" Financial Analysis ")
    print("------------------------------------------")
    print(f"Total Months : {num_months} ")
    print(f"Total : {total} ")
    print(f"Average Change : {average}")
    print(f"Greatest increase in Profits: ${maxi} ")
    print(f"Greatest decrease in Profits: ${mini} ")



