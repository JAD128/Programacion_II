class Mascota:
    
    def __init__(self, nombre,especie, idMascota ,edad, sexo, raza, peso):
       
        self.nombre = nombre
        self.especie = especie
        self.edad=edad
        self.id = idMascota
        self.sexo = sexo
        self.raza = raza
        self.peso = peso
        
    def __str__(self):
        return (f'Nombre Paciente: {self.nombre} \nIdentificación Paciente: {self.id} \nEspecie Paciente: {self.especie} \Raza Paciente: {self.raza} \nEdad Paciente: {self.edad} años \nPeso Paciente: {self.peso} Kg')

    def visualizarMascota(self):
        print(f'Nombre Paciente: {self.nombre} \nIdentificación Paciente: {self.id}')
        print('----------------------------------------')
    