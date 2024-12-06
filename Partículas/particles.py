# -*- coding: utf-8 -*-
"""Particles.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16b0fe2RMeYOvQ5YK2r5hVcomxMKpAtLu
"""

import pandas as pd
import matplotlib.pyplot as plt

"""**CLASE PARA PARTÍCULAS:** Una forma de crear una clase para partículas elementales consiste en recopilar propiedades de éstas (como carga, masa, etc) y ocuparlas para diferentes fines. Primeramente, se crea la clase 'Particle', la cual reune datos como: nombre de la partícula, antipartícula, carga, masa y spin. Posteriormente, se crean subclases de 'Particle', las cuales corresponden a los tipos fundamentales de partículas: 'Leptones', 'Quarks', 'Bosones' y heredan sus características de la clase principal, pero a éstas se les puede agregar más propiedades, como el tipo de partículas, isospín, generación, sabor superior,... dependiendo el caso."""

### SE CRE LA CLASE PARTICLE.  ###
class Particle:
    '''Una particula es un constituyente fundamental del universo.
    Atributos
    ----------
    carga: carga en unidades de [e]
    masa: masa en unidades de [GeV/c**2]
    spin
    Entre otras...
    '''

    def __init__(self, nombre, antiparticula, carga, masa, spin):         ### Se definen las variables.
        self.nombre = nombre
        self.antiparticula = antiparticula
        self.carga = carga
        self.masa = masa
        self.spin = spin
    def info(self):                                                       ### La función 'info()' arroja los datos adquiridos de las variables definidas en lista vertical.
        inf = f"Partícula: {self.nombre}\nAntipartícula: {self.antiparticula}\nCarga: {self.carga}\nMasa: {self.masa}"
        print (inf)

### SE CREAN LAS SUBCLASES ANTES MENCIONADAS. Nótese que cada subclase adquiere variables diferentes unas de otras y heredan las de la clase principal. ###
class Quark(Particle):
    type = 'Fermión (Quark)'
    def __init__(self, nombre, antiparticula, carga, masa, spin, isospin, sabor_ex, sabor_en, sabor_sup, sabor_inf, generacion):
        super().__init__(nombre, antiparticula, carga, masa, spin)
        self.isospin = isospin
        self.sabor_ex = sabor_ex
        self.sabor_en = sabor_en
        self.sabor_sup = sabor_sup
        self.sabor_inf = sabor_inf
        self.generacion = generacion
    def info(self):
        inf = f'''Partícula: {self.nombre}\nAntipartícula: {self.antiparticula}\nCarga (e): {self.carga}\nMasa (MeV / c**2): {self.masa}\nSpin: {self.spin}\nIsospín: {self.isospin}\n''' + (
        f'''Sabor extraño: {self.sabor_ex}\nSabor encantado: {self.sabor_en}\nSabor superior: {self.sabor_sup}\nSabor inferior: {self.sabor_inf}\nGeneración: {self.generacion}\nTipo: {self.type}''')
        print (inf)
    def lista(self):                                             ### La función 'lista()' arroja una lista con los valores de las variables requeridas.
        l = [{self.nombre}, {self.antiparticula}, {self.carga}, {self.masa}, {self.spin}, {self.isospin}, {self.sabor_ex}, {self.sabor_en}, {self.sabor_sup}, {self.sabor_inf}, {self.generacion}]
        return l

class Lepton(Particle):
    type = 'Fermión (leptón)'
    def __init__(self, nombre, antiparticula, carga, masa, spin, vida_media, momento_magnetico, long_des, generacion):
        super().__init__(nombre, antiparticula, carga, masa, spin)
        self.vida_media = vida_media
        self.momento_magnetico = momento_magnetico
        self.long_des = long_des
        self.generacion = generacion
    def info(self):
        inf = f'''Partícula: {self.nombre}\nAntipartícula: {self.antiparticula}\nCarga (e): {self.carga}\nMasa (MeV / c**2): {self.masa}\nSpin: {self.spin}\n''' + (
        f'''Vida media: {self.vida_media}\nMomento magnético (e*cm): {self.momento_magnetico}\nLongitud de desintegración (cτ): {self.long_des}\nGeneración: {self.generacion}\nTipo: {self.type}''')
        print (inf)
    def lista(self):
        l = [{self.nombre}, {self.antiparticula}, {self.carga}, {self.masa}, {self.spin}, {self.vida_media}, {self.momento_magnetico}, {self.long_des}, {self.generacion}]
        return l

