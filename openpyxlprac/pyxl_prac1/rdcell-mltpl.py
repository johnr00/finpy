
#reading multiple cells
#make and write new Workbook
from openpyxl import Workbook

book = Workbook
sheet = book.active

rows = (
    ('Items', 'Quantity'),
    ('coins', 23),
    ('chairs', 3),
    ('pencils', 5),
    ('bottles', 8),
    ('books', 30)
)

for row in rows:
    sheet.append(row)

book.save('rdmulticells.xlsx')

#reading multiple cells
#import module
import openpyxl
#init book, existing cel
book = openpyxl.load_workbook('rdmulticells.xlsx')
#init sheet
sheet = book.active

#read data from cells A1 to B6, think box
cells = sheet['A1': 'B6']

for c1, c2 in cells:
    print('{0:8} {1:8}'.format(c1.value, c2.value))
