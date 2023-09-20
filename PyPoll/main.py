# Modules
import os
import csv

csvpath = os.path.join("PyPoll","Resources","election_data.csv")

ballots = 0
candidates = []
votes = []
percent = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Advance passed header
    csv_header = next(csvreader)

    # read through CSV
    for row in csvreader:
        
        # Count the ballots
        ballots = ballots + 1

        # find unique candidates
        # counter needed as the value of x after the loop was not always correct
        found = False
        counter = -1
        x = 0
        for x in range(len(candidates)):
            counter = counter + 1
            if row[2] == candidates[x]:
                found = True
                break

        # candidate not found, need to append to list
        if found == False:
            candidates.append(row[2])
            votes.append(0)
            counter = counter + 1

        # after we found who got a vote, increment the votes list in the same position
        votes[counter] = votes[counter] + 1

    csvfile.close()

# Set variable for output file
output_file = os.path.join("PyPoll","analysis","results.txt")

#  Open the output file
with open(output_file, "w") as datafile:

    # print first section to outputs
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {ballots}')
    print("----------------------------")
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Votes: {ballots}\n')
    datafile.write("----------------------------\n")

    i = 0
    mostVotes = 0
    for i in range(len(candidates)):
        # calculate percentage, add to new list
        percent.append(round(votes[i]*100/ballots,3))

        # print output within loop
        print(f'{candidates[i]}: {percent[i]}% ({votes[i]})')
        datafile.write(f'{candidates[i]}: {percent[i]}% ({votes[i]})\n')

        # determine winner
        if votes[i] > mostVotes:
            mostVotes = votes[i]
            winnerMessage = "Winner: " + candidates[i]

    # print winner message to outputs
    print('----------------------------')
    print(winnerMessage)
    print('----------------------------')
    datafile.write("----------------------------\n")
    datafile.write(f'{winnerMessage}\n')
    datafile.write("----------------------------")

    datafile.close





