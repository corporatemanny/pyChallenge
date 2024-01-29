import csv 
import os

csvpath = os.path.join('Pybank', 'Resources', 'budget_data.csv')

def PyBank():

    with open(csvpath, 'r') as bank_csv:
        bank_reader = csv.reader(bank_csv)

        next(bank_reader)

        total = 0
        dates, profitLoss = [], []

        for line in bank_reader:
            dates.append(line[0])
            profitLoss.append(int(line[1]))

    months = len(dates)
    total = sum(profitLoss)
    profitChange = [profitLoss[i + 1] - profitLoss[i] for  i in range(months - 1)]
    averageChange = round(sum(profitChange) / (months - 1), 2)

    greatestIncreaseDate = dates[profitChange.index(max(profitChange)) + 1]
    greatestDecreaseDate = dates[profitChange.index(min(profitChange)) + 1]


    print('Financial Analysis')
    print('------------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${averageChange}')
    print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${max(profitChange)})")
    print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${min(profitChange)})")

    writepath = os.path.join('PyBank', 'Analysis', 'budgetresults.txt')

    with open(writepath, 'w') as file:

        file.write("Financial Analysis\n")
        file.write(f"Total Months: {months}\n")
        file.write(f"Total: ${total}\n")
        file.write(f"Average Change: ${averageChange}\n")
        file.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${max(profitChange)})\n")
        file.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${min(profitChange)})\n")

PyBank()
