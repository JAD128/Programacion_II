class Libro:
    
    def __init__(self, nombre, codigo, precio):
        
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        
    def __str__(self):
        return (f'Título del libro: {self.nombre}\nISBN: {self.codigo}\nPrecio: {self.precio}')