class Boson(Particle):
    type = 'Bosón'
    def __init__(self, nombre, antiparticula, carga, masa, spin, vida_media, ancho_des):
        super().__init__(nombre, antiparticula, carga, masa, spin)
        self.vida_media = vida_media
        self.ancho_des = ancho_des
    def info(self):
        inf = f'''Partícula: {self.nombre}\nAntipartícula: {self.antiparticula}\nCarga (e): {self.carga}\nMasa (MeV / c**2): {self.masa}\nSpin: {self.spin}\n''' + (
        f'''Vida media: {self.vida_media}\nAncho de desintegración (Γ): {self.ancho_des}\nTipo: {self.type}''')
        print (inf)
    def lista(self):
        l = [{self.nombre}, {self.antiparticula}, {self.carga}, {self.masa}, {self.spin}, {self.vida_media}, {self.ancho_des}]
        return l

"""Posteriormente, se definen todas las partículas con las variables requeridas, según sea el tipo de subclase a la que pertenece cada partícula. En este apartado, se definen **Leptones** con la subclase Lepton:"""

Electrón = Lepton(nombre = 'Electrón', antiparticula = 'Positrón', carga = -1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '> 6.6 × 10**28 años', momento_magnetico = '(1159.65218062 ± 0.00000012) × 10**(-6)', long_des = '---', generacion = 1)
Positrón = Lepton(nombre = 'Positrón', antiparticula = 'Electrón', carga = 1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '> 6.6 × 10**28 años', momento_magnetico = '(1159.65218062 ± 0.00000012) × 10**(-6)', long_des = '---', generacion = 1)
Muon = Lepton(nombre = 'Muon', antiparticula = 'Antimuon', carga = -1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '(2.1969811 ± 0.0000022) × 10**(−6) s', momento_magnetico = '(11659205.9 ± 2.2) × 10**(−10)', long_des = '658.6384 m', generacion = 2)
Antimuón = Lepton(nombre = 'Antimuon', antiparticula = 'Muon', carga = 1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '(2.1969811 ± 0.0000022) × 10**(−6) s', momento_magnetico = '(11659205.9 ± 2.2) × 10**(−10)', long_des = '658.6384 m', generacion = 2)
Tau = Lepton(nombre = 'Tau', antiparticula = 'Antitau', carga = -1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '(290.3 ± 0.5) × 10**(−15) s', momento_magnetico = '−0.057 a 0.024', long_des = '87.03 μm', generacion = 3)
Antitau = Lepton(nombre = 'Antitau', antiparticula = 'Tau', carga = 1, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '(290.3 ± 0.5) × 10**(−15) s', momento_magnetico = '−0.057 a 0.024', long_des = '87.03 μm', generacion = 3)
Neutrino_electrón = Lepton(nombre = 'Neutrino electrón', antiparticula = 'Antineutrino electrón', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 1)
Antineutrino_electrón = Lepton(nombre = 'Antineutrino electrón', antiparticula = 'Neutrino electrón', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 1)
Neutrino_muon = Lepton(nombre = 'Neutrino_muon', antiparticula = 'Antineutrino_muon', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 2)
Antineutrino_muon = Lepton(nombre = 'Antineutrino_muon', antiparticula = 'Neutrino_muon', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 2)
Neutrino_tau = Lepton(nombre = 'Neutrino tau', antiparticula = 'Antineutrino tau', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 3)
Antineutrino_tau = Lepton(nombre = 'Antineutrino tau', antiparticula = 'Neutrino tau', carga = 0, masa = '0.51099895000 ± 0.00000000015', spin = 0.5, vida_media = '---', momento_magnetico = '< 0.064 × 10**(−10)', long_des = '---', generacion = 3)

"""En este apartado, se definen **Quarks** con la subclase Quark:"""

