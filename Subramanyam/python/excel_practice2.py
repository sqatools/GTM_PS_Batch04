import openpyxl

def write_even_number_rows(filename,sheetname):
    wb=openpyxl.load_workbook(filename)
    sheet=wb[sheetname]
    for num in range(2,21,2):
        sheet["B"+str(num//2)]=num
    wb.save(filename)

#write_even_number_rows("even_numbers.xlsx","Even Numbers")



def table():
    wb=openpyxl.load_workbook("table_of_5.xlsx")
    sheet=wb.active
    sheet["A1"]="5*n"
    sheet["B1"]="multiplication"

    for i in range(1,11):
        n=i
        multiplication=5 * n
        sheet[f'A{i+1}']=f'5*n'
        sheet[f'B{i+1}']=multiplication
    wb.save("table_3.xlsx")
table()
