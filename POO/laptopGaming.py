from laptop import Laptop

class Laptop_Gaming (Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_grafica ,costo=500, inpuestos=10):
        super().__init__(marca, procesador, memoria, costo, inpuestos)
        self.tarjeta_grafica = tarjeta_grafica
    
    
    def realizar_diagnostico_sistema(self):
       resultado_diagnostico = super().realizar_diagnostico_sistema()
       resultado_juegos = self.realizar_diagnostico_juegos()
       resultado_diagnostico["Resultado Juegos"] = resultado_juegos
       return resultado_diagnostico
   
    def realizar_diagnostico_juegos(self):
        juegos = ["Fortnite","COD","GTA"]
        resultado = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarjeta_grafica:
                fps = fps_base*3
            elif "GTX" in self.tarjeta_grafica:
                fps = fps_base*3
            else:
                fps = fps_base
            resultado[juego] = f"{fps} FPS"
        return resultado
    pass