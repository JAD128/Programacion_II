class Leer:

    def __init__(self, cad):
        self.cadena = cad
    
    def leerInt(self):

        try:
            opc = int(input(self.cadena))
            return opc
        except ValueError:
            print('ERROR: Digite un valor valido... \n')
    
    def leerFloat(self):

        try:
            opc = float(input(self.cadena))
            return opc
        except ValueError:
            print('ERROR: Digite un valor valido...\n')

    def leerCadena(self):

        try:

            opc = str(input(self.cadena))
            return opc
        except ValueError:
            print('ERROR: Digite un valor valido...\n')