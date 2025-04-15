class Empleado():
    def __init__(self, nombre, salario_base):
        pass
        self.nombre = nombre
        self.salario_base = salario_base
    def calcular_salario():
        pass
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)
    def calcular_salario(self):
        return self.salario_base + ((20 * self.salario_base)/100)
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)
    def calcular_salario(self):
        return self.salario_base + ((10 * self.salario_base)/100)