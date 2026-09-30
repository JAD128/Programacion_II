class Nodo:
    def __init__(self, info): 
        self.info = info
        self.sig = None


class Cola:
    def __init__(self):
        self.pri = None
        self.ult = None

    def ingresar(self, info):
        print(f"Agregado {info} en la Cola")
        # Si no hay info, agregamos el valor en el elemento pri y regresamos
        if self.pri == None:
            self.pri = Nodo(info)
            self.ult = self.pri
            return
        
        nuevo_nodo = Nodo(info)
        self.ult.sig = nuevo_nodo
        self.ult = nuevo_nodo
      

    def sacar(self):
        # Si no hay info en el nodo pri, regresamos
        if self.pri == None:
            print("No se puede sacar")
            return

        print(f"Sale {self.pri.info}")
        self.pri = self.pri.sig

    def imprimir(self):
        if self.pri == None:
            print("No hay ningún elemento en la Cola...")
            return
        print("Datos de la Cola:")
        # Recorrer la Cola e imprimir valores
        aux = self.pri
        while aux != None:
            print(f"{aux.info}", end=",")
            aux = aux.sig
        print(" None")

op = 1
while(op != 5):
    print("MENU Cola")
    print ("1. Inicializar Cola")
    print ("2. ingresar")
    print ("3. Sacar")
    print ("4. Imprimir")
    print ("5. Salir")
    op = int(input("Digite su opción: "))
    if op == 1:
      print('Inicializar')
      cola = Cola()
      
    if op == 2:
      print('Ingresar')
      dato = input("Dato: ")
      cola.ingresar(dato)  

    if op == 3:
      cola.imprimir()        
      cola.sacar()

    if op == 4:
      print('Imprimir')
      cola.imprimir()

    if op == 5:
      print('Salir')
