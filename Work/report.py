#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import fileparse
import csv
import stock
import tableformat

def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and prices.[]
    '''
    with open(filename) as lines:
        pdict = fileparse.parse_csv(lines,select=['name','shares','price'], types=[str,int,float])
        portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in pdict ]

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as lines:
        rows = fileparse.parse_csv(lines, types=[str,float], has_headers=False)
        for row in rows:
            if row:
                name, price = row
                prices[name] = price

    return prices

def make_report(portfolio, prices):
    price_change = []
    for stock in portfolio:
        row = (stock.name, int(stock.shares), float(prices[stock.name]), float(stock.price) - float(prices[stock.name]))
        price_change.append(row)

    return price_change

def print_report(reportdata: list, formatter):
    """
    Print the report
    """
    formatter.headings([ 'Name', 'Shares', 'Price', 'Change' ])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def print_portfolio_value(portfolio: list, prices: list):
    portfolio_value = 0.0
    current_value = 0.0
    for stock in portfolio:
        portfolio_value += float(stock.shares) * float(stock.price)
        current_value += float(stock.shares) * float(prices[stock.name])


    print('Portfolio value:', portfolio_value)
    print('Current value:', current_value)
    print('Gain / Loss', portfolio_value - current_value)

def portfolio_report(portfolio_name: str, price_name: str):
    portfolio = read_portfolio(portfolio_name)
    prices = read_prices(price_name)

    report = make_report(portfolio, prices)

    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)
    print_portfolio_value(portfolio, prices)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio_file price_file')
    portfile = argv[1]

    pricefile = argv[2]
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
