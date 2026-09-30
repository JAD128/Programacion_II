def punto19():
    print('''19.Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
el par mayor y las veces que se repite
el primo menor y las veces que se repite
el Fibonacci menor y las veces que se repite
Con estos datos hallar:
El factorial de la suma del par y del primo
La multiplicación con sumas de los contadores del primo y del Fibonacci.''')
    
    print('-------------------------------------------------------------------------------------')
    # l = []
    # llenarLista(l)
    l= [3, 11, 5, 2, 17, 11, 14, 25]
    m = [[9 , 15, 7], [3, 10, 11], [14, 2, 9]]
    # m = []
    # llenarMAtriz(m)
    listaUnion = unionMatrizLista(m, l)
    parMay, cVeces = parMayor(listaUnion)
    print(f'Par mayor: {parMay} | Veces que se repite: {cVeces}')
    primMen, cVecesP = primoMenor(listaUnion) 
    print(f'Primo menor: {primMen} | Veces que se repite: {cVecesP}')
    fibMen, cVecesF = fibMenor(listaUnion)
    print(f'Fibonacci menor: {fibMen} | Veces que se repite: {cVecesF}')    
    fac = factorialSumaParPrimo(parMay, primMen)
    print(f'Factorial de la suma del par {parMay} y del primo {primMen}: {fac}')
    mult = multiplicacionSumas(cVecesP, cVecesF)
    print(f'Multiplicacion contadores primo y fibonacci: {mult}')
    print('-------------------------------------------------------------------------------------')
    
def unionMatrizLista(m, l):
    
    lu = []
    for elem in m:
        for ele in elem:
            lu.append(ele)
    for nr in l:
        lu.append(nr)
    return lu

def parMayor(lu):
    
    parMay = lu[0]
    for elem in lu:
        if elem % 2 == 0:
            if elem > parMay:
                parMay = elem
    cv = vecesRepiteNumero(lu, parMay)
    
    return parMay, cv

def primoMenor(lu):
    
    primMenor = lu[0]
    for elem in lu:
        if detPrimo(elem):
            if elem < primMenor:
                primMenor = elem
    cvp = vecesRepiteNumero(lu, primMenor)
    return primMenor, cvp

def fibMenor(lu):
    
    fibMen = lu[0]
    for elem in lu:
        if detFibonacci(elem):
            if elem <fibMen:
                fibMen = elem
    cvf = vecesRepiteNumero(lu, fibMen)
    return fibMen, cvf
    
def factorialSumaParPrimo(par, primo):
    sum = par + primo
    fac = 1
    while sum > 0:
        fac = fac * sum
        sum = sum - 1
    return fac

def multiplicacionSumas(n1, n2):
    
    mult = 0
    for i in range(n1):
        mult = mult + n2
    return mult
        

def vecesRepiteNumero(l, nro):
    cv = 0
    for elem in l:
        if elem == nro:
            cv+=1
    return cv

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
        print(t)
    if t == nro:
        return True
    else:
        return False    

detFibonacci(5)


            
    
    