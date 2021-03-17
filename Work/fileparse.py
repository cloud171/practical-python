# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, silence_errors=False, delimiter=','):
    '''
    "Parase a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if has_headers:
            headers = next(rows)

            if not select:
                select = headers
            indices = [ headers.index(colname) for colname in select ]

        records = []
        try:
            for row_idx, row in enumerate(rows):
                if not row:
                    continue

                if types:
                    row = [func(val) for func, val in zip(types, row)]

                if has_headers:
                    record = { colname: row[index] for colname, index in zip(select, indices)  }
                else:
                    record = [ col for col in row]
                    record = tuple(record)


                records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {row_idx}: {e}')

        return records
