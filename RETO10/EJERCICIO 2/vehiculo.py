class Vehiculo():
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def descripcion(self):
        print(f"----VEHICULO----\nMARCA: {self.marca}\nMODELO: {self.modelo}\nAÑO DE FABRICACIÓN: {self.anio}")
        
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio,num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas
    def descripcion(self):
        super().descripcion()
        print(f"NUMERO DE PUERTAS: {self.num_puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio,tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    def descripcion(self):
        super().descripcion()
        print(f"TIPO DE MOTO: {self.tipo}")