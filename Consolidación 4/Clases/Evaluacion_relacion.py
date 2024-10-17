from Vehiculos import Particular, Carga, Bicicleta, Motocicleta, Automovil, Vehiculo

particular = Particular("Toyota", "4Runner", 4, 180, 500, 5)
carga = Carga("Toyota", "Hilux", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Bianchi", "Corsa", 2, "Mountain")
motocicleta = Motocicleta(
    "Ninja", "300", 2, "Deportiva", "2T", "Doble Viga", 21)

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("Motocicleta es instancia con relación a Vehículo:",
      isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil:",
      isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:",
      isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:",
      isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:",
      isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:",
      isinstance(motocicleta, Motocicleta))
