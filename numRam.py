import random
from datetime import datetime, timedelta

'''codigos bres al zar'''

# cantidad = 47

# rango_inicio = 100000
# rango_fin = 900000

# def generar_numeros_unicos(cantidad, rango_inicio, rango_fin):
#     # Verificar si la cantidad de números solicitada es mayor que el rango disponible
#     if cantidad > (rango_fin - rango_inicio + 1):
#         print("No se pueden generar tantos números únicos en el rango proporcionado.")
#         return

#     numeros_generados = []

#     while len(numeros_generados) < cantidad:
#         numero = random.randint(rango_inicio, rango_fin)

#         # Verificar si el número ya ha sido generado
#         if numero not in numeros_generados:
#             numeros_generados.append(numero)

#     return numeros_generados

# lis = generar_numeros_unicos(cantidad, rango_inicio, rango_fin)

# for elem in lis:
#     print(elem)
# Lista principal
# lista_principal = [
#     5.001, 5.002, 5.004, 5.021, 5.03, 5.031, 5.034, 5.036, 5.038, 5.04,
#     15.832, 5.044, 5.045, 5.051, 5.055, 5.059, 5.079, 5.088, 5.091, 5.093,
#     5.101, 5.107, 5.113, 5.12, 5.125, 5.129, 5.134, 5.138, 5.142, 5.145,
#     5.147, 15.476, 5.15, 5.154, 5.172, 5.19, 5.197, 5.206, 5.209, 5.212,
#     5.234, 5.237, 5.24, 5.25, 5.264, 5.266, 5.282, 23.675, 5.306, 5.308,
#     5.31, 27.361, 5.315, 5.318, 5.321, 5.347, 5.353, 5.36, 5.361, 5.086,
#     5.368, 5.376, 5.38, 5.39, 5.4, 5.411, 5.425, 5.44, 5.467, 5.475,
#     5.48, 5.483, 5.49, 5.495, 5.501, 5.541, 5.543, 5.576, 5.579, 5.585,
#     5.591, 5.604, 5.607, 5.615, 5.628, 5.631, 5.642, 15.189, 52.699, 5.652,
#     5.656, 68.575, 68.573, 5.66, 5.664, 5.667, 5.67, 5.674, 5.679, 5.69,
#     5.697, 5.736, 5.761, 50.37, 5.789, 5.79, 5.792, 5.809, 5.819, 5.837,
#     5.842, 5.847, 5.854, 5.856, 5.858, 5.861, 5.885, 5.887, 5.89, 5.893,
#     5.895, 8.001, 8.078, 8.141, 8.296, 8.421, 8.433, 8.436, 8.549, 8.558,
#     8.634, 8.638, 8.675, 8.685, 8.758, 8.77, 8.832, 8.849, 13.006, 13.042,
#     13.052, 13.062, 13.14, 13.16, 13.188, 13.212, 13.222, 13.248, 13.43,
#     13.433, 13.44, 13.458, 13.468, 13.473, 13.49, 13.549, 13.58, 13.6,
#     13.647, 13.65, 13.657, 13.673, 13.683, 13.744, 13.76, 13.78, 13.81,
#     13.836, 13.838, 13.873, 15.001, 15.022, 15.047, 15.051, 15.09, 15.092,
#     15.097, 15.104, 15.106, 15.109, 15.114, 15.131, 15.135, 15.162, 15.172,
#     15.176, 15.18, 15.183, 15.185, 15.187, 15.204, 15.212, 15.215, 15.218,
#     15.223, 15.224, 15.226, 15.232, 15.236, 15.238, 15.244, 15.248, 15.272,
#     15.276, 15.293, 15.296, 15.299, 15.317, 15.322, 15.325, 15.332, 15.362,
#     15.367, 15.368, 15.377, 15.38, 15.401, 15.425, 15.442, 15.455, 15.464,
#     15.466, 15.469, 15.48, 15.491, 15.494, 15.5, 15.507, 15.511, 15.514,
#     15.516, 15.518, 15.522, 15.531, 15.533, 15.542, 15.55, 15.572, 15.58,
#     15.599, 15.6, 15.621, 15.632, 15.638, 15.646, 15.66, 15.673, 15.686,
#     15.69, 15.696, 15.72, 15.723, 15.74, 15.753, 15.755, 15.757, 15.759,
#     15.761, 15.762, 15.763, 15.764, 15.774, 15.776, 15.778, 15.79, 15.798,
#     15.804, 15.808, 15.81, 15.814, 15.82, 15.822, 15.835, 15.839, 15.842,
#     15.861, 15.879
# ]

