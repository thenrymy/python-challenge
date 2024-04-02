# Import operating system and csv module
import os
import csv

# Read from the file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv 
with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    total_month = 0
    total = 0

    # List to store data
    profit_loss = []
    value_change = []
    date = []
    
    for row in csv_reader:
        # print(row)

        # Count the number of data rows
        total_month += 1

        # Add list of Profit & Losses
        profit_loss.append(int(row[1]))

        # Add list of dates
        date.append(row[0])

    # Add list of value change
    value_change = [profit_loss[i] - profit_loss[i - 1] for i in range(1, len(profit_loss))]

    # Calculate the average
    average = sum(value_change) / len(value_change)

    # Find the max value change month
    max_index = value_change.index(max(value_change))
    max_month = date[max_index + 1]

    # Find the min value change month
    min_index = value_change.index(min(value_change))
    min_month = date[min_index + 1]

# Print to terminal
print("Financial Analysis")
print("----------------------------")

# Output results
print(f"Total Months: {total_month}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max(value_change)})")
print(f"Greatest Decrease in Profits: {min_month} (${min(value_change)})")

# Set variable for output file
output_file = os.path.join("analysis", "budget_data_analysis.txt")

# Open the output file
with open(output_file, 'w') as f:
    
    # Output header
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    
    # Output results
    print(f"Total Months: {total_month}", file=f)
    print(f"Total: ${sum(profit_loss)}",file=f)
    print(f"Average Change: ${average:.2f}", file=f)
    print(f"Greatest Increase in Profits: {max_month} (${max(value_change)})", file=f)
    print(f"Greatest Decrease in Profits: {min_month} (${min(value_change)})", file=f)