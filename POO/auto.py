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

auto_juan = Auto("Chevrolet","Tracker",2018,15000)


auto_juan.actualizar_kilometraje(20000)
auto_juan.realizar_viaje(23)
auto_juan.mostrar_informacion()
auto_juan.estado_auto()
        