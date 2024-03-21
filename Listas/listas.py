#Listas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano" ,"Neptuno"]
#print(planetas[-1])
print(planetas[1: ])
gravedadEnPlanetas = [3.7 ,8.87 ,9.8 ,3.71 ,24.79, 10.44, 8.87,15]
pesoBus = 124054

print(f"El valor en la tierra de un autobus de dos pisos es {pesoBus} N")
print(f"El valor en Mercurio de un autobus de dos pisos es {pesoBus * gravedadEnPlanetas[0]} N")
print(f"El Peso de un autobus de dos pisos en el planeta liviano es {pesoBus * min(gravedadEnPlanetas)} N")
print(f"El Peso de un autobus de dos pisos en el planeta mas pesado es {pesoBus * max(gravedadEnPlanetas)} N")
gravedadEnPlanetas.append(0.90)
print(gravedadEnPlanetas[8])