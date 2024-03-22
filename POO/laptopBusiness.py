from laptop import Laptop
import random

class LaptopBusiness(Laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento,duracion_bateria, costo=500, inpuestos=10):
        super().__init__(marca, procesador, memoria, costo, inpuestos)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
        
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_business = self.realizar_diagnostico_business()
        resultado_diagnostico["Resultado Business"] = resultado_business
        resultado_red = self.verificar_conectividad_red()
        resultado_diagnostico["Diagnostico de Red"] = resultado_red
        return resultado_diagnostico
    
    def realizar_diagnostico_business(self):
        if self.almacenamiento < 120:
            valor = "Poco Almacenamiento"
        elif 121 <= self.almacenamiento <= 250:
            valor = "Almacenamiento adecuado"
        else:
            valor = "Almacenamiento de sobra"
        return f"{valor} GB"
    
    def verificar_conectividad_red(self):
        disponibilidad_wifi = random.choice([True,False])
        acceso_servidores = random.choice([True,False])
        latencia_red = random.randint(1,30)
        resultados = {
            "Wifi-Disponible " : "OK" if disponibilidad_wifi == True else "Error",
            "Acceso a Servidores " : "Ok" if acceso_servidores == True else "Error",
            "Latencia de red" : "Ok " if latencia_red >= 19 and latencia_red <= 30 else "Latencia mala"
        }
        return resultados