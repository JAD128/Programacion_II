from Club import *
from Leer import *
import os, pickle

#Mostar producto / Consultar Producto

def menuPrincipal():
    
    if not os.path.exists('archCentral.dat'):
        club = Club()
    else:
        club = deserializarCentral()
        
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('             Menu Club          ')
        print('---------------------------------------')    
        print(' 1. Manejo de Socios')
        print(' 2. Manejo de Autorizados')
        print(' 3. Manejo de Consumos')
        print(' 4. Manejo Estadisticas ')
        print(' 5. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    menuManejoSocios(club)
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    menuManejoAutorizados(club)
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    menuManejoConsumo(club)
                    os.system('pause')
                    # os.system('cls')   
                case 4:
                    # os.system('cls')
                    menuManejoEstadistica(club)
                    os.system('pause')
                    # os.system('cls')
                case 5:
                    print('---------------------------------------') 
                    print('            * Saliendo *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    serializarCentral(club)
                    # os.system('cls')
                    break
                case other:
                    print('\nError: Digite un opción valida...\n')
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 

def menuManejoSocios(club):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Socios          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Socios')
        print(' 2. Modificar Socio')
        print(' 3. Eliminar socio')
        print(' 4. Consultar Socio con Autorizados')
        print(' 5. Regresar')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    club.adicionarSocio()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    pass
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    club.eliminarSocio()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    # os.system('cls')
                    club.mostrarSocio()
                    os.system('pause')
                    # os.system('cls')
                case 5:
                    print('---------------------------------------') 
                    print('   * Regresando a Menu Club *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    print('\nError: Digite un opción valida...\n')
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
            
def menuManejoAutorizados(club):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Afiliados          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Afiliados')
        print(' 2. Modificar Afiliado')
        print(' 3. Eliminar Afiliado')
        print(' 4. Consultar Afiliado con Socio')
        print(' 5. Regresar')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    club.adicionarAfiliado()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    # club.eliminarSocio()
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    # club.eliminarSocio()
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    # os.system('cls')
                    club.mostrarAutorizado()
                    os.system('pause')
                    # os.system('cls')
                case 5:
                    print('---------------------------------------') 
                    print('   * Regresando a Menu Club *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    print('\nError: Digite un opción valida...\n')
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
            
def menuManejoConsumo(club):
    
    while True:      
        # os.system('cls')
        print('---------------------------------------')
        print('        Menu Manejo Consumos          ')
        print('---------------------------------------')    
        print(' 1. Adicionar Consumo')
        print(' 2. Pagar Consumo')
        print(' 3. Modificar Consumo')
        print(' 4. Consultar Consumos Socio')
        print(' 5. Salir')
        print('---------------------------------------')      
        
        try:      
            opc = Leer('Digite una opcion: -> ').leerInt() 
            match opc:
                case 1: 
                    # os.system('cls')
                    club.adicionarCosumos()
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    club.pagarCosumos()
                    # os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    pass
                    # os.system('pause')
                    # os.system('cls')
                case 4:
                    # os.system('cls')
                    club.consumosSocio()
                    # os.system('pause')
                    # os.system('cls')
                case 5:
                    print('---------------------------------------') 
                    print('   * Regresando a Manejo Usuarios *    ')
                    print('---------------------------------------\n')
                    os.system('pause')
                    # os.system('cls')
                    break
                case other:
                    print('\nError: Digite un opción valida...\n')
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
    
def menuManejoEstadistica(Club):
    while True:    
        
        # os.system('cls')
        print('---------------------------------------')
        print('     Menu Manejo Estadisticas     ')
        print('---------------------------------------')    
        print(' 1. Total Consumos')
        print(' 2. Total Consumos por Socio')
        print(' 3. Socio que mas consumio')
        print(' 4. Total Consumo por tipo de usuario')
        print(' 5. Salir')
        print('---------------------------------------')            
        
        try:
            opc = int(input('Digite una opcion: '))
            match opc:
                case 1: 
                    # os.system('cls')
                    Club.totalConsumos()
                    os.system('pause')
                    # os.system('cls')
                case 2:
                    # os.system('cls')
                    pass
                    os.system('pause')
                    # os.system('cls')
                case 3:
                    # os.system('cls')
                    pass
                    os.system('pause')
                    # os.system('cls')
                case 4:
                    # os.system('cls')
                    Club.consumosTipoSocio()
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
                    print('\nError: Digite un opción valida...\n')
                    os.system('pause')
                    # os.system('cls')
        except ValueError:
            # os.system('cls')
            print('\nERROR: Digite un valor entero\n')
            os.system('pause')
            # os.system('cls') 
    
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