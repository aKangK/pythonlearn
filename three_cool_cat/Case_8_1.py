from datetime import datetime,date,time
print(datetime.now())
today=datetime.now()
print(datetime.date(today))
print(datetime.time(today))
print(datetime.ctime(today))
print(datetime.utcnow())
print(datetime.timestamp(today))
print(datetime.fromtimestamp(datetime.timestamp(today)))
date1=date(2019,12,31)
time1=time(23,59,59)
print(datetime.combine(date1,time1))
datetime1=datetime(2019,12,31,23,59,59)
print(datetime1)
datetime2=datetime.strptime("12/2/18 20:59",'%d/%m/%y %H:%M')
print(datetime2)
for i in datetime.timetuple(today):
    print(i)
print(today.isocalendar())
print(today.strftime("%Y年%m月%d日 %H:%M:%S %p"))
print(today.strftime("%Y年%m月%d日 %H:%M:%S %p  %a %A %b %B %c %j %p %U %w %W %x %X %Z"))