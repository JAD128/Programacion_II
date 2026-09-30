from Leer import *
from Central import *

class Usuario:
    
    def __init__(self, nomUsuario, codUsuario):
        
        self.nomUsuario = nomUsuario
        self.codUsuario = codUsuario
        self.prestamos = []
    
    def usuario(self):
        print(f'Nombre: {self.nomUsuario}\nCodigo: {self.codUsuario}')
    
    def visualizarUsuarios(self, usuarios):
        pass
    
    def prestamosUsuario(self, recursos, user):
        pass
    
    def buscarRecurso1(sefl, codigo, recursos):
        for rec in recursos:
            if rec.codigo == codigo:
                return rec
    
    def buscarRecurso(sefl, codigo, recursos):
        for rec in recursos:
            if rec.codigo == codigo:
                return True
        else:
            return False
        
    def mostrarRecursos(self, recursos):
        print('\n----------------------------------------')
        print('          * Recursos Central  *         ')
        print('----------------------------------------')
        for rec in recursos:
            print(rec.recurso())
            print('----------------------------------------')
    
    def devolucionRecurso(self, codidoRecurso, recursos, codUsuario, usuario):
        pass
    
    def usuarioSencillo(self):
        print(f'Nombre: {self.nomUsuario}\nCodigo: {self.codUsuario}')
    
class Estudiante(Usuario):
    
    def __init__(self, nomEstudiante, codEstudiante):
        
        super().__init__(nomEstudiante, codEstudiante)
        
    def visualizarUsuarios(self, usuarios):
        for estudiantes in usuarios:
            if isinstance(estudiantes, Estudiante):
                estudiantes.usuario()
                print('----------------------------------------') 
    
    def prestamosUsuario(self, recursos, user):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea pedir: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            if rec.estado:
                rec.estado = False
                user.prestamos.append(rec)
                print('\n--------- ¡Prestamo Realizado! ---------')           
            else:
                print('\nEl recurso no esta disponible...\n')
        else:
            print('\nEl codigo digitado no existe...\n')  
    
    def devolucionRecurso(self, recursos, usuario):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea devolver: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            rec.estado = True
            usuario.prestamos.remove(rec)
            print('\n--------- ¡Devolución Realizada! ---------')        
        else:
            print('\nEl codigo digitado no coincide con ningun recurso...\n')
               
class Docente(Usuario):
    
    def __init__(self, nomDocente, codDocente, tipoDocente):
        
        super().__init__(nomDocente, codDocente)
        self.tipoDocente = tipoDocente
    
    def usuario(self):
        super().usuario()
        if self.tipoDocente == 1:
            tipo = 'Tiempo Completo'
        elif self.tipoDocente == 2:
            tipo = 'Hora Catedrá'
        elif self.tipoDocente == 3:
            tipo = 'Servicios Prestados'
        print(f'Tipo Docente: {tipo}')
    
    def visualizarUsuarios(self, usuarios):
        for docentes in usuarios:
            if isinstance(docentes, Docente):
                docentes.usuario()
                print('----------------------------------------') 
    
    def prestamosUsuario(self, recursos, user):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea pedir: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            if rec.estado:
                if len(user.prestamos) < 2:
                    rec.estado = False
                    user.prestamos.append(rec)
                    print('\n--------- ¡Prestamo Realizado! ---------')
                else:
                    print('\nEl docente no puede pedir mas recursos...')           
            else:
                print('\nEl recurso no esta disponible...\n')
        else:
            print('\nEl codigo digitado no coincide con ningun recurso...\n')
    
    def devolucionRecurso(self, recursos, usuario):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea devolver: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            rec.estado = True
            usuario.prestamos.remove(rec)
            print('\n--------- ¡Devolución Realizada! ---------')        
        else:
            print('\nEl codigo digitado no coincide con ningun recurso...\n')
                
class Trabajador(Usuario):
    
    def __init__(self, nomTrabajador, codTrabajador, tipoTrabajador):
        
        super().__init__(nomTrabajador, codTrabajador)
        self.tipoTrabajador = tipoTrabajador
    
    def usuario(self):
        super().usuario()
        if self.tipoTrabajador == 1:
            tipo = 'Vinculado'
        elif self.tipoTrabajador == 2:
            tipo = 'Servicios Prestados'
        print(f'Tipo Trabajador: {tipo}')
    
    def visualizarUsuarios(self, usuarios):
        for trabajadores in usuarios:
            if isinstance(trabajadores, Trabajador):
                trabajadores.usuario()
                print('----------------------------------------') 
    
    def prestamosUsuario(self, recursos, user):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea pedir: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            if rec.estado:
                if len(user.prestamos) < 3:
                    rec.estado = False
                    user.prestamos.append(rec) 
                    print('\n--------- ¡Prestamo Realizado! ---------')  
                else:
                    print('\nEl trabajdor no puede pedir mas recursos...\n')             
            else:
                print('\nEl recurso no esta disponible...\n')
        else:
            print('\nEl codigo digitado no existe...\n')
    
    def devolucionRecurso(self, recursos, usuario):
        
        self.mostrarRecursos(recursos)
        codRec = Leer('\nIngrese el codigo del recurso que desea devolver: ').leerInt()
        if self.buscarRecurso(codRec, recursos):
            rec = self.buscarRecurso1(codRec,recursos)
            rec.estado = True
            usuario.prestamos.remove(rec)
            print('\n--------- ¡Devolución Realizada! ---------')        
        else:
            print('\nEl codigo digitado no coincide con ningun recurso...\n')
