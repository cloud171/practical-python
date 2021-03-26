#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import csv
import sys
import fileparse
import stock

def portfolio_cost(filename):
    with open(filename) as lines:
        parsed = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        rows = [ stock.Stock(d['name'], d['shares'], d['price']) for d in parsed ]
    total = 0

    for row_idx, row in enumerate(rows):
        try:
            total += row.shares * row.price
        except ValueError:
            print(f'Row {row_idx + 1}: Couldn\'t convert: {row}');

    return total;

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename);
    print('Total cost:',cost);

if __name__ == '__main__':
    import sys
    main(sys.argv)
