# report.py
#
# Exercise 2.4
import fileparse
import csv

def read_portfolio(filename: str) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and prices.[]
    '''
    return fileparse.parse_csv('Data/portfolio.csv',select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    prices = {}
    rows = fileparse.parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
    for row in rows:
        if row:
            name, price = row
            prices[name] = price

    return prices

def make_report(portfolio, prices):
    price_change = []
    for stock in portfolio:
        row = (stock['name'], int(stock['shares']), float(prices[stock['name']]), float(stock['price']) - float(prices[stock['name']]))
        price_change.append(row)

    return price_change

def print_report(report: list):
    """
    Print the report
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d}  ${price:>10.2f} {change:>10.2f}')

def print_portfolio_value(portfolio: list, prices: list):
    portfolio_value = 0.0
    current_value = 0.0
    for stock in portfolio:
        portfolio_value += float(stock['shares']) * float(stock['price'])
        current_value += float(stock['shares']) * float(prices[stock['name']])


    print('Portfolio value:', portfolio_value)
    print('Current value:', current_value)
    print('Gain / Loss', portfolio_value - current_value)

def portfolio_report(portfolio_name: str, price_name: str):
    portfolio = read_portfolio(portfolio_name)
    prices = read_prices(price_name)

    report = make_report(portfolio, prices)
    print_report(report)
    print_portfolio_value(portfolio, prices)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
