from laptop import Laptop

class Laptop_Gaming (Laptop):
    def __init__(self, marca, procesador, memoria, tarjeta_grafica ,costo=500, inpuestos=10):
        super().__init__(marca, procesador, memoria, costo, inpuestos)
        self.tarjeta_grafica = tarjeta_grafica
    
    def __str__(self):
            return f"Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \nTarjeta Grafica: {self.tarjeta_grafica} Precio: {self.costo}"
    
    
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

    def realizar_informe_uso(self):
        informe = super().realizar_informe_uso()
        informe.update({
            "Tipo": "Gaming",
            "Uso Recomendado": "Video Juegos",
            "Horas de Uso" : 10,
            "Recomendaciones de Software": ["Antivirus","VPN"]  
        })
        return informe