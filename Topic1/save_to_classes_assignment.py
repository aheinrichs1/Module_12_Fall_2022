"""
Program: save_to_classes_assignment.py
Author: Alex Heinrichs
Date Created: 11/10/2022

Create a class that can hold data to be imported from an Iowa Census
Population Income csv and use it to print from a specific county and
find a summary from all counties
"""
import csv


class CountyData:
    def __init__(self, per_capita_income, median_household_income,
                 median_family_income, population, number_of_households):
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.number_of_households = number_of_households


if __name__ == '__main__':
    with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # initialize empty dictionary
        county = {}
        for row in csv_reader:
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            # skip the line if there is no number for rank
            # (for the Iowa State and United States lines)
            if row[0] == '':
                continue
            # create an item in dictionary county with a key of the
            # county name and a value of the object
            county[str(row[1])] = CountyData(row[2], row[3], row[4],
                                             row[5], row[6])

        # Finding population of Dallas
        print('The population of Dallas is '
              + county['Dallas'].population.replace(',', ''))

        # Finding sum of population
        pop_sum = 0
        for key in county:
            pop_sum += int(county[key].population.replace(',', ''))
        print('The total population of Iowa is ' + str(pop_sum))
