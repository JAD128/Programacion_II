from Leer import *
from datetime import datetime
# from Cita import *

class Servicio:
    def __init__(self, razonservicio, valortotal, idServicio):
        self.idServicio = idServicio
        self.razonservicio = razonservicio
        self.valortotal = valortotal
        
    def servicio(self):
        pass
    
    def visualizarServicio(self):
        pass
    
class ServivioMedico(Servicio):

    def __init__(self, razonservicio, valortotal, idServicio):
        super().__init__(razonservicio, valortotal, idServicio)
    
    def servicio(self):
        print(f'Servicio médico: {self.razonservicio}\nCodigo Servicio: {self.idServicio} \nValor del servicio: {self.valortotal}')
        print('----------------------------------------')
    
    
class ServicioEstetico(Servicio):

    def __init__(self, razonservicio, valortotal, idServicio):
        super().__init__(razonservicio, valortotal, idServicio)

    def servicio(self):
        print(f'Servicio estetico: {self.razonservicio}\nCodigo Servicio: {self.idServicio} \nValor del servicio: {self.valortotal}')
        print('----------------------------------------')
        