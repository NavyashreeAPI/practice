from xlrd import *

def readfile(sheet):
    d={}
    wb=open_workbook("../Excel/locators.xlsx")
    sh=wb.sheet_by_name(sheet)
    row_count=sh.nrows
    for i in range(1,row_count):
        data=sh.row_values(i)
        d[data[0]]=(data[1],data[2])
    return d

