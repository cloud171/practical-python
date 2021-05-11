# ticket.py

from follow import follow
import report
import csv
import tableformat

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfolio_file, stocklog_file, fmt):
    portfolio = report.read_portfolio(portfolio_file)
    rows = parse_stock_data(follow(stocklog_file))
    rows = (row for row in rows if row['name'] in portfolio)

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change']    )
    for stock in rows:
        rowdata = [ stock['name'], f"{stock['price']:0.2f}", f"{stock['change']:0.2f}" ]
        formatter.row(rowdata)


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)

