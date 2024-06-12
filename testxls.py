# pip install XlsxWriter
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A2', 'Hello11 world')
worksheet.write('B5', 'Hello22 world')
worksheet.write('E8', 'Hello33 world')
worksheet.write('G12', 'Hello44 world')

workbook.close()