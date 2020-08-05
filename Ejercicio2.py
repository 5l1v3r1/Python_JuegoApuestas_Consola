# import libs
from random import randrange
import time
from os import system

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
    apuesta = 0
    def apostar(apuesta):
        print("Escoja una apuesta")
        print(">>  1.          X1")
        print(">>  3.          X3")
        print(">>  5.          X5")
        print(">>  7.          X7")

        de = input("Ingrese su número de apuesta: ")

        if de == "1":
            apuesta = 1
        elif de == "3":
            apuesta = 3
        elif de == "5":
            apuesta = 5
        elif de == "7":
            apuesta = 7
        elif de != "1" or de != "3" or de != "5" or de != "7":
            system("cls")
            apostar("")
        return apuesta


    def Juego(saldo,apuesta):
        print("Su saldo es de: " + str(saldo))
        print("Se mostrará el juego en 2 segundos:")
        print("Su apuesta es: X"+str(apuesta))
        time.sleep(2)

        matriz = [
            ##[2, 2, 2],
            #[2, 2, 2],
            #[2, 2, 2]
            [randrange(10), randrange(10), randrange(10)],
            [randrange(10), randrange(10), randrange(10)],
            [randrange(10), randrange(10), randrange(10)]
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
                # print("1 Verifica Vertical FALSE")

            if matriz[0][1] == matriz[1][1] and matriz[2][1] == matriz[0][1]:
                pass
                # print("2 Verifica Vertical TRUE")
            else:
                valor = False
                # print("2 Verifica Vertical FALSE")

            if matriz[0][2] == matriz[1][2] and matriz[2][2] == matriz[0][2]:
                pass
                # print("2 Verifica Vertical TRUE")
            else:
                valor = False
                # print("3 Verifica Vertical FALSE")
            return valor

        def VerificaHorizontal():
            valor = True
            if matriz[0][0] == matriz[0][1] and matriz[0][2] == matriz[0][0]:
                pass
                # print("1 Verifica Horizontal TRUE")
            else:
                valor = False
                # print("1 Verifica Horizontal FALSE")

            if matriz[1][0] == matriz[1][1] and matriz[1][2] == matriz[1][0]:
                pass
                # print("2 Verifica Horizontal TRUE")
            else:
                valor = False
                # print("2 Verifica Horizontal FALSE")

            if matriz[2][0] == matriz[2][1] and matriz[2][2] == matriz[2][0]:
                pass
                # print("3 Verifica Horizontal TRUE")
            else:
                valor = False
                # print("3 Verifica Horizontal FALSE")
            return valor

        def VerificaIntermedio():
            valor = True
            if matriz[0][0] == matriz[1][1] and matriz[2][2] == matriz[0][0]:
                pass
                # print("1 Verifica Intermedio TRUE")
            else:
                valor = False
                # print("1 Verifica Intermedio FALSE")

            if matriz[2][0] == matriz[1][1] and matriz[0][2] == matriz[2][0]:
                pass
                # print("2 Verifica Intermedio TRUE")
            else:
                valor = False
                # print("2 Verifica Intermedio FALSE")

            return valor
        if apuesta == 7:
            if VerificaHorizontal() and VerificaIntermedio() and VerificaVertical():
                print("Ganó Apuesta X7")
                saldo = int(saldo) + 7000
            else:
                print("Usted perdió la Apuesta X7")
                saldo = int(saldo) - 7000
        else:
            pass

        if apuesta == 5:
            if VerificaIntermedio():
                print("Ganó Apuesta X5")
                saldo = int(saldo) + 5000
            else:
                print("Usted perdió la Apuesta X5")
                saldo = int(saldo) -5000

        if apuesta == 3:
            if VerificaHorizontal():
                print("Ganó Apuesta X3")
                saldo = int(saldo) + 1000
            else:
                print("Usted perdió la Apuesta X3")
                saldo = int(saldo) - 1000
        if apuesta == 1:
            if VerificaHorizontalUnidad():
                print("Ganó Apuesta X1")
                saldo = int(saldo) + 500
            else:
                print("Usted perdió la Apuesta X1")
                saldo = int(saldo) - 500
        return saldo

    apuesta = apostar(apuesta)
    saldo = Juego(saldo,apuesta)
    print("Su saldo es de: "+str(saldo))
    print("Finalizó juego.\nVolviendo al menú en 10 segundos...")
    time.sleep(10)
    return saldo


def SacarDinero(saldo):
    system("cls")
    print("El dinero en total es: " + str(saldo))
    return saldo


def Menu(saldo):
    print(">>  1. Ingrese Dinero")
    print(">>  2. Jugar")
    print(">>  3. Sacar Dinero")

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
