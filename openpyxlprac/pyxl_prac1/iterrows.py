
#iterating rows: returns cells from the WB as rows

import openpyxl
book = openpyxl.load_worbook('iterbyrows.xlsx')
sheet = book.active
#iterates of data row by row, provides the boundaries
for row in sheet.iter_rows(min_row = 1, min_col = 1, max_row = 6, max_col = 3):
    for cell in row:
        print(cell.value, end =" ")
    print()

book.save('iterbyrows.xlsx')
