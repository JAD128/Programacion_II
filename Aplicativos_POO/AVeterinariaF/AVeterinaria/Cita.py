from Servicio import *

class Cita:
      
    def __init__(self, idCita, fechaCita, trabajador, paciente, dueño, servicio):
        self.fechaCita = fechaCita
        self.idCita = idCita
        self.trabajador = trabajador
        self.paciente = paciente
        self.dueño = dueño
        self.servicio = servicio
    
    def cita(self):
        print(f'Cita: {self.idCita}\nFecha: {self.fechaCita} \nServicio: {self.servicio.razonservicio}\nEncargado: {self.trabajador.nombre}\nPaciente: {self.paciente.nombre}')
        print('------------------------------------') 
        
    def citas(self):
        print(f'Cita: {self.idCita}\nFecha: {self.fechaCita} \nServicio: {self.servicio.razonservicio}')
        print('------------------------------------') 
                
            