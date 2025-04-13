class Auto:
    def __init__(self,marca,modelo,año,kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    def mostrar_informacion(self):
        print(f"AUTO\nMARCA: {self.marca}\nMODELO: {self.modelo}\nAÑO: {self.año}\nKILOMETRAJE: {self.kilometraje}")
    def actualizar_kilometraje(self,new):
        if(new>self.kilometraje):
            self.kilometraje = new
            print(f"KILOMETRAJE ACTUALIZADO CORRECTAMENTE\nNUEVO KILOMETRAJE:{self.kilometraje}")
        else:
            print("NO SE PUEDE REDUCIR EL KILOMETRAJE")
    def realizar_viaje(self,km_recorridos):
        if(km_recorridos>0):
            self.kilometraje = self.kilometraje + km_recorridos
        else:
            print("INGRESE UN VALOR POSITIVO")
    def estado_auto(self):
        if(self.kilometraje<20000):
            print("Estoy como nuevo")
        elif(self.kilometraje>=20000 and self.kilometraje<=100000):
            print("Ya estoy usado")
        elif(self.kilometraje>100000):
            print("¡Ya déjame descansar por favor!")


car = Auto("Ford","Mustang","2024")
car.mostrar_informacion()
car.actualizar_kilometraje(5000)
car.realizar_viaje(360)
car.estado_auto()