class Personas():

    def __init__(self, nombre, edad, residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
    
    def descripcion(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad} Residencia: {self.residencia}")

class Empleados(Personas):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}")


Manuel=Empleados(1500, 15, "Manuel", 55, "Colombia")

Manuel.descripcion()

print(isinstance(Manuel, Empleados))
print(isinstance(Manuel, Personas))
