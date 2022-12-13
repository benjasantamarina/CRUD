class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#Creo una funcion

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


vehiculo5=Camion()

desplazamientoVehiculo(vehiculo5)



