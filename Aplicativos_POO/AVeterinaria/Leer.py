from datetime import datetime
import os
class Leer:

    def __init__(self, cad):
        self.cadena = cad
    
    def leerInt(self):
        while True:
            try:
                opc = int(input(self.cadena))
                return opc
            except ValueError:
                print('\nERROR: Digite un valor valido... \n')
    
    def leerFloat(self):
        while True:
            try:
                opc = float(input(self.cadena))
                return opc
            except ValueError:
                print('\nERROR: Digite un valor valido...\n')

    def leerCadena(self):
        while True:
            try:
                opc = str(input(self.cadena))
                return opc
            except ValueError:
                print('\nERROR: Digite un valor valido...\n')
    
    def leerFecha(self):
        while True:
            try:
                fechaHora = datetime.strptime(input(self.cadena), "%d/%m/%Y %H:%M")
                return fechaHora
            except ValueError:
                print('\nERROR: Digite un valor valido...\n')
    
    def leerSexo(self):
        while True:
            try:
                sexo = str(input(self.cadena))
                if sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f':
                    return sexo
                else:
                    print('\nERROR: Digite un valor valido...\n')
            except ValueError:
                print('ERROR: Digite un valor valido...\n')