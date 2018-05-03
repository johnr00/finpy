#navigate to head of directory for the project
#source: zetcode.com/articles/openpyxl

#MAKE A NEW WB
#importing Workbook class from openpyxl module, container for the doc
from openpyxl import Workbook
#importing time module, which does....
import time

#creates a new workbook (excel doc), called book
book = Workbook()
#refer to the sheet you want, makes 'sheet' the active sheet
sheet = book.active
#write to cells A1 and C2
sheet['A1'] = 56
sheet['A2'] = 43
#find current time, set it in sheet['A3']
now = time.strftime('%x')
sheet['A3'] = now
#saves book in CD
book.save('make-save-wb-basic.xlsx')
