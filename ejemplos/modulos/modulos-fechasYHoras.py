import time

tiempo = time.time()
time.localtime(timepo)
timepo.tm_year

time.strftime('%d/%m/$Y %H:%M:%S')
time.strftime('%d/%b/$Y %H:%M:%S')


from datetime import datetime, date, time, timedelta

datetime.now()
hora = time(10,5,0)
hora1 = time(23,15,0)
hora < hora1

fecha = date.today()
fecha1 = fecha.timedelta(days = 2)

timepo = datetime.strptime("12/12/2003", '%d/%m/%Y')


import calendar

anyo = date.today().year
mes = date.today().month
calendarioMes = calendar.month(anyo, mes)

print(calendar.TextCalendar(calendar.MONDAY).formatyear(2017, 2, 1, 1, 2))
