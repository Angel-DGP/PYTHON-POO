from Auto import Auto
car = Auto("Ford","Mustang",2023,2)
toyota_car = Auto.toyota_auto()
camaro_car = Auto.camaro_auto()
print(toyota_car.__dict__)
print(camaro_car.__dict__)
print(Auto.comparar_kilometraje(car,toyota_car))
print(Auto.comparar_año(camaro_car,car))
