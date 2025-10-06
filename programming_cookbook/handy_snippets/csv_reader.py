import csv

# Suppose we have a file 'data.csv' with:
# name,age,city
# Alice,25,Paris
# Bob,30,London

with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)  # read as dictionary
    for row in reader:
       print(row['name'], row['age'])

