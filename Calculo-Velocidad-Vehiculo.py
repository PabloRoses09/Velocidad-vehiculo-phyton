#
tipodedato = 0
tipodedato2 = 0
distancia = 0
tiempo = 0 
div = 0
div1 = 0
print("\n","\nEl siguiente programa saca la velocidad en Kilometros de un Vehiculo\n")
i = input("----------------Presione [ Enter ] Para Continuar-----------------\n")

def pregunta1():
    global tipodedato, distancia
    print("\nPorfavor seleccione si el calculo de la DISTANCIA esta en kilometro o metros.\n \n0: Metros\n \n1: Kilometros\n")
    tipodedato = int(input())
    if tipodedato == 0 or tipodedato == 1:
        print("\nDato Agregado Correctamente\n")
        if tipodedato == 0:
            print("\nDigite los Metros")
            distancia = float(input())
        if tipodedato == 1:
            print("\nDigite los Kilometros")
            distancia = float(input())
    else:
        print("\nDato Incorrecto Intente De Nuevo")
        pregunta1()

def pregunta2():
    global tipodedato2,tiempo
    print("\nSeleccione si el calculo del TIEMPO es en minutos o horas\n \n0: Segundos\n \n1: Minutos\n \n2: Horas\n")
    tipodedato2 = int(input())
    if tipodedato2 == 0 or tipodedato2 == 1 or tipodedato2 == 2:
        print("\nDato Agregado Correctamente")
        if tipodedato2 == 0:
            print("\nDigite los Segundos")
            tiempo = float(input())
        if tipodedato2 == 1:
            print("\nDigite los Minutos")
            tiempo = float(input())
        if tipodedato2 == 2:
            print("\nDigite las Horas")
            tiempo = float(input())
    else:
        print("\nDato Incorrecto Intente De Nuevo")
        pregunta2()


def calculovelocidad():
    global tipodedato2, tipodedato, tiempo, distancia
    print("\nA continuacion se le va a generar el calculo de la velocidad\n", tipodedato, tipodedato2)
    i = input("Presine [ Enter ] Para Continuar")
    if tipodedato == 0 and tipodedato2 == 0:
        div = distancia / tiempo * 1 / 1000 * 3600 / 1
    if tipodedato == 0 and tipodedato2 == 1:
        div = distancia / tiempo * 1 / 1000 * 60 / 1
    if tipodedato == 0 and tipodedato2 == 2:
        div = distancia / tiempo * 1 / 1000
    if tipodedato == 1 and tipodedato2 == 0:
        div = distancia / tiempo * 1 / 1 * 3600 / 1
    if tipodedato == 1 and tipodedato2 == 1:
        div = distancia / tiempo * 60 / 1
    if tipodedato == 1 and tipodedato2 == 2:
        div = distancia / tiempo 
    #------------------------------------------------------------------
    div = round(div,2)
    print("\nLa velocidad del vehiculo es de {}km/h" .format(div))


if __name__ == "__main__":
    pregunta1()
    pregunta2()
    calculovelocidad()