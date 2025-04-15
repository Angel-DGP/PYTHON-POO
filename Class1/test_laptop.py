from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_buisness import Laptop_Buisness
laptop_pepito = Laptop("Lenovo","i7",32)
laptop_maria = Laptop("Lenovo","i7",32,200)
laptop_juanito = Laptop_Gaming("Asus","i9",32,"RTX",2000)
laptop_daniel = Laptop_Buisness("Hp","i5",4,256,"20h")

#print(laptop_juanito.__dict__)
#print(laptop_juanito.realizar_diagnostico())
#print(laptop_daniel.realizar_diagnostico())


#for i in range(1,1001):
#    asus_laptop = Laptop.asus_laptop(costo= i)
#    print(asus_laptop.__dict__)
#print(Laptop.comparar_costo(laptop_pepito,laptop_maria))

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave,valor in informe.items():
        print(f"{clave} : {valor}")

print("PEPITO: ")
imprimir_informe(laptop_pepito)        
print("JUANITO: ")
imprimir_informe(laptop_juanito)