Up = Quark(nombre = 'Up', antiparticula = 'Antiup', carga = 2/3, masa = '2.16 ± 0.07', spin = 1/2, isospin = 1/2, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 1)
Antiup = Quark(nombre = 'Antiup', antiparticula = 'Up', carga = -2/3, masa = '2.16 ± 0.07', spin = 1/2, isospin = -1/2, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 1)
Down = Quark(nombre = 'Down', antiparticula = 'Antidown', carga = -1/3, masa = '4.70 ± 0.07', spin = 1/2, isospin = -1/2, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 1)
Antidown = Quark(nombre = 'Antidown', antiparticula = 'Down', carga = 1/3, masa = '4.70 ± 0.07', spin = 1/2, isospin = 1/2, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 1)
Charm = Quark(nombre = 'Charm', antiparticula = 'Anticharm', carga = 2/3, masa = '1273.0 ± 4.6', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = 1, sabor_sup = 0, sabor_inf = 0, generacion = 2)
Anticharm = Quark(nombre = 'Anticharm', antiparticula = 'Charm', carga = -2/3, masa = '1273.0 ± 4.6', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = -1, sabor_sup = 0, sabor_inf = 0, generacion = 2)
Strange = Quark(nombre = 'Strange', antiparticula = 'Antistrange', carga = -1/3, masa = '93.5 ± 0.8', spin = 1/2, isospin = 0, sabor_ex = -1, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 2)
Antistrange = Quark(nombre = 'Antistrange', antiparticula = 'Strange', carga = 1/3, masa = '93.5 ± 0.8', spin = 1/2, isospin = 0, sabor_ex = 1, sabor_en = 0, sabor_sup = 0, sabor_inf = 0, generacion = 2)
Top = Quark(nombre = 'Top', antiparticula = 'Antitop', carga = 2/3, masa = '172.57 ± 0.29 GeV', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = 0, sabor_sup = 1, sabor_inf = 0, generacion = 3)
Antitop = Quark(nombre = 'Antitop', antiparticula = 'Top', carga = -2/3, masa = '172.57 ± 0.29 GeV', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = 0, sabor_sup = -1, sabor_inf = 0, generacion = 3)
Bottom = Quark(nombre = 'Bottom', antiparticula = 'Antibottom', carga = -1/3, masa = '4183 ± 7', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = -1, generacion = 3)
Antibottom = Quark(nombre = 'Antibottom', antiparticula = 'Bottom', carga = 1/3, masa = '4183 ± 7', spin = 1/2, isospin = 0, sabor_ex = 0, sabor_en = 0, sabor_sup = 0, sabor_inf = 1, generacion = 3)

"""Y en este apartado, se definen **Bosones** con la subclase Boson:"""

Fotón = Boson(nombre = 'Fotón', antiparticula = '---', carga = 0, masa = '< 1 × 10**(−18) eV', spin = 1, vida_media = 'Estable', ancho_des = 'Estable')
Gluón = Boson(nombre = 'Gluón', antiparticula = '---', carga = 0, masa = '0 (teórico)', spin = 1, vida_media = 'Estable', ancho_des = '---')
Wmas = Boson(nombre = 'W+', antiparticula = 'W-', carga = 1, masa = '80.3692 ± 0.0133', spin = 1, vida_media = '3 × 10**(−25) s', ancho_des = '2.085 ± 0.042 GeV')
Wmenos = Boson(nombre = 'W-', antiparticula = 'W+', carga = -1, masa = '80.3692 ± 0.0133', spin = 1, vida_media = '3 × 10**(−25) s', ancho_des = '2.085 ± 0.042 GeV')
Z = Boson(nombre = 'Z', antiparticula = '---', carga = 0, masa = '91.1880 ± 0.0020', spin = 1, vida_media = '3 × 10**(−25) s', ancho_des = '2.4955 ± 0.0023 GeV')
Higgs = Boson(nombre = 'Bosón de Higgs', antiparticula = '---', carga = 0, masa = '125.20 ± 0.11', spin = 0, vida_media = '---', ancho_des = '3.7 ± 1.9 MeV')