# # Lista de datos a buscar
# datos_a_buscar = municipios = [
#     15.092, 15.109, 13.836, 5.861, 15.464, 15.466, 68.573, 15.491, 15.58,
#     15.494, 15.162, 15.48, 15.798, 5.347, 13.6, 15.638, 15.401, 5.495, 5.212,
#     5.361, 68.575, 5.4, 13.49, 15.332, 5.607, 15.69, 15.425, 5.89, 15.293,
#     5.697, 15.522, 5.306, 5.04, 13.188, 8.421, 13.657, 5.642, 15.69, 15.109,
#     5.321, 5.887, 5.736, 5.467, 5.04, 15.104, 15.753, 13.76, 13.647, 13.16,
#     5.353, 5.044, 5.154, 15.776, 15.189, 5.642
# ]



# # Usando lista de comprensión para buscar datos
# datos_encontrados = [dato for dato in datos_a_buscar if dato in lista_principal]

# val =0
# for elem in datos_encontrados:
#     print(elem)
#     val +=1
#     print(val)



'''Fehcas al azar''' 

# def generar_fechas_nacimiento(cantidad):
#     fechas_nacimiento = []

#     for _ in range(cantidad):
#         # Generar un año de nacimiento entre 1950 y 2005
#         anio = random.randint(1950, 2005)
        
#         # Generar un mes y un día al azar
#         mes = random.randint(1, 12)
#         dia = random.randint(1, 28)  # Limitado a 28 para simplificar, ajusta según tus necesidades
        
#         # Crear la fecha de nacimiento
#         fecha_nacimiento = datetime(anio, mes, dia)
        
#         # Agregar la fecha de nacimiento a la lista
#         fechas_nacimiento.append(fecha_nacimiento.strftime("%d/%m/%Y"))

#     return fechas_nacimiento

# # Ejemplo de uso: Generar 60 fechas de nacimiento al azar
# fechas_generadas = generar_fechas_nacimiento(60)
# for fecha in fechas_generadas:
#     print(fecha)

'''Edad'''

# def calcular_edad(fecha_nacimiento):
#     fecha_actual = datetime.now()
#     fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
#     edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
#     return edad

# # Utilizando las fechas generadas en el ejemplo anterior
# fechas_generadas = ['17/03/1965',
# '15/10/1966',
# '03/01/1993',
# '04/10/1957',
# '02/02/2001',
# '20/07/1969',
# '05/03/1997',
# '19/11/2005','23/06/1989',
# '17/01/1972',
# '08/10/1957',
# '04/09/1976',
# '20/01/1994',
# '10/07/1950',
# '10/12/1982',
# '17/08/1950',
# '14/08/1993',
# '10/05/1987',
# '15/04/2002',
# '27/06/1979',
# '05/04/1988',
# '23/01/1958',
# '10/12/1950',
# '04/05/1975',
# '18/06/1996',
# '07/02/1974',
# '04/11/1997',
# '14/07/1955',
# '13/11/1954',
# '06/02/1955',
# '09/12/1992',
# '13/04/1973',
# '27/02/1971',
# '24/09/1950',
# '09/03/1964',
# '27/04/1984',
# '21/11/1950',
# '01/12/1994',
# '04/12/1972',
# '03/06/1963',
# '07/12/1974',
# '15/03/2003',
# '25/01/2005',
# '15/09/1985',
# '16/04/1962',
# '23/05/1979',
# '28/01/1963',
# '25/09/1993',
# '03/11/1953',
# '16/11/1990',
# '10/05/1991',
# '25/09/1995',
# '07/02/1979',
# '16/08/1962',
# '27/04/1982',
# '26/10/1978',
# '09/05/1988',
# '08/10/1967',
# '07/07/1970',
# '27/10/1954']  # Reemplaza con tus fechas generadas

