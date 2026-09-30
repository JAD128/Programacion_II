import os
import pickle
from Veterinaria import *
from Leer import *



def menuprincipal():
    os.system('cls')
    if not os.path.exists('MiVeterinaria.dat'):
        mi_veterinaria = Veterinaria()
    else:
        mi_veterinaria = deserializacionVeterianaria()
    
    while True: 
        
        print('----------------------------------------')
        print('     Bienvenido Al Menú Principal       ')
        print('       Veterinaria HUella Amiga      ')
        print('----------------------------------------')
        print(' 1. Manejo de Usuarios')
        print(' 2. Manejo Servicios')
        print(' 3. Manejo Citas Médicos/Esteticos')
        print(' 4. Manejo Estadisticas')
        print(' 5. Salir')
        print('----------------------------------------')

        opcion= Leer('Seleccione la opción -> ').leerInt()

        match opcion:
            case 1: 
                menuManejoUsuarios(mi_veterinaria)
                os.system('pause')
            case 2: 
                menuServicios(mi_veterinaria)
                os.system('pause')
            case 3:
                mansermed(mi_veterinaria)
                os.system('pause')
            case 4:
                manejoEstadisticas(mi_veterinaria)
                os.system('pause')
            case 5:
                serializarVeterinaria(mi_veterinaria)
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')

def menuServicios(mi_veterinaria):
    
    while True:
        print('----------------------------------------')
        print('        * Manejo Servicios *        ')
        print('----------------------------------------')
        print(' 1. Adicionar Servicio')
        print(' 2. Modificar Servicio')
        print(' 3. Eliminar Servicio')
        print(' 4. Visualizar Servicios')
        print(' 5. Regresar')
        print('----------------------------------------\n')
        
        opc = Leer('Seleccione una opción -> ').leerInt()
        match opc:
            case 1:
                mi_veterinaria.adicionarSerivico()
                os.system('pause')
            case 2:
                mi_veterinaria.modificarServicio()
                os.system('pause')
            case 3:
                mi_veterinaria.eliminarServicio()
                os.system('pause')
            case 4:
                mi_veterinaria.visualizarServicios()
                os.system('pause')
            case 5:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')
    

def menuManejoUsuarios(mi_veterinaria):
    
    while True:
        
        print('----------------------------------------')
        print('          * Manejo Usuarios *           ')
        print('----------------------------------------')
        print(' 1. Manejo Trabajadores ')
        print(' 2. Manejo Clientes')
        print(' 3. Manejo Pacientes')
        print(' 4. Regresar')
        print('----------------------------------------\n')
        
        opc = Leer('Seleccione una opción -> ').leerInt()
        
        match opc:
            case 1:
                manejoTrabajadores(mi_veterinaria)
                os.system('pause')
            case 2:
                manejoClientes(mi_veterinaria)
                os.system('pause')
            case 3: 
                manejoPacientes(mi_veterinaria)
                os.system('pause')
            case 4:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')
                
def manejoTrabajadores(mi_veterinaria):
    
    while True:
        print('----------------------------------------')
        print('        * Manejo Trabajadores *        ')
        print('----------------------------------------')
        print(' 1. Adicionar Trabajador')
        print(' 2. Modificar Trabajador')
        print(' 3. Eliminar Trabajador')
        print(' 4. Visualizar Trabjadores')
        print(' 5. Regresar')
        print('----------------------------------------\n')
        
        opc = Leer('Seleccione una opción -> ').leerInt()
        match opc:
            case 1:
                mi_veterinaria.adicionarTrabajador()
                os.system('pause')
            case 2:
                mi_veterinaria.modificarTrabajador()
                os.system('pause')
            case 3:
                mi_veterinaria.eliminarTrabajador()
                os.system('pause')  
            case 4:
                mi_veterinaria.visualizarTrabajadores()
                os.system('pause')
            case 5:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')
                
def manejoClientes(mi_veterinaria):
    
    while True:
        print('----------------------------------------')
        print('          * Manejo Clientes *           ')
        print('----------------------------------------')
        print(' 1. Adicionar Cliente')
        print(' 2. Modificar Cliente')
        print(' 3. Eliminar Cliente')
        print(' 4. Visualizar Clientes')
        print(' 5. Regresar')
        print('----------------------------------------\n')
        opc = Leer('Seleccione una opción -> ').leerInt()
        match opc:
            case 1:
                mi_veterinaria.añadirCliente()
                os.system('pause')
            case 2:
                mi_veterinaria.modificarCliente()
                os.system('pause')
            case 3:
                mi_veterinaria.eliminarCliente() 
                os.system('pause')
            case 4:
                mi_veterinaria.visualizarClientes()
                os.system('pause')
            case 5:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')
                    
