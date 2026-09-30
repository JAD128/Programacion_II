class Factura:
    
    def __init__(self, consumo, valor, cedula, valorDescuento):
        
        self.consumo = consumo
        self.valor = valor
        self.cedula = cedula
        self.valorDescuento = valorDescuento
    
    def factura(self):
        print(f'Cedula: {self.cedula}\nConsumo: {self.consumo}\nValor: {self.valor}\nValor Con Descuento: {self.valorDescuento}')
    