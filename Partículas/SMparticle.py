class StandardModelParticle:
    def __init__(self, name, symbol, mass, charge, spin, type_of_particle, is_antiparticle=False):
        """
        Clase que representa una partícula del modelo estándar.
        
        :param name: Nombre de la partícula.
        :param symbol: Símbolo de la partícula.
        :param mass: Masa de la partícula en MeV/c^2.
        :param charge: Carga de la partícula en unidades de la carga del electrón.
        :param spin: Espín de la partícula.
        :param type_of_particle: Tipo de partícula, como 'fermion' o 'boson'.
        :param is_antiparticle: Booleano que indica si es la antipartícula.
        """
        self.name = name
        self.symbol = symbol
        self.mass = mass
        self.charge = charge
        self.spin = spin
        self.type_of_particle = type_of_particle
        self.is_antiparticle = is_antiparticle

    def info(self):
        """Devuelve una descripción de la partícula."""
        return (f"{self.name} ({self.symbol}) - Masa: {self.mass} MeV/c^2, Carga: {self.charge}, "
                f"Espín: {self.spin}, Tipo: {self.type_of_particle}, Antipartícula: {self.is_antiparticle}")
