from Leer import *
class Cliente:

    def __init__(self, idCliente, nomCliente, contacto):

        self.idCliente = idCliente
        self.nomCliente = nomCliente
        self.contacto = contacto
        self.mascotas = []
        self.facturas = []

    def __str__(self):

        return(f'Identificacion: {self.idCliente}\nNombre: {self.nomCliente}\nContacto: {self.contacto}')
    
    def cliente(self):
        print(f'Identificación Cliente: {self.idCliente}\nNombre Cliente: {self.nomCliente}')
        print('----------------------------------------')
    
    def pagarFactura(self, cliente, citasAtendidas):
        if cliente.facturas != []:
            valorTotalNeto = 0
            i = 0
            print('------------- * Facturas * -------------\n')
            for facturas in cliente.facturas:
                print(f'------------ * Factura {i+1} * -------------')
                facturas.factura()
                valorTotalNeto += facturas.valorFactura
                i += 1
            print(f'Valor Total: {valorTotalNeto}') 
            print('----------------------------------------')
            opc = Leer('Digite el numero de la factura que desea pagar: ').leerInt()
            while True:
                if opc <= len(cliente.facturas):
                    for i in range(len(cliente.facturas)):
                        if i == opc -1:
                            citasAtendidas.remove(facturas.cita)
                            cliente.facturas.remove(cliente.facturas[i-1])
                            print('----------------------------------------')
                            print('           * Factura Pagada *         ')
                            print('----------------------------------------')
                            return
                else:
                    print('----------------------------------------')
                    print('\nError: Digite una opcion valida...\n')
                    print('----------------------------------------\n')
                    opc = Leer('Digite el numero de la factura que desea pagar: ').leerInt()
        else:
            print('----------------------------------------')
            print('\nEl cliente no tiene facturas por pagar\n')
            print('----------------------------------------\n')
            
    def facturasCliente(self, cliente):
        print(f'------------ * Facturas * -------------')
        if cliente.facturas != []:
            for facturas in cliente.facturas:
                facturas.facturaCliente()
        else:
            print('----------------------------------------')
            print('\nEl clienet no tiene facturas por pagar\n')   
            print('----------------------------------------\n')  