class Venta:

    def __init__(self, producto, cantidad):

        self.producto = producto
        self.cantidad = cantidad
        
    def realizarVenta(self):
        
        vent = self.producto.valUni * self.cantidad
        print(f'Producto: {self.producto.nombre}\nValor Unitario: {self.producto.valUni}\nCantidad a comprar: {self.cantidad}')
        print('------------------------------------')
        print(f'Total a producto: {vent}')
        print('------------------------------------')

        return vent, self.producto
    
    def realizarVenta1(self):
        
        self.producto.canBod -= self.cantidad

        return self.producto
    
    def venta(self):
        vent = self.producto.valUni * self.cantidad
        print(f'Producto: {self.producto.nombre}\nValor Unitario: {self.producto.valUni}\nCantidad a comprar: {self.cantidad}')
        print('------------------------------------')
        print(f'Total a producto: {vent}')
        print('------------------------------------')
        
        
        

