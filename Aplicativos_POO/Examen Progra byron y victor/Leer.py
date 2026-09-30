class Leer:

    def __init__(self, cad):
        self.cadena = cad
    
    def leerInt(self):
       while True:
        try:
            opc = int(input(self.cadena))
            return opc
        except ValueError:
            print('ERROR: FAVOR DIGITE UN VALOR QUE SEA VALIDO ... \n')
    
    def leerFloat(self):
        while True:
            try:
                opc = float(input(self.cadena))
                return opc
            except ValueError:
                print('ERROR: FAVOR DIGITE UN VALOR QUE SEA VALIDO ...\n')

    def leerCadena(self):
        
        while True:
            try:

                opc = str(input(self.cadena))
                return opc
            except ValueError:
                print('ERROR: FAVOR DIGITE UN VALOR QUE SEA VALIDO ...\n')