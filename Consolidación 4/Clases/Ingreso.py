from Vehiculos import Automovil


num_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
vehiculos = []

for i in range(num_vehiculos):
    print("Datos del automóvil", i + 1)
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    num_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("Inserte el cilindraje en cc: "))

    automovil = Automovil(marca, modelo, num_ruedas, velocidad, cilindraje)
    vehiculos.append(automovil)

print("Imprimiendo por pantalla los Vehículos:")
for i, automovil in enumerate(vehiculos):
    print("Datos del automóvil", i + 1, ":", "Marca", automovil.marca + ",", "Modelo",
          automovil.modelo + ",", automovil.num_ruedas, "ruedas,", automovil.velocidad, "Km/h,")
    print(automovil.cilindraje, "cc")
