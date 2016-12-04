from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

class Ejecutable():

    def exe(self):
        listaElec = []
        listaElec.append(Electrodomestico(400,'Amarillo','A',30))
        listaElec.append(Lavadora(250,'Blanco','F',55))
        listaElec.append(Television())
        listaElec.append(Lavadora())
        listaElec.append(Electrodomestico())
        listaElec.append(Television())
        listaElec.append(Lavadora())
        listaElec.append(Electrodomestico())
        listaElec.append(Electrodomestico())
        listaElec.append(Television())

        FinalElec = 0
        FinalLava = 0
        FinalTele = 0

        for i in listaElec:
            if(isinstance(i,Electrodomestico)):
                FinalElec+=i.precioFinal()
            if(isinstance(i,Lavadora)):
                FinalLava+=i.precioFinal()
            if(isinstance(i,Television)):
                FinalTele+=i.precioFinal()

        print ("Los electrodomesticos tienen un precio total de "+str(FinalElec))
        print ("Las Lavadoras tienen un precio total de "+ str(FinalLava))
        print ("Las Televisiones tienen un precio total de " +str(FinalTele))

run = Ejecutable()
run.exe()