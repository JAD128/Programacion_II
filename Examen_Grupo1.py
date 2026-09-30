def punto1():
    print('''1. Se tiene un vector y una matriz con datos numéricos, buscar un dato en el vector que tiene estas condiciones:
El dato es el segundo Fibonacci de un rango en un vector cuyos límites están determinados por el primo1 y primo2 presentes en 
el rango de la matriz comprendido entre el mayor y el menor es esta.
Mostrar el dato y su posición.
''')
    # l = []
    # llenarLista(l)
    l= [3, 11, 5, 8, 17, 11, 7, 25]
    m = [[9 , 15, 7], [3, 10, 11], [14, 2, 9]]
    # m = []
    # llenarMAtriz(m)
    print(f'Lista:\n{l}\nMatriz:\n{m}')
    pos1, pos2 = mayMenMatriz(m)
    primr1, primr2 = primRnagos(m, pos1, pos2)
    ran1, ran2 = buscarDatosLista(l, primr1, primr2)
    sFibonacci, posFi = buscarFiboLista(l, ran1, ran2)
    print(f'El segundo fibonacci en la lista es {sFibonacci} y su posicion {posFi}')

def punto2():
    punt2 = '''2.Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Hallar la clave del primo mayor y Fibonacci menor que están en las listas de los valores y formar una lista con los pares 
comprendidos entre estos dos valores y el promedio de estos.
'''
    # dic = {}
    # llenarDiccionarioListas(dic)
    dic = {3:[12, 2, 6, 4], 5: [24, 56, 78, 89], 4: [22, 56, 71, 86]}
    print(f'Diccionario: \n{dic}')
    fibM, clFi, prM, clPr = clavePriMayorFibMen(dic)
    print(f'La clave del primo mayo: {prM} es: {clPr}\nLa clave del fibonacci menor {fibM} es: {clFi}')
    pos1, pos2, m = posicionesMatriz(fibM, prM, dic)
    lp = llenarListaPares(pos1, pos2, m)
    print(f'Lista de pares: {lp}')
    promedio = promedioLista(lp)
    print(f'El promedio de la lista de pares es: {promedio} ')
  
def punto3():
    punt3 = '''3.Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Formar dos conjuntos asi:
Conjunto 1 con los número pares de la lista valor de aquellas claves que son primos 
Conjunto 2 con los número pares de la lista valor de aquella claves que son fibonacci
Con estos dos conjuntos formar dos cadenas
Cadena1 con los pares comunes
Cadena2 con la unión de los pares sin elementos comunes
'''
    print(punt3)
    dic = {}
    llenarDiccionarioListas(dic)
    s1 = conjunto1(dic)
    print(f'Conjunto 1: \n{s1}')
    s2 = conjunto2(dic)
    print(f'Conjunto 2: \n{s2}')
    string1 = paresComunes(s1, s2)
    print(f'Cadena con pares comunes: {string1}')
    string2 = paresNoComunes(s1, s2)
    print(f'Cadena de pares no comunes: {string2}')
      
def llenarDiccionarioListas(dic):
    
    cl = int(input('Cantidad de llaves: '))
    for i in range(cl):
        clave = int(input('Clave: '))
        lista = []
        cd = int(input('Cantidad de datos de la lista: '))
        for j in range(cd):
            lista.append(int(input(f'Datos {j+1} de la lista: ')))
        dic[clave] = lista

def conjunto1(dic):
    
    s1 = set()
    for llaves, valores in dic.items():
        if detPrimo(llaves) == True:
            for elem in valores:
                if elem % 2 == 0:
                    s1.add(elem) 
    return s1 

def conjunto2(dic):
    s2 = set()
    for llaves, valores in dic.items():
        if detFibonacci(llaves) == True:
            for elem in valores:
                if elem % 2 == 0:
                    s2.add(elem) 
    return s2

def paresComunes(s1, s2):
    
    for elem in s1:
        if (elem in s2) == True:
            cad1 = ' ' + str(elem)
    return cad1

def paresNoComunes(s1, s2):
    
    for elem in s1:
        if (elem in s2) == False:
            cad = ' ' + str(elem)
    for ele in s2:
        if (ele in s1) == False:
            cad1 = " " + str(ele)        
    cad2 = cad + cad1 
    return cad2
                
def detPrimo(nro):
    b = 0
    c = 2
    while c < nro:
        if nro % c == 0:
            b = 1
        c+=1
    if b == 0:
        return True
    else:
        return False

def detFibonacci(nro):
    s = 0
    r = 1
    t = 0
    while t < nro:
        t = s + r
        s = r
        r = t
    if t == nro:
        return True
    else:
        return False
    
