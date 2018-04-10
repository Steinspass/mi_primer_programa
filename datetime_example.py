import datetime

year = int(input("Dime el año: "))
month = int(input("dime el mes: "))
day = int(input("dime el dia: "))

user_date = datetime.datetime(year=year, month=month, day=day )

time_remaining = user_date - datetime.datetime.now()

print("Faltan {} dias y {} minutos".format(time_remaining.days, int(time_remaining.seconds / 60)))
print("pues el dia es  {}".format(user_date.strftime("%d del %m de %Y")))