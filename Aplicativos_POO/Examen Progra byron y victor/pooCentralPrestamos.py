from Central import *
from Leer import *
import os

#Mostar producto / Consultar Producto

def menuPrincipal():
    
    centralP = Central()
    os.system('cls')
    while True:    
        
        print('****************************************')
        print('|            Menu Principal            |')
        print('****************************************')    
        print('| 1. Manejo recursos                   |')
        print('| 2. Manejo usuarios                   |') 
        print('| 3. Manejo prestamos y devoluciones   |')
        print('| 4. Salir                             |')
        print('***************************************')    
        try:        
            opc = Leer('Digite una opción: *> ').leerInt()
                        
            match opc:
                
                case 1:
                    os.system('cls')
                    menuManejoRecursos(centralP) 
                case 2:
                    os.system('cls')
                    menuManejoUsuarios(centralP) 
                case 3:
                    os.system('cls')
                    menuPrestamosDevoluciones(centralP)                                                          
                case 4:
                    print('***************************************') 
                    print('|             Hasta Pronto            |')
                    print('***************************************')
                    break
                
                case other:
                    os.system('pause')
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls')           
            
def menuManejoRecursos(centralP):
    while True:      
        os.system('cls')
        print('***************************************')
        print('|      Menu Manejo De Recursos        |')
        print('***************************************')    
        print('| 1. Adicionar recurso                |')
        print('| 2. consultar recurso                |')
        print('| 3. Modificar recurso                |')
        print('| 4. Mostrar recursos                 |')
        print('| 5. Eliminar recursos                |')
        print('| 6. Salir                            |')
        print('***************************************')      
        
        try:      
            opc = Leer('Digite una opcion: *> ').leerInt() 
            match opc:
                case 1: 
                    os.system('cls')
                    centralP.Agregarrecurso()
                    os.system('cls')
                case 2:
                    os.system('cls')
                    centralP.Recursoaconsultar()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    # centralP.modificarRecurso()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    centralP.mostrarRecursos()
                    os.system('pause')
                    os.system('cls')   
                case 5:
                    os.system('cls')
                    # centralP.eliminarRecurso()
                    os.system('pause')
                    os.system('cls')
                case 6:
                    os.system('cls')
                    print('****************************************') 
                    print('|     Regresando al menu principal  n1   |')
                    print('****************************************\n')
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

def menuManejoUsuarios(centralP):
    while True:      
        os.system('cls')
        print('***************************************')
        print('|      Menu Manejo De Usuarios        |')
        print('***************************************')    
        print('| 1. Adicionar usuarios               |')
        print('| 2. Consultar usuarios               |')
        print('| 3. Modificar usuarios               |')
        print('| 4. Eliminar usuarios                |')
        print('| 5. Mostrar Usuarios                 |')
        print('| 6. Salir                            |')
        print('***************************************')      
        
        try:      
            opc = Leer('Digite una opcion: *> ').leerInt() 
            match opc:
                case 1: 
                    os.system('cls')
                    centralP.adicionarUsuario()
                    os.system('cls')
                case 2:
                    os.system('cls')
                    centralP.consultarUsuario()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    # centralP.modificarLibro()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    # centralP.consultarLibro()
                    os.system('pause')
                    os.system('cls')   
                case 5:
                    os.system('cls')
                    centralP.mostrarUsuarios()
                    os.system('pause')
                    os.system('cls')
                case 6:
                    os.system('cls')
                    print('***************************************') 
                    print('|   * Regresando al menu principal *   |')
                    print('***************************************\n')
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
    
def menuPrestamosDevoluciones(centralP):
    while True:    
        
        os.system('cls')
        print('***************************************')
        print('|     Menu Prestamos y Devoluciones    |')
        print('***************************************')    
        print('| 1. Prestamo de recurso               |')
        print('| 2. Devolucion de recurso             |')
        print('| 3. Mostrar prestamos usuario         |')
        print('| 4. Mostrar prestamos usuarios        |')
        print('| 5. Salir                             |')
        print('***************************************')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    os.system('cls')
                    centralP.prestarRecurso()
                    os.system('pause')
                    os.system('cls')
                case 2:
                    os.system('cls')
                    centralP.devolucionRecurso()
                    os.system('pause')
                    os.system('cls')
                case 3:
                    os.system('cls')
                    centralP.prestamoUsuario()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    os.system('cls')
                    centralP.prestamosUsuarios()
                    os.system('pause')
                    os.system('cls')
                case 5:
                    os.system('cls')
                    print('***************************************') 
                    print('|   * Regresando al menu principal *   |')
                    print('***************************************\n')
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