class Persona:
    def __init__(self,dni,nombre):
        self.dni = dni
        self.nombre = nombre
    
    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    def saludo(self):
        return f'Bienvenida {self.nombre}'