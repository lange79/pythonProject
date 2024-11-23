import datetime
from calendar import month

mi_hora= datetime.time(17,35)
mi_dia=datetime.date(2024,11,23)


print(mi_hora)
print(mi_dia)
print(mi_dia.ctime())
print(mi_dia.today())


from datetime import datetime
mi_fecha = datetime(2025,5,15,22,10,15,2500)
mi_fecha = mi_fecha.replace(month = 7)

print(mi_fecha)


from datetime import date

nacimiento=date(1995,3,5)
defuncion=date(2095,6,19)

vida= defuncion-nacimiento

print("Vivio: ",vida)
print(vida.days)

from datetime import datetime

despierta = datetime(2022,10,5,7,30)
duerme= datetime(2022,10,5,23,45)

vigilia=duerme-despierta
print(vigilia)
print(vigilia.seconds)

from datetime import date

hoy = date.today()
print("Hoy es: ",hoy)

hora_actual=datetime.now()
print(hora_actual)