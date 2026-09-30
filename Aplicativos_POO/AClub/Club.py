import os
from Leer import *
from Socios import *
from Facturas import *
from Afiliados import *

class Club:
    
    def __init__(self):
        
        self.socios = []
    
    def adicionarSocio(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    # os.system('cls')
                    usuario = self.adicionarSoc()
                    if usuario != None:
                        self.socios.append(usuario)
                    resp = Leer('\nDesea adicionar a otro socio? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    # os.system('cls')
                    os.system('pause')
                    break
                case other:
                    # os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro socio? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    # os.system('cls')
    
    def adicionarSoc(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Socio *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite la cedula del socio: ').leerInt()
        if not self.buscarSocio(codigo):
            nombre = Leer('Digite el nombre del socio: ').leerCadena()
            print('----------------------------------------')
            print(f'Tipo de Socio: \n1. Platinum \n2. Gold \n3. Silver')
            print('----------------------------------------')
            tipo = Leer('\nDigite el tipo de Socio: ').leerInt()
            while True:
                match tipo:
                    case 1: 
                        print('\n----------------------------------------')
                        user = Platinum(codigo, nombre, 0.15)
                        print('  ¡Socio adicionado exitosamente!   ')
                        print('----------------------------------------')
                        return user
                    case 2:
                        print('\n----------------------------------------')
                        user = Gold(codigo, nombre, 0.1)
                        print('  ¡Socio adicionado exitosamente!   ')
                        print('----------------------------------------')
                        return user
                    case 3:
                        print('\n----------------------------------------')
                        user = Silver(codigo, nombre, 0.05)
                        print('  ¡Socio adicionado exitosamente!   ')
                        print('----------------------------------------')
                        return user
                    case other:
                        print('\nError: Digite una opción valida...\n')
                        print('\n----------------------------------------')
                        tipo = Leer('\nDigite el tipo de socio: ').leerInt()       
        else:
            print('\nEl codigo del socio ya existe...')
        
    def eliminarSocio(self):
    
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.eliminarSoc()
                        resp = Leer('\nDesea eliminar a otro socio? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea eliminar a otro socio? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')
            
    def eliminarSoc(self):
        
        print('\n----------------------------------------')
        print('        * Eliminar Socio *         ')
        print('----------------------------------------')
        self.mostrarSocios1()
        codigo = Leer('\nDigite la cedula del socio: ').leerInt()
        if self.buscarSocio(codigo):
            socio = self.buscarSocio1(codigo)
            self.socios.remove(socio) 
            print('----------------------------------------')
            print('        * Socio Removido *         ')
            print('----------------------------------------')      
        else:
            print('----------------------------------------')
            print('\nEl codigo del socio no existe...\n')
            print('----------------------------------------')
            
    def mostrarSocios(self):
        
        print('\n----------------------------------------')
        print('        * Mostrar Socios *         ')
        print('----------------------------------------') 
        for socio in self.socios:
            if isinstance(socio, Platinum):
                print('----- * Socios Platinum * -------') 
                socio.socio()
            elif  isinstance(socio, Gold):
                print('----- * Socios Gold * -------') 
                socio.socio()
            elif  isinstance(socio, Silver):
                print('----- * Socios Silver * -------') 
                socio.socio()
                
    def mostrarSocios1(self):
        
        print('------ * Socios Platinum * ------') 
        for socio in self.socios:
            if isinstance(socio, Platinum):
                socio.socio()
                print('---------------------------------')
        print('\n-------- * Socios Gold * --------')
        for socio in self.socios:
            if isinstance(socio, Gold): 
                socio.socio()
                print('---------------------------------')
        print('\n------- * Socios Silver * -------')
        for socio in self.socios:
            if isinstance(socio, Silver): 
                socio.socio()
                print('---------------------------------')
        
    def buscarSocio(sefl, cedula):
        
        for soc in sefl.socios:
            if soc.cedula == cedula:
                return True
        else:
            return False
        
    def buscarSocio1(sefl, cedula):
        
        for soc in sefl.socios:
            if soc.cedula == cedula:
                return soc
            
    def mostrarSocio(self):
        
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.mostrarSoc()
                        resp = Leer('\nDesea ver a otro socio? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea ver a otro socio? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')
    
    def mostrarSoc(self):
        
        print('\n----------------------------------------')
        print('        * Visualizar Socio *         ')
        print('----------------------------------------')
        self.mostrarSocios1()
        codigo = Leer('Digite la cedula del socio: ').leerInt()
        if self.buscarSocio(codigo):
            socio = self.buscarSocio1(codigo)
            print('-------------- * Socio * ---------------')
            socio.socio()
            print('----------------------------------------')
            print('--- * Visualizar Autorizados Socio * ---')
            if socio.afiliados != []:
                for afiliados in socio.afiliados:
                    print(afiliados)
                    print('----------------------------------------')
            else:
                print('----------------------------------------')
                print('\nEl socio no tiene autorizados...\n')
                print('----------------------------------------')
        else:
            print('----------------------------------------')
            print('\nEl codigo del socio no existe...\n')
            print('----------------------------------------')
            
    def adicionarAfiliado(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI' | 'Si' | 's' :
                    # os.system('cls')
                    self.adicionarAfi()
                    resp = Leer('\nDesea adicionar a otro afiliado? si/no -> ').leerCadena()
                case 'no' | 'No' |'NO' |'n' :
                    # os.system('cls')
                    os.system('pause')
                    break
                case other:
                    # os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea adicionar a otro afiliado? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    # os.system('cls')
    
    def adicionarAfi(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Afiliado *         ')
        print('----------------------------------------')
        codigo = Leer('Digite la cedula del Socio: ').leerInt()
        print('----------------------------------------')
        if self.buscarSocio(codigo):
            socio = self.buscarSocio1(codigo)
            user = self.buscarSocio1(codigo)
            codigoAfiliado = Leer('Digite la cedula del afiliado: ').leerInt()
            if not self.buscarUsuario(codigoAfiliado, user.afiliados):
                nombre = Leer('Digite el nombre del afiliado: ').leerCadena()
                afiliado = Afiliado(codigoAfiliado, nombre)
                print('----------------------------------------')
                print('  ¡Afiliado adicionado exitosamente!   ')
                print('----------------------------------------')
                socio.afiliados.append(afiliado)
            else: 
                print('----------------------------------------')
                print('\nEl afiliado ya existe...\n')   
                print('----------------------------------------') 
        else:
            print('\nEl codigo del socio no existe...\n')
            print('----------------------------------------')
    
    def buscarUsuario(self, id, lista):
        
        for user in lista:
            if user.cedula == id:
                return True
        else:
            return False
        
    def buscarUsuario1(self, id, lista):
        
        for user in lista:
            if user.cedula == id:
                return user
    
    def mostrarAutorizado(self):
        
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.mostrarAut()
                        resp = Leer('\nDesea ver a otro socio? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea ver a otro socio? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')
    
    def mostrarAut(self):
        
        print('\n----------------------------------------')
        print('        * Visualizar Autorizado *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite la cedula del autorizado: ').leerInt()
        if self.buscarSocioAutorizado(codigo, self.socios):
            socio = self.buscarSocioAutorizado1(codigo, self.socios)
            autorizado = self.buscarUsuario1(codigo, socio.afiliados)
            print('----------- * Autorizado * -------------')
            print(autorizado)
            print('----------------------------------------')
            print('--------- * Socio Autorizado * ---------')
            socio.socio()
            print('----------------------------------------')
        else:
            print('----------------------------------------')
            print('\nEl codigo del autorizado no existe...\n')
            print('----------------------------------------')
                                
        # if not self.buscarSocio(codigo):
        #     socio = self.buscarSocio1(codigo)
        #     socio.socio()
        #     print('   * Visualizar Afiliados Socio *     ')
        #     for afiliados in socio.afiliados:
        #         print(afiliados)
        # else:
        #     print('\nEl codigo del socio ya existe...')
    
    def buscarSocioAutorizado(self, codAutorizado, listaSocios):
        for socios in listaSocios:
            for afiliado in socios.afiliados:
                if afiliado.cedula == codAutorizado:
                    return True
        return False
   
    def buscarSocioAutorizado1(self, codAutorizado, listaSocios):
        for socios in listaSocios:
            for afiliado in socios.afiliados:
                if afiliado.cedula == codAutorizado:
                    return socios
    
    def adicionarCosumos(self):
        
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.adicionarCon()
                        resp = Leer('\nDesea adicionar otro? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea adicionar otro? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')
            
    def adicionarCon(self):
        
        print('\n----------------------------------------')
        print('        * Adicionar Consumo *         ')
        print('----------------------------------------')
        codigo = Leer('\nDigite la cedula: ').leerInt()
        if self.buscarSocio(codigo):
            print('----------------------------------------')
            socio = self.buscarSocio1(codigo)
            fac = socio.consumo(codigo)
            socio.facturas.append(fac)
            print('----------------------------------------')
            print('        * Consumo Adicionado *         ')
            print('----------------------------------------')
        elif self.buscarSocioAutorizado(codigo, self.socios):
            print('----------------------------------------')
            socio = self.buscarSocioAutorizado1(codigo, self.socios)
            fac = socio.consumo(codigo)
            socio.facturas.append(fac)
            print('----------------------------------------')
            print('        * Consumo Adicionado *         ')
            print('----------------------------------------')
        else:
            print('\nEl codigo no existe...\n')
        
    def pagarCosumos(self):
        
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.pagarCon()
                        resp = Leer('\nDesea realizar otro pago? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea realizar otro pago? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')     
    
    def pagarCon(self):
        
        print('\n----------------------------------------')
        print('        * Pagar Consumo *         ')
        print('----------------------------------------')
        self.mostrarSocios1()
        codigo = Leer('\nDigite la cedula: ').leerInt()
        if self.buscarSocio(codigo):
            socio = self.buscarSocio1(codigo)
            socio.pagarConsumo(socio)
        # elif self.buscarSocioAutorizado(codigo, self.socios):
        #     socio = self.buscarSocioAutorizado1(codigo, self.socios)
        #     socio.pagarConsumo(socio)
        else:
            print('\nEl codigo no existe...\n')
    
    def consumosSocio(self):
        
        if self.socios != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI' | 'Si' | 's' :
                        # os.system('cls')
                        self.consumosSoc()
                        resp = Leer('\nDesea ver otros consumos? si/no -> ').leerCadena()
                    case 'no' | 'No' |'NO' |'n' :
                        # os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        # os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea ver otros consumos? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        # os.system('cls')
        else:
            print('\nNo hay socios en el club...\n')
    
    def consumosSoc(self):
        
        print('\n----------------------------------------')
        print('          * Consumos Socio *         ')
        print('----------------------------------------')
        self.mostrarSocios1()
        cedula = Leer('\nDigite la cedula del socio: ').leerInt()
        if self.buscarSocio(cedula):
            socio = self.buscarSocio1(cedula)
            socio.consumosSocio(socio)
        else:
            print('\nEl codigo no existe...\n')

    def totalConsumos(self):
        print('\n----------------------------------------')
        print('           * Total Consumos *         ')
        print('----------------------------------------')
        self.totalcon()
        
    def totalcon(self):
        i = 0
        valorNetoTotal = 0
        valorDescuentoTotal = 0
        for socio in self.socios:
            for facturas in socio.facturas:
                print(f'------------ * Factura {i+1} * -------------')
                facturas.factura()
                valorNetoTotal += facturas.valor
                valorDescuentoTotal += facturas.valorDescuento
                i += 1
        print('----------------------------------------')
        print(f'Valor Total Neto: {valorNetoTotal}\nValor Total Descuento: {valorDescuentoTotal}')
        print('----------------------------------------\n')
        
    def consumosTipoSocio(self):
        print('\n----------------------------------------')
        print('        * Consumos Tipo Socio *         ')
        print('----------------------------------------\n')
        print('----- * Consumos Socios Platinum * -----')
        valNeto = 0
        valDesc = 0 
        for socio in self.socios:
            if isinstance(socio, Platinum):
                vN, vD = socio.facturasSocio()
                valNeto += vN
                valDesc += vD         
        print('----------------------------------------')
        print(f'Valor Total Neto Premier: {valNeto}\nValor Total con Descuento Premier: {valDesc}') 
        print('----------------------------------------')
        valNeto = 0
        valDesc = 0 
        print('\n------- * Consumos Socios Gold * -------')
        for socio in self.socios:
            if isinstance(socio, Gold): 
                vN, vD = socio.facturasSocio(socio)
                valNeto += vN
                valDesc += vD 
        print('----------------------------------------')
        print(f'Valor Total Neto Premier: {valNeto}\nValor Total con Descuento Premier: {valDesc}') 
        print('----------------------------------------')
        valNeto = 0
        valDesc = 0 
        print('\n------ * Consumos Socios Silver * ------')
        for socio in self.socios:
            if isinstance(socio, Silver): 
                vN, vD = socio.facturasSocio(socio)
                valNeto += vN
                valDesc += vD 
        print('----------------------------------------')
        print(f'Valor Total Neto Premier: {valNeto}\nValor Total con Descuento Premier: {valDesc}') 
        print('----------------------------------------')
