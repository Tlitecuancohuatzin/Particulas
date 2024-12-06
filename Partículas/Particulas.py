class Particle:
    '''Una particula es un constituyente fundamental del universo.
    Atributos
    ----------
    c: carga en unidades de [e]
    m: masa en unidades de [GeV]
    '''
    type = 'Partícula'
    def __init__(self, name, charge, mass):
        self.name = name
        self.charge = charge
        self.mass = mass
    def info(self):
        return f'Particle: self.name, Charge: self.charge, Mass: self.mass'

class Quark(Particle):
    def __init__(self, name, charge, mass, color_charge):
        super().__init__(name, charge, mass)
        self.color_charge = color_charge
    def info(self):
        return f'Quark: self.name, Charge: self.charge, Mass: self.mass, Color Charge: self.color_charge'

class Lepton(Particle):
    def __init__(self, name, charge, mass, generation):
        super().__init__(name, charge, mass)
        self.generation = generation
    def info(self):
        return f'nombre: {str(self.name)}' + f'carga: {str(self.charge)}'\n + f'masa: {str(self.mass)} \n' + f'generación: {str(self.generation)} \n'

Electrón = Lepton(name = 'Electrón', charge = '-1 e', mass = '0.51099895000 $\pm$ 0.00000000015', generation = 6.6)

