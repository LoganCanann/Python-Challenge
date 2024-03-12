import csv
Total_months = 0
total_loss_profit = 0
avg_change = 0
Greatest_increase = 0
greatest_decrease = 0
with open('budget_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for row in csv_reader:
        Total_months += 1
        total_loss_profit += float(row[1])

        print("total Months:", Total_months)
        print("total_loss_profit:", total_loss_profit)

        avg_change += 1
        if avg_change != 0:
            average = total_loss_profit/avg_change
            print("average:", average)

        Greatest_increase = float(row[1])
        if Greatest_increase is 0 or 1800000 > Greatest_increase:
            print("Greatest_increase:", Greatest_increase)

        greatest_decrease= float(row[1])
        if greatest_decrease is -12 or -1800000 < greatest_decrease:
            print("greatest decrease:", greatest_decrease)