from Leer import *
from Facturas import *
class Afiliado:
    
    def __init__(self, cedula, nombre):
        
        self.cedula = cedula
        self.nombre = nombre
        
    def __str__(self) -> str:
        return(f'Autorizado: {self.nombre}\nCedula: {self.cedula}')
    
    def consumo(self, cedula, descuetno):
        consumo = Leer('\nDigite el consumo: ').leerInt()
        valor = Leer('\nDigite el valor del consumo: ').leerFloat()
        valorFinal = valor * descuetno
        fac = Factura(consumo, valorFinal, cedula)
        return fac