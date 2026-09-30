class Tienda:
    
    dineroEnCaja = 0
    
    def __init__(self, product1 , product2, product3, product4):
        self.prod1 = product1
        self.prod2 = product2
        self.prod3 = product3
        self.prod4 = product4
        self.listaProd = [self.prod1, self.prod2, self.prod3, self.prod4] 
    
    def mostarProductos(self):
        print('\n----------------------------------------')
        print('       *Productos de la tienda*         ')
        print('----------------------------------------')
        print('                 - 1 -                  ')
        print(f'{self.prod1}')
        print('----------------------------------------')
        print('                 - 2 -                  ')
        print(f'{self.prod2}')
        print('----------------------------------------')
        print('                 - 3 -                  ')
        print(f'{self.prod3}')
        print('----------------------------------------')
        print('                 - 4 -                  ')
        print(f'{self.prod4}')
        print('----------------------------------------\n')
        
    def mostarProductos1(self):
        print('\n----------------------------------------')
        print('       *Productos de la tienda*         ')
        print('----------------------------------------')
        print(f'1. {self.prod1.nombre}')
        print(f'2. {self.prod2.nombre}')
        print(f'3. {self.prod3.nombre}')
        print(f'4. {self.prod4.nombre}')
        print('----------------------------------------\n')
        
    # def mostrarProducto(self, nombre):
    
    def buscarProducto(self, nombre):
        
        listaP = [self.prod1, self.prod2, self.prod3, self.prod4]
        b = 0
        for i in range(len(listaP)):
            if listaP[i].nombre == nombre:
                print(listaP[i])
                b = 1
        if b == 0:
            print('No se encontro el producto buscado')
            
    def buscarProducto1(self, name):
        
        for product in self.listaProd:
            if product.nombre == name:
                return True
        return False
            
    def realizarVenta(self):
        
        valT = 0 
        self.mostarProductos()
        listaP = [self.prod1, self.prod2, self.prod3, self.prod4]
        opc = int(input(f'Qué producto desea comprar?  -> '))
        match opc:
            case 1 | 2 | 3 | 4:
                cant = int(input('\nCantidad de elementos: '))
                for i in range(len(listaP)):
                    if opc-1 == i:
                        if listaP[i].canBod != 0:
                            if listaP[i].canBod > cant:
                                listaP[i].canBod = listaP[i].canBod - cant
                                listaP[i].canVen = listaP[i].canVen + cant
                                valT = listaP[i].valUni * cant 
                                prod = listaP[i]
                                Tienda.dineroEnCaja += valT
                                self.ventaRealizada(valT, prod, cant) 
                            else:
                                cant = listaP[i].canBod
                                listaP[i].canBod -= cant
                                listaP[i].canVen += cant
                                valT = listaP[i].valUni * cant 
                                prod = listaP[i]
                                Tienda.dineroEnCaja += valT
                                self.ventaRealizada(valT, prod, cant) 
                        else:
                            print('\nNo hay elementos disponibles...')
            case other:
                print('\nOpcion invalida...\n')
           
    def ventaRealizada(self, val, prod, cant):
        
        print('------------------------------------------')
        print('             Factura de venta             ')
        print('------------------------------------------')
        print(f'Prodcuto:\nNombre: {prod.nombre}\nCantidad Disponibe: {prod.canBod}\nPrecio por unidad: {prod.valUni}')
        print('------------------------------------------')
        print(f'Cantidad del producto: {cant}\nTotal a pagar: {val}')
        print('------------------------------------------')
        
    def ventasTotales(self):
        
        print('------------------------------------------')
        print('             Ventas Totales               ')
        print('------------------------------------------')
        for i in range(len(self.listaProd)):
            print(f'----- Producto {i+1} -----')
            print(f'Producto: \nNombre: {self.listaProd[i].nombre}\nValor unitario: {self.listaProd[i].valUni}\nUnidades Vendidas: {self.listaProd[i].canVen}')
        print('------------------------------------------')
        print(f'Dinero Total de Ventas: {Tienda.dineroEnCaja}')
        print('------------------------------------------\n')
        
    def ventasProducto(self):
        self.mostarProductos1()
        opc = int(input(f'Qué producto desea ver?  -> '))
        match opc:
            case 1 | 2 | 3 | 4 :
                print('\n------------------------------------------')
                print('          Ventas por producto             ')
                for i in range(len(self.listaProd)):
                    if opc-1 == i:
                        print(f'------------------------------------------')
                        print(f'         ----- Producto {i+1} -----       ')
                        print(f'Producto: \nNombre: {self.listaProd[i].nombre}\nValor unitario: {self.listaProd[i].valUni}\nUnidades Vendidas: {self.listaProd[i].canVen}')
                        print(f'------------------------------------------')
                        print(f'Ventas total del producto: {self.listaProd[i].canVen * self.listaProd[i].valUni}')
                        print('------------------------------------------\n')
            case other:
                print('\nOpcion no valida...\n')
        
    def realizarPedido(self):
        
        self.mostarProductos1()
        opc = int(input(f'\nQué producto desea pedir?  -> '))
        
        for i in range(len(self.listaProd)):
            if opc-1 == i:
                if self.listaProd[i].canBod <= self.listaProd[i].canMin:
                    cant = int(input('\nCantidad de unidades que desea pedir? -> '))
                    self.listaProd[i].canBod += cant
                    print('\nPedido realizado con exito...\n')
                else:
                    print('\nNo se puede realizar el pedido... \n')
    
    def determinarProducto(self):
        
        self.mostarProductos1()
        opc = int(input(f'\nQué producto desea pedir?  -> '))
        match opc:
            case 1 | 2 | 3 | 4:
                for i in range(len(self.listaProd)):
                    if opc-1 == i:
                        if self.listaProd[i].canBod <= self.listaProd[i].canMin:
                            print(f'\n------------------------------------------')
                            print(f'         ----- Producto {i+1} -----       ')
                            print(f'Producto: \nNombre: {self.listaProd[i].nombre}\nUnidades en bodega: {self.listaProd[i].canBod}\nCantidad minima: {self.listaProd[i].canMin}')
                            print(f'------------------------------------------')
                            print(f'Es necesario realizar un pedido para abastecer la tienda...')
                            print(f'------------------------------------------\n')        
                        else:
                            print(f'\n------------------------------------------')
                            print(f'No es necesario realizar un pedido, quedan unidades disponibles para vender...')
                            print(f'------------------------------------------\n')
            case other:
                print('\nOpcion invalida...\n')
        
    def promedioVentas(self):
        
        sumVen = 0
        venT = 0
        print('------------------------------------------')
        print('          * Promedio Ventas *             ')
        print('------------------------------------------')
        if Tienda.dineroEnCaja > 0: 
            for i in range(len(self.listaProd)):
                sumVen += self.listaProd[i].canVen*self.listaProd[i].valUni
                venT += self.listaProd[i].canVen
            print(f'Dinero total: {sumVen}\nProductos vendidos: {venT}')
            print(f'Promedio: {sumVen/venT}')    
        else:
            print('No se han realizado ventas...')
        print('------------------------------------------')
    
    def productoMasVendido(self):
        
        print('------------------------------------------')
        print('        * Producto más vendido *          ')
        print('------------------------------------------')
        if Tienda.dineroEnCaja > 0:
            prodMasVend = self.listaProd[0].canVen
            prod =self.listaProd[0]
            for i in range(len(self.listaProd)):
                if self.listaProd[i].canVen > prodMasVend:
                    prodMasVend = self.listaProd[i].canVen
                    prod = self.listaProd[i]
            print(f'Producto:\nNombre: {prod.nombre}\nCantidad vendida: {prod.canVen}')
        else:
            print('No se han realizado ventas...')
        print('------------------------------------------')
                    
        