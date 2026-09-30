class Citas:
    def __init__(self, idcita, fecha, idCliente, mascota, trabajador, servicio, costo):
        
        self.idCita = idcita
        self.fecha = fecha
        self.idCliente = idCliente
        self.mascota = mascota
        self.trabajador = trabajador
        self.servicio = servicio
        self.costo =costo

    # def __str__(self):
    #     return(f' Identificación del paciente: {self.id_paciente} - Hora: {self.hora} - Fecha: {self.fecha}  - Trabajador: {self.trabajador}  -  Razón: {self.razon}')
        
        # def agendarcita(self,hora):
        #     if self.citasprogramadas(hora):
        #         pass