# for fecha in fechas_generadas:
#     edad = calcular_edad(fecha)
#     print(edad)
    
'''Barrio aletorio'''

# # Lista original
# codigos_dane_municipio = [
#     5.001, 5.002, 5.004, 5.021, 5.03, 5.031, 5.034, 5.036, 5.038, 5.04,
#     15.832, 5.044, 5.045, 5.051, 5.055, 5.059, 5.079, 5.088, 5.091, 5.093,
#     5.101, 5.107, 5.113, 5.12, 5.125, 5.129, 5.134, 5.138, 5.142, 5.145,
#     5.147, 15.476, 5.15, 5.154, 5.172, 5.19, 5.197, 5.206, 5.209, 5.212,
#     5.234, 5.237, 5.24, 5.25, 5.264, 5.266, 5.282, 23.675, 5.306, 5.308,
#     5.31, 27.361, 5.315, 5.318, 5.321, 5.347, 5.353, 5.36, 5.361, 5.086,
#     5.368, 5.376, 5.38, 5.39, 5.4, 5.411, 5.425, 5.44, 5.467, 5.475,
#     5.48, 5.483, 5.49, 5.495, 5.501, 5.541, 5.543, 5.576, 5.579, 5.585,
#     5.591, 5.604, 5.607, 5.615, 5.628, 5.631, 5.642, 15.189, 52.699, 5.652,
#     5.656, 68.575, 68.573, 5.66, 5.664, 5.667, 5.67, 5.674, 5.679, 5.69,
#     5.697, 5.736, 5.761, 50.37, 5.789, 5.79, 5.792, 5.809, 5.819, 5.837,
#     5.842, 5.847, 5.854, 5.856, 5.858, 5.861, 5.885, 5.887, 5.89, 5.893,
#     5.895, 8.001, 8.078, 8.141, 8.296, 8.421, 8.433, 8.436, 8.549, 8.558,
#     8.634, 8.638, 8.675, 8.685, 8.758, 8.77, 8.832, 8.849, 13.006, 13.042,
#     13.052, 13.062, 13.14, 13.16, 13.188, 13.212, 13.222, 13.248, 13.43,
#     13.433, 13.44, 13.458, 13.468, 13.473, 13.49, 13.549, 13.58, 13.6,
#     13.647, 13.65, 13.657, 13.673, 13.683, 13.744, 13.76, 13.78, 13.81,
#     13.836, 13.838, 13.873, 15.001, 15.022, 15.047, 15.051, 15.09, 15.092,
#     15.097, 15.104, 15.106, 15.109, 15.114, 15.131, 15.135, 15.162, 15.172,
#     15.176, 15.18, 15.183, 15.185, 15.187, 15.204, 15.212, 15.215, 15.218,
#     15.223, 15.224, 15.226, 15.232, 15.236, 15.238, 15.244, 15.248, 15.272,
#     15.276, 15.293, 15.296, 15.299, 15.317, 15.322, 15.325, 15.332, 15.362,
#     15.367, 15.368, 15.377, 15.38, 15.401, 15.425, 15.442, 15.455, 15.464,
#     15.466, 15.469, 15.48, 15.491, 15.494, 15.5, 15.507, 15.511, 15.514,
#     15.516, 15.518, 15.522, 15.531, 15.533, 15.542, 15.55, 15.572, 15.58,
#     15.599, 15.6, 15.621, 15.632, 15.638, 15.646, 15.66, 15.673, 15.686,
#     15.69, 15.696, 15.72, 15.723, 15.74, 15.753, 15.755, 15.757, 15.759,
#     15.761, 15.762, 15.763, 15.764, 15.774, 15.776, 15.778, 15.79, 15.798,
#     15.804, 15.808, 15.81, 15.814, 15.82, 15.822, 15.835, 15.839, 15.842,
#     15.861, 15.879
# ]


