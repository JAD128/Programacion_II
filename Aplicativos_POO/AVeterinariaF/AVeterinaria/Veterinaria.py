from Mascota import *
from Factura import *
from Cliente import *
from Servicio import *
from Leer import *
from Trabajador import *
from Cita import *
from datetime import datetime
import os

class Veterinaria:

    dineroEnCaja=0
    numeroFactura=0

    def __init__(self):
        self.clientes = []
        self.citasAtendidas = []
        self.servicios = []
        self.trabajadores = []
        self.citasPorAtender = []
        
    def adicionarTrabajador(self):
        
        resp = 's'
        print('\n----------------------------------------')
        print('        * Registro Trabajadores *       ')
        print('----------------------------------------\n')
        while True:   
            match resp:
                case 's' | 'Si' | 'SI' | 'S' | 'si':
                    self.adiTrabajador()
                    print('----------------------------------------\n')
                    resp = Leer('Desea adicionar más trabajadores? S/N -> ').leerCadena()
                case 'n' | 'No' | 'NO' | 'N' | 'no':
                    # os.system('pause')
                    break
                case other:
                    print('\nError: Digite una opción correcta... \n')
                    resp = Leer('Desea adicionar más trabajadores? S/N -> ').leerCadena()
        
    def adiTrabajador(self):
        print('     --- * Registro en proceso * ---   ')
        print('----------------------------------------')
        idTrabajador = Leer('Digite la identificación del trabajador: ').leerInt()
        if not self.buscarTrabajador(idTrabajador):
            nomTrabajador = Leer('Digite el nombre del trabajador: ').leerCadena()
            sexTrabajador = Leer('Digite el sexo del trabajador (M/F): ').leerSexo()
            salTrabajador = Leer('Digite el salario del trabajdor: ').leerFloat()
            print('----------------------------------------')
            print('Tipo de Trabajador: \n1. Medico Veterinario \n2. Enfermero \n3. Esteticista')
            print('----------------------------------------')
            tipoTrabajador = Leer('Tipo de trabajador: ').leerInt()
            while True:
                match tipoTrabajador:
                    case 1: 
                        vet = Veterinario(nomTrabajador, sexTrabajador, idTrabajador, salTrabajador)
                        self.trabajadores.append(vet)
                        print('----------------------------------------')
                        print('           ¡Registro Exitoso!         ')
                        break
                    case 2: 
                        enf = Enfermero(nomTrabajador, sexTrabajador, idTrabajador, salTrabajador)
                        self.trabajadores.append(enf)
                        print('----------------------------------------')
                        print('           ¡Registro Exitoso!         ')
                        break
                    case 3:
                        est = Esteticista(nomTrabajador, sexTrabajador, idTrabajador, salTrabajador)
                        self.trabajadores.append(est)
                        print('----------------------------------------')
                        print('           ¡Registro Exitoso!         ')
                        break
                    case other:
                        print('\nError: Digite una opción correcta...\n')
                        tipoTrabajador = Leer('Digite el tipo de trabajador: ').leerInt()
        else:
            print('----------------------------------------')
            print('\nLa identificación ingresada ya existe...\n')
                    
    def buscarTrabajador(self, idTrabajador):
        for elem in self.trabajadores:
            if elem.id == idTrabajador:
                return True
        return False
    
    def buscarTrabajador1(self, idTrabajador):
        for elem in self.trabajadores:
            if elem.id == idTrabajador:
                return elem
            
    def buscarCliente(self, idCliente):
        for elem in self.clientes:
            if elem.idCliente == idCliente:
                return True
        return False
    
    def buscarCliente1(self, idCliente):
        for elem in self.clientes:
            if elem.idCliente == idCliente:
                return elem
    
    def modificarTrabajador(self):
        
        if self.trabajadores != []:
            resp = 's'
            print('\n----------------------------------------')
            print('         * Modificar Trabajador *       ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.modificarTraba()
                        print('----------------------------------------\n')
                        resp = Leer('Desea modificar a otro trabajador? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea modificar a otro trabajador? S/N -> ').leerCadena()
        else:
            print('No hay trabajadores en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def modificarTraba(self):
        print('   --- * Modificación en proceso * ---')
        print('----------------------------------------')
        self.visualizarTrabajadores1()
        idTrabajador = Leer('Digite la identificación del trabajador que desea modificar: ').leerInt()
        if self.buscarTrabajador(idTrabajador):
            trabajador = self.buscarTrabajador1(idTrabajador)
            trabajador.nombre = Leer('Digite el nombre del trabajador: ').leerCadena()
            trabajador.sexo = Leer('Digite el sexo del trabajador (M/F): ').leerCadena()
            trabajador.salario = Leer('Digite el salario del trabajdor: ').leerFloat() 
            print('----------------------------------------')
            print('       * ¡Modificación exitosa! *     ')
        else:
            print('----------------------------------------')
            print('\nLa identificacion ingresada no existe...\n')
            
    def visualizarTrabajadores(self):
        
        print('\n----------------------------------------')
        print('      * Visualizar Trabajadores *      ')
        print('----------------------------------------\n')
        if self.trabajadores != []:
            print('--------- * Veterinarios * ---------')
            for elem in self.trabajadores:
                if isinstance(elem, Veterinario):
                    elem.visualizarTrabajador()
            print('\n---------- * Enfermeros * ----------')
            for elem in self.trabajadores:
                if isinstance(elem, Enfermero):
                    elem.visualizarTrabajador()
            print('\n--------- * Esteticistas * ---------')
            for elem in self.trabajadores:
                if isinstance(elem, Esteticista):
                    elem.visualizarTrabajador()
        else:
            print('No hay trabajadores en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def visualizarTrabajadores1(self):
        
        print('            * Trabajadores *            ')
        print('----------------------------------------')
        print('  --------- * Veterinarios * ---------')
        for elem in self.trabajadores:
            if isinstance(elem, Veterinario):
                elem.verTrabajador()
        print('\n  ---------- * Enfermeros * ----------')
        for elem in self.trabajadores:
            if isinstance(elem, Enfermero):
                elem.verTrabajador()
        print('\n  --------- * Esteticistas * ---------')
        for elem in self.trabajadores:
            if isinstance(elem, Esteticista):
                elem.verTrabajador()
    
    def eliminarTrabajador(self):
        
        if self.trabajadores != []:
            resp = 's'
            print('\n----------------------------------------')
            print('        * Eliminar Trabajador  *       ')
            print('----------------------------------------')  
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.eliminarTraba()
                        resp = Leer('Desea remover a otro trabajador? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea remover a otro trabajador? S/N -> ').leerCadena()
        else:
            print('No hay trabajadores en la veterinaria...\n')
            print('----------------------------------------\n')
        
    def eliminarTraba(self):
        print('     --- * Remoción en proceso * ---')
        print('----------------------------------------')
        self.visualizarTrabajadores1()
        idTrabajador = Leer('Digite la identificación del trabajador que desea remover: ').leerInt()
        if self.buscarTrabajador(idTrabajador):
            trabajador = self.buscarTrabajador1(idTrabajador)
            if trabajador.disponibilidad:
                self.trabajadores.remove(trabajador)
                print('----------------------------------------')
                print('         ¡Remoción Exitosa!         ')  
                print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('No se puede remover al trabajador...    ')  
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nLa identificación ingresada no existe...\n')
            print('----------------------------------------\n')
            
    def añadirCliente(self):
        
        resp = 's'
        print('\n----------------------------------------')
        print('         * Registro Clientes *       ')
        print('----------------------------------------\n')
        while True:   
            match resp:
                case 's' | 'Si' | 'SI' | 'S' | 'si':
                    self.adicionarCliente()
                    resp = Leer('Desea adicionar más clientes? S/N -> ').leerCadena()
                case 'n' | 'No' | 'NO' | 'N' | 'no':
                    # os.system('pause')
                    break
                case other:
                    print('\nError: Digite una opción correcta... \n')
                    resp = Leer('Desea adicionar más clientes? S/N -> ').leerCadena()
                    
    def adicionarCliente(self):
        print('   ----- * Registro en proceso * -----')
        print('----------------------------------------')
        idCliente = Leer('Digite la identificación del cliente: ').leerInt()
        if not self.buscarCliente(idCliente):
            nomCliente = Leer('Digite el nombre del cliente: ').leerCadena()
            contactoCliente = Leer('Digite un medio contacto (Telefono o correo electronico): ').leerCadena()
            cliente = Cliente(idCliente, nomCliente, contactoCliente)
            self.clientes.append(cliente)
            print('------------------------------------')
            print('         ¡Registro Exitoso!         ')
            print('------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nLa identificación ingresada ya existe...\n')
            print('----------------------------------------\n')
    
    def modificarCliente(self):
        
        if self.clientes != []:
            resp = 's'
            print('\n----------------------------------------')
            print('          * Modificar Cliente *       ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.modClinete()
                        resp = Leer('Desea modificar a otro cliente? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea modificar a otro cliente? S/N -> ').leerCadena()
        else:
            print('\nNo hay clientes en la veterinaria...\n')
            
    def modClinete(self):
        print('   --- * Modificación en proceso * ---')
        print('----------------------------------------')
        self.visualizarClientes1()
        idCliente = Leer('Digite la identificación del cliente que desea modificar: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            cliente.nomCliente = Leer('Digite el nombre del cliente: ').leerCadena()
            cliente.contacto = Leer('Digite un medio contacto (Telefono o correo electronico): ').leerCadena() 
            print('----------------------------------------')
            print('         ¡Modificación exitosa!       ')
            print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('La identificacion ingresada no existe...')
            print('----------------------------------------\n')
            
    def eliminarCliente(self):
        
        if self.clientes != []:
            resp = 's'
            print('\n----------------------------------------')
            print('         * Eliminar Cliente  *       ')
            print('----------------------------------------\n')  
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.elimCliente()
                        resp = Leer('Desea remover a otro cliente? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea remover a otro cliente? S/N -> ').leerCadena()
        else:
            print('\nNo hay clientes en la veterinaria...\n')
            
    def elimCliente(self):
        print('     --- * Remoción en proceso * ---')
        print('----------------------------------------')
        self.visualizarClientes1()
        idCliente = Leer('Digite la identificación del cliente que desea remover: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            if cliente.mascotas == []:
                self.clientes.remove(cliente)
                print('----------------------------------------')
                print('           ¡Remoción Exitosa!         ')  
                print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('No se puede remover al cliente...        ')  
                print('----------------------------------------\n')        
        else:
            print('----------------------------------------')
            print('\nLa identificación ingresada no existe...\n')  
            print('----------------------------------------\n')
        
    def visualizarClientes(self):
        
        print('\n----------------------------------------')
        print('         * Visualizar Clientes *      ')
        print('----------------------------------------')
        if self.clientes != []:
            for elem in self.clientes:
                print(elem)
                print('----------------------------------------')
        else:
            print('No hay clientes en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def visualizarClientes1(self):
        
        print('\n              * Clientes *      ')
        print('----------------------------------------')
        for elem in self.clientes:
            elem.cliente()
     
    def añadirPaciente(self):
        
        resp = 's'
        print('\n----------------------------------------')
        print('         * Registro Pacientes *       ')
        print('----------------------------------------\n')
        while True:   
            match resp:
                case 's' | 'Si' | 'SI' | 'S' | 'si':
                    self.regPaciente()
                    resp = Leer('Desea adicionar más pacientes? S/N -> ').leerCadena()
                case 'n' | 'No' | 'NO' | 'N' | 'no':
                    break
                case other:
                    print('\nError: Digite una opción correcta... \n')
                    resp = Leer('Desea adicionar más pacientes? S/N -> ').leerCadena()
                    
    def regPaciente(self):
        print('    --- * Registro en proceso * ---')
        print('----------------------------------------')
        idCliente = Leer('Digite la identificación del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            idPaciente = Leer('Digite la identificación del paciente: ').leerInt()
            if not self.buscarPaciente(cliente, idPaciente):
                nomPaciente = Leer('Digite el nombre del paciente: ').leerCadena()
                espPaciente = Leer('Digite la especie del paciente: ').leerCadena()
                razaPaciente = Leer('Digite la raza del paciente: ').leerCadena()
                sexoPaciente = Leer('Digite el sexo del paciente (M/H): ').leerCadena()
                edaPaciente = Leer('Digite la edad del paciente (Años): ').leerInt()
                pesoPaciente = Leer('Digite el peso del paciente (Kg): ').leerCadena()
                paciente = Mascota(nomPaciente, espPaciente, idPaciente, edaPaciente, sexoPaciente, razaPaciente, pesoPaciente)
                cliente.mascotas.append(paciente)
                print('----------------------------------------')
                print('           ¡Registro Exitoso!         ')
                print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('\nLa identificación del paciente ingresada ya existe...\n')
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nLa identificación ingresada no existe...\n')
            print('----------------------------------------\n')
    
    def modificarPaciente(self):
         
        if self.clientes != []:
            resp = 's'
            print('\n----------------------------------------')
            print('          * Modificar Paciente *       ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.modPaciente()
                        resp = Leer('Desea modificar a otro paciente? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea modificar a otro paciente? S/N -> ').leerCadena()
        else:
            print('----------------------------------------')
            print('\nNo hay clientes en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def modPaciente(self):
        print('   --- * Modificación en proceso * ---')
        print('----------------------------------------')
        self.visualizarClientes1()
        idCliente = Leer('Digite la identificación del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            if cliente.mascotas != []:
                self.visualizarPacientesDueño(cliente)
                idPaciente = Leer('Digite la identificación del paciente que desea modificar: ').leerInt()
                if self.buscarPaciente(cliente, idPaciente):
                    paciente = self.buscarPaciente1(idPaciente, cliente)
                    paciente.nombre = Leer('Digite el nombre del paciente: ').leerCadena()
                    paciente.especie = Leer('Digite la especie del paciente: ').leerCadena()
                    paciente.raza = Leer('Digite la raza del paciente: ').leerCadena()
                    paciente.sexo = Leer('Digite el sexo del paciente (M/H): ').leerCadena()
                    paciente.edad = Leer('Digite la edad del paciente (Años: ').leerInt()
                    paciente.peso = Leer('Digite el peso del paciente (Kg): ').leerCadena()
                    print('----------------------------------------')
                    print('        ¡Modificación exitosa!      ')
                    print('----------------------------------------\n')
                else: 
                    print('----------------------------------------')
                    print('\nLa identificación del paciente ingresada no existe...\n')
                    print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('\nEl cliente no tiene mascotas/pacientes registrados...\n')
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nLa identificacion ingresada no existe...\n')
            print('----------------------------------------\n')
     
    def eliminarPaciente(self):
        
        if self.clientes != []:
            resp = 's'
            print('\n----------------------------------------')
            print('         * Eliminar Paciente  *       ')
            print('----------------------------------------\n')  
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.eliminarTraba()
                        resp = Leer('Desea remover a otro paciente? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea remover a otro paciente? S/N -> ').leerCadena()
        else:
            print('----------------------------------------')
            print('\nNo hay pacientes en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def eliminarPac(self):
        print('     --- * Remoción en proceso * ---')
        print('----------------------------------------')
        self.visualizarClientes1()
        idCliente = Leer('\nDigite la identificación del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            if cliente.mascotas != []:
                self.visualizarPacientesDueño(cliente)
                idPaciente = Leer('\nDigite la identificación del paciente que desea remover: ').leerInt()
                print('\n-------- * Mascotas * --------')
                if self.buscarPaciente(cliente, idPaciente):
                    paciente = self.buscarPaciente1(idPaciente, cliente)
                    cliente.mascotas.remove(paciente)
                    print('----------------------------------------')
                    print('         ¡Remoción Exitosa!         ')  
                    print('----------------------------------------\n')
                    
                else: 
                    print('----------------------------------------')
                    print('\nLa identificación del paciente ingresada no existe...\n')
                    print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('\nEl cliente no tiene mascotas/pacientes registrados...\n')
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('La identificacion ingresada no existe...')
            print('----------------------------------------\n')
                 
    def buscarPaciente(self, cliente, idPaciente):
        
        for elem in cliente.mascotas:
            if elem.id == idPaciente:
                return True
        return False
         
    def visualizarPacientes(self):
        
        if self.clientes != []:
            print('\n----------------------------------------')
            print('      * Visualizar Pacientes *      ')
            print('----------------------------------------')
            for cliente in self.clientes:
                print(f'\nDueño: {cliente.nomCliente} | Id: {cliente.idCliente}')
                print('    --- * Mascotas/Pacientes * ---')
                print('----------------------------------------')
                if cliente.mascotas != []:
                    for mascota in cliente.mascotas:
                        mascota.visualizarMascota()
                else:
                    print('El Cliente no tiene mascotas registradas...')
                    print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nNo hay pacientes en la veterinaria...\n')
            print('----------------------------------------\n')
           
    def visualizarPaciente(self):
        
        if self.clientes != []:
            resp = 's'
            print('\n----------------------------------------')
            print('        * Visualizar Paciente  *     ')
            print('----------------------------------------\n')  
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.verPaciente()
                        resp = Leer('Desea ver a otro paciente? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea ver a otro paciente? S/N -> ').leerCadena()
        else:
            print('----------------------------------------')
            print('\nNo hay pacientes en la veterinaria...\n')
            print('----------------------------------------\n')
            
    def verPaciente(self):
        print('  --- * Visualización en proceso * ---')
        print('----------------------------------------')
        self.visualizarClientes1()
        idCliente = Leer('\nDigite la identificación del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            if cliente.mascotas != []:
                self.visualizarPacientesDueño(cliente)
                idPaciente = Leer('\nDigite la identificación del paciente que desea visualizar: ').leerInt()
                print('\n-------- * Mascotas * --------')
                if self.buscarPaciente(cliente, idPaciente):
                    paciente = self.buscarPaciente1(idPaciente, cliente)
                    print(paciente)
                    print('----------------------------------------\n')
                else: 
                    print('----------------------------------------')
                    print('\nLa identificación del paciente ingresada no existe...\n')
                    print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('\nEL cliente no tiene pacientes registrados...\n')
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('La identificacion ingresada no existe...')
            print('----------------------------------------\n')
    
    def visualizarPacientesDueño(self, dueño):
        
        print('\n---------- * Pacientes * ----------')
        for mascota in dueño.mascotas:
            mascota.visualizarMascota()
   
    def buscarPaciente1(self, idMascota, dueño):
        for paciente in dueño.mascotas:
            if paciente.id == idMascota:
                return paciente
     
    def adicionarSerivico(self):
        
        resp = 's'
        print('\n----------------------------------------')
        print('         * Registro Servicios *   ')
        print('----------------------------------------\n')
        while True:   
            match resp:
                case 's' | 'Si' | 'SI' | 'S' | 'si':
                    self.regServicios()
                    resp = Leer('Desea adicionar más servicos? S/N -> ').leerCadena()
                case 'n' | 'No' | 'NO' | 'N' | 'no':
                    # os.system('pause')
                    break
                case other:
                    print('\nError: Digite una opción correcta... \n')
                    resp = Leer('Desea adicionar más servicios? S/N -> ').leerCadena()
    
    def regServicios(self):
        print('    --- * Registro en proceso * ---')
        print('----------------------------------------')
        idServicio = Leer('Digite el codigo del servicio : ').leerInt()
        if not self.buscarServicio(idServicio):
            razonServicio = Leer('Digite la razon del servicio: ').leerCadena()
            precioServicio = Leer('Digite el precio del servico: ').leerFloat()
            print('----------------------------------------')
            print(f'Tipo de servicio: \n1. Servico Médico \n2. Servico Estetico')
            print('----------------------------------------')
            tipoServicio = Leer('Digite el tipo de servicio: ').leerInt()
            while True:
                match tipoServicio:
                    case 1:
                        servicio = ServivioMedico(razonServicio, precioServicio, idServicio)
                        self.servicios.append(servicio)
                        print('----------------------------------------')
                        print('            ¡Registro Exitoso!         ')
                        print('----------------------------------------\n')
                        break
                    case 2:
                        servicio = ServicioEstetico(razonServicio, precioServicio, idServicio)
                        self.servicios.append(servicio)
                        print('----------------------------------------')
                        print('            ¡Registro Exitoso!         ')
                        print('----------------------------------------\n')
                        break
                    case other:
                        print('\nError: Digite una opción correcta...\n')
                        tipoServicio = Leer('Digite el tipo de servicio: ').leerInt() 
        else:
            print('----------------------------------------')
            print('\nEl codigo ingresado ya existe...\n')
            print('----------------------------------------\n')
    
    def modificarServicio(self):
         
        if self.servicios != []:
            resp = 's'
            print('\n----------------------------------------')
            print('          * Modificar Servicio *       ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.modServicio()
                        resp = Leer('Desea modificar a otro servicios? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea modificar a otro servicios? S/N -> ').leerCadena()
        else:
            print('----------------------------------------')
            print('\nNo hay servicios en la veterinaria...\n')
            print('----------------------------------------\n')
      
    def modServicio(self):
        print('   --- * Modificación en proceso * ---')
        print('----------------------------------------')
        self.visualizarServicios1()
        idServicio = Leer('Digite el id del servicio que desea modificar: ').leerInt()
        if self.buscarServicio(idServicio):
            servicio = self.buscarServicio1(idServicio)
            servicio.razonservicio = Leer('Digite la razon del servicio: ').leerCadena()
            servicio.valortotal = Leer('Digite el valor del servicio: ').leerFloat()
            print('----------------------------------------')
            print('       * ¡Modificación exitosa! *     ')
            print('----------------------------------------\n')
        else: 
            print('----------------------------------------')
            print('\nLa id del servicio ingresado no existe...\n')
            print('----------------------------------------\n') 
    
    def visualizarServicios(self):
        
        if self.servicios != []:
            print('----------------------------------------')
            print('        * Visualizar Servicios *       ')
            print('----------------------------------------')
            self.visualizarServicios1()
        else:
            print('\nNo hay servicios en la veterinaria...\n')
            
    def visualizarServicios1(self):
        c = 0
        print('     \n--- *  Servicios Médicos * ---')
        print('----------------------------------------')
        for servicio in self.servicios:
            if isinstance(servicio, ServivioMedico):
                servicio.servicio()
                c+=1
        if c == 0:
            print('----------------------------------------')
            print('No hay servicios en la veterinaria')
            print('----------------------------------------')
        c = 0       
        print('     \n--- * Servicios Esteticos * ---')
        print('----------------------------------------')
        for servicio in self.servicios:
            if isinstance(servicio, ServicioEstetico):
                servicio.servicio()
                c+=1
        if c == 0:
            print('----------------------------------------')
            print('No hay servicios en la veterinaria')
            print('----------------------------------------')
         
    def buscarServicio(self, idServ):
        
        for serv in self.servicios:
            if serv.idServicio == idServ:
                return True
        return False  
    
    def buscarServicio1(self, idServ):
        
        for serv in self.servicios:
            if serv.idServicio == idServ:
                return serv
            
    def agendarCita(self):
        if self.clientes != [] and self.servicios != [] and self.trabajadores != []:
            resp = 's'
            print('\n----------------------------------------')
            print('           * Agendar Cita  *   ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.agendarCi()
                        resp = Leer('Desea agendar otra cita? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea agendar otra cita? S/N -> ').leerCadena()
        else: 
            print('----------------------------------------')
            print('\nLa veterinaria no puede agendar citas...\n')   
            print('----------------------------------------\n')
    
    def eliminarServicio(self):
        if self.servicios != []:
            resp = 's'
            print('\n----------------------------------------')
            print('          * Remover Servicio *       ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.removerServ()
                        resp = Leer('Desea modificar a otro servicios? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea modificar a otro servicios? S/N -> ').leerCadena()
        else:
            print('\nNo hay servicios en la veterinaria...\n')
            
    def removerServ(self):
        print('    --- * Remoción en proceso * ---')
        print('----------------------------------------')
        self.visualizarServicios1()
        idServicio = Leer('\nDigite el id del servicio que desea modificar: ').leerInt()
        if self.buscarServicio(idServicio):
            servicio = self.buscarServicio1(idServicio)
            self.servicios.remove(servicio)
            print('------------------------------------')
            print('     * ¡Remoción exitosa! *     ')
            print('------------------------------------')
        else: 
            print('\nLa id del servicio ingresado no existe...\n')
            print('------------------------------------')  
        
    
    def agendarCi(self):
        print('   --- * Agendamiento en proceso * ---')
        print('----------------------------------------')
        idCita = Leer('Digite el codigo de la cita: ').leerInt()
        if not self.buscarCita(idCita):
            self.visualizarClientes1()
            idCliente = Leer('Digite la identificación del cliente: ').leerInt()
            if self.buscarCliente(idCliente):
                cliente = self.buscarCliente1(idCliente)
                if cliente.mascotas != []:
                    self.visualizarPacientesDueño(cliente)
                    idPaciente = Leer('Digite la identificación del paciente para su cita: ').leerInt()
                    if self.buscarPaciente(cliente, idPaciente):
                        paciente = self.buscarPaciente1(idPaciente, cliente)
                        self.visualizarServicios1()
                        idServicio = Leer('Digite el codigo del servicio para su cita: ').leerInt()
                        if self.buscarServicio(idServicio):
                            servicio = self.buscarServicio1(idServicio)
                            trabajador = self.servicioCita(servicio)
                            if trabajador != None:
                                if trabajador.disponibilidad:
                                    fecha = Leer('Digite la fecha de la cita (formato: dd/mm/yyyy HH:mm): ').leerFecha()
                                    cita = Cita(idCita, fecha, trabajador, paciente, cliente, servicio)
                                    trabajador.disponibilidad = False
                                    self.citasPorAtender.append(cita)
                                    print('----------------------------------------')
                                    print('            ¡Cita Agendada!      ')
                                    print('----------------------------------------\n')
                                else:
                                    print('----------------------------------------')
                                    print('\nEl trabajador no se encuentra disponible...\n')
                                    print('----------------------------------------\n')
                        else:
                            print('----------------------------------------')
                            print('\nEl codigo del serivicio ingresada no existe...\n')
                            print('----------------------------------------\n')
                    else: 
                        print('----------------------------------------')
                        print('\nLa identificación del paciente ingresada no existe...\n')
                        print('----------------------------------------\n')
                else:
                    print('----------------------------------------')
                    print('\nEL cliente no tiene mascotas/pacientes registrados...\n')
                    print('----------------------------------------\n')
            else:
                print('----------------------------------------')
                print('La identificacion ingresada no existe...')
                print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nEl codigo digitado ya existe...\n')   
            print('----------------------------------------\n')  
    
    def buscarCita(self, idCita):
        
        for citas in self.citasPorAtender:
            if citas.idCita == idCita:
                return True
        return False

    def buscarCita1(self, idCita):
        
        for citas in self.citasPorAtender:
            if citas.idCita == idCita:
                return citas
    
    def servicioCita(self, servico):
        
        if isinstance(servico, ServivioMedico):
            print('\n---------- * Personal Medico * ---------')
            for trabajador in self.trabajadores:
                if isinstance(trabajador, Veterinario) or isinstance(trabajador, Enfermero):
                    trabajador.trabajador()
            codigoTrabajador = Leer('Digite el codigo del encargado para la cita: ').leerInt()
            if self.buscarTrabajador(codigoTrabajador):
                trabajador = self.buscarTrabajador1(codigoTrabajador)
                return trabajador
            else:
                print('\nEl codigo digitado no existe...\n')
                return None
        elif isinstance(servico, ServicioEstetico):
            print('\n--------- * Personal Estetico * ----------')
            for trabajador in self.trabajadores:
                if isinstance(trabajador, Esteticista):
                    trabajador.trabajador()
            codigoTrabajador = Leer('Digite el codigo del trabajador para la cita: ').leerInt()
            if self.buscarTrabajador(codigoTrabajador):
                trabajador = self.buscarTrabajador1(codigoTrabajador)
                return trabajador
            else:
                print('\nEl codigo digitado no existe...\n')
                return None
            
    def visualizarCitasServicios(self):
        
        if self.citasPorAtender != []:
            print('\n----------------------------------------')
            print('     * Visualizar Citas Servicio *       ')
            print('----------------------------------------')
            print('    --- * Servicios Esteticos * ---')
            print('----------------------------------------')
            for cita in self.citasPorAtender:
                if isinstance(cita.servicio, ServicioEstetico):
                    cita.cita()
            print('   \n --- *  Servicios Médicos * ---')
            print('----------------------------------------')
            for cita in self.citasPorAtender:
                if isinstance(cita.servicio, ServivioMedico):
                    cita.cita()
        else:
            print('----------------------------------------') 
            print('\nNo hay citas disponibles...\n')
            print('----------------------------------------\n') 
    
    def visualizarCitas(self):
        if self.citasPorAtender != []:
            print('\n----------------------------------------')
            print('         * Visualizar Citas *       ')
            print('----------------------------------------')
            for cita in self.citasPorAtender:
                cita.cita()    
        else:
            print('----------------------------------------') 
            print('\nNo hay citas disponibles...\n')
            print('----------------------------------------') 
    
    def visualizarCitas1(self):
        for cita in self.citasPorAtender:
            cita.citas()
     
    def cancelarCita(self):
        
        if self.citasPorAtender != []:
            resp = 's'
            print('\n----------------------------------------')
            print('         * Cancelar Cita  *   ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.cancelarCit()
                        resp = Leer('Desea cancelar otra cita? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea cancelar otra cita? S/N -> ').leerCadena()
        else:
            print('----------------------------------------') 
            print('\nNo hay citas disponibles...\n')
            print('----------------------------------------\n') 
         
       
    def cancelarCit(self):
        print('  --- * Cancelamiento en proceso * ---  ')
        print('----------------------------------------')
        self.visualizarCitas1()
        idCita = Leer('Digite el codigo de la cita: ').leerInt()
        if self.buscarCita(idCita):
            citaRemover = self.buscarCita1(idCita)
            self.citasPorAtender.remove(citaRemover)
            print('------------------------------------') 
            print('        * Cita Cancelada *         ')
            print('------------------------------------')
        else:
            print('------------------------------------')
            print('\nEl codigo digitado no existe...\n')   
            print('------------------------------------\n') 
    
    def atencionCita(self):
        
        if self.citasPorAtender != []:
            resp = 's'
            print('\n------------------------------------')
            print('         * Atencion Cita  *   ')
            print('------------------------------------')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.atencionCit()
                        resp = Leer('Desea atender otra cita? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea atender otra cita? S/N -> ').leerCadena()
        else:
            print('------------------------------------') 
            print('\nNo hay citas disponibles...\n')
            print('------------------------------------') 
            
    def atencionCit(self):
        print('  --- * Atencion en proceso * ---')
        print('------------------------------------')
        print('            --- Citas ---')
        self.visualizarCitas1()
        idCita = Leer('\nDigite el codigo de la cita: ').leerInt()
        if self.buscarCita(idCita):
            cita = self.buscarCita1(idCita)
            cita.trabajador.disponibilidad = True
            factura = Factura(idCita, cita.dueño, cita.servicio, cita)
            cita.dueño.facturas.append(factura)
            self.citasAtendidas.append(cita)
            self.citasPorAtender.remove(cita)
            print('----------------------------------------')
            print('           ¡Cita Atendida!          ')
            print('----------------------------------------\n')
        else:
            print('----------------------------------------')
            print('\nEl codigo digitado no existe...\n')   
            print('----------------------------------------\n')
            
    def visualiarFacturas(self):
        if self.citasAtendidas != []:
            i = 0
            print('\n----------------------------------------')
            print('         * Visualizar Facturas *       ')
            print('----------------------------------------\n')
            for cliente in self.clientes:
                for factura in cliente.facturas:
                    print(f'------------ * Factura {i+1} * -------------')
                    factura.factura()
                    i += 1
            # print('----------------------------------------')
            # print(f'Ventas Totales: {Factura.valorServicios}')
            # print('----------------------------------------')
        else:
            print('----------------------------------------') 
            print('\nNo hay facturas disponibles...\n')
            print('----------------------------------------\n')  
    
    def visualiarFacturaClientes(self):
        if self.citasAtendidas != []:
            resp = 's'
            print('\n----------------------------------------')
            print('           * Facturas Cliente  *   ')
            print('----------------------------------------\n')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.visualizarCitaClie()
                        resp = Leer('Desea ver otras facturas? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea ver otras facturas? S/N -> ').leerCadena()
        else:
            print('----------------------------------------') 
            print('\nNo hay facturas disponibles...\n')
            print('----------------------------------------\n') 
    
    def visualizarCitaClie(self):
        
        self.visualizarClientes1()
        idCliente = Leer('Digite la identificacion del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            cliente.facturasCliente(cliente)   
        else:
            print('----------------------------------------')
            print('\nLa identificación digitada no existe...\n')   
            print('----------------------------------------\n')
        
    def visualiarFacturaServicio(self):
        if self.citasAtendidas != []:
            print('\n----------------------------------------')
            print('         * Facturas Servicios  *   ')
            print('----------------------------------------\n')
            Factura.verFacturasServicio(Factura, self.citasAtendidas)
        else:
            print('------------------------------------') 
            print('\nNo hay facturas disponibles...\n')
            print('------------------------------------') 
    
    def pagarFactura(self):
        
        if self.citasAtendidas != []:
            resp = 's'
            print('\n----------------------------------------')
            print('            * Pago Factura  *   ')
            print('----------------------------------------')
            while True:   
                match resp:
                    case 's' | 'Si' | 'SI' | 'S' | 'si':
                        self.pagoFac()
                        resp = Leer('Desea ver otras facturas? S/N -> ').leerCadena()
                    case 'n' | 'No' | 'NO' | 'N' | 'no':
                        # os.system('pause')
                        break
                    case other:
                        print('\nError: Digite una opción correcta... \n')
                        resp = Leer('Desea ver otras facturas? S/N -> ').leerCadena()
        else:
            print('----------------------------------------') 
            print('\nNo hay facturas disponibles...\n')
            print('----------------------------------------\n')
             
            
    def pagoFac(self):
        
        self.visualizarClientes1()
        idCliente = Leer('Digite la identificacion del cliente: ').leerInt()
        if self.buscarCliente(idCliente):
            cliente = self.buscarCliente1(idCliente)
            cliente.pagarFactura(cliente, self.citasAtendidas)   
        else:
            print('----------------------------------------')
            print('\nLa identificación digitada no existe...\n')   
            print('----------------------------------------\n')