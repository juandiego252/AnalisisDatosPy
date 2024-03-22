class Auto:
    def __init__(self,marca,modelo,anio,kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        print("-- Informacion Auto --")
        print(self.marca)
        print(self.modelo)
        print(self.anio)
        
    def actualizar_kilometraje(self,actualizar_kilometraje):
        if(actualizar_kilometraje >= self.kilometraje):
            self.kilometraje = actualizar_kilometraje
            print("Kilometraje actualizado correctmente")
        else:
            print("El kilometraje es menor al actual")
    
    def realizar_viaje (self,kilometros):
        if(kilometros > 0):
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilometros debe ser positiva")
    
    def estado_auto(self):
        if (self.kilometraje < 20000):
            print("Estoy nuevo")
        elif (self.kilometraje >= 20000 and self.kilometraje < 100000):
            print("Ya estoy usado") 
        else:
            print("Ya dejame descansar porfavor !!!")   
    @classmethod
    def autosToyota(cls):
            marca = "Toyota"
            anio = 2024
            return cls(marca,"Fortuner",anio)
    @staticmethod
    def validar_mismo_kilometraje (Auto1,Auto2):
        if (Auto1.kilometraje == Auto2.kilometraje):
            return "Tienen el mismo kilometraje"
        return "No tienene el mismo Kilometraje"
    @classmethod
    def autosHyundai(cls):
        marca = "Hyundai"
        anio = 2025
        return cls (marca,"Modelo Terracan",anio)
    @staticmethod
    def validar_mismo_anio (Auto1,Auto2):
        if(Auto1.anio == Auto2.anio):
            return "Mismo año de lanzamiento"
        return "Año de lanzamineto diferentes"
    
auto_Juan = Auto.autosToyota()
auto_Diego = Auto.autosHyundai()
print(auto_Juan.__dict__)
print(auto_Diego.__dict__)
print(Auto.validar_mismo_anio(auto_Juan,auto_Diego))
print(Auto.validar_mismo_kilometraje(auto_Juan,auto_Diego))



    
    
    
    
# auto_juan = Auto("Chevrolet","Tracker",2018,15000)
# auto_juan.actualizar_kilometraje(20000)
# auto_juan.realizar_viaje(23)
# auto_juan.mostrar_informacion()
# auto_juan.estado_auto()