class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje


class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje, puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindraje)
        self.puestos = puestos

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindraje} cc, Puestos: {self.puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindraje} cc, Carga: {self.peso_carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"
