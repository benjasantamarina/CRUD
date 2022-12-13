class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelera(self):
        self.acelera=True

    def frena(self):
        self.frena=True
    
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena}")

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"



class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    #A continuación sobreescribo el metodo estado de la clase padre

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelera} \nFrenando: {self.frena} \n {self.hcaballito}")


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

#Creo una clase bicicleta electrica con herencia multiple - Se da preferencia a la primera clase que indiques para el pase de parametros

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miMoto=Moto("Honda","CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

miBici=BicicletaElectrica("Orbea", "HJ")