import openpyxl

file_path=r"C:\Git_Repo\GTM_PS_Batch04\NikhilaJoy\pytest\excelfile\test_data.xlsx"

def read_excel(cell,filename=file_path,sheet_name='Sheet1'):
    wb=openpyxl.load_workbook(filename)
    sheet=wb[sheet_name]
    cell=sheet[cell]
    return cell.value
#val=read_excel(filename=file_path,sheet_name='Sheet1',cell='A1')
#print(val)