"""De este modo, podemos ocupar las funciones y variables definidas para diferentes fines, por ejemplo ver las propiedades de as partículas tanto en lista como en tabla dataframe:"""

### Electrón.info() arroja todas las características del electrón. En general, para ello se escribe la partícula seguida de .info() ###
Electrón.info()

Antimuón.info()

Up.info()

Z.info()

"""**DATAFRAME: BOSONES**"""

### Usando la función de lista, se crean los Dataframes para la visualización general de las características de las partículas
df_Bosones = pd.DataFrame({'Fotón': Fotón.lista(), 'Gluón': Gluón.lista(), 'W+': Wmas.lista(), 'W-': Wmenos.lista(), 'Z': Z.lista(), 'Bosón de Higgs': Higgs.lista()}, index=['Nombre', 'Antipartícula', 'Carga (e)' , 'Masa (MeV / c**2)' , 'Spin' , 'Vida media', 'Ancho de desintegración (Γ)'])
df_Bosones

"""**DATAFRAME: LEPTONES**"""

df_Leptones = pd.DataFrame({'Electrón': Electrón.lista(), 'Positrón': Positrón.lista(), 'Muon': Muon.lista(), 'Antimuón': Antimuón.lista(), 'Tau': Tau.lista(), 'Antitau': Antitau.lista(), 'Neutrino electrón': Neutrino_electrón.lista(), 'Antineutrino electrón': Antineutrino_electrón.lista(), 'Neutrino muon': Neutrino_muon.lista(), 'Antineutrino muon': Antineutrino_muon.lista(), 'Neutrino tau': Neutrino_tau.lista(), 'Antineutrino tau': Antineutrino_tau.lista()}, index=['Nombre', 'Antipartícula', 'Carga (e)' , 'Masa (MeV / c**2)' , 'Spin' , 'Vida media', 'Momento magnético', 'Longitud de desintegración (Γ)', 'Generación'])
df_Leptones

"""**DATAFRAME: QUARKS**"""

df_Quarks = pd.DataFrame({'Up': Up.lista(), 'Antiup': Antiup.lista(), 'Down': Down.lista(), 'Antidown': Antidown.lista(), 'Charm': Charm.lista(), 'Anticharm': Anticharm.lista(), 'Strange': Strange.lista(), 'Antistrange': Antistrange.lista(), 'Top': Top.lista(), 'Antitop': Antitop.lista(), 'Bottom': Bottom.lista(), 'Antibottom': Antibottom.lista()}, index=['Nombre', 'Antipartícula', 'Carga (e)' , 'Masa (MeV / c**2)' , 'Spin' , 'Isospín', 'Sabor extraño', 'Sabor encantado', 'Sabor superior', 'Sabor inferior', 'Generación'])
df_Quarks

"""Una aplicación de los datos proporcionados por las partículas es definir funciones que creen **HADRONES**, es decir, si forman mesones, se necesitan de dos quarks (quark-antiquark), extrayendo los valores de la carga para calcular la carga total del mesón; por otro lado, si forman bariones, se necesitan de tres quarks, aplicando el mismo principio."""

