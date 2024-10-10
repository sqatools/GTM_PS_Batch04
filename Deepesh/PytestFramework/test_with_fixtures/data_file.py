from utility_tools import read_excel_data

param_data = [('user_A', '543543'),
             ('user_B', '%^^&%'),
             ('user_C', '%&^*%^&%'),
             ('user_D', '^&%^&%*&')]

excel_data = [(read_excel_data(cell="A1"), read_excel_data(cell="B1")),
              (read_excel_data(cell="A2"), read_excel_data(cell="B2")),
              (read_excel_data(cell="A3"), read_excel_data(cell="B3")),
              (read_excel_data(cell="A4"), read_excel_data(cell="B4"))]


bulk_data = []
n = 39
for i in range(1, n):
    bulk_data.append((read_excel_data(cell=f"D{i}"), read_excel_data(cell=f"F{i}")))
