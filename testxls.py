# pip install XlsxWriter
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')
worksheet.write('B4', 'Hello world')
worksheet.write('E7', 'Hello world')
worksheet.write('G11', 'Hello world')

workbook.close()