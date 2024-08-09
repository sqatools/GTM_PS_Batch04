from utility_file import read_excel_data

param_data=[('user_A' , 'pass1'),
            ('user-B' , 'pass2'),
            ('user_C' , 'pass3'),
            ('user_D' , 'pass4')

]

excel_data=[(read_excel_data(cell='A1'),read_excel_data(cell='B1')),
            (read_excel_data(cell='A2'),read_excel_data(cell='B2')),
            (read_excel_data(cell='A3'),read_excel_data(cell='B3')),
            (read_excel_data(cell='A4'),read_excel_data(cell='B4'))
            ]


bulk_data = []
n = 39
for i in range(1, n):
    bulk_data.append((read_excel_data(cell=f"D{i}"), read_excel_data(cell=f"E{i}")))
