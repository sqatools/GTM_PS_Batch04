
import openpyxl

file_path = r"D:\GitRepo\AutomationRepo\Seleniumpython\GTM_PS_Batch04\Mahila\pytest_framework\test_fixtures\excel_file\test_data.xlsx"
def read_excel_data(cell,filename=file_path,sheet='Sheet1'):  #cell name only change
    wb=openpyxl.load_workbook(filename)
    sheet = wb[sheet]
    cell = sheet[cell]
    return cell.value