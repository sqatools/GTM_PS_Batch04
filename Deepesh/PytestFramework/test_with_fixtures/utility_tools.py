import openpyxl

file_path = r"E:\Trainings\GTM_PS_Batch04_13May24\GTM_PS_Batch04\Deepesh\PytestFramework\excel_file\test_data.xlsx"


def read_excel_data(cell, filename=file_path, sheet_name='Sheet1'):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet_name]
    cell = sheet[cell]
    return cell.value

#val = read_excel_data(file_path, sheet_name='Sheet1', cell='A1')
#print("excel value :", val)
