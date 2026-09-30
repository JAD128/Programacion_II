class Trabajador:
    def __init__(self, nombre, sexo, id, salario):
        self.nombre = nombre
        self.sexo=sexo
        self.id = id
        self.salario = salario
        self.disponibilidad = True
        
    def visualizarTrabajador(self):
        pass
    
    def verTrabajador(self):
        pass
    
    def trabajador(self):
        pass
    
class Veterinario(Trabajador):
    def __init__(self, nombre, sexo, id, salario):
        super().__init__(nombre, sexo, id, salario)

    def visualizarTrabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print(f'Nombre Veterinario: {self.nombre}\nIdentificación: {self.id}\nSexo: {self.sexo}\nSalario: ${self.salario}\nEstado: {estado}')
        print('----------------------------------------')
        
    def verTrabajador(self):
        print(f'Nombre Veterinario: {self.nombre}\nIdentificación: {self.id}')
        print('----------------------------------------')
        
    def trabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print(f'Nombre Veterinario: {self.nombre}\nIdentificación: {self.id}\nEstado: {estado}')
        print('----------------------------------------')

class Enfermero(Trabajador):
    def __init__(self, nombre, sexo, id, salario):
        super().__init__(nombre, sexo, id, salario)
        
    def visualizarTrabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print (f'Nombre Enfermero: {self.nombre}\nIdentificación: {self.id}\nSexo: {self.sexo}\nSalario: ${self.salario}\nEstado: {estado}')
        print('----------------------------------------')
        
    def verTrabajador(self):
        print(f'Nombre Enfermero: {self.nombre}\nIdentificación: {self.id}')
        print('----------------------------------------')
        
    def trabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print(f'Nombre Enfermero: {self.nombre}\nIdentificación: {self.id}\nEstado: {estado}')
        print('----------------------------------------')
        
class Esteticista(Trabajador):

    def __init__(self, nombre, sexo, id, salario):
        super().__init__(nombre, sexo, id, salario)

    def visualizarTrabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print (f'Nombre Esteticista: {self.nombre}\nIdentificación: {self.id}\nSexo: {self.sexo}\nSalario: ${self.salario}\nEstado: {estado}')
        print('----------------------------------------')
    
    def verTrabajador(self):
        print(f'Nombre Esteticista: {self.nombre}\nIdentificación: {self.id}')
        print('----------------------------------------')
        
    def trabajador(self):
        if self.disponibilidad == True:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        print(f'Nombre Esteticista: {self.nombre}\nIdentificación: {self.id}\nEstado: {estado}')
        print('----------------------------------------')