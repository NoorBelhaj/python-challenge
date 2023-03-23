#Importing required modules 

import csv

# path to source data contained in budget_data.cvs
# and output data that will be stored in a file name: analysis.csv

csvfile = "Resources/election_data.csv"
output_file = "Resources/anaysis.csv"
total_cast = 0
number_of_candidates = 0
candidates = []
votes_candidate = []
vote_count = 0
# resultats =[]

#######################################
# Lets get the candidta elist first   #
#######################################
with open(csvfile) as csvhandler:
    csvreader = csv.reader(csvhandler, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_cast = total_cast + 1
        if row[2] not in candidates:
            candidates.append(row[2])
    # print("Total Cast : ",total_cast)
    # print(candidates)

 ###################################################################
 # NOw that we have the candidates we will loop throough each one  #
 # and count the votes                                             #
 ###################################################################
   
for index in range(len(candidates)):
        candidate_current = candidates[index]
        # print("Current Candidate " + candidate_current)

        with open(csvfile) as csvhandler:
            csvreader = csv.reader(csvhandler, delimiter = ",")
            csv_header = next(csvreader)
            for row in csvreader:
           
                if candidate_current == row[2]:
                    vote_count = vote_count + 1
        
        votes_candidate.append(vote_count)
        vote_count = 0
    
print("The total number of votes cast " + str(total_cast))
print("A complete list of candidates who received votes ", candidates)
print("The total number of votes each candidate won ",votes_candidate)
# Header = [ "Candidates", "Number of Votes"] 
winner_score = 0
winner_name =""

for i in range(len(candidates)):
    name = candidates[i]
    percentage = round(int(votes_candidate[i])/int(total_cast)*100,3)

    print(name + ":  "+ str(percentage)+ " %    (" + str(votes_candidate[i]) + ")")
    
    # winner = max(votes_candidate)
    winner_index = votes_candidate.index(max(votes_candidate))
    winner_name = candidates[winner_index]

print("Winner is " + winner_name)

with open(output_file, 'w') as file:

    # Initialize csv.writer
        csvwriter = csv.writer(file)
        # csvwriter

        file.write(" ``` Text \n")
        file.write("Elections Results - Nour Belhaj \n")
        file.write("-----------------------------------\n")
        for i in range(len(candidates)):
            name = candidates[i]
            percentage = round(int(votes_candidate[i])/int(total_cast)*100,3)
            file.write(name + "   :  " + str(percentage) + " %    ("+ str(votes_candidate[i]) +")    \n")
        file.write("-----------------------------------\n")
        file.write("Winner is " )
        file.write(winner_name)
        file.write("    \n")
        file.write("-----------------------------------\n")
        file.write(" ```  \n")
        
