from datetime import datetime

def edad(fechaIn):
    fechaA = datetime.now()
    if fechaIn.month > fechaA.month and fechaIn.day >= fechaA.day:
        años = fechaA.year - fechaIn.year - 1
    elif fechaIn.month < fechaA.month:
        años = fechaA.year - fechaIn.year 
    elif fechaIn.month == fechaA.month and fechaIn.day <= fechaA.day:
        años = fechaA.year - fechaIn.year 
    elif fechaIn.month == fechaA.month and fechaIn.day > fechaA.day:
        años = fechaA.year - fechaIn.year - 1
    return años
def dias(fechaIn):
    
    fechaA = datetime.now()
    dias1 = fechaA - fechaIn
    return dias1

def calcular_diferencia_desde_2023(fecha_referencia):
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_referencia
    años = diferencia.days // 365
    meses = (diferencia.days % 365) // 30
    dias = (diferencia.days % 365) % 31
    return años, meses, dias

años, meses, días = calcular_diferencia_desde_2023(datetime(2001, 3, 13))

print(f"Han pasado {años} años, {meses} meses y {días} días")

años = edad(datetime(2001,3,2))
print(años)
dia = dias(datetime(2004, 11, 6))
print(dia.days)

