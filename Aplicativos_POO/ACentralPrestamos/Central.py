from Usuario import *
from Recurso import *
from Leer import *
import os

class Central:
    
    def __init__(self):
        
        self.usuarios = []
        self.recursos = []
    
    def adicionarRecurso(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    rec = self.adicionarRec()
                    if rec != None:
                        self.recursos.append(rec)
                        print('    ¡Recurso adicionado exitosamente!   ')
                        print('----------------------------------------')
                    resp = Leer('\nDesea añadir otro recurso? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea añadir otro recurso? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
                    
    def adicionarRec(self):
        
        print('\n----------------------------------------')
        print('         * Adicionar recurso *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite el codigo del recurso: ').leerInt()
        if not self.buscarRecurso(codigo):
            nombre = Leer('Digite el nombre del recurso: ').leerCadena()
            print('\n----------------------------------------')
            recurso = Recurso(nombre, codigo)
            return recurso
        else:
            print('\nEl recurso ya existe...\n')
        
    
    def buscarRecurso(sefl, codigo):
        
        for rec in sefl.recursos:
            if rec.codigo == codigo:
                return True
        else:
            return False
        
    def buscarRecurso1(sefl, codigo):
        
        for rec in sefl.recursos:
            if rec.codigo == codigo:
                return rec
        
    def consultarRecurso(self):
        if self.recursos != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarRec()
                        resp = Leer('\nDesea añadir otro recurso? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea añadir otro recurso? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay recursos en  la central...\n')
    
    def consultarRec(self):
        
        print('\n----------------------------------------')
        print('         * Consultar recurso *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el codigo del recurso que desea consultar: ').leerInt()
        if self.buscarRecurso(cod):
            print('\n----------------------------------------')
            print(self.buscarRecurso1(cod))
            print('----------------------------------------')
        else:
            print('\nEl codigo ingresado no corresponde a ningun recurso...')
    
    def mostrarRecursos(self):
        
        if self.recursos != []:
            print('\n----------------------------------------')
            print('          * Recursos Central  *         ')
            print('----------------------------------------')
            for rec in self.recursos:
                print(rec.recurso())
                print('----------------------------------------')
        else:
            print('\nNo hay recursos en  la central...\n')
        
    def adicionarUsuario(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    usuario = self.adicionarUser()
                    if usuario != None:
                        self.usuarios.append(usuario)
                        print('  ¡Usuario adicionado exitosamente!   ')
                        print('----------------------------------------')
                    resp = Leer('\nDesea adicionar a otro usuario? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro usuario? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
    
    def buscarUsuario(self, cod):
       
        for user in self.usuarios:
            if user.codigo == cod:
                return True
        return False
    
    def buscarUsuario1(self, cod):
       
        for user in self.usuarios:
            if user.codigo == cod:
                return user
        return None
            
    def adicionarUser(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Usuario *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite el codigo del usuario: ').leerInt()
        if not self.buscarUsuario(codigo):
            nombre = Leer('Digite el nombre del usuario: ').leerCadena()
            print('----------------------------------------')
            print(f'Tipos de usuarios: \n1. Estudiante\n2. Docente\n3. Trabajador')
            print('----------------------------------------')
            tipo = Leer('\nDigite el tipo de usuarios: ').leerInt()
            print('\n----------------------------------------')
            user = Usuario(nombre, codigo, tipo)
            return user
        else:
            print('\nEl codigo del usuario ya existe...')
            
    def consultarUsuario(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarUser()
                        resp = Leer('\nDesea adicionar a otro usuario? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea adicionar a otro usuario? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def consultarUser(self):
        
        print('\n----------------------------------------')
        print('        * Consultar usuario *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el codigo del usuario que desea consultar: ').leerInt()
        if self.buscarUsuario(cod):
            print('\n----------------------------------------')
            print(self.buscarUsuario1(cod))
            print('----------------------------------------')
        else:
            print('\nEl codigo digitado no existe...')
    
    def mostrarUsuarios(self):
        
        if self.usuarios != []:
            print('----------------------------------------')
            print('        * Usuarios Central *         ')
            print('----------------------------------------')
            for user in self.usuarios:
                print(user)
                print('----------------------------------------')
        else:
            print('\nNo hay usuarios en la central...\n')
            
    def prestarRecurso(self):
        
        if self.recursos != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.prestRecurso()
                        resp = Leer('\nDesea prestar otro recurso? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea prestar otro recurso? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay recursos en la central...\n')
            
    def prestRecurso(self):
        
        self.mostrarUsuarios()
        cod = Leer('\nIngrese el codigo del usuario: ').leerInt()
        if self.buscarUsuario(cod):
            self.mostrarRecursos()
            codRec = Leer('\nIngrese el codigo del recurso que desea pedir: ').leerInt()
            rec = self.buscarRecurso1(codRec)
            if rec.estado:
                user = self.buscarUsuario1(cod)
                if user.tipo == 1:
                    rec.estado = False
                    user.prestamos.append(rec)
                    print('\n--------- ¡Prestamo Realizado! ---------')
                if user.tipo == 2:
                    if len(user.prestamos) < 2:
                        rec.estado = False
                        user.prestamos.append(rec)
                        print('\n--------- ¡Prestamo Realizado! ---------')
                    else:
                        print('\nEl usuario no puede pedir mas recursos...')
                if user.tipo == 3:
                    if len(user.prestamos) < 1:
                        rec.estado = False
                        user.prestamos.append(rec) 
                        print('\n--------- ¡Prestamo Realizado! ---------')  
                    else:
                        print('\nEl usuario no puede pedir mas recursos...\n')             
            else:
                print('\nEl recurso no esta disponible...\n')
        else:
            print('\nEl codigo digitado no existe...\n')
        
    def prestamosUsuarios(self):
        
        if self.usuarios != []:
            print('\n----------------------------------------')
            print('         * Prestamos Central *         ')
            print('----------------------------------------\n')
            for user in self.usuarios:
                print('--------------* usuario *---------------')
                print(user)
                print('---------* Recursos prestados *---------')
                if user.prestamos != []:
                    for rec in user.prestamos:
                        print(f'{rec}')
                    print('----------------------------------------\n')
                else:
                    print('\nEl usuario no tiene recursos prestados...\n')
                    print('----------------------------------------\n')            
        else:
            print('\nNo hay usuarios en la central...\n')         
                
    def prestamoUsuario(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.prestUsuario()
                        resp = Leer('\nDesea visualizar los prestamos de otro usuario? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea visualizar los prestamos de otro usuario? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
            
        
    def prestUsuario(self):
        
        print('\n----------------------------------------')
        print('         * Prestamos Usuario *         ')
        print('----------------------------------------\n')
        self.mostrarUsuarios()
        codUser = Leer('\nDigite el codigo del usuario: ').leerInt()
        if self.buscarUsuario(codUser):
            user = self.buscarUsuario1(codUser)
            print('\n-------------* Usuario *-------------')
            print(user)
            if user.prestamos != []:
                print('---------* Recursos prestados *---------')
                for rec in user.prestamos:
                    print(rec)
                    print('----------------------------------------')
            else:
                print('----------------------------------------')
                print('\nEl usuario no tiene recursos prestados...\n')
                print('----------------------------------------')
        else:
            print('\nEl codigo del usuario no existe...\n')
            
    def devolucionRecurso(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.devRecurso()
                        resp = Leer('\nDesea regresar otro recurso? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea regresar otro recurso? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
            
    def devRecurso(self):
        
        print('\n----------------------------------------')
        print('       * Devolucion de recursos *         ')
        print('----------------------------------------\n')
        self.mostrarUsuarios()
        codUser = Leer('\nDigite el codigo del usuario: ').leerInt()
        os.system('cls')
        if self.buscarUsuario(codUser):
            user = self.buscarUsuario1(codUser)
            print('----------------------------------------')
            if user.prestamos != []:
                print('\n-------------* Usuario *-------------')
                print(user)
                print('---------* Recursos prestados *---------')
                for rec in user.prestamos:
                    print(rec)
                    print('----------------------------------------')
                codRec = Leer('\nDigite el codigo del recurso que desea regresar: ').leerInt()
                if self.buscarRecurso(codRec):
                    rec = self.buscarRecurso1(codRec)
                    rec.estado = True
                    user.prestamos.remove(rec)
                    print('\n---------* Recurso regresado *---------')
                else:
                    print('\nEl codigo ingresado no existe...\n')
            else:
                print('\nEl usuario no tiene recursos prestados...\n')
                print('----------------------------------------')
        else:
            print('\nEl codigo del usuario no existe...\n')    