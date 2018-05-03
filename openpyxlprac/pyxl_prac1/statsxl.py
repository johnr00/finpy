#imports module
import openpyxl
#imports a module as a shortened name to be called later
import statistics as stats
#imports the data, only pulls the data not the underlying formula
book = openpyxl.load_workbook('numbers.xlsx', data_only = True)
#grabs the current active sheet, sets it to var sheet
sheet = book.active
#garbs the current rows w/ value, sets it to var rows
rows = sheet.rows
#values equal empty list
values = []
#fills in values list, by row (l->r), with append
for row in rows:
    for cell in row:
        values.append(cell.value)
#brackets pull the format function, doesn't need a 0
print('Number of values: {0}'.format(len(values)))
print('Sum of values: {0}'.format(sum(values)))
print('Minimum value: {0}'.format(min(values)))
print('Minimum value: {0}'.format(max(values)))
print('Mean: {0}'.format(stats.mean(values)))
print('Median: {0}'.format(stats.median(values)))
print('Standard Deviation: {0}'.format(stats.stdev(values)))
print('Variance: {0}'.format(stats.variance(values)))
