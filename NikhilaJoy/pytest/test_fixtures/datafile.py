
from utilitytools import read_excel

param_data=[('user_A','ghuh'),
            ('user_B','ewr'),
            ('user_C','yg5'),
            ('user_D','3tr')]

excel_data=[(read_excel(cell="A1"),read_excel(cell="B1")),
            (read_excel(cell="A2"),read_excel(cell="B2")),
            (read_excel(cell="A3"),read_excel(cell="B3")),
            (read_excel(cell="A4"),read_excel(cell="B4"))]

bulk_data=[]
for i in range(1,24):
    bulk_data.append((read_excel(cell=f"E{i}"),read_excel(cell=f"F{i}")))