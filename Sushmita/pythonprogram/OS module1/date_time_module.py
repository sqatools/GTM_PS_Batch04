import datetime

today_date = datetime.date.today()
print(today_date)

current_time_with_date = datetime.datetime.now()
print(current_time_with_date)

# date time formating

date_var = current_time_with_date.strftime("%d_%m_%Y_%H_%M_%S")
print(date_var)
