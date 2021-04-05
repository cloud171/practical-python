#!/usr/bin/env python3
# tableformat.py
#

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()
    
def create_formatter(name):
  if name == 'txt':
    formatter = TextTableFormatter()
  elif name == 'csv':
    formatter = CSVTableFormatter()
  elif name == 'html':
    formatter = HTMLTableFormatter()
  else:
    raise RuntimeError(f'Unknown format {fmt}')
  
  return formatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a stable in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end= ' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output protofio data in csv format
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output protofio data in csv format
    '''

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):

        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

