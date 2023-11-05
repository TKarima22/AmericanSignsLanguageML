# import modules
import csv
import pandas as pd
# list of files
files = ['MS-ASL/csv_data/MSASL_test.csv', 'MS-ASL/csv_data/MSASL_train.csv', 'MS-ASL/csv_data/MSASL_val.csv']
aggregate_data = []

# get the header of the file
with open(files[0], 'r', newline='') as file:
    reader = csv.reader(file)

    # Read and add the first row (header) to aggregate_data
    first_row = next(reader)
    print(first_row)
    aggregate_data.append(aggregate_data)


# open the file, read the content, write it on the new one
for file in files:
    with open(file, 'r', newline='') as f:
        read_line = csv.reader(f)

        # Skip the header
        next(read_line)

        # Append the data to the aggregated_data list
        aggregate_data.extend(list(read_line))

# Write the aggregated data to the output file
with open('MS-ASL/aggregated_data/aggregated_data.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(aggregate_data)

# count number of rows in each file
# Initialize a row counter
row_count = 0
for file in files:
    with open(file, 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            row_count += 1

print(f"Number of rows in the 3 files is': {row_count}")

row_count_agg = 0
with open('MS-ASL/aggregated_data/aggregated_data.csv', 'r', newline='') as file:
    reader = pd.read_csv(file)

    for row in reader:
        row_count_agg += 1

if (row_count_agg == (row_count -2)):
    print("Data aggregation complete. Aggregated data saved to 'aggregated_data.csv'.")
else:
    print("Data aggregation went wrong.")


