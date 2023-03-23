#IMprting required modules 

import csv

# path to source data contained in budget_data.cvs
# and output data that will be stored in a file name: analysis.csv

csvfile = "Resources/budget_data.csv"
output_file = "Resources/anaysis.csv"

# Setting all variablles to initial values

number_months = 0
pnl = 0
changes = []
tot_change = 0
greatest_increase = 0
greatest_decrease = 0

# Main loop that will extract all requested infos: 
with open(csvfile) as csvhandler:
    csvreader = csv.reader(csvhandler, delimiter = ",")
    csv_header = next(csvreader)
    prev_pnl = 0

    for row in csvreader:
        number_months= number_months + 1
        pnl = pnl + float(row[1])
        new_change= float(row[1])-prev_pnl
        changes.append(new_change)
        prev_pnl=float(row[1])
        if new_change > greatest_increase:
            greatest_increase = new_change
            date_greatest_increase = row[0]
        elif new_change < greatest_decrease:
            greatest_decrease = new_change
            date_greatest_decrease = row[0]


    
    for i in range(len(changes)-1):
        tot_change = tot_change + changes[i+1]
    
    avg_change = round(tot_change/(len(changes)-1),2)
    pnl = round(pnl,2)
    # greatest_increase = round(greatest_increase,0)
    # greatest_decrease = round(greatest_decrease,0)

    print(" Number of Months : " + str(number_months))
    print(" Total Profit & Losses : " + str(pnl))
    # print(changes)
    print(" Average change ; " + str(avg_change))
    print("greatest_increase =", greatest_increase)
    print("date_greatest_increase =", date_greatest_increase)
    print("greatest_decrease =", greatest_decrease)
    print("date_greatest_decrease =",date_greatest_decrease)

    with open(output_file, 'w') as file:

    # Initialize csv.writer
        csvwriter = csv.writer(file)
        # csvwriter

        file.write(" ``` Text \n")
        file.write("Financial Analysis - Nour Belhaj \n")
        file.write("-----------------------------------\n")

        file.write(" Number of Months : "+ str(number_months)+"\n")
        file.write(" Total Profit & Losses : " + str(f"{pnl:,.0f}")+"\n")
        file.write(" Average chnnge ; " + str(avg_change)+"\n")
        file.write(" Greatest Increase in Profits: = "+ date_greatest_increase+ "  $(" + str(f"{greatest_increase:,.0f}")+")\n")
        file.write(" Greatest Increase in Profits: = "+ date_greatest_decrease+ "  $(" + str(f"{greatest_decrease:,.0f}")+")\n")
        file.write(" ```  \n")


    

   




