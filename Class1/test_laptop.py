from laptop import Laptop

laptop_pepito = Laptop("Lenovo","i7",32)
laptop_maria = Laptop("Lenovo","i7",32,200)


for i in range(1,1001):
    asus_laptop = Laptop.asus_laptop(costo= i)
    print(asus_laptop.__dict__)
#print(Laptop.comparar_costo(laptop_pepito,laptop_maria))
