#reading cells- reading previously written data

#notice no import of Workbook, bc the Workbook exists
import openpyxl

#loads existing xlsx file
book = openpyxl.load_workbook('make-save-wb.xlsx')
sheet = book.active

#set contents of the sheet['cell'] to a var
a1 = sheet['A1']
a2 = sheet['A2']
a3 = sheet.cell(row = 3, column = 1)

#prints the value w/in the vars
print(a1.value)
print(a2.value)
print(a3.value)
