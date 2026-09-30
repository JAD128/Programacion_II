class Recurso:
    
    def __init__(self, nombre, codigo):
        
        self.nombre = nombre
        self.codigo = codigo
        self.estado = True
        
    def __str__(self):
        return(f'Recurso: {self.nombre}\nCodig: {self.codigo}')
    
    def recurso(self):
        
        if self.estado:
            estado = 'Disponible'
        else:
            estado = 'No Disponible'
        return(f'Recurso: {self.nombre}\nCodig: {self.codigo}\nEstado: {estado}')