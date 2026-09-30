class Producto:
    
    def __init__(self, nombre, tipo, valorUni, canBod, cantMin, cantVend):
        
        self.nombre = nombre
        self.tipo = tipo
        self.valUni = valorUni
        self.canBod = canBod 
        self.canMin = cantMin
        self.canVen = cantVend
        
    def __str__(self): #Para usar con el print, asi ya no imprime la direccion del objeto, sino lo que se esta retornando dentro del metodo
        return (f'Nombre: {self.nombre}\nTipo: {self.tipo}\nValor unitario: {self.valUni}\nCantidad en bodega: {self.canBod}')
    
        

        