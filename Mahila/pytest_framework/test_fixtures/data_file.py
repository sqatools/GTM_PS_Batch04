
from utility_tools import read_excel_data

parm_data = [('user_A', 'sdfdg'),('userB', 'fgfdbdgfb'),
             ('userC', 'fbdgbdeb'),('userD', 'kkjkjkiji')]

excel_data = [(read_excel_data(cell="A1"),read_excel_data(cell="B1")),
              (read_excel_data(cell="A2"),read_excel_data(cell="B2")),
              (read_excel_data(cell="A3"),read_excel_data(cell="B3")),
              (read_excel_data(cell="A4"),read_excel_data(cell="B4"))]

bulk_data=[]
n=16
for i in range(1,n+1):
    bulk_data.append((read_excel_data(cell=f"E{i}"), read_excel_data(cell=f"F{i}")))







