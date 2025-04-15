from empleado import EmpleadoTiempoCompleto,EmpleadoMedioTiempo

empleados = []
empleados.append(EmpleadoTiempoCompleto("Daniel",470))
empleados.append(EmpleadoTiempoCompleto("Danna",490))
empleados.append(EmpleadoMedioTiempo("Didier",320))
empleados.append(EmpleadoMedioTiempo("Dayanis",350))

for empleado in empleados:
    print(f"EL EMPLEADO: {empleado.nombre} CON EL BONO SU SALARIO ES: {empleado.calcular_salario()}")