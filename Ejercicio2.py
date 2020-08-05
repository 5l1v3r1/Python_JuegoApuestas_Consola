# import libs
from random import randrange
import time
from os import system


# Declaración de variables


def IngreseDinero(saldo):
    system("cls")
    saldo = input("Ingrese su saldo para jugar : ")
    return saldo


def Jugar(saldo):
    system("cls")

    if saldo == 0:
        print("Usted no tiene saldo, vuelva al menú")
        time.sleep(2)
        Menu(saldo)
    else:
        system("cls")
        print("Jugar Suerte")
        pass


    print("Su saldo es de: " + str(saldo))
    print("Se mostrará el juego en 2 segundos:")
    time.sleep(2)

    matriz = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
        ##[randrange(10),randrange(10),randrange(10)]
    ]
    print("\n")
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print("\n\n")

    def VerificaHorizontalUnidad():
        valor = False
        if matriz[0][0] == matriz[0][1] and matriz[0][2] == matriz[0][0]:
            valor = True
            # print("1 Verifica Horizontal TRUE")
        else:
            pass
            # print("1 Verifica Horizontal FALSE")

        if matriz[1][0] == matriz[1][1] and matriz[1][2] == matriz[1][0]:
            valor = True
            # print("2 Verifica Horizontal TRUE")
        else:
            pass
            # print("2 Verifica Horizontal FALSE")

        if matriz[2][0] == matriz[2][1] and matriz[2][2] == matriz[2][0]:
            valor = True
            # print("3 Verifica Horizontal TRUE")
        else:
            pass
            # print("3 Verifica Horizontal FALSE")
        return valor
    def VerificaVertical():
        valor = True
        if matriz[0][0] == matriz[1][0] and matriz[2][0] == matriz[0][0]:
            pass
            # print("1 Verifica Vertical TRUE")
        else:
            valor = False
            #print("1 Verifica Vertical FALSE")

        if matriz[0][1] == matriz[1][1] and matriz[2][1] == matriz[0][1]:
            pass
            #print("2 Verifica Vertical TRUE")
        else:
            valor = False
            #print("2 Verifica Vertical FALSE")

        if matriz[0][2] == matriz[1][2] and matriz[2][2] == matriz[0][2]:
            pass
            #print("2 Verifica Vertical TRUE")
        else:
            valor = False
            #print("3 Verifica Vertical FALSE")
        return valor

    def VerificaHorizontal():
        valor = True
        if matriz[0][0] == matriz[0][1] and matriz[0][2] == matriz[0][0]:
            pass
            #print("1 Verifica Horizontal TRUE")
        else:
            valor = False
            #print("1 Verifica Horizontal FALSE")

        if matriz[1][0] == matriz[1][1] and matriz[1][2] == matriz[1][0]:
            pass
            #print("2 Verifica Horizontal TRUE")
        else:
            valor = False
            #print("2 Verifica Horizontal FALSE")

        if matriz[2][0] == matriz[2][1] and matriz[2][2] == matriz[2][0]:
            pass
            #print("3 Verifica Horizontal TRUE")
        else:
            valor = False
            #print("3 Verifica Horizontal FALSE")
        return valor

    def VerificaIntermedio():
        valor = True
        if matriz[0][0] == matriz[1][1] and matriz[2][2] == matriz[0][0]:
            pass
            #print("1 Verifica Intermedio TRUE")
        else:
            valor = False
            #print("1 Verifica Intermedio FALSE")

        if matriz[2][0] == matriz[1][1] and matriz[0][2] == matriz[2][0]:
            pass
            #print("2 Verifica Intermedio TRUE")
        else:
            valor = False
            #print("2 Verifica Intermedio FALSE")

        return valor

    if VerificaHorizontal() and VerificaIntermedio() and VerificaVertical():
        print("Ganó Apuesta X7")
        saldo = saldo * 7
    elif VerificaIntermedio():
        print("Usted Gano Apuesta X5")
        saldo = saldo *5
    elif VerificaHorizontal():
        print("Usted Gano Apuesta X3")
        saldo = saldo *3
    elif VerificaHorizontalUnidad():
        print("Usted Gano Apuesta X3")
        saldo = saldo *1

    print("Finalizó juego.\nVolviendo al menú en 10 segundos...")
    time.sleep(10)
    return saldo


def SacarDinero(saldo):
    system("cls")
    print("El dinero en total es: " + str(saldo))
    return saldo


def Menu(saldo):
    print("1. Ingrese Dinero")
    print("2. Jugar")
    print("3. Sacar Dinero")

    de = input("Ingrese una opción: ")

    if de == "1":
        saldo = IngreseDinero(saldo)
        Menu(saldo)
    elif de == "2":
        saldo = Jugar(saldo)
        Menu(saldo)
    elif de == "3":
        saldo = SacarDinero(saldo)
    elif de != "1" or de != "2" or de != "3":
        system("cls")
        Menu(saldo)


if __name__ == '__main__':
    saldo = 0
    Menu(saldo)
