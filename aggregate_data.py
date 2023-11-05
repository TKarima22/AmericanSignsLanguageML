import csv
import pandas as pd

# List of files
files = ['MS-ASL/csv_data/MSASL_test.csv', 'MS-ASL/csv_data/MSASL_train.csv', 'MS-ASL/csv_data/MSASL_val.csv']

# Open the output file for writing
with open('MS-ASL/aggregated_data/aggregated_data.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    # Write the header in the new file
    with open(files[0], 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and store the header
        writer.writerow(header)  # Write the header to the output file

    # Initialize a row counter
    row_count = 0

    # Iterate through each input file
    for file in files:
        with open(file, 'r', newline='') as input_file:
            reader = csv.reader(input_file)

            # Skip the header in each input file
            next(reader)

            # Write the rows directly to the output file
            for row in reader:
                writer.writerow(row)
                row_count += 1  # Increment the row counter

# Count the number of rows in the new file
row_count_agg = 0
with open('MS-ASL/aggregated_data/aggregated_data.csv', 'r', newline='') as file:
    reader = pd.read_csv(file)
    row_count_agg = len(reader)  # Count the rows in the aggregated data

# Print row counts
print(f"Number of rows in the 3 input files is: {row_count}")
print(f"Number of rows in the new file is: {row_count_agg}")

if (row_count_agg == row_count):
    print("Data aggregation complete. Aggregated data saved to 'aggregated_data.csv'.")
else:
    print("Data aggregation went wrong.")