### La función 'Mesones' recoge dos valores (los nombres de las partículas) y por medio de condicionales arroja el nombre del mesón formado y su carga total, ocupando .carga ###
def Mesones(part1, part2):
  if part1 == Down and part2 == Antistrange:
    print('Tipo de mesón: Kaon: K(0)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Up and part2 == Antistrange:
    print('Tipo de mesón: Kaon: K(+)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Strange and part2 == Antistrange:
    print('Tipo de mesón: Eta: η´(0)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Up and part2 == Antidown:
    print('Tipo de mesón: Pion: π(+)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Down and part2 == Antiup:
    print('Tipo de mesón: Pion: π(-)')
    print('Carga total =', part1.carga + part2.carga)
  elif (part1 == Up and part2 == Antiup) or (part1 == Down and part2 == Antidown):
    print('Tipo de mesón: Pion: π(0)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Strange and part2 == Antiup:
    print('Tipo de mesón: Kaon: K(-)')
    print('Carga total =', part1.carga + part2.carga)
  elif part1 == Strange and part2 == Antidown:
    print('Tipo de mesón: Kaon: K(0)-')
    print('Carga total =', part1.carga + part2.carga)
  else:
    print('Inforación no proporconada')                ### Si no se reconoce, saldrá este mensaje.

Mesones(Down, Antiup)

Mesones(Strange, Antidown)

Mesones(Up, Up)

def Bariones(part1, part2, part3):
  if part1 == Up and part2 == Down and part3 == Down:
    print('Tipo de barión: Neutrón: n')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Up and part2 == Up and part3 == Down:
    print('Tipo de barión: Protón: p')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Down and part2 == Down and part3 == Strange:
    print('Tipo de barión: Sigma: Σ(-)')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Up and part2 == Down and part3 == Strange:
    print('Tipo de barión: Sigma: Σ(0) o Lambda: Λ(0)')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Up and part2 == Up and part3 == Strange:
    print('Tipo de barión: Sigma: Σ(+)')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Down and part2 == Strange and part3 == Strange:
    print('Tipo de barión: Xi: Ξ(-)')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  elif part1 == Up and part2 == Strange and part3 == Strange:
    print('Tipo de barión: Xi: Ξ(0)')
    print('Carga total =', part1.carga + part2.carga + part3.carga)
  else:
    print('Inforación no proporconada')

Bariones (Up, Down, Strange)

Bariones (Up, Up, Down)

"""**Ahora, Se crea una nueva clase específicamente para hadrones, en los que se destacan características como carga, spin, isospin y extrañeza.**"""

### Clase Hadron, igual hecha como en Particle ###
class Hadron:
    def __init__(self, nombre, carga, spin, isospin, extraneza):
        self.nombre = nombre
        self.carga = carga
        self.spin = spin
        self.isospin = isospin
        self.extraneza = extraneza
    def info(self):
        inf = f"Partícula: {self.nombre}\nCarga: {self.carga}\nIsospin: {self.isospin}\nExtrañeza: {self.extraneza}"
        print (inf)

class Meson(Hadron):
    type = 'Mesón'
    def __init__(self, nombre, carga, spin, isospin, extraneza):
        super().__init__(nombre, carga, spin, isospin, extraneza)
    def info(self):
        inf = f'''Partícula: {self.nombre}\nCarga (e): {self.carga}\nSpin (MeV / c**2): {self.spin}\nIsospin: {self.isospin}\nExtrañeza: {self.extraneza}\nTipo: {self.type}'''
        print (inf)
    def lista(self):
        l = [{self.nombre}, {self.carga}, {self.spin}, {self.isospin}, {self.extraneza}]
        return l

class Barion(Hadron):
    type = 'Barión'
    def __init__(self, nombre, carga, spin, isospin, extraneza):
        super().__init__(nombre, carga, spin, isospin, extraneza)
    def info(self):
        inf = f'''Partícula: {self.nombre}\nCarga (e): {self.carga}\nSpin (MeV / c**2): {self.spin}\nIsospin: {self.isospin}\nExtrañeza: {self.extraneza}\nTipo: {self.type}'''
        print (inf)
    def lista(self):
        l = [{self.nombre}, {self.carga}, {self.spin}, {self.isospin}, {self.extraneza}]
        return l

"""Se definen los **mesones** para aplicar las funciones definidas en la clase y en cada subclase."""

K_0 = Meson(nombre = 'Kaon: K(0)', carga = 0, spin = 0, isospin = -1/2, extraneza = 1)
K_mas = Meson(nombre = 'Kaon: K(+)', carga = 1, spin = 0, isospin = 1/2, extraneza = 1)
K_menos = Meson(nombre = 'Kaon: K(-)', carga = -1, spin = 0, isospin = -1/2, extraneza = -1)
K_0_menos = Meson(nombre = 'Kaon: K(0)-', carga = 0, spin = 0, isospin = 1/2, extraneza = -1)
Pion_menos = Meson(nombre = 'Pion: π(-)', carga = -1, spin = 0, isospin = -1, extraneza = 0)
Pion_0 = Meson(nombre = 'Pion: π(0)', carga = 0, spin = 0, isospin = 0, extraneza = 0)
Pion_mas = Meson(nombre = 'Pion: π(+)', carga = 1, spin = 0, isospin = 1, extraneza = 0)
Eta_0 = Meson(nombre = 'Eta: η(0)', carga = 0, spin = 0, isospin = 0, extraneza = 0)
Eta_0_prima = Meson(nombre = 'Eta: η´(0)', carga = 0, spin = 0, isospin = 0, extraneza = 0)

Eta_0_prima.info()

K_menos.info()

"""En este apartado, se definen los **bariones** de spin = 1/2."""

Neutrón = Barion(nombre = 'Neutrón: n', carga = 0, spin = 1/2, isospin = -1/2, extraneza = 0)
Protón = Barion(nombre = 'Protón: p', carga = 1, spin = 1/2, isospin = 1/2, extraneza = 0)
Sigma_menos = Barion(nombre = 'Sigma: Σ(-)', carga = -1, spin = 1/2, isospin = -1, extraneza = -1)
Sigma_0 = Barion(nombre = 'Sigma: Σ(0)', carga = 0, spin = 1/2, isospin = 0, extraneza = -1)
Sigma_mas = Barion(nombre = 'Sigma: Σ(+)', carga = 1, spin = 1/2, isospin = 1, extraneza = -1)
Lambda_0 = Barion(nombre = 'Lambda: Λ(0)', carga = 0, spin = 1/2, isospin = 0, extraneza = -1)
Xi_0 = Barion(nombre = 'Xi: Ξ(0)', carga = 0, spin = 1/2, isospin = 1/2, extraneza = -2)
Xi_menos = Barion(nombre = 'Xi: Ξ(-)', carga = -1, spin = 1/2, isospin = -1/2, extraneza = -2)

Sigma_0.info()

"""En este apartado, se definen los **bariones** de spin = 3/2."""

Delta_menos = Barion(nombre = 'Delta: Δ(-)', carga = -1, spin = 3/2, isospin = -3/2, extraneza = 0)
Delta_0 = Barion(nombre = 'Delta: Δ(0)', carga = 0, spin = 3/2, isospin = -1/2, extraneza = 0)
Delta_mas = Barion(nombre = 'Delta: Δ(+)', carga = 1, spin = 3/2, isospin = 1/2, extraneza = 0)
Delta_masmas = Barion(nombre = 'Delta: Δ(++)', carga = 2, spin = 3/2, isospin = 3/2, extraneza = 0)
Sigma_xmenos = Barion(nombre = 'Sigma vec: Σ*(-)', carga = -1, spin = 3/2, isospin = -1, extraneza = -1)
Sigma_x0 = Barion(nombre = 'Sigma vec: Σ*(0)', carga = 0, spin = 3/2, isospin = 0, extraneza = -1)
Sigma_xmas = Barion(nombre = 'Sigma vec: Σ*(+)', carga = 1, spin = 3/2, isospin = 1, extraneza = -1)
Xi_x0 = Barion(nombre = 'Xi vec: Ξ*(0)', carga = 0, spin = 3/2, isospin = 1/2, extraneza = -2)
Xi_xmenos = Barion(nombre = 'Xi vec: Ξ*(-)', carga = -1, spin = 3/2, isospin = -1/2, extraneza = -2)
Omega_menos = Barion(nombre = 'Omega: Ω(-)', carga = -1, spin = 3/2, isospin = 0, extraneza = -3)

Delta_masmas.info()

"""Se crea Dataframe para **MESONES**."""

df_Mesones = pd.DataFrame({'K(0)': K_0.lista(), 'K(+)': K_mas.lista(), 'K(-)': K_menos.lista(), 'K(0)-': K_0_menos.lista(), 'π(-)': Pion_menos.lista(), 'π(0)': Pion_0.lista(), 'π(+)': Pion_mas.lista(), 'η(0)': Eta_0.lista(), 'η´(0)': Eta_0_prima.lista()}, index=['Nombre', 'Carga (e)' , 'Spin' , 'Isospin' , 'Extrañeza'])
df_Mesones

