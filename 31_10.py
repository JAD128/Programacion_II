class Entero:

    def __init__(self, numero):

        self.nro = numero

    

    @property
    def numero(self):
        return self.nro
    
    # @setNumber.setter
    # def setNumber(self, numero):
    #     self.nro = numero


    def detPrimo(self):

        c = 2
        b = False
        while c <= self.nro and b == False:
            if self.nro % c == 0:
                b = True
            c += 1
        if b == False and self.nro > 1:
            return True
        
    def detPrimo1(self):

        b = 0
        c = 2
        while c < self.nro-1:
            if self.nro % c == 0:
                b = 1
            c +=1
        if b == 0:
            return True
        else:
            return False

        
    def detFibonacci(self):

        r = 0
        s = 1
        t = 0

        while t < self.nro:
            t = r + s
            r = s
            s = t
        
        if self.nro == t:
            return True
        else:
            return False
    
    def detPar(self):
        if self.nro % 2 == 0:
            return True
        else:
            return False

class Lista:
    def __init__(self, lista):
        self.lista = lista
        
    def __str__(self):
        return (f'{self.lista}')

    def listaPrimos(self):

        lp = []
        c = Entero(self.lista[0])
        print(c.numero)
        for elem in self.lista:
            c.nro = elem
            if c.detPrimo1():
                lp.append(elem)
        return lp
    
    def sinRepetidos(self):
        s1 = set(self.lista)
        return list(s1)
    
    def mayorLista(self):
        may = self.lista[0]
        for ele in self.lista:
            if ele > may:
                may = ele
        return may
    
    def menorLista(self):
        men = self.lista[0]
        for ele in self.lista:
            if ele < men:
                men = ele
        return men

    def paresLista(self):

        lp = []
        c = Entero(self.lista[0])
        for elem in self.lista:
            c.nro = elem
            if c.detPar:
                lp.append(elem)
        return lp
    
    def fibonacciLista(self):

        lf = []
        c = Entero(self.lista[0])
        for elem in self.lista:
            c.nro = elem
            if c.detFibonacci():
                lf.append(elem)
        return lf
    
    def promedioLista(self):
        
        c = 0
        sum = 0
        for ele in self.lista:
            sum = sum + ele
            c += 1
        prom = sum / c
        return prom
    
    @staticmethod
    def unionListas(lista1, lista2):
        lUnion = lista1.union(lista2)
        return lUnion
    
    @staticmethod
    def interseccionListas(lista1, lista2):
        lInter = lista1.intersection(lista2)
        return lInter


    
class Matriz:
    def __init__(self, matriz):
        self.m = matriz

    def matrizLista(self):
        lm = []
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                lm.append(self.m[i][j])
        return lm
    


# l1 = Lista([3,5,10,20,30,5,60])
# print(l1.listaPrimos())

#Crear objeto matriz
m1 = Matriz([[5, 5, 7], [4 , 13 , 15], [9, 3, 2]])
# #Crea lista Matriz 
# lm = m1.matrizLista()
# #Crear objeto lista con lm
# llm =  Lista(lm)
# #Sacar primos de llm
# lp = llm.listaPrimos()
# #Crear objeto clase lista lp
# llp = Lista(lp)
# lpsr = llp.sinRepetidos()
# print(lpsr)


#Optimizado
lmatriz = Lista(m1.matrizLista())
lp = lmatriz.listaPrimos()
lsp = Lista(lp)
print(lsp.sinRepetidos())

print(Lista(Lista(m1.matrizLista()).listaPrimos()).sinRepetidos())




