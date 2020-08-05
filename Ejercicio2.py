# import libs
from random import randrange
import time
from os import system

# Declaración de variables



def IngreseDinero(saldo):
    print("Ingrese Dinero")
    saldo = input("Ingrese su saldo")

def Jugar(saldo):
    print("Jugar")

    print("Su saldo es de: " + str(saldo))
    time.sleep(1)

    matriz = [
        [2, 6, 2],
        [2, 2, 2],
        [2, 2, 2]
        ##[randrange(10),randrange(10),randrange(10)]
    ]

    print(matriz)
    print("\n")
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print("\n\n")

    def VerificaVertical():
        valor = True
        if matriz[0][0] == matriz[1][0] and matriz[2][0] == matriz[0][0]:
            print("1 Verifica Vertical TRUE")
        else:
            valor = False
            print("1 Verifica Vertical FALSE")

        if matriz[0][1] == matriz[1][1] and matriz[2][1] == matriz[0][1]:
            print("2 Verifica Vertical TRUE")
        else:
            valor = False
            print("2 Verifica Vertical FALSE")

        if matriz[0][2] == matriz[1][2] and matriz[2][2] == matriz[0][2]:
            print("2 Verifica Vertical TRUE")
        else:
            valor = False
            print("3 Verifica Vertical FALSE")
        return valor

    def VerificaHorizontal():
        valor = True
        if matriz[0][0] == matriz[0][1] and matriz[0][2] == matriz[0][0]:
            print("1 Verifica Horizontal TRUE")
        else:
            valor = False
            print("1 Verifica Horizontal FALSE")

        if matriz[1][0] == matriz[1][1] and matriz[1][2] == matriz[1][0]:
            print("2 Verifica Horizontal TRUE")
        else:
            valor = False
            print("2 Verifica Horizontal FALSE")

        if matriz[2][0] == matriz[2][1] and matriz[2][2] == matriz[2][0]:
            print("3 Verifica Horizontal TRUE")
        else:
            valor = False
            print("3 Verifica Horizontal FALSE")
        return valor

    def VerificaIntermedio():
        valor = True
        if matriz[0][0] == matriz[1][1] and matriz[2][2] == matriz[0][0]:
            print("1 Verifica Intermedio TRUE")
        else:
            valor = False
            print("1 Verifica Intermedio FALSE")

        if matriz[2][0] == matriz[1][1] and matriz[0][2] == matriz[2][0]:
            print("2 Verifica Intermedio TRUE")
        else:
            valor = False
            print("2 Verifica Intermedio FALSE")

        return valor

    if VerificaHorizontal() and VerificaIntermedio() and VerificaVertical():
        print("Ganó Apuesta X7")
    else:
        print("No Gano X/")


def SacarDinero(saldo):
    print("Sacar Dinero")


def Menu():
    print("1. Ingrese Dinero")
    print("2. Jugar")
    print("3. Sacar Dinero")
    de = 0
    saldo = 0
    def m():
        try:
            de = int(input("Ingrese una opción: "))
        except:
            m()
    m()

    IngreseDinero(saldo) if de == 1 else False
    Jugar(saldo) if de == 2 else False
    SacarDinero(saldo) if de == 3 else False
    Menu() if de != 1 or de != 2 or de != 3 else False



if __name__ == '__main__':
    Menu()




