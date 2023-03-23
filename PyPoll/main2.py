#Importing required modules 

import csv

# path to source data contained in budget_data.cvs
# and output data that will be stored in a file name: analysis.csv

csvfile = "Resources/election_data - Copy.csv"
output_file = "Resources/anaysis.csv"
total_cast = 0

candidate_names = []
candidates_votes = {}

number_of_candidates = 0

# Main loop that will extract all requested infos: 
with open(csvfile) as csvhandler:
    csvreader = csv.reader(csvhandler, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:

        total_cast += 1
        candidate_name = row[2]

        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidates_votes[candidate_name] = 0
            number_of_candidates = number_of_candidates + 1

        candidates_votes[candidate_name] += 1

    print("Total Cast is here ; " + str(total_cast))
    print(candidate_names)
    print(candidates_votes)
    # print(vote_count)
    print(number_of_candidates)