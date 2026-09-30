from Leer  import *
from Facturas import *
class Socio:
    
    def __init__(self, cedula, nombre, descuento):
        
        self.cedula = cedula
        self.nombre = nombre
        self.descuento = descuento
        self.afiliados = []
        self.facturas = []
    
    def socio(self):
        print(f'Socio: {self.nombre}\nCedula: {self.cedula}')
        
    def pagarConsumo(self, socio):
        if socio.facturas != []:
            valorTotalNeto = 0
            valorTotalDescuento = 0
            i = 0
            print('------------- * Facturas * -------------\n')
            for facturas in socio.facturas:
                print(f'------------ * Factura {i+1} * -------------')
                facturas.factura()
                print('----------------------------------------')
                valorTotalNeto += facturas.valor
                valorTotalDescuento += facturas.valorDescuento
                i += 1
            print('----------------------------------------')
            print(f'Valor Total Neto: {valorTotalNeto}\nValor Total con Descuento: {valorTotalDescuento}') 
            print('----------------------------------------')
            opc = Leer('Digite el numero de la factura que desea pagar: ').leerInt()
            while True:
                if opc <= len(socio.facturas):
                    for i in range(len(socio.facturas)):
                        if i == opc -1:
                            socio.facturas.remove(socio.facturas[i-1])
                            print('----------------------------------------')
                            print('           * Consumo Pagado *         ')
                            print('----------------------------------------')
                            return
                else:
                    print('----------------------------------------')
                    print('\nError: Digite una opcion valida...\n')
                    print('----------------------------------------')
                    opc = Leer('Digite el numero de la factura que desea pagar: ').leerInt()
        else:
            print('----------------------------------------')
            print('\nEl socio no tiene facturas por pagar...\n')
            print('----------------------------------------')
    
    def facturasSocio(self):
        valNeto = 0
        valDesc = 0
        for factura in self.facturas:
            print(f'------------ * Factura * ---------------')
            factura.factura()
            valNeto += factura.valor
            valDesc += factura.valorDescuento
        return valNeto, valDesc  
    
    def consumosSocio(self, socio):
        if socio.facturas != []:
            i = 0
            print('\n-------------- * Socio * ---------------')
            socio.socio()
            print('------------- * Facturas * -------------')
            valorTotalNeto = 0
            valorTotalDescuento = 0
            for facturas in socio.facturas:
                print(f'------------ * Factura {i+1} * -------------')
                facturas.factura()
                valorTotalNeto += facturas.valor
                valorTotalDescuento += facturas.valorDescuento
                i += 1
            print('----------------------------------------')
            print(f'Valor Total Neto Facturas: {valorTotalNeto}\nValor Total con Descuento Facturas: {valorTotalDescuento}') 
            print('----------------------------------------')    
        else:
            print('----------------------------------------')
            print('\nEl socio no ha realizado consumos...\n')
            print('----------------------------------------')   
            
class Platinum(Socio):
    
    def __init__(self, cedula, nombre, descuento):
        super().__init__(cedula, nombre, descuento)
        
    def consumo(self, cedula):
        consumo = Leer('\nDigite el consumo: ').leerCadena()
        valor = Leer('Digite el valor del consumo: ').leerFloat()
        valorFinal = valor - valor * self.descuento
        fac = Factura(consumo, valor, cedula, valorFinal)
        return fac    
        
class Gold(Socio):
    
    def __init__(self, cedula, nombre, descuento):
        super().__init__(cedula, nombre, descuento)
        
    def consumo(self, cedula):
        consumo = Leer('\nDigite el consumo: ').leerCadena()
        valor = Leer('Digite el valor del consumo: ').leerFloat()
        valorFinal = valor - valor * self.descuento
        fac = Factura(consumo, valor, cedula, valorFinal)
        return fac
        
class Silver(Socio):
    
    def __init__(self, cedula, nombre, descuento):
        super().__init__(cedula, nombre, descuento)
    
    def consumo(self, cedula):
        consumo = Leer('\nDigite el consumo: ').leerCadena()
        valor = Leer('Digite el valor del consumo: ').leerFloat()
        valorFinal = valor - valor * self.descuento
        fac = Factura(consumo, valor, cedula, valorFinal)
        return fac
        