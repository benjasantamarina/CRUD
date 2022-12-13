class Coche():
  
    def __init__(self):
    
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4  # el doble guion bajo: Encapsulamiento de la variable para que no sea accesible desde fuera de la clase
        self.__en_marcha=False

    def arrancar(self, arrancamos):
        self.__en_marcha=arrancamos

        if (self.__en_marcha):
            chequeo=self.__chequeo_interno()

        if (self.__en_marcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__en_marcha and chequeo==False):
            return "Algo ha salido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta detenido"

    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

        
   

mi_coche=Coche()   #Instanciar una clase

print(mi_coche.arrancar(True))
mi_coche.estado()

print("---------------A continuacion creamos el segundo objeto---------------------")

mi_coche2=Coche()

print(mi_coche2.arrancar(False))
mi_coche2.__ruedas=2
mi_coche2.estado()

