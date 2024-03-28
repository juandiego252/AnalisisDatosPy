import random

class Laptop:
    def __init__(self, marca, procesador, memoria, costo=500, impuestos=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuestos
        
    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo * descuento) / 100
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "Marca": self.marca,
            "Procesador": self.procesador,
            "RAM": "Ok" if self.memoria >= 8 else "Aumentar memoria RAM",
            "Bateria": "Ok" if random.choice([True, False]) else "Cambiar de Bateria",
        }
        return resultado
    
    def realizar_informe_uso(self):
        resultado_informe = {
            "Tipo": "Generica",
            "Uso Recomendado": "Tareas Cotidianas",
            "Horas de Uso": 5,
            "Diagnostico actual": self.realizar_diagnostico_sistema(),   
        }
        return resultado_informe
        
    @staticmethod
    def comparar_costo(Laptop1, Laptop2):
         if Laptop1.costo == Laptop2.costo:
             return "Los costos son iguales"
         return "Los costos son diferentes"
     
    @classmethod
    def asus_laptop(cls):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria)
