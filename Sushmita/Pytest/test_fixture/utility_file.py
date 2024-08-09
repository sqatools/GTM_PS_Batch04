import openpyxl

file_path=r"C:\GitRepo\Sushmitashastri23\Newpython\GTM_PS_Batch04\Sushmita\Pytest\excel_file\data_file.xlsx"

def read_excel_data(cell, filename=file_path, sheet_name='Sheet1'):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet_name]
    cell = sheet[cell]
    return cell.value

# val = read_excel_data(file_path, sheet_name='Sheet1',cell='A1')
# print("excel value :", val)
