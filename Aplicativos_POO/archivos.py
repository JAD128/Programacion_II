'''
Archivos 
    Campo -> Variables 
    - Campos relacionados 
        EJ:
        cod nombre apellido cedula...
            Registro
            - Conjunto de eregistros 
            - archivo 
Administrador de la informacion 
    Administrar dispositivos de almacenamiento (Auxiliar) D.D
    Archivos <- Carpetas 
        Datos .dat | .txt       | 
        Fuente .py | .java      | Informacion permanete 
        Ejecutables .exe        |

Programa 
    Datos:
        - Variables 
        - Requisitos 
    Permanetes
        Archivos
            Texto -> Caracteres -> ASCII -> bicode
            Binario         | Serializacion 
            Datos | Objetos | POO
    
Abrir archivo para:
    Leer informacion -> 'r' | vacio -> f = open('datos.dat', 'r') | Debe existir, caso contrario genera error
    Escribir -> 'w' -> f1 = open('datos2.dat', 'w') | Con 'w' si no esta, crea el archivo
    Adicionar -> 'a' -> f2 = open('datos2.dat', 'a') | Modificar el archivo
open(nombre_archivo, [modo apertura -> opcional])
    nombre_archivo -> ruta - path:
                                - Relativo 
                                    open('Dato1.dat) -> abre para lectura 
                                        relativo 
                                - Absoluto 
                                    'c:Documento/Archivo/...'
Open -> clase -> objeto 
f = open('Archivo') | Se debe cerrar los archivos f1.close()
'''
# #Llenar informacion en archivo

# f = open('archivo.dat', 'w')
# f.write('Cadena\nCadena1\n')
# f.write('Primera cadena en archivo\n')
# f.write('Segunda cadena\n')
# f.write('Tercera cadena\n')
# f.close()
# '''Notas: La forma como se escribe en un archivo, debe ser la forma como se lee'''

# #leer informacion archivo

# '''Lectura:
#         - read() | Lee todo el archivo y forma un string
#         - readline()
#         - readlines()'''
# f = open('archivo.dat', 'r')
# print(f.read())
# f.seek(0)
# print(f'Lista: {f.readlines()}') # Cadena vacia

# f.seek(0)
# print(f'\nImprimir cadenas\n')
# for elem in f:
#     print(f'linea: {elem}')

# #Modificar archivo

# f = open('archivo.dat', 'a')
# f.write('New cadena| cosas que el profe no enseño')
# f.close()

# f = open('archivo.dat', 'r')
# print(f.read())

######################################################

cf = open('calificaciones.dat', 'w')
lc = [1, 2, 3, 4]
mc = [[3.5, 3.5, 5], [1, 1, 1], [5, 5, 5], [4.5, 4.5, 4.5]]
print(f'Lista: {lc}\nMatriz: {mc}')

for i in range(len(lc)):
    cf.write(f'{str(lc[i])} ')
    for no in mc[i]:
        cad = f'{str(no)} '
        cf.write(cad)
    cf.write(' \n')

cf.close()

cff = open('calificaciones.dat', 'r')
print(cff.read())
cff.seek(0)
for ele in cff:
    print(f'Lista: {ele}')
cff.seek(0)
lm2 = []
lm1 = []
for cad in cff:
    lm1.append(cad)

for ele in lm1:
    lv = []
    for cad in ele:
        lv = ele.strip()
        
    lm2.append(lv)

nl = []
for val in lm2:
    nl.append(val.split())

lc1 = []  
lm3 = []
for l in nl:
    lm1 = [] 
    for i in range(len(l)):
         
        if i == 0:
            lc1.append(int(l[i]))
        else:
            lm1.append(float(l[i]))
    lm3.append(lm1)
        
print(lc1)
print(lm3)