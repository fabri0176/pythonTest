import datetime
import locale
import pytz # pip3 install pytz
locale.setlocale(locale.LC_ALL, 'es') #Estableciendo lenguaje

dt = datetime.datetime.now() #ahora
print(dt)
print("Año: ",dt.year)
print("Mes: ",dt.month)
print("Hora: ",dt.hour)
print("Minuto: ",dt.minute)
print("Segundo: ",dt.second)
print("Microsegundo: ",dt.microsecond)
print("Microsegundo: ",dt.tzinfo)
for i in range(60):
    print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("====================================")
#get Fecha
dt_old = datetime.datetime(2000,1,1)
print(dt_old)

dt_old = dt_old.replace(year=3000)
print(dt_old)
print("====================================")
print("Formateo Datetime")
print("ISO Format",dt.isoformat())
print("====================================")
print("Formateo Manual Español: ",dt.strftime("%A %d %B %Y %I:%M")) #Hora meridiano

print("Formateo Manual Español: ",dt.strftime("%A %d  de %B del %Y %H:%M")) #Hora 24 horas
print("====================================")
print("SUMA FECHAS")
t = datetime.timedelta(days=14,hours=4)
proxima_fecha = dt+t
print("Sumar dos semanas: ",proxima_fecha.strftime("%A %d  de %B del %Y %H:%M")) #Hora 24 horas

hace_tiempo = dt-t
print("Sumar dos semanas: ",hace_tiempo.strftime("%A %d  de %B del %Y %H:%M")) #Hora 24 horas
print("====================================")
print("Zonas Horarias") # pip3 install pytz
print(pytz.all_timezones)
print("====================================")
new_date = datetime.datetime.now(pytz.timezone('America/Bogota'))
print(new_date)
print("Sumar dos semanas: ",hace_tiempo.strftime("%A %d  de %B del %Y %H:%M")) #Hora 24 horas
