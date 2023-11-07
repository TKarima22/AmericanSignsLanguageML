# import modules
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# read the data from the file
data = pd.read_csv('MS-ASL/aggregated_data/aggregated_data.csv')
pd.set_option('display.max_columns', None)



print('\n############### Data  describe ##################')
# let's see the description of the file
print(data.describe())

'''Analyse column by column - labels'''
print('\n############### value count in label ##################')
label_count = data['label'].value_counts()
print(label_count)

print('\n############### frequency of each label ##################')
label_frequency = data['label'].value_counts()/len(data)
print(label_frequency)

print('\n############### most common labels ##################')
most_common_labels = label_count.head(10)
print(most_common_labels)

print('\n############### visualize distribution of labels ##################')
plt.figure(figsize=(10, 6))
plt.hist(label_count, bins=30, edgecolor='k')
plt.title('Distribution of Class Labels')
plt.xlabel('Class Label')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
'''
What we can notice here the imbalance of frequency - some labels are more
frequent than others- which can impact the performance of the model
'''


'''Analyse column by column - box'''
df = data[['box','height','width']]
print(df.head(5))
df1 = pd.DataFrame()
df1['x0'] = df['box'] * df['width'] / 2
df1['y0'] = df['box'] * df['height']
df1['x1'] = df['box'] * df['width'] / 2
df1['y1'] = df['box'] * df['height']

# Create histograms for x0, y0, x1, and y1
plt.figure(figsize=(12, 8))

# Histogram for x0
plt.subplot(2, 2, 1)
plt.hist(df1['x0'], bins=30, color='b')
plt.title('Histogram of x0')
plt.xlabel('x0')
plt.ylabel('Frequency')

# Histogram for y0
plt.subplot(2, 2, 2)
plt.hist(df1['y0'], bins=30, color='g')
plt.title('Histogram of y0')
plt.xlabel('y0')
plt.ylabel('Frequency')

# Histogram for x1
plt.subplot(2, 2, 3)
plt.hist(df1['x1'], bins=30, color='r')
plt.title('Histogram of x1')
plt.xlabel('x1')
plt.ylabel('Frequency')

# Histogram for y1
plt.subplot(2, 2, 4)
plt.hist(df1['y1'], bins=30, color='y')
plt.title('Histogram of y1')
plt.xlabel('y1')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
