from Tienda import *
from Producto import *
import os

#Mostar producto / Consultar Producto

def main():
    
    os.system('cls')
    if os.path.exists('productos.dat'):
        crearTienda()
        ct = True
    else:
        ct = False
    while True:    
        
        print('---------------------------------------')
        print('            Menu Principal             ')
        print('---------------------------------------')    
        print(' 1. Crear Tienda')
        print(' 2. Mostar Productos')
        print(' 3. Manejo ventas')
        print(' 4. Manejo pedidos')
        print(' 5. Manejo estadisticas')
        print(' 6. Salir')
        print('---------------------------------------')    
        try:        
            opc = int(input('Digite una opcion: '))
                        
            match opc:
                case 1: 
                    if not ct:
                        os.system('cls')
                        tienda = crearTienda()
                        if tienda != None:
                            ct = True
                            print('\n---------------------------------------') 
                            print('     ¡Se ha cargado la tienda!   ')
                            print('---------------------------------------\n')
                        os.system('pause')
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('* Ya existen productos en la tienda *\n')
                        os.system('pause')
                        os.system('cls')
                case 2:
                    if ct:
                        os.system('cls')
                        tienda.mostrarProdcutos()
                        os.system('pause')
                        os.system('cls')
                    else:
                        os.system('cls')
                        print('* No hay productos en la tienda *\n')
                        os.system('pause')
                        os.system('cls')
                case 3:
                    if ct:
                        os.system('cls')
                        menuVentas(tienda)
                    else:
                        os.system('cls')
                        print('* No hay productos en la tienda *\n')
                        os.system('pause')
                        os.system('cls')  
                case 4:
                    if ct:
                        os.system('cls')
                        menuPedidos(tienda)
                    else:
                        os.system('cls')
                        print('* No hay productos en la tienda *\n')
                        os.system('pause')
                        os.system('cls')                    
                case 5:
                    if ct:
                        os.system('cls')
                        menuEstadisticas(tienda)
                    else:
                        os.system('cls')
                        print('* No hay productos en la tienda *\n')
                        os.system('pause')
                        os.system('cls')                                        
                case 6:
                    tienda.guardarProductos()
                    print('---------------------------------------') 
                    print('           * Hasta Pronto *            ')
                    print('---------------------------------------')
                    break
                
                case other:
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls')           
            
def menuVentas(tienda):
    while True:      
        os.system('cls')
        print('---------------------------------------')
        print('            Menu Ventas             ')
        print('---------------------------------------')    
        print(' 1. Realizar venta')
        print(' 2. Mostrar resumen facturas')
        print(' 3. Mostrar detalles facturas')
        print(' 4. Mostrar detalles factura')
        print(' 5. Eliminar producto de facturas')
        print(' 6. Mostrar venta por producto')
        print(' 7. Eliminar factura')
        print(' 8. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = int(input('Digite una opcion: ')) 
            match opc:
                case 1: 
                    os.system('cls')
                    tienda.crearFacturaPrincipal()
                    os.system('cls')
                case 2:
                    os.system('cls')
                    tienda.mostrarFacturas()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    tienda.facturasDetalles()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    tienda.consultarFactura()
                    os.system('pause')
                    os.system('cls')   
                case 5:
                    os.system('cls')
                    tienda.eliminarIFactura()
                    os.system('pause')
                    os.system('cls')
                case 6:
                    os.system('cls')
                    tienda.ventasPorProducto()
                    os.system('pause')
                    os.system('cls')                    
                case 7:
                    tienda.eliminarFactura()
                case 8:
                    os.system('cls')
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    os.system('cls')
                    break
                case other:
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls') 
    
def menuPedidos(tienda):
    while True:    
        
        os.system('cls')
        print('---------------------------------------')
        print('             Menu Pedidos              ')
        print('---------------------------------------')    
        print(' 1. Determinar producto')
        print(' 2. Realizar pedido')
        print(' 3. Salir')
        print('---------------------------------------')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    os.system('cls')
                    tienda.determinarProducto()
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    tienda.realizarPedido()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    os.system('cls')
                    break
                case other:
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls') 

def menuEstadisticas(tienda):
    while True:    
        
        os.system('cls')
        print('---------------------------------------')
        print('           Menu Estadisticas           ')
        print('---------------------------------------')    
        print(' 1. Ventas Totales')
        print(' 2. Ventas por producto')
        print(' 3. Promedio ventas')
        print(' 4. Producto más vendido')
        print(' 5. Salir')
        print('---------------------------------------')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    os.system('cls')
                    tienda.ventasTotales()
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    tienda.ventasPorProducto()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    tienda.promedioVentas()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    tienda.productoMasVendido()
                    os.system('pause')
                    os.system('cls')
                case 5:
                    os.system('cls')
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    os.system('cls')
                    break
                case other:
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls') 
    
def crearTienda():
    
    tienda = Tienda([],[])
    if tienda.productos == []:   
        tienda.leerProductos()
        if tienda.productos == []:
            tienda.adicionarProductosTienda()
    
    return tienda

def busProd(tienda):
    os.system('cls')
    opc = 's'
    while True:
        match opc:
            case 's' | 'S':
                nomProdcuto = str(input('\nDigite el nombre del producto que busca: '))
                print('\n----------------------------------------------')
                tienda.buscarProducto(nomProdcuto)
                print('----------------------------------------------')
                opc = str(input('Desea buscar otro producto? S/N -> '))
                print('----------------------------------------------')

            case 'n' | 'N':
                break
            case other:
                print('Digite un valor valido ')
                opc = str(input('\nValores validos: S/N -> '))

if __name__ == '__main__':
    main()   