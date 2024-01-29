import os
import csv 


def PyPoll():

    csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

    totalVotes = 0
    voteCount = {}

    with open(csvpath, 'r') as poll_csv:
        poll_reader = csv.reader(poll_csv)
        next(poll_reader)

        for line in poll_reader:

            totalVotes+= 1

            if line[2] in voteCount:
                voteCount[line[2]] += 1
            else:
                voteCount[line[2]] = 1

    print('Election Results')
    print('------------------------------------------')
    print(f'Total Votes: {totalVotes}')
    print('------------------------------------------')

    for candidate, votes in voteCount.items():
        print(f'{candidate}: {round((votes / totalVotes) * 100, 3)}% ({votes})')

    print('------------------------------------------')
    print(f'Winner: {max(voteCount, key=voteCount.get)}')

    writepath = os.path.join('PyPoll', 'Analysis', 'election_results.txt')

    with open(writepath, 'w') as file:
        file.write('Election Results\n')
        file.write('------------------------------------------\n')
        file.write(f'Total Votes: {totalVotes}\n')
        file.write('------------------------------------------\n')

        for candidate, votes in voteCount.items():
            file.write(f'{candidate}: {round((votes / totalVotes) * 100, 3)}% ({votes})\n')

        file.write('------------------------------------------\n')
        file.write(f'Winner: {max(voteCount, key=voteCount.get)}\n')



PyPoll()