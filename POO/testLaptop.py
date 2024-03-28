from laptop import Laptop
from laptopGaming import Laptop_Gaming
from laptopBusiness import LaptopBusiness

laptop_pepito = Laptop("Lenovo", "I5", "1 gb")
laptop_maria = Laptop("Asus", "i3", "1gb")

latop_gamingJuanito = Laptop_Gaming("MSI", "i7", 8, "RTX 8GB")
laptop_david = LaptopBusiness("Asus", "i9", 18, 256, 3)

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()  # Llamar al método realizar_informe_uso
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")

print("\n")

imprimir_informe(latop_gamingJuanito)

# asusLaptop = Lapto
# p.asus_laptop()

# print(asusLaptop.__dict__)

# print(Laptop.comparar_costo(laptop_pepito,laptop_maria))
