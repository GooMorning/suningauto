import xlrd
color = []
Glass = []
gooid = []
data = xlrd.open_workbook('C:/Users/86177/Desktop/苏宁自动脚本/autoin/商品.xlsx')

table = data.sheet_by_name('Sheet1')

goodsname = table.cell_value(0, 1)
goodsmodel = table.cell_value(1, 1)
VOLUM = str(table.cell_value(2, 1))
BRGEW = str(table.cell_value(3, 1))
texture = table.cell_value(4, 1)
price = table.cell_value(7,1)
# for i in range(0,table.ncols):
#     color.append(str(table.cell_value(5,i)))
# color = [table.cell_value(5, 1), table.cell_value(5, 2), table.cell_value(5, 3), table.cell_value(5, 4)]
# for i in range(0,table.)
# Glass = [str(table.cell_value(6, 1)), str(table.cell_value(6, 2)), str(table.cell_value(6, 3)), str(table.cell_value(6, 4))]

table2 = data.sheet_by_name('Sheet2')
color = table.row_values(5)
Glass = table.row_values(6)
color = [i for i in color if i != '']
Glass = [i for i in Glass if i != '']
Glass = [str(i) for i in Glass]
del color[0]
del Glass[0]
# print(color,Glass)
for i in range(0, table2.nrows):
    gooid.append(str(table2.cell_value(i, 0)))

# print(gooid)
