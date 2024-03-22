from laptop import Laptop

laptop_pepito = Laptop("Lenovo","I5","1 gb")
laptop_maria = Laptop("Asus","i3","1gb")

asusLaptop = Laptop.asus_laptop()

print(asusLaptop.__dict__)

print(Laptop.comparar_costo(laptop_pepito,laptop_maria))
