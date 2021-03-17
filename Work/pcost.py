# pcost.py
#
# Exercise 1.27

import csv
import sys
import fileparse

def portfolio_cost(filename):
    rows = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    total = 0

    for row_idx, row in enumerate(rows):
        try:
            total += row['shares'] * row['price']
        except ValueError:
            print(f'Row {row_idx + 1}: Couldn\'t convert: {row}');

    return total;

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename);
print('Total cost:',cost);
