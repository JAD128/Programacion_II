from Leer import *
from Producto import *
from Venta import *
from Factura import *
import os

class Tienda:
    
    dineroEnCaja = 0
    numFacturas = 0
    
    def __init__(self, producto , facturas):
        self.productos = producto
        self.Facturas = facturas

    def adicionarProductosTienda(self):
        self.productos.append(Producto('no products', 1, 2000, 50, 10))
        self.productos.append(Producto('Cuaderno', 1, 3000, 50, 10))
        self.productos.append(Producto('Aspirina', 2, 1000, 50, 5))
        self.productos.append(Producto('Arroz', 3, 3000, 50, 5))
        self.productos.append(Producto('Papa', 3, 3000, 50, 5))

    def mostrarProdcutos(self):
        
        os.system('cls')

        if len(self.productos)>0:
            print('\n----------------------------------------')
            print('       *Productos de la tienda*         ')
            print('----------------------------------------')
            for prod in self.productos:
                print(prod)
                print('----------------------------------------')
        else:
            print('No hay productos en la tienda')
    
    def facturasDetalles(self):
        if Tienda.numFacturas > 0:
            for fac in self.Facturas:
                os.system('cls')
                fac.facturaIndividual()
                os.system('pause')
                os.system('cls')
        else:
            print('\nNo hay facturas disponibles...\n')

    def facturasDetalles1(self):
        if Tienda.numFacturas > 0:
            for fac in self.Facturas:
                fac.facturaIndividual()
        else:
            print('\nNo hay facturas disponibles...\n')
                
            
    def consultarFactura(self):
        
        if Tienda.numFacturas > 0:
            print('---------------------------------------')
            print('          Consultar Factura            ')
            print('---------------------------------------') 
            print('Facturas disponibles: ')
            for i in range(Tienda.numFacturas):
                print(f'Factura {i+1}')
            
            opc = 's'
            while True:
                match opc:
                    case 's' | 'S':
                        resp = Leer('Qué factura desea? -> ').leerInt()
                        for i in range(len(self.Facturas)):
                            if resp-1 == i:
                                self.Facturas[i].facturaIndividual()
                        opc = Leer('\nDesea ver los detalles de alguna factura? s/n -> ').leerCadena()
                    case 'n' | 'N':
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...\n')
                        resp = Leer('\nDesea compar otro producto? -> ').leerCadena()
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay facturas disponibles...\n')
                   
    def crearFacturaPrincipal(self):

        fac = Factura(len(self.Facturas)+1)
        resp = Leer('\nDesea compar otro producto? s/n -> ').leerCadena()
        pos  = 0
        while True:
            match resp:
                case 's' | 'S':
                    os.system('cls')
                    self.mostrarProdcutos()
                    opc = Leer('Qué producto desea comprar?  -> ').leerInt()
                    match opc:
                        case 1 | 2 | 3 | 4 | 5: 
                            cant = Leer('\nCantidad de elementos: ').leerInt()
                            for i in range(len(self.productos)):
                                if opc-1 == i:
                                    if self.productos[i].canBod != 0:
                                        if self.productos[i].canBod > cant:
                                            if self.buscarProd(self.productos[i].nombre, fac) == False:
                                                venta = Venta(self.productos[i], cant)
                                                venta.realizarVenta1()
                                                fac.ventas.append(venta)
                                            else:
                                                venta.realizarVenta1()
                                                pos = self.buscarProd1(self.productos[i].nombre, fac)
                                                cant += fac.ventas[pos].cantidad
                                                venta = Venta(self.productos[i], cant)
                                                fac.ventas[pos] = venta
                                        else:
                                            if self.buscarProd(self.productos[i].nombre, fac) == False:
                                                venta = Venta(self.productos[i], cant)
                                                fac.ventas.append(venta)
                                            else:
                                                pos = self.buscarProd1(self.productos[i].nombre, fac)
                                                cant += fac.ventas[pos].cantidad
                                                venta = Venta(self.productos[i], cant)
                                                fac.ventas[pos] = venta
                                    else: 
                                        print('\nNo hay elementos disponibles...')
                            resp = Leer('\nDesea compar otro producto? -> ').leerCadena() 
                        case other:
                            os.system('cls')
                            print('\nERROR: Digite un valor valido...\n')
                            os.system('pause')
                            os.system('cls')
                case 'n' | 'N':
                    if fac.ventas == []:
                        os.system('cls')
                        print('\nNo se ha realizado ninguna venta...\n')
                        os.system('pause')
                        os.system('cls')
                    else:
                        os.system('cls')
                        valFacTotal = fac.crearFactura()
                        Tienda.dineroEnCaja += valFacTotal
                        Tienda.numFacturas += 1
                        self.Facturas.append(fac)
                        os.system('pause')
                        os.system('cls')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...\n')
                    resp = Leer('\nDesea compar otro producto? -> ').leerCadena()
                    os.system('pause')
                    os.system('cls')
                    
    def buscarProd(self, nombreProd, fac):
        
        for vent in fac.ventas:
            if vent.producto.nombre == nombreProd:
                return True
            else:
                print('')
        return False
    
    def buscarProd1(self, nombre, fac):
        
        for vent in fac.ventas:
            if vent.producto.nombre == nombre:
                pos = fac.ventas.index(vent)
                return pos
                
                                  
    def mostrarFacturas(self):
        
        if Tienda.numFacturas > 0:
            print('\n----------------------------------------')
            print('              * Facturas *         ')
            print('----------------------------------------')
            for fac in self.Facturas:
                print(fac)
                print('----------------------------------------\n')
        else:
            print('\nNo hay facturas disponibles...\n')
            
    def eliminarItemFactura(self, numFac):
        
        self.facturasDetalles1()
        nombreProducto = Leer('Cuál es el nombre del producto que desea eliminar? -> ').leerCadena()
        for i in range(len(self.Facturas)):
            if numFac-1 == i:
                for vent in self.Facturas[i].ventas:
                    if vent.producto.nombre == nombreProducto:
                        self.Facturas[i].ventas.remove(vent)
                        totVen = vent.producto.valUni * vent.cantidad
                        self.Facturas[i].valorFactura -= totVen
        print('\nModificacion Exitosa...\n')
    
    def eliminarIFactura(self):
        
        print('---------------------------------------')
        print('       Eliminar Item Factura           ')
        print('---------------------------------------') 
        print('Facturas disponibles: ')
        for i in range(Tienda.numFacturas):
            print(f'Factura {i+1}')
        print('---------------------------------------')
        numFactura = Leer('Cuál es la factura que desea modificar? -> ').leerInt()
        self.eliminarItemFactura(numFactura)
        
    def ventasTotales(self):
        
        print('------------------------------------------')
        print('             Ventas Totales               ')
        print('------------------------------------------')
        for i in range(len(self.productos)):
            print(f'----- Producto {i+1} -----')
            print(f'Producto: \nNombre: {self.productos[i].nombre}\nValor unitario: {self.productos[i].valUni}\nUnidades Vendidas: {self.productos[i].canVen}')
        print('------------------------------------------')
        print(f'Dinero Total de Ventas: {Tienda.dineroEnCaja}')
        print('------------------------------------------\n')
        
    def realizarPedido(self):
        
        self.mostrarProdcutos()
        opc = int(input(f'\nQué producto desea pedir?  -> '))
        
        for i in range(len(self.productos)):
            if opc-1 == i:
                if self.productos[i].canBod <= self.productos[i].canMin:
                    cant = int(input('\nCantidad de unidades que desea pedir? -> '))
                    self.productos[i].canBod += cant
                    print('\nPedido realizado con exito...\n')
                else:
                    print('\nNo se puede realizar el pedido... \n')
    
    def determinarProducto(self):
        
        self.mostrarProdcutos()
        opc = int(input(f'\nQué producto desea pedir?  -> '))
        match opc:
            case 1 | 2 | 3 | 4 | 5:
                for i in range(len(self.productos)):
                    if opc-1 == i:
                        if self.productos[i].canBod <= self.productos[i].canMin:
                            print(f'\n------------------------------------------')
                            print(f'         ----- Producto {i+1} -----       ')
                            print(f'Producto: \nNombre: {self.productos[i].nombre}\nUnidades en bodega: {self.productos[i].canBod}\nCantidad minima: {self.listaProd[i].canMin}')
                            print(f'------------------------------------------')
                            print(f'Es necesario realizar un pedido para abastecer la tienda...')
                            print(f'------------------------------------------\n')        
                        else:
                            print(f'\n------------------------------------------')
                            print(f'No es necesario realizar un pedido, quedan unidades disponibles para vender...')
                            print(f'------------------------------------------\n')
            case other:
                print('\nOpcion invalida...\n')
        
    
    def ventasPorProducto(self):
        
        sumVen = 0
        venT = 0
        print('------------------------------------------')
        print('        * Ventas por productos *          ')
        print('------------------------------------------')
        self.mostrarProdcutos()
        nombreProducto = Leer('\nQué producto desea ver? -> ').leerCadena()
        if Tienda.dineroEnCaja > 0:
            for prod in self.productos:
                if prod.nombre == nombreProducto:
                    sumVen += prod.canVen * prod.valUni
                    venT += prod.canVen
            print('------------------------------------------\n')
            print(f'Producto: {nombreProducto}\nDinero total: {sumVen}\nCantidad: {venT}')
            print('------------------------------------------')
        else:
            print('No se han realizados ventas...')
            print('------------------------------------------\n')
    
    def promedioVentas(self):
        
        sumVen = 0
        venT = 0
        print('------------------------------------------')
        print('          * Promedio ventas *          ')
        print('------------------------------------------')
        self.mostrarProdcutos()
        if Tienda.dineroEnCaja > 0:
            for prod in self.productos:
                sumVen += prod.canVen * prod.valUni
                venT += prod.canVen
            print('------------------------------------------\n')
            print(f'Dinero total: {sumVen}\nCantidad: {venT}')
            print('------------------------------------------')
            print(f'Promedio ventas: {sumVen/venT}')
            print('------------------------------------------')
        else:
            print('No se han realizados ventas...')
            print('------------------------------------------\n')
            
    def productoMasVendido(self):
        
        print('------------------------------------------')
        print('        * Producto más vendido *          ')
        print('------------------------------------------')
        if Tienda.dineroEnCaja > 0:
            prodMasVend = self.Facturas[0].ventas[0].canVen
            prod =self.Facturas[0].ventas[0]
            for i in range(len(self.productos)):
                if self.productos[i].canVen > prodMasVend:
                    prodMasVend = self.productos[i].canVen
                    prod = self.productos[i]
            print(f'Producto:\nNombre: {prod.nombre}\nCantidad vendida: {prod.canVen}')
        else:
            print('No se han realizado ventas...')
        print('------------------------------------------') 

    def eliminarFactura(self):

        print('---------------------------------------')
        print('          Consultar Factura            ')
        print('---------------------------------------') 
        print('Facturas disponibles: ')
        for i in range(Tienda.numFacturas):
            print(f'Factura {i+1}')
        opc = Leer('Qué factura desea eliminar? -> ').leerInt()
        for i in range(len(self.Facturas)):
            if opc-1 == i:
                self.Facturas.remove(self.Facturas[i])   
                Tienda.numFacturas -= 1  
                
    def guardarProductos(self):
        try:
            while True:
                archivo = Leer('Nombre del archivo: ').leerCadena()
                if os.path.exists(archivo):
                    print('\nEl archivo existe, desea sobreescribirlo? ')
                    resp = Leer('Si/No').leerCadena()
                    match resp:
                        case 's' | 'Si' | 'SI' | 'si':
                            fArc = open(archivo, 'w')
                        case 'n' | 'No' | 'NO' | 'no':
                            fArc = open(archivo, 'a')
                else:
                    print('\nEl archivo no existe...\n')
                    resp = Leer('Desea guardar la informacion? Si/NO -> ').leerCadena()
                    if resp == 'no' or resp == 'No':
                        return
                    fArc = open(archivo, 'w')
                
                for prod in self.productos:
                    registro = (f'{prod.nombre} {prod.tipo} {prod.valUni} {prod.canBod} {prod.canMin}\n')
                    fArc.write(registro)
                print('\nInformacion guardada...\n')
                os.system('pause')
                break
        except FileNotFoundError:
            print('\nERROR: Problemas para abrir el archivo...\n')
        finally:
            fArc.close()
    
    def leerProductos(self):
        try:
            while True:
                archivo = Leer('Nombre del archivo: ').leerCadena()
                if os.path.exists(archivo):
                    fArc = open(archivo, 'r')
                    registro = fArc.readlines()
                    for elem in registro:
                        linea = elem.strip().split()
                        produc = Producto(linea[0], int(linea[1]), float(linea[2]), int(linea[3]), int(linea[4]))
                        self.productos.append(produc) 
                    break      
                else:
                    print('\nEl archivo no existe...\n')
                    resp = Leer('\nhhDesea continuar? Si/No ->').leerCadena()
                    match resp:
                        case 'no' | 'No' | 'n' | 'No':
                            print('\nNo se abre el archivo...\n')
                            os.system('pause')
                            break
        except FileNotFoundError:
            print('\nERROR: Problemas para abrir el archivo...\n')