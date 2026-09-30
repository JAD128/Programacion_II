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
        
    def adicionarDocente(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    usuario = self.adicionarDocen()
                    if usuario != None:
                        self.usuarios.append(usuario)
                        print('  ¡Docente adicionado exitosamente!   ')
                        print('----------------------------------------')
                    resp = Leer('\nDesea adicionar a otro docente? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro docente? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
    
    def adicionarDocen(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Docente *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite el codigo del docente: ').leerInt()
        if not self.buscarUsuario(codigo):
            nombre = Leer('Digite el nombre del docente: ').leerCadena()
            print('----------------------------------------')
            print(f'Tipo de Docente: \n1. Tiempo Completo\n2. Hora Catedra \n3. Servicios Prestados')
            print('----------------------------------------')
            tipo = Leer('\nDigite el tipo de docente: ').leerInt()
            while True:
                match tipo:
                    case 1: 
                        print('\n----------------------------------------')
                        user = Docente(nombre, codigo, tipo)
                        return user
                    case 2:
                        print('\n----------------------------------------')
                        user = Docente(nombre, codigo, tipo)
                        return user
                    case 3:
                        print('\n----------------------------------------')
                        user = Docente(nombre, codigo, tipo)
                        return user
                    case other:
                        print('\nError: Digite una opción valida...\n')
                        print('\n----------------------------------------')
                        tipo = Leer('\nDigite el tipo de docente: ').leerInt()       
        else:
            print('\nEl codigo del docente ya existe...')
    
    def buscarUsuario(self, cod):
       
        for user in self.usuarios:
            if user.codUsuario == cod:
                return True
        return False
    
    def buscarUsuario1(self, cod):
       
        for user in self.usuarios:
            if user.codUsuario == cod:
                return user
        return None
                    
    def adicionarTrabajador(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    usuario = self.adicionarTraba()
                    if usuario != None:
                        self.usuarios.append(usuario)
                        print('  ¡Trabajador adicionado exitosamente!  ')
                        print('----------------------------------------')
                    resp = Leer('\nDesea adicionar a otro trabajador? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro trabajador? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
                    
    def adicionarTraba(self):
        print('\n----------------------------------------')
        print('        * Adicionar Trabajador *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite el codigo del trabajador: ').leerInt()
        if not self.buscarUsuario(codigo):
            nombre = Leer('Digite el nombre del trabajador: ').leerCadena()
            print('----------------------------------------')
            print(f'Tipo de trabajador: \n1. Vinculado \n2. Servicios Prestados ')
            print('----------------------------------------')
            tipo = Leer('\nDigite el tipo de trabajador: ').leerInt()
            while True:
                match tipo:
                    case 1: 
                        print('\n----------------------------------------')
                        user = Trabajador(nombre, codigo, tipo)
                        return user
                    case 2:
                        print('\n----------------------------------------')
                        user = Trabajador(nombre, codigo, tipo)
                        return user
                    case other:
                        print('\nError: Digite una opción valida...')
                        print('\n----------------------------------------')
                        tipo = Leer('\nDigite el tipo de trabajador: ').leerInt()       
        else:
            print('\nEl codigo del trabajador ya existe...')
   
    def adicionarEstudiante(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    os.system('cls')
                    usuario = self.adicionarEst()
                    if usuario != None:
                        self.usuarios.append(usuario)
                        print('  ¡Estudiante adicionado exitosamente!   ')
                        print('----------------------------------------')
                    resp = Leer('\nDesea adicionar a otro estudiante? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro estudiante? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
    
    def adicionarEst(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Estudiante *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite el codigo del estudiante: ').leerInt()
        if not self.buscarUsuario(codigo):
            nombre = Leer('Digite el nombre del estudiante: ').leerCadena()
            print('----------------------------------------')
            user = Estudiante(nombre, codigo)
            return user
        else:
            print('\nEl codigo del estudiante ya existe...')
     
    #Ver la adicion de usuarios, ver si lo puedo controlar con el isinstrance
           
    def consultarDocente(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarUser()
                        resp = Leer('\nDesea consultar a otro docente? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea consultar a otro docente? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def consultarDocen(self):
        
        print('\n----------------------------------------')
        print('       * Consultar Docente *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el codigo del docente que desea consultar: ').leerInt()
        if self.buscarUsuario(cod):
            user = self.buscarUsuario1(cod)
            if isinstance(user,Docente):
                print('\n----------------------------------------')
                user.usuario()
                print('----------------------------------------')
            else:
                print('\nEl codigo dijitado no corresponde a un docente...')
        else:
            print('\nEl codigo digitado no existe...')
    
    def consultarTrabajador(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarTraba()
                        resp = Leer('\nDesea consultar a otro trabajador? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea consultar a otro trabajador? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def consultarTraba(self):
        
        print('\n----------------------------------------')
        print('       * Consultar Trabajador *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el codigo del trabajador que desea consultar: ').leerInt()
        if self.buscarUsuario(cod):
            user = self.buscarUsuario1(cod)
            if isinstance(user,Trabajador):
                print('\n----------------------------------------')
                user.usuario()
                print('----------------------------------------')
            else:
                print('\nEl codigo dijitado no corresponde a un trabajador...')
        else:
            print('\nEl codigo digitado no existe...')
            
    def consultarEstudiante(self):
        
        if self.usuarios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        os.system('cls')
                        self.consultarEst()
                        resp = Leer('\nDesea consultar a otro estudiante? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea consultar a otro estudiante? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def consultarEst(self):
        
        print('\n----------------------------------------')
        print('       * Consultar Estudiante *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el codigo del estudiante que desea consultar: ').leerInt()
        if self.buscarUsuario(cod):
            user = self.buscarUsuario1(cod)
            if isinstance(user,Estudiante):
                print('\n----------------------------------------')
                user.usuario()
                print('----------------------------------------')
            else:
                print('\nEl codigo dijitado no corresponde a un estudiante...')
        else:
            print('\nEl codigo digitado no existe...')
            
    def visualizarDocentes(self):
        
        if self.usuarios != []:
            print('----------------------------------------')
            print('        * Docentes Central *         ')
            print('----------------------------------------')
            Docente.visualizarUsuarios(Docente,self.usuarios)
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def visualizarEstudiantes(self):
        
        if self.usuarios != []:
            print('----------------------------------------')
            print('        * Estudiantes Central *         ')
            print('----------------------------------------')
            Estudiante.visualizarUsuarios(Estudiante,self.usuarios)
        else:
            print('\nNo hay usuarios en la central...\n')
    
    def visualizarTrabajadores(self):
        
        if self.usuarios != []:
            print('----------------------------------------')
            print('       * Trabajadores Central *         ')
            print('----------------------------------------')
            Trabajador.visualizarUsuarios(Trabajador,self.usuarios)
        else:
            print('\nNo hay usuarios en la central...\n')
        
    def visualizarUsuarios(self):
        self.visualizarEstudiantes()
        self.visualizarDocentes()
        self.visualizarTrabajadores()
            
    def prestarRecurso(self):
        
        print('\n----------------------------------------')
        print('       * Prestamo de recursos *         ')
        print('----------------------------------------\n')
        if self.recursos != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.visualizarUsuarios()
                        idUsuario = Leer('\nDigite el codigo del usuario: ').leerInt()
                        if self.buscarUsuario(idUsuario):
                            user = self.buscarUsuario1(idUsuario)
                            user.prestamosUsuario(self.recursos, user)
                        else:
                            print('\nEl codigo digitado no existe...')
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
        
    def prestamosUsuarios(self):
        
        if self.usuarios != []:
            print('\n----------------------------------------')
            print('         * Prestamos Central *         ')
            print('----------------------------------------\n')
            for user in self.usuarios:
                print('--------------* usuario *---------------')
                user.usuario()
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
        self.visualizarUsuarios()
        codUser = Leer('\nDigite el codigo del usuario: ').leerInt()
        if self.buscarUsuario(codUser):
            user = self.buscarUsuario1(codUser)
            print('\n-------------* Usuario *-------------')
            user.usuarioSencillo()
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
                        self.visualizarUsuarios()
                        idUsuario = Leer('\nDigite el codigo del usuario: ').leerInt()
                        if self.buscarUsuario(idUsuario):
                            user = self.buscarUsuario1(idUsuario)
                            user.devolucionRecurso(self.recursos, user)
                        else:
                            print('\nEl codigo digitado no existe...')
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
            
