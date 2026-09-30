#Fuciones puntos del examen

def punto1():
    
    punt1 = '''1.Se tiene un vector y una matriz con datos numéricos
Buscar un dato en una matriz.
El dato es el segundo primo de un rango de la matriz cuyos límites están determinados por el Fibonacci 1 y 2 del rango del vector determinado por el número mayor y menor de este.
Mostrar el dato y su posición
'''
    print(punt1)
    m = []
    llenarMAtriz(m)
    # m = [[4, 6, 5], [8, 4, 13], [3, 5, 7]]
    print(f'Matriz:\n{m}')
    # l = [3,15,4,5,3,2,10,7]
    l = []
    llenarLista(l)
    print(f'Lista:\n{l}')
    pos1, pos2 = mayorMenorLista(l)
    fib1, fib2 = fibonacciLista(l, pos1, pos2)
    segPrim, posPrim = buscarPrimoMatriz(m, fib1, fib2)
    print(f'El segundo primo de la matriz es {segPrim} y su poscicion en la matriz: {posPrim}')
    
def punto2():
    
    punt2 = '''2.Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Modificar las claves de la clave mayor y la clave menor con la siguiente información:
Clave mayor: conjunto1
Clave menor: conjunto2
Los  conjuntos están formados así:
Conjunto 1 con los número primos presentes en las diferentes listas sin repetidos 
Conjunto 2 con los número Fibonacci de las diferentes listas de valores sin repetidos
'''
    print(punt2)
    dic = {}
    llenarDiccionarioListas(dic)
    print(dic)
    men, lista1, may, lista2 = mayorMenorClaves(dic)
    conjunto1 = listaConjuntosPrimos(lista1)
    conjunto2 = listaConjuntosFibo(lista2)
    print(f'Llave menor: {men} | Conjunto: {conjunto1}\n Llave mayor: {may} | Conjunto: {conjunto2}')

def punto3():
    
    punt3 = '''3.Se tiene un diccionario con la siguiente información
Clave numero entero
Valor lista de números
Ordenar las listas de los valores asi:
En orden ascendente aquellas claves que sean primos
En orden descendente aquellas claves que sen Fibonacci
Primero se ordenan primos y luego Fibonacci con los que resten, es decir, no se vuelven a ordenar los Fibonacci que son primos
'''
    print(punt3)
    dic = {}
    llenarDiccionarioListas(dic)
    print(dic)
    ordenarClavesValores(dic)
    print(f'El diccionario resultante es: {dic}')
    
#Metodos utilizados en los 3 puntos
    
def llenarLista(l):
    
    cd = int(input('Cantidad de datos: '))
    for i in range(cd):
        l.append(int(input(f'Dato {i+1} de la lista: ')))

def mayorMenorLista(l):
    
    may = l[0]
    men = l[0]
    
    for i in range(len(l)):
        if l[i] > may:
            may = l[i]
            pos1 = i
        if l[i] < men:
            men = l[i]
            pos2 = i
    return pos1, pos2

def fibonacciLista(l, pos1, pos2):
    
    if pos1 < pos2:
        cp = 0
        i = pos1
        while i < pos2:
            if detFibonacci(l[i])== True:
                cp = cp +1
            if cp == 1:
                fib1 = l[i]
            if cp == 2:
                fib2 = l[i]
            i+=1
    elif pos2 < pos1:
        cp = 0
        
        i = pos2+1
        while i < pos1:
            if detFibonacci(l[i])== True:
                cp = cp + 1
            if cp == 1:
                fib1 = l[i]
            if cp == 2:
                fib2 = l[i]
            i+=1
    return fib1, fib2

def buscarPrimoMatriz(m, fib1, fib2):
    
    b = 0
    i = 0
    pos1 = []
    pos2 = []
    b1 = 0
    b2 = 0
    while i < len(m) and b == 0:
        j = 0
        while j < len(m[i]) and b == 0:
            if m[i][j] == fib1 and b1 == 0:
                pos1 = [i, j]
                b1 = 1
            if m[i][j] == fib2 and b2 == 0:
                pos2 = [i, j]
                b2 = 1
            j += 1
        i += 1
            
    cp = 0 
    i = pos1[0]
    j = pos1[1]
    b3 = 0
    while i < len(m) and b == 0:
        while j < len(m[i]) and b == 0:
            if i == pos2[0] and j == pos2[1]:
                b = 1
            if b == 0:
                if detPrimo(m[i][j])== True:
                    cp = cp + 1
                if cp == 2 and b3 == 0:
                    segPrimo = m[i][j]
                    posprim = [i, j]
                    b3 = 1
            j+=1
        j = 0
        i += 1
    return segPrimo, posprim
    
def llenarMAtriz(m):
    
    nf = int(input("Numero de filas: "))
    nc = int(input("Numero de columnas: "))
    
    for i in range(len(m)):
        lc = []
        for j in range(len(m[i])):
            lc.append(int(input(f'Dato de la matriz {i}, {j}: ')))
        m.append(lc)
    
def llenarDiccionarioListas(dic):
    cl = int(input('Cantidad de llaves: '))
    for i in range(cl):
        clave = int(input('Clave: '))
        lista = []
        cd = int(input('Cantidad de datos de la lista: '))
        for j in range(cd):
            lista.append(int(input(f'Datos {j+1} de la lista: ')))
        dic[clave] = lista

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
        
def mayorMenorClaves(dic):
    
    l = list(dic.keys())
    may = l[0]
    men = l[0]
        
    for llaves, valores in dic.items():
        if llaves < men:
            men  = llaves
            l1 = valores
            print(l1)
                
        if llaves > may:
            may = llaves
            l2 = valores
            print(l2)
    
    return men , l1 , may, l2

def listaConjuntosPrimos(l):
    s1 = set()
    for elem in l:
        if detPrimo(elem) == True:
            s1.add(elem)    
    return s1

def listaConjuntosFibo(l):
    s1 = set()
    for elem in l:
        if detFibonacci(elem) == True:
            s1.add(elem)    
    return s1    

def ordenarClavesValores(dic):
    
    for llaves, valores in dic.items():
        
        if detPrimo(llaves) == True: 
            listaAscendente(valores) 
            dic[llaves] = valores
        elif detFibonacci(llaves) == True:
            listaDescendente(valores)
            dic[llaves] = valores

def listaAscendente(lista):
    
    for i in range(len(lista)):
        j = i+1
        while j < len(lista):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j += 1

def listaDescendente(lista):
    
    for i in range(len(lista)):
        j = i+1
        while j < len(lista):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j +=1
              
        
#Ejecucion dle primer punto

punto1()