import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Print the header
    print("Financial Analysis")
    print("----------------------------------------------------")

# Skip the header row
    next(csv_reader, None)

# Initialize variables
    total_months = 0
    total_amount = 0
    changes_per_period = []
    profit_per_period = []
    row_previous = None

# Store all data from the CSV file in a list
    all_data = list(csv_reader)

# Loop through all the data in the list
    for row in all_data:

# Count the total number of months
        total_months+=1

# Sum the total amount
        total_amount = total_amount + int(row[1])

        current_value = int(row[1])

# Calculate the change in profit/loss
        if row_previous is not None:
            previous_value = int(row_previous[1])
            change = current_value - previous_value
            changes_per_period.append(change)
        row_previous = row

 # Print the calculated values
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    average_change = round(sum(changes_per_period) / len(changes_per_period), 2)
    print(f"Average Change: ${average_change}")

# Find the greatest increase and decrease values and dates
    greatest_increase_value = max(changes_per_period)
    greatest_decrease_value = min(changes_per_period)
    greatest_increase_index = changes_per_period.index(greatest_increase_value)
    greatest_decrease_index = changes_per_period.index(greatest_decrease_value)
    greatest_increase_date = all_data[greatest_increase_index + 1][0]
    greatest_decrease_date = all_data[greatest_decrease_index + 1][0]

    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})")

    # Create a text file to write the results
    output_file = os.path.join("analysis", "PyBank_analysis.txt")
    with open(output_file, 'w') as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------------------------------\n")
        textfile.write(f"Total Months: {total_months}\n")
        textfile.write(f"Total: ${total_amount}\n")
        textfile.write(f"Average Change: ${average_change}\n")
        textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_value})\n")
        textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_value})\n")