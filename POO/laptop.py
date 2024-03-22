import random
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
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "Marca" : f"{self.marca}",
            "Procesador" : f"{self.procesador}",
            "Ram" : "Ok" if self.memoria >= 8 else "Aumentar memoria ram",
            "Bateria " : "Ok" if random.choice([True,False]) else "Cambiar de Bateria",
        }
        return resultado
    
    @staticmethod
    def comparar_costo(Laptop1,Laptop2):
         if(Laptop1.costo == Laptop2.costo):
             return "Los costos son iguales"
         return "Los costos son diferentes"
     
    @classmethod
    def asus_laptop(cls):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca,procesador,memoria)