def clavePriMayorFibMen(dic):
    
    l = list(dic.values())
    print(l)
    i  = 0
    b = 0
    while i < len(l) and b == 0:
        j = 0
        while j < len(l[i]) and b == 0:
            if i == 0 and j == 0:
                priMay = l[i][j]
                fibMen = l[i][j]
                b = 1
            j+=1
        i+=1
    
    for llaves, values in dic.items():
        for elem in values:
            if detFibonacci(elem)==True:
                if elem < fibMen:
                    fibMen = elem
                    claveFi = llaves
            elif detPrimo(elem) == True:
                if elem > priMay:
                    priMay = elem
                    clavePr = llaves
    return fibMen, claveFi, priMay, clavePr

def posicionesMatriz(fibmen, primmay, dic):
    
    b1 = 0
    b2 = 0
    m = list(dic.values())
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == fibmen and b1 == 0:
                pos1 = [i,j]
                b1 = 1
            if m[i][j] == primmay and b2 == 0:
                pos2 = [i, j]
                b2 = 1
    return pos1, pos2, m

def llenarListaPares(pos1, pos2, m):
    lp = []
    b = 0
    if pos1[0] < pos2[0]:
        i = pos1[0]
        j = pos1[1]
        while i < len(m) and b == 0:
            while j < len(m[i]) and b == 0:
                if i == pos2[0] and j == pos2[1]:
                    b = 1
                if m[i][j] % 2 == 0:
                    lp.append(m[i][j])
                j+=1
            j = 0
            i+=1
    elif pos2[0] < pos1[0]:
        i = pos2[0]
        j = pos2[1]
        while i < len(m) and b == 0:
            while j < len(m[i]) and b == 0:
                if i == pos1[0] and j == pos1[1]:
                    b = 1
                if m[i][j] % 2 == 0:
                    lp.append(m[i][j])
                j+=1
            j=0
            i+=1
    return lp

def promedioLista(l):
    c = 0
    sum = 0
    for elem in l:
        sum = sum + elem
        c+=1
    prom = sum/c
    return prom

def llenarMAtriz(m):
    
    nf = int(input("Numero de filas: "))
    nc = int(input("Numero de columnas: "))
    
    for i in range(len(m)):
        lc = []
        for j in range(len(m[i])):
            lc.append(int(input(f'Dato de la matriz {i}, {j}: ')))
        m.append(lc)
        
def llenarLista(l):
    
    cd = int(input('Cantidad de datos: '))
    for i in range(cd):
        l.append(int(input(f'Dato {i+1} de la lista: ')))
        
def mayMenMatriz(m):
    
    pos1 = [0, 0]
    pos2 = [0, 0]
    may = m[0][0]
    men = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] < men:
                men = m[i][j]
                pos1 = [i, j]
            if m[i][j] > may:
                may = m[i][j]
                pos2 = [i, j]
                
    return pos1, pos2

def primRnagos(m, pos1, pos2):
    
    b = 0
    cp = 0
    b1 = 0
    b2 = 0
    if pos1[0] < pos2[0]:
        i = pos1[0]
        j = pos1[1]+1
        while i < len(m) and b == 0:
            while j < len(m[i]) and b == 0:
                if i == pos2[0] and j == pos2[1]:
                    b = 1
                if detPrimo(m[i][j]):
                    cp += 1
                if cp == 1 and b1 == 0:
                    primR1 = m[i][j]
                    b1 = 1
                if cp == 2 and b2 == 0:
                    primR2 = m[i][j]
                    b2 = 1
                j+=1
            j = 0
            i += 1
    elif pos2[0] < pos1[0]:
        i = pos2[0]
        j = pos2[1] + 1
        while i < len(m) and b == 0:
            while j < len(m[i]) and b == 0:
                if i == pos1[0] and j == pos1[1]:
                    b = 1
                if detPrimo(m[i][j]):
                    cp += 1
                if cp == 1 and b1 == 0:
                    primR1 = m[i][j]
                    b1 = 1
                if cp == 2 and b2 == 0:
                    primR2 = m[i][j]
                    b2 = 1
                j+=1
            j = 0
            i += 1
    return primR1, primR2        
                
def buscarDatosLista(l, prim1, prim2):
    
    b1 = 0
    b2 = 0
    
    for i in range(len(l)):
        if l[i] == prim1 and b1 == 0:
            rang1 = i
            b1 = 1
        if l[i] == prim2 and b2 == 0:
            rang2 = i
            b2 = 1
    
    return rang1, rang2

def buscarFiboLista(l, rang1, rang2):
    
    cf = 0
    b = 0
    b1 = 0
    if rang1 < rang2:
        i  = rang1+1
        while i < len(l) and b == 0:
            if i == rang2:
                b = 1
            if detFibonacci(l[i]):
                cf += 1
            if cf == 2 and b1 == 0:
                segundoFib = l[i]
                posfi = i
                b1 = 1
            i+=1
    elif rang2 < rang1:
        i  = rang2+1
        while i < len(l) and b == 0:
            if i == rang1:
                b = 1
            if detFibonacci(l[i]):
                cf += 1
            if cf == 2 and b1 == 0:
                segundoFib = l[i]
                posfi = i
                b1 = 1
            i+=1
    return segundoFib, posfi
             
punto1()

    