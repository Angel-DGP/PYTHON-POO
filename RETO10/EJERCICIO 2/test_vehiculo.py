from vehiculo import Auto, Moto

vehiculos = []
vehiculos.append(Auto("Ford","Mustang","2024",2))
vehiculos.append(Moto("Ducati","Panigale","2023","Deportiva"))
vehiculos.append(Auto("Chevrolet","Camaro","2024",2))
vehiculos.append(Moto("BMW ","M 1000 R","2023","Deportiva"))

for vehiculo in vehiculos:
    vehiculo.descripcion()