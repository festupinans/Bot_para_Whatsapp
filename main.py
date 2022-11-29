import time
from datetime import datetime
import pywhatkit
import openpyxl
from numpy.core.defchararray import upper

book = openpyxl.load_workbook('aver.xlsx', data_only=True)
hoja = book.active
celdas = hoja['A2' : 'B5']
list_numeros = []

for numero in list_numeros:
    seconds = time.time() + 60
    date = datetime.fromtimestamp(seconds)
    pywhatkit.sendwhatmsg(f'+{numero[1]}', "Pruebas con python, si le llego el mensaje, voy triunfando hpta", date.hour, date.minute, 10, True, 10)
    print(f'A {upper(numero[0])}, Se le ha enviado el mensaje existosamente')