def manejoPacientes(mi_veterinaria):
    while True:
        print('----------------------------------------')
        print('          * Manejo Pacientes *           ')
        print('----------------------------------------')
        print(' 1. Adicionar Paciente')
        print(' 2. Modificar Paciente')
        print(' 3. Eliminar Paciente')
        print(' 4. Visualizar Pacientes')
        print(' 5. visualizar Paciente')
        print(' 6. Regresar')
        print('----------------------------------------\n')
        
        opc = Leer('Seleccione una opción -> ').leerInt()
        match opc:
            case 1:
                mi_veterinaria.añadirPaciente()
                os.system('pause')
            case 2:
                mi_veterinaria.modificarPaciente()
                os.system('pause')
            case 3:
                mi_veterinaria.eliminarPaciente()
                os.system('pause')
            case 4:
                mi_veterinaria.visualizarPacientes()
                os.system('pause')
            case 5:
                mi_veterinaria.visualizarPaciente()
                os.system('pause')
            case 6:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')

def mansermed(mi_veterinaria):
    while True:
        print('----------------------------------------')
        print('      Manejo Citas Médico/Estetico   ')
        print('----------------------------------------') 
        print(' 1. Agendar Cita Servicio Médico/Estetico' ) 
        print(' 2. Cancelar Cita Servicio Médico/Estetico')
        print(" 3. Lista de Citas")
        print(" 4. Lista de Citas Servicios") 
        print(' 5. Atencion Cita')
        print(" 6. Volver al menú principal ")
        print('---------------------------------------')
        opcion= Leer('Seleccione la opción--> ').leerInt()
        match opcion: 
            case 1: 
                mi_veterinaria.agendarCita()
                os.system('pause')  
            case 2:
                mi_veterinaria.cancelarCita()
                os.system('pause') 
            case 3:
                mi_veterinaria.visualizarCitas()
                os.system('pause')
            case 4:
                mi_veterinaria.visualizarCitasServicios()     
                os.system('pause') 
            case 5:
                mi_veterinaria.atencionCita()
                os.system('pause')
            case 6: 
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                break 
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')
            
def manejoEstadisticas(mi_veterinaria):
    while True:
        print('----------------------------------------')
        print('          * Manejo Estadisticas *           ')
        print('----------------------------------------')
        print(' 1. Visualizar Facturas')
        print(' 2. Visualizar Facturas Cliente')
        print(' 3. Visualizar Facturas Servicio')
        print(' 4. Pagar Factura')
        print(' 5. Regresar')
        print('----------------------------------------\n')
        
        opc = Leer('Seleccione una opción -> ').leerInt()
        match opc:
            case 1:
                mi_veterinaria.visualiarFacturas()
                os.system('pause')
            case 2:
                mi_veterinaria.visualiarFacturaClientes()
                os.system('pause')
            case 3:
                mi_veterinaria.visualiarFacturaServicio()
                os.system('pause')
            case 4:
                mi_veterinaria.pagarFactura()
                os.system('pause')
            case 5:
                print('\n----------------------------------------')
                print('            * Regresando... *           ')
                print('----------------------------------------\n')
                os.system('pause')
                break
            case other:
                print('\nError: Digite un valor valido...\n')
                os.system('pause')

def serializarVeterinaria(mi_veterinaria):
    arcSerializacion = open('MiVeterinaria.dat', 'wb')
    pickle.dump(mi_veterinaria, arcSerializacion)
    arcSerializacion.close()
    
def deserializacionVeterianaria():
    try:
        arcVeterinaria = open('MiVeterinaria.dat', 'rb')
        mi_veterinaria = pickle.load(arcVeterinaria)
        arcVeterinaria.close()
        return mi_veterinaria
    except FileNotFoundError:
        print('\nArchivo no encontrado...\n')
    
    
def main():
    menuprincipal()
    
    
if __name__ == '__main__':
    main()