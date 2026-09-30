def punto17():
    print('''17.Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave''')
    
    print('----------------------------------------------------------------------------------------------------------------')
    cad1 = llenarCadena()
    print(f'Cadena: {cad1}')
    cad2 = llenarCadena()
    print(f'Cadena: {cad2}')
    cad3 = llenarCadena()
    print(f'Cadena: {cad3}')
    dicN, dicA = cadenaDiccionarios(cad1, cad2, cad3)
    print(f'Diccionario con clave caracter: \n{dicA}\nDiccionario con clave digito: \n{dicN}')
    dicValores = ordenarValor(dicN)
    print(f'Diccionario ordenado por valores: \n{dicValores}')
    dicLlaves = ordenarllaves(dicA)
    print(f'Diccionario ordenado por llaves: \n{dicLlaves}')
    
def llenarCadena():
    c = str(input('Digite una cadena con letras y números: '))
    return c

def cadenaDiccionarios(cad1, cad2, cad3):
    
    cdt = cad1 + cad2 + cad3
    dic = {}
    '''__'''
    for elem in cdt:
        if elem.isnumeric() == True:
            dic[elem] = cdt.count(elem)
    dic1 = {}
    
    for letter in cdt:
        if letter.isalpha() == True:
            dic1[letter] = cdt.count(letter)
    return dic, dic1

def ordenarValor(dic):
    dic1 = sorted(dic.items(), key= lambda x: x[1])
    return dict(dic1)
def ordenarllaves(dic):
    dic1 = sorted(dic.items(), key= lambda x: x[0])
    return dict(dic1)
    
punto17()