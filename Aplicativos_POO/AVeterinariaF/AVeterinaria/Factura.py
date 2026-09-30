from Servicio import *

class Factura:
    valorServicios = 0
    def __init__(self, numeroFactura, dueño, servicio, cita):
        
        self.dueño = dueño
        self.servicio = servicio
        self.numeroFactura = numeroFactura
        self.valorFactura = servicio.valortotal
        self.cita = cita
        Factura.valorServicios += self.valorFactura
        
    def factura(self):
        print(f'Cita: {self.numeroFactura}\nCliente: {self.dueño.nomCliente}\nServicio: {self.servicio.razonservicio}')
        print('----------------------------------------')
        print(f'Valor: ${self.valorFactura}')
        print('----------------------------------------')
        
    def facturaCliente(self):
        print(f'Cita: {self.numeroFactura}\nCliente: {self.dueño.nomCliente}\nIdentificación: {self.dueño.idCliente}\nContacto: {self.dueño.contacto} \nServicio: {self.servicio.razonservicio}')
        print('----------------------------------------')
        print(f'Valor: ${self.valorFactura}')
        print('----------------------------------------')
     
    def verFacturasServicio(self, listaCitas):
        print(f'--- * Facturas Servicios Médicos * ---')
        for cita in listaCitas:
            for facturas in cita.dueño.facturas:
                if isinstance(cita.servicio, ServivioMedico):
                    facturas.factura()
        print(f'--- * Facturas Servicios Esteticos * ---')
        for cita in listaCitas:
            for facturas in cita.dueño.facturas:
                if isinstance(cita.servicio, ServicioEstetico):
                    facturas.factura()
                