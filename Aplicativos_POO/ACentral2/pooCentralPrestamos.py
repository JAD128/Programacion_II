from Central import *
from Leer import *
import os, pickle

#Mostar producto / Consultar Producto

def menuPrincipal():
    
    if not os.path.exists('archCentral.dat'):
        centralP = Central()
    else:
        centralP = deserializarCentral()
    
    
    # os.system('cls')
    while True:    
        
        print('---------------------------------------')
        print('            Menu central             ')
        print('---------------------------------------')    
        print(' 1. Manejo recursos')
        print(' 2. Manejo usuarios')
        print(' 3. Manejo prestamos y devoluciones')
        print(' 4. Salir')
        print('---------------------------------------')    
        try:        
            opc = Leer('Digite una opción: -> ').leerInt()
                        
            match opc:
                
                case 1:
                    # os.system('cls')
                    menuManejoRecursos(centralP) 
                case 2:
                    # os.system('cls')
                    menuManejoUsuarios(centralP) 
                case 3:
                    # os.system('cls')
                    menuPrestamosDevoluciones(centralP)                                                          
                case 4:
                    print('---------------------------------------') 
                    print('           * Hasta Pronto *            ')
                    print('---------------------------------------')
                    serializarCentral(centralP)
                    break
                
                case other:
                    os.system('pause')
                    
                    # os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls')           
            
def menuManejoRecursos(centralP):
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('       Menu Manejo De Recursos         ')
        print('---------------------------------------')    
        print(' 1. Adicionar recurso')
        print(' 2. consultar recurso')
        print(' 3. Modificar recurso')
        print(' 4. Mostrar recursos')
        print(' 5. Eliminar recursos')
        print(' 6. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    centralP.adicionarRecurso()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    centralP.consultarRecurso()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    os.system('cls')
                    # centralP.modificarRecurso()
                    os.system('pause')
                    os.system('cls')
                case 4:
                    # os.system('cls')
                    centralP.mostrarRecursos()
                    os.system('pause')
                    # os.system('cls')   
                case 5:
                    # os.system('cls')
                    # centralP.eliminarRecurso()
                    os.system('pause')
                    # os.system('cls')
                case 6:
                    # os.system('cls')
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
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
        # os.system('cls')
        print('---------------------------------------')
        print('      Menu Manejo De Usuarios          ')
        print('---------------------------------------')    
        print(' 1. Manejo de Estudiantes')
        print(' 2. Manejo de Docentes')
        print(' 3. Manejo de Trabajadores')
        print(' 4. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    menuManejoEstudiantes(centralP)
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    menuManejoDocentes(centralP)
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    menuManejoTrabajador(centralP)
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 

def menuManejoEstudiantes(centralP):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Estudiantes          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Estudiante')
        print(' 2. Consultar Estudiante')
        print(' 3. Mostrar Estudiantes')
        print(' 4. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    centralP.adicionarEstudiante()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    centralP.consultarEstudiante()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    centralP.visualizarEstudiantes()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    print('---------------------------------------') 
                    print('   * Regresando a Manejo Usuarios *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
            
def menuManejoDocentes(centralP):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Docentes          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Docente')
        print(' 2. Consultar Docente')
        print(' 3. Mostrar Docentes')
        print(' 4. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    centralP.adicionarDocente()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    centralP.consultarDocente()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    os.system('cls')
                    centralP.visualizarDocentes()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    print('---------------------------------------') 
                    print('   * Regresando a Manejo Usuarios *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 

def menuManejoTrabajador(centralP):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Trabajador          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Trabajador')
        print(' 2. Consultar Trabajador')
        print(' 3. Mostrar Trabajadores')
        print(' 4. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    centralP.adicionarTrabajador()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    centralP.consultarTrabajador()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    centralP.visualizarTrabajadores()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    print('---------------------------------------') 
                    print('   * Regresando a Manejo Usuarios *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
    
def menuPrestamosDevoluciones(centralP):
    while True:    
        
        # os.system('cls')
        print('---------------------------------------')
        print('     Menu Prestamos y Devoluciones     ')
        print('---------------------------------------')    
        print(' 1. Prestamo de recurso')
        print(' 2. Devolucion de recurso')
        print(' 3. Mostrar prestamos usuario')
        print(' 4. Mostrar prestamos usuarios')
        print(' 5. Salir')
        print('---------------------------------------')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    # os.system('cls')
                    centralP.prestarRecurso()
                    os.system('pause')
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    centralP.devolucionRecurso()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    centralP.prestamoUsuario()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    # os.system('cls')
                    centralP.prestamosUsuarios()
                    os.system('pause')
                    # os.system('cls')
                case 5:
                    # os.system('cls')
                    print('---------------------------------------') 
                    print('   * Regresando al menu principal *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            os.system('cls') 
    
def main():
    menuPrincipal()
    
def serializarCentral(central):
    
    archivoCentral = open('archCentral.dat', 'wb')
    pickle.dump(central, archivoCentral)
    archivoCentral.close()

def deserializarCentral():
    
    archivoCentral = open('archCentral.dat', 'rb')
    central = pickle.load(archivoCentral)
    archivoCentral.close()
    return central

if __name__ == '__main__':
    main()   