# # Seleccionar 55 números al azar
# numeros_seleccionados=[]
# for i in range(60):
#     numeros_seleccionados.append(random.choice(codigos_dane_municipio))

# # Imprimir los números seleccionados
# for elem in numeros_seleccionados:
#     print(elem)






# numeros = [326, 568, 396,262,517,258,971,806,617,851,430,675,204,445,400,399,168,487,621,855,853,489,217,826,216,356,709,723,154,148,947,775,543,153,455,693,461,848,346,789,930,814,938,469,863,712,922,937,760,365,576,745,513,933,702,460,481,133,909,961,959,112,726,186,718,892,686,225,101,223,419,139,405,973,860,792,516,159,382,549,505,654,952,252,108,852,312,129,606,921]

# # Seleccionar tres números aleatorios sin repetición
# numeros_aleatorios = random.sample(numeros, 55)

# for elem in numeros_aleatorios:
#     print(elem)


# def generar_nombre_completo(genero):
#     nombres_hombre = ["Juan", "Carlos", "Miguel", "David", "Luis", "Javier", "Francisco", "Andrés", "Alejandro", "Daniel", Pedro, 'Felipe', 'Sebastian', 'Jairo', 'Fernando', 'Erick', 'Jonathan', 'Martín']
#     nombres_mujer = ["Ana", "María", "Laura", "Elena", "Isabel", "Carmen", "Sofía", "Andrea", "Luisa", "Paula", 'Adriana', 'Angela', 'Marta', 'Lucia', 'Carla', 'Martina', 'Paula', 'Leticia', 'Aurora', 'Lina']

#     apellidos = ["García", "Martínez", "López", "Fernández", "Pérez", "Gómez", "Rodríguez", "Sánchez", "Romero", "Díaz"
#                  , 'Erazo', 'Ceballos', 'Delgado', 'Ascuntar', 'Rivera', 'Montenegro', 'Coronel', 'Cordoba', 'Chapal']

#     # Elegir aleatoriamente un nombre y dos apellidos
#     if genero.lower() == 'hombre':
#         nombre = random.choice(nombres_hombre)
#     elif genero.lower() == 'mujer':
#         nombre = random.choice(nombres_mujer)
#     else:
#         raise ValueError("Género no reconocido. Utiliza 'hombre' o 'mujer'.")

#     apellido_1 = random.choice(apellidos)
#     apellido_2 = random.choice(apellidos)

#     return f"{nombre} {apellido_1} {apellido_2}"

# # Generar 55 nombres, 25 para hombres y 30 para mujeres
# nombres_hombres = [generar_nombre_completo("hombre") for _ in range(25)]
# nombres_mujeres = [generar_nombre_completo("mujer") for _ in range(30)]

# # Combinar las listas de nombres para obtener una lista completa
# nombres_completos = nombres_hombres + nombres_mujeres

# # Imprimir los nombres generados
# for i, nombre in enumerate(nombres_completos, start=1):
#     print(f"{nombre}")


# Obtén la fecha actual
fecha_actual = datetime.now()

# Lista para almacenar las fechas generadas
fechas_al_azar = []

# Genera 60 fechas al azar de este año
for _ in range(45):
    # Genera un número aleatorio de días atrás desde la fecha actual
    dias_atras = random.randint(0, 364)
    
    # Calcula la fecha restando días aleatorios
    fecha_generada = fecha_actual - timedelta(days=dias_atras)
    
    # Agrega la fecha a la lista
    fechas_al_azar.append(fecha_generada.strftime("%d/%m/%Y"))

# Imprime las fechas generadas
for fecha in fechas_al_azar:
    print(fecha)

  
