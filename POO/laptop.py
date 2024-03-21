class Laptop:
    def __init__(self,marca,procesador,memoria,costo = 500,inpuestos = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.inpuesto = inpuestos
        
    def valor_final(self):
        return self.costo + self.inpuesto
    def valor_descuento(self,descuento):
        return (self.costo * descuento) / 100
laptop_pepito = Laptop("Lenovo","i7","16 gb")

print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final())
print(laptop_pepito.valor_descuento(10))