from Electrodomestico import Electrodomestico

class Television(Electrodomestico):
    def __init__(self, precio=100, color='Blanco', consumo='F', peso=5,resolucion=20,fourK=False):
        Electrodomestico.__init__(self,precio,color,consumo,peso)
        self.fourK = fourK
        self.resolucion = resolucion

    def getResolucion(self):
        return self.resolucion
    def getfourK(self):
        return self.fourK

    def precioFinal(self):
        self.final = Electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.final = (self.final*0.3) + self.final
        if self.fourK == True:
            self.final=self.final +50
        return self.final
