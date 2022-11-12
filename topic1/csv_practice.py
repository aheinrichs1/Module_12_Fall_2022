"""
Practice for gathering data
"""
import csv
from topic1.CountyDemos import CountyDemos


with open('ExampleCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county = {}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the
        # county name and a value of the object
        county[str(row[0])] = CountyDemos(row[1], row[2])

    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].population.replace(',',''))
    print(pop_sum)
