from Libro import *
from Leer import *
from CarritoCompras import *
from VentasLibro import *
import os
class TiendaLibros:
    
    def __init__(self): 
        self.catalogo = []
        
    def adicionarLibro(self):
        
        resp = 'si'
        while True:
            match resp:
                case 'si' | 'SI':
                    os.system('cls')
                    libro = self.adicionarLib()
                    if libro != None:
                        lib = Libro(libro[0], libro[1], libro[2])
                        self.catalogo.append(lib)
                    resp = Leer('\nDesea añadir otro libro? si/no -> ').leerCadena()
                case 'no' | 'No':
                    os.system('cls')
                    os.system('pause')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea añadir otro libro? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
                                   
    def adicionarLib(self):
        
        print('\n----------------------------------------')
        print('          * Adicionar libro *         ')
        print('----------------------------------------')
        codigo = Leer('Digite ISBN del libro: ').leerInt()
        if not self.buscarLibro(codigo):
            nombre = Leer('Digite el nombre del libro: ').leerCadena()
            precio = Leer('Digite el precio del libro: ').leerFloat()
            print('----------------------------------------')
            print('       ¡Libro añadido con exito!        ')
            print('----------------------------------------')
            libro = (nombre, codigo, precio)
            return libro
        else: 
            print('\nEl libro ya existe... ')
            return None
    
    def buscarLibro(self, cod):
        
        for lib in self.catalogo:
            if lib.codigo == cod:
                return True
        return False
    
    def eliminarLibro(self):
        
        if self.catalogo != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI'| 'Si':
                        os.system('cls')
                        self.mostrarCatalogo()
                        self.elimiLibro()
                        resp = Leer('\nDesea eliminar otro libro? si/no -> ').leerCadena()
                    case 'no' | 'No' | 'NO':
                        os.system('cls')
                        os.system('pause')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea eliminar otro libro? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay libros en el catalogo...\n')         
                    
    def mostrarCatalogo(self):
        
        if self.catalogo != []:
            print('\n----------------------------------------')
            print('              * Catalogo *         ')
            print('----------------------------------------')
            for libro in self.catalogo:
                print(libro)
                print('----------------------------------------')
        else:
            print('\nNo hay libros en el catalogo...')
            
    def elimiLibro(self):
        
        cod = Leer('\nDigite el ISBN del libro que desea eliminar: ').leerInt()
        if self.buscarLibro(cod):
            for lib in self.catalogo:
                if lib.codigo == cod:
                    self.catalogo.remove(lib)
                    print('----------------------------------------')
                    print('      ¡Libro removido exitosamente! ')
                    print('----------------------------------------')             
        else:
            print('\nEl ISBN ingresado no existe...')
        
    def consultarLibro(self):
        
        if self.catalogo != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI'| 'Si':
                        os.system('cls')
                        self.consultarLib()
                        resp = Leer('\nDesea consultar otro libro? si/no -> ').leerCadena()
                    case 'no' | 'No' | 'NO':
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea consultar otro libro? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay libros en el catalogo...\n')   
    
    def consultarLib(self):
        
        print('\n----------------------------------------')
        print('           * Consultar libro *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el ISBN del libro que desea consultar: ').leerInt()
        if self.buscarLibro(cod):
            for libro in self.catalogo:
                if libro.codigo == cod:
                    print('\n----------------------------------------')
                    print('             * Detalles *         ')
                    print('----------------------------------------')
                    print(libro)
                    print('----------------------------------------')
        else:
            print('\nEl ISBN ingresado no existe...')
    
    def modificarLibro(self):
        
        if self.catalogo != []:
            resp = 'si'
            while True:
                match resp:
                    case 'si' | 'SI'| 'Si':
                        os.system('cls')
                        self.modificarLib()
                        resp = Leer('\nDesea modificar otro libro? si/no -> ').leerCadena()
                    case 'no' | 'No' | 'NO':
                        os.system('cls')
                        break
                    case other:
                        os.system('cls')
                        print('\nERROR: Digite un valor valido...')
                        resp = Leer('\nDesea modificar otro libro? si/no-> ').leerCadena()
                        print('')
                        os.system('pause')
                        os.system('cls')
        else:
            print('\nNo hay libros en el catalogo...\n')
            
    def modificarLib(self):
        
        print('\n----------------------------------------')
        print('           * Modificar libro *         ')
        print('----------------------------------------')
        cod = Leer('\nDigite el ISBN del libro que desea modificar: ').leerInt()
        if self.buscarLibro(cod):
            pos = self.posicionLibro(cod)
            self.catalogo[pos].nombre = Leer('Digite el nombre del libro: ').leerCadena()
            self.catalogo[pos].precio = Leer('Digite el precio del libro: ').leerFloat()
            print('----------------------------------------')
            print('     ¡Libro modificado exitosamente! ')
            print('----------------------------------------')
        else:
            print('\nEl ISBN ingresado no existe..')
                    
    def posicionLibro(self, cod):
        
        for lib in self.catalogo:
            if lib.codigo == cod:
                pos = self.catalogo.index(lib)
                return pos
    
    def buscarNombre(self, nombre):
        
        c = 0
        for lib in self.catalogo:
            if lib.nombre == nombre:
                c += 1
        return c
    
    def buscarNombre1(self, nombre):
        
        for lib in self.catalogo:
            if lib.nombre == nombre:
                return True
        return False
            
    def adicionarCompra(self):
        
        cc = CarritoCompras()
        print('\n----------------------------------------')
        print('          * Adicionar Compra *         ')
        print('----------------------------------------')
        while True:
            resp = 'si'
            match resp:
                case 'si' | 'SI'| 'Si':
                    opc = Leer('\Digite el nombre del libro a comprar: ').leerCadena()
                    cantidad = self.buscarNombre(opc)
                    if cantidad > 0:
                        for prod in self.catalogo:
                            if self.buscarNombre1:
                                cant  = Leer('Cantidad que desea comprar: ').leerInt()
                                lVen = VentasLibro(prod, cant)
                                cc.librosCompras.append(lVen)
                                print('           * Venta realizada *         ')
                                print('----------------------------------------')
                    else:
                        print('\nEl libro que busca no se encuentra disponible...')          
                    resp = Leer('\nDesea comprar otro libro? si/no -> ').leerCadena()
                case 'no' | 'No' | 'NO':
                    os.system('cls')
                    break
                case other:
                    os.system('cls')
                    print('\nERROR: Digite un valor valido...')
                    resp = Leer('\nDesea comprar otro libro? si/no-> ').leerCadena()
                    print('')
                    os.system('pause')
                    os.system('cls')
            
            
                
            
        
        