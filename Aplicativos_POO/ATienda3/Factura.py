from Venta import *
class Factura:

    def __init__(self, numero):
        self.numFacturas = numero
        self.valorFactura = 0
        self.ventas = []
        
    def __str__(self):
        return (f'Numero Factura: {self.numFacturas}\nValor de la factura: {self.valorFactura}\nCantidad de Ventas: {len(self.ventas)}')
        
    def crearFactura(self):
        
        print('\n----------------------------------------')
        print(f'            * Factura {self.numFacturas} *         ')
        print('----------------------------------------')
        for prod in self.ventas:
            toVen = prod.realizarVenta()
            self.valorFactura += toVen[0]
            prod = toVen[1]
        print('-----------------------------------------')
        print(f'Total Factura: {self.valorFactura}')
        print('-----------------------------------------\n')
        return self.valorFactura
    
    def facturaIndividual(self):
        
        print('\n----------------------------------------')
        print(f'            * Factura {self.numFacturas} *         ')
        print('----------------------------------------')
        for prod in self.ventas:
            prod.venta()
        print('\n-----------------------------------------')
        print(f'Total Factura: {self.valorFactura}')
        print('-----------------------------------------\n')

        return self.valorFactura