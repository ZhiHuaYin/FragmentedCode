import xlrd, xlwt
import json

data = {}

path = 'TRD_Mnth.xlsx'

wb = xlrd.open_workbook(path)

sheet_new = wb.sheets()[0]

columns = sheet_new._cell_values[0][1:]

tp = list(range(2, len(columns) + 2))
columns_dict = dict(zip(columns, tp))

rows_list = [x[0] for x in sheet_new._cell_values[1:]]
rows_dict = dict(zip(rows_list, list(range(2, 2 + len(rows_list)))))

data[0] = rows_dict
data[1] = columns_dict
with open('./tp.json', 'w') as f:
    json.dump(data, f, indent=2)

# wb.sheets()[0]._cell_values[rows_id][cols_id] = ??
# wb.sheets()[1]._cell_values[1:]
"""
sheet2 = wb_new.sheets()[1]
for example in sheet2._cell_values[1:]:
    rows_id = rows_dict[example[0]]
    orig = example[1].split('-')
    orig_id = 'TP{}/{}'.format(orig[0], int(orig[1]))
    cols_id = columns_dict[orig_id]
    value = example[2]
    wb_new.sheets()[0]._cell_values[rows_id][cols_id] = value

wb_new.save('ret.xlsx')
"""
