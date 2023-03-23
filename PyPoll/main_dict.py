#Importing required modules 

import csv

# path to source data contained in budget_data.cvs
# and output data that will be stored in a file name: analysis.csv

csvfile = "Resources/election_data.csv"
output_file = "Resources/anaysis.csv"
total_cast = 0
number_of_candidates = 0
candidates = []
votes_candidate = {}
winner = 0
winner_name = ""

#######################################
# Lets get the candidta elist first   #
#######################################
with open(csvfile) as csvhandler:
    csvreader = csv.reader(csvhandler, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        candidates = row[2]
        total_cast = total_cast + 1
        if candidates in votes_candidate.keys():
            votes_candidate[candidates] += 1
            
        else:
            votes_candidate[candidates] = 1
           
  
print("The total number of votes cast " + str(total_cast))
print("A complete list of candidates who received votes ")
for candidates in votes_candidate.keys():
       percentage = round(int(votes_candidate[candidates])/int(total_cast)*100,3)
       print(candidates +" : " + str(percentage) + "%   ( " + str(votes_candidate[candidates])+ ")")
       if votes_candidate[candidates] > winner:
            winner = votes_candidate[candidates]
            winner_name = candidates
            

print("The winner of the election is: " + winner_name)            


with open(output_file, 'w') as file:

#     # Initialize csv.writer
    csvwriter = csv.writer(file)
#     # csvwriter

    file.write(" ``` Text \n")
    file.write("Elections Results - Nour Belhaj \n")
    file.write("-----------------------------------\n")

    for candidates in votes_candidate.keys():
        percentage = round(int(votes_candidate[candidates])/int(total_cast)*100,3)
        file.write(candidates +" : " + str(percentage) + "%   ( " + str(votes_candidate[candidates])+ ") \n")
    file.write("-----------------------------------\n")
    file.write("Winner is " )
    file.write(winner_name)
    file.write("    \n")
    file.write("-----------------------------------\n")
    file.write(" ```  \n")
        
