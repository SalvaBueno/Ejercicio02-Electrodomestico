from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, precio=100, color='Blanco', consumo='F', peso=5,carga=5):
        Electrodomestico.__init__(self,precio,color,consumo,peso)
        self.precioBase = precio
        self.color = color
        self.comprobarConsumoEnergetico(consumo)
        self.consumoEnergetico = consumo
        self.peso = peso
        self.carga=carga

    def getCarga(self):
        return self.Carga

    def precioFinal(self):
        self.fina = Electrodomestico.precioFinal(self)
        if self.carga>30:
            self.fina=+50
        return self.fina

