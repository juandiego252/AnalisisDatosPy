print("¡Viaja con KrakeTravels!")
print("Escoge tu país de Destino")
print("----------------------------")
print("1. Ecuador")
print("2. Perú")
print("3. Colombia")
print("----------------------------")
paisUsuario = int(input("Escoge su opción (1-3): "))
velocidadUsuario = int(input("Ingrese su velocidad: "))
if paisUsuario == 1:
    print(f"Tu velocidad de {velocidadUsuario} km/h en Ecuador esta dentro de la zona:")
    if velocidadUsuario >= 10 and velocidadUsuario <= 50:
        print("Urbana")
    elif velocidadUsuario >= 51 and velocidadUsuario <= 70:
        print("Rural")
    elif velocidadUsuario >= 71 and velocidadUsuario <= 90:
        print("Perimetral")
    else :
        print("Su velocidad es muy baja o usted ya exedio el limite de velocidad")
        
if paisUsuario == 2:
    print(f"Tu velocidad de {velocidadUsuario} km/h en Peru esta dentro de la zona:")
    if velocidadUsuario >= 10 and velocidadUsuario <= 40:
        print("Urbana")
    elif velocidadUsuario >= 41 and velocidadUsuario <= 60:
        print("Rural")
    elif velocidadUsuario >= 61 and velocidadUsuario <= 120:
        print("Perimetral")
    else :
        print("Su velocidad es muy baja o usted ya exedio el limite de velocidad")
if paisUsuario == 3:
    print(f"Tu velocidad de {velocidadUsuario} km/h en Colombia esta dentro de la zona:")
    if velocidadUsuario >= 10 and velocidadUsuario <= 30:
        print("Urbana")
    elif velocidadUsuario >= 31 and velocidadUsuario <= 80:
        print("Rural")
    elif velocidadUsuario >= 81 and velocidadUsuario <= 100:
        print("Perimetral")
    else :
        print("Su velocidad es muy baja o usted ya exedio el limite de velocidad")