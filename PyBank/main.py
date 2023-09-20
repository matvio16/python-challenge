# Modules
import os
import csv

csvpath = os.path.join("PyBank","Resources","budget_data.csv")

months = 0
profit_Losses = 0
old = 0
greatest = 0
least = 0
changes= []
monthList = []
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Advance passed header
    csv_header = next(csvreader)

    # read through CSV
    for row in csvreader:

        # count months
        months = months + 1

        # sum total profit/losses
        profit_Losses = profit_Losses + int(row[1])

        # build the profit/loss change list
        if old != 0:
            new = int(row[1])
            changes.append(new-old)
        else:
            changes.append(int(row[1]))
        old = int(row[1])

        # save list of months
        monthList.append(row[0])

    # find greatest and least changes within list
    greatest = max(changes)
    least = min(changes)

    # check the change list for the greatest and least
    # find the month in the same position in the list
    for x in range(len(changes)):
        if changes[x] == greatest:
            greatestMonth = monthList[x]
        if changes[x] == least:
            worstMonth = monthList[x]

    # Added the first row to the list, need to ignore it here
    average = round((sum(changes)-changes[0])/(len(changes)-1),2)

    # Print output to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${profit_Losses}') 
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {greatestMonth} (${greatest})')
    print(f'Greatest Decrease in Profits: {worstMonth} (${least})')

    csvfile.close()

# Set variable for output file
output_file = os.path.join("PyBank","analysis","results.txt")

#  Open the output file
with open(output_file, "w") as datafile:

    # Write to file
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {months}\n')
    datafile.write(f'Total: ${profit_Losses}\n') 
    datafile.write(f'Average Change: ${average}\n')
    datafile.write(f'Greatest Increase in Profits: {greatestMonth} (${greatest})\n')
    datafile.write(f'Greatest Decrease in Profits: {worstMonth} (${least})')

    datafile.close()