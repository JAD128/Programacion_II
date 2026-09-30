from Usuario import *
from Recurso import *
from Leer import *
import os

class Central:
    
    def __init__(self):
        
        self.usuarios = []
        self.recursos = []
    
    def Agregarrecurso(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    rec = self.adicionarRec()
                    if rec != None:
                        self.recursos.append(rec)
                        print('****************************************')
                        print('|    EL RECURSO HA SIDO AGREGADO CORRECTAMENTE  |')
                        print('****************************************')
                    resp = Leer('\nDesea agregar otro recurso? si/no *> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digitar un valor valido...')
                    resp = Leer('\nDesea agregar otro recurso? si/no*> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
                    
    def adicionarRec(self):
        
        print('\n****************************************')
        print('|          Adicionar recurso           |')
        print('****************************************')
        codigo = Leer('\nDigitar el codigo del recurso: ').leerInt()
        if not self.busquedarecur(codigo):
            nombre = Leer('Digitar el nombre del recurso: ').leerCadena()
            print('\n****************************************')
            recurso = Recurso(nombre, codigo)
            return recurso
        else:
            print('\nya existe este recurso...\n')
        
    
    def busquedarecur(sefl, codigo):
        
        for rec in sefl.recursos:
            if rec.codigo == codigo:
                return True
        else:
            return False
        
    def busquedarecur1(sefl, codigo):
        
        for rec in sefl.recursos:
            if rec.codigo == codigo:
                return rec
        
    def Recursoaconsultar(self):
        if self.recursos != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarRec()
                        resp = Leer('\nDeseas agregar otro recurso? si/no *> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: agregue un valor valido...')
                        resp = Leer('\nDeseas agregar otro recurso? si/no*> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNO SE ENCUENTRA EL RECURSO SOLICITADO...\n')
    
    def consultarRec(self):
        
        print('\n****************************************')
        print('|        recurso a consultar            |')
        print('******************************************')
        cod = Leer('\nfAVOR DIGITE EL RECURSO A CONSULTAR EN LA CENTRAL: ').leerInt()
        if self.busquedarecur(cod):
            print('\n****************************************')
            print(self.busquedarecur1(cod))
            print('****************************************')
        else:
            print('\nEL CODIGO INGRESADO NO HACE PARTE DE NINGUN RECURSO...')
    
    def mostrarRecursos(self):
        
        if self.recursos != []:
            print('\n****************************************')
            print('|           Recursos Central           |')
            print('****************************************')
            for rec in self.recursos:
                print(rec.recurso())
                print('****************************************')
        else:
            print('\nNO HAY RECURSO EN LA CENTRAL...\n')
        
    def adicionarUsuario(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    usuario = self.adicionarUser()
                    if usuario != None:
                        self.usuarios.append(usuario)
                        print('  ¡EL USUARIO HA SIDO ASIGNADO!   ')
                        print('****************************************')
                    resp = Leer('\nDESEA ADICIONAR UN NUEVO USUARIO? si/no *> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDESEA ADICIONAR UN NUEVO USUARIO? si/no*> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
    
    def buscarUsuario(self, cod):
       
        for user in self.usuarios:
            if user.codigo == cod:
                return True
        return False
    
    def buscarUsuario1(self, cod):
       
        for est in self.usuarios:
            if est.codigo == cod:
                return est
        return None
            
    def adicionarUser(self):
        
        print('\n***************************************')
        print('|        * Adicionar Usuario *         |')
        print('****************************************')
        codigo = Leer('\nDigite el codigo del usuario: ').leerInt()
        if not self.buscarUsuario(codigo):
            nombre = Leer('Digite el nombre del usuario: ').leerCadena()
            print(f'Tipos de usuarios: \n1. estudiante\n2. Docente\n3. Trabajador')
            tipo = Leer('Digite el tipo de usuarios: ').leerInt()
            print('\n****************************************')
            user = Usuario(nombre, codigo, tipo)
            return user
        else:
            print('\nEl codigo del USUARIO ya existe...')
            
    def consultarUsuario(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.USUARIOAMOSTRARr()
                        resp = Leer('\nDesea adicionar a otro usuario? si/no *> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea adicionar a otro usuario? si/no*> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def USUARIOAMOSTRARr(self):
        
        print('\n****************************************')
        print('|         Consultar usuario            |')
        print('****************************************')
        cod = Leer('\nDigite el codigo del usuario que desea consultar: ').leerInt()
        if self.buscarUsuario(cod):
            print('\n****************************************')
            print(self.buscarUsuario1(cod)                )
            print('****************************************')
        else:
            print('\nEl codigo digitado no existe...')
    
    def USUARIOAMOSTRAR(self):
        
        if self.usuarios != []:
            print('****************************************')
            print('|         Usuarios Central             |')
            print('****************************************')
            for est in self.usuarios:
                print(est)
                print('****************************************')
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
                        resp = Leer('\nDesea prestar otro recurso? si/no *> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea prestar otro recurso? si/no*> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay recursos en la central...\n')
            
    def prestRecurso(self):
        
        self.USUARIOAMOSTRAR()
        cod = Leer('\nIngrese el codigo del usuario: ').leerInt()
        if self.buscarUsuario(cod):
            self.mostrarRecursos()
            codRec = Leer('\nIngrese el codigo del recurso que desea pedir: ').leerInt()
            rec = self.busquedarecur1(codRec)
            if rec.estado:
                user = self.buscarUsuario1(cod)
                if user.tipo == 1:
                    rec.estado = False
                    print('\n********* ¡Prestamo Realizado! *********')
                    user.prestamos.append(rec)
                if user.tipo == 2:
                    if len(user.prestamos) < 2:
                        rec.estado = False
                        print('\n********* ¡Prestamo Realizado! *********')
                        user.prestamos.append(rec)
                    else:
                        print('\nError, solo se pueden prestar 2 recursos a un usuario.\n')
                    
                if user.tipo == 3:
                    if len(user.prestamos) < 1:
                        rec.estado = False
                        print('\n********* ¡Prestamo Realizado! *********')
                        user.prestamos.append(rec)  
                    else:
                        print('\nError, solo se pueden prestar 1 recursos a un usuario.\n')              
               
            else:
                print('\nEl recurso no esta disponible...\n')
        else:
            print('\nEl codigo digitado no existe...\n')
        
    def prestamosUsuarios(self):
        
        if self.usuarios != []:
            print('\n****************************************')
            print('|        * Prestamos Central           |')
            print('****************************************\n')
            for user in self.usuarios:
                print('************** usuario **************')
                print(user)
                print('********** Recursos prestados **********')
                if user.prestamos != []:
                    for rec in user.prestamos:
                        print(f'{rec}')
                    print('****************************************\n')
                else:
                    print('\nACTUALMENTE EL USUARIO NO CUENTA CON UN RECURSO PRESTADO...\n')
                    print('****************************************\n')
                    
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
                        resp = Leer('\nDeseas visualizar los prestamoss de otros usuarios? si/no *> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDeseas visualizar los prestamos de otros usuarios? si/no*> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo se encuentra usuarios en la central...\n')
            
        
    def prestUsuario(self):
        
        print('\n****************************************')
        print('|         * Prestamos Usuario *        |')
        print('****************************************\n')
        self.USUARIOAMOSTRAR()
        codEst = Leer('\nDigitar el codigo del usuario: ').leerInt()
        if self.buscarUsuario(codEst):
            user = self.busquedarecur1(codEst)
            print('\n************** usuario **************')
            print(user)
            if user.prestamos != []:
                print('********** Recursos prestados **********')
                for rec in user.prestamos:
                    print(rec)
                    print('****************************************')
            else:
                print('****************************************')
                print('\nEl usuario no presenta recursos prestados...\n')
                print('****************************************')
        else:
            print('\nEl codigo del usuario no se encuentra...\n')
            
    def devolucionRecurso(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.devRecurso()
                        resp = Leer('\nDeseas devolver otro recurso? si/no *> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: ingrese un valor valido...')
                        resp = Leer('\nDeseas devolver otro recurso? si/no*> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
            
    def devRecurso(self):
        
        print('\n****************************************')
        print('|      * Devolucion de recursos *       |')
        print('****************************************\n')
        self.USUARIOAMOSTRAR()
        codEst = Leer('\nDigitar el codigo del usuario: ').leerInt()
        os.system('cls')
        if self.buscarUsuario(codEst):
            user = self.buscarUsuario1(codEst)
            if user.prestamos != []:
                print('\n************** Usuario **************')
                print(user)
                print('********** Recursos prestados **********')
                for rec in user.prestamos:
                    print(rec)
                    print('****************************************')
                codRec = Leer('\nDigitar el codigo del recurso que desea regresar: ').leerInt()
                if self.busquedarecur(codRec):
                    rec = self.busquedarecur1(codRec)
                    rec.estado = True
                    user.prestamos.remove(rec)
                    print('\n********** Recurso ha sido regresado **********')
                else:
                    print('\nEl codigo ingresado no existe...\n')
            else:
                print('****************************************')
                print('\nEl usuario no tiene recursos prestados...\n')
                print('****************************************')
        else:
            print('\nEL CODIGO DEL SUARIO NO SE ENCUENTRA O NO EXISTE...\n')
        
        
        
        
                
        
    