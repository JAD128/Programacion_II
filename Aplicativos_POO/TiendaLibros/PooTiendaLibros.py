from Leer import *
from TiendaLibros import *
import os

#Mostar producto / Consultar Producto

def menuPrincipal():
    
    tiendaLib = TiendaLibros()
    os.system('cls')
    while True:    
        
        print('---------------------------------------')
        print('            Menu Principal             ')
        print('---------------------------------------')    
        print(' 1. Manejo libros')
        print(' 2. Venta libro')
        print(' 3. Salir')
        print('---------------------------------------')    
        try:        
            opc = Leer('Digite una opción: -> ').leerInt()
                        
            match opc:
                
                case 1:
                    os.system('cls')
                    menuManejoLibros(tiendaLib) 
                case 2:
                    os.system('cls')
                    menuManejoVentas()                                                          
                case 3:
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
            
def menuManejoLibros(tiendaLib):
    while True:      
        os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo De Libros          ')
        print('---------------------------------------')    
        print(' 1. Adicionar libro')
        print(' 2. Eliminar libro')
        print(' 3. Modificar libro')
        print(' 4. Consultar libro')
        print(' 5. Mostrar libros')
        print(' 6. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    os.system('cls')
                    tiendaLib.adicionarLibro()
                    os.system('cls')
                case 2:
                    os.system('cls')
                    tiendaLib.eliminarLibro()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    tiendaLib.modificarLibro()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    tiendaLib.consultarLibro()
                    os.system('pause')
                    os.system('cls')   
                case 5:
                    os.system('cls')
                    tiendaLib.mostrarCatalogo()
                    os.system('pause')
                    os.system('cls')
                case 6:
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
    
def menuManejoVentas(tiendaLib):
    while True:    
        
        os.system('cls')
        print('---------------------------------------')
        print('          Menu Manejo Ventas           ')
        print('---------------------------------------')    
        print(' 1. Adicionar compra')
        print(' 2. Consultar compra')
        print(' 3. Determinar valor compra')
        print(' 4. Salir')
        print('---------------------------------------')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    os.system('cls')
                    # tiendaLib.determinarProducto() 
                    os.system('pause') 
                    os.system('cls')
                case 2:
                    os.system('cls')
                    # tiendaLib.realizarPedido()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    # tiendaLib.realizarPedido()
                    os.system('pause')
                    os.system('cls')
                case 4:
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
    
def main():
    menuPrincipal()

if __name__ == '__main__':
    main()   