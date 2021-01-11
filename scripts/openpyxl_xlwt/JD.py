import openpyxl
import json

wb = openpyxl.load_workbook('./TRD_Mnth.xlsx')
sheet0 = wb.get_sheet_by_name('2015-2019-mean')
sheet1 = wb.get_sheet_by_name('Sheet1')

with open('tp.json', 'r') as f:
    data = json.load(f)

row_dict = data['0']
col_dict = data['1']

for i, row in enumerate(sheet1.rows):
    if i == 0:
        continue
    row_id_index = row[0].value
    tp = row[1].value
    col_id_index = 'TP{}/{}'.format(tp.split('-')[0], int(tp.split('-')[1]))
    value = row[2].value

    if row_id_index in row_dict.keys() and col_id_index in col_dict.keys():
        sheet0.cell(row=row_dict[row_id_index], column=col_dict[col_id_index]).value = value

wb.save('ret.xlsx')
