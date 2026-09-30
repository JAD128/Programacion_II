class Usuario:
    
    def __init__(self, nombre, codigo, tipo):
        
        self.nombre = nombre
        self.codigo = codigo
        self.tipo = tipo
        self.prestamos = []
    
    def __str__(self):
        if self.tipo == 1:
            tipo = 'Estudiante'
        if self.tipo == 2:
            tipo = 'Docente'
        if self.tipo == 3:
            tipo = 'Trabajador'
        return (f'Nombre: {self.nombre}\nCodigo: {self.codigo}\nTipo: {tipo}')