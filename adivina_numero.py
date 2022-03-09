import random

def main():
    intentos = 1
    x = 0
    numero_bot = random.randint(1,100)
    lista = []
    while True:
        tu_numero = int(input("Dime un numero: \n"))
        if (tu_numero == numero_bot):
            lista.append(tu_numero)
            print("Has acertado con {} intentos".format(intentos))
            for i in lista:
                x += 1
                print("en el intento {} has dicho el numero {}".format(x, i))
            break
        elif (intentos == 5):
            lista.append(tu_numero)
            print("Has perdido")
            print("El número era {}".format(numero_bot))
            for i in lista:
                x += 1
                print("en el intento {} has dicho el numero {}".format(x, i))
            break
        elif(tu_numero < numero_bot):
            print("Demasiado bajo")
            lista.append(tu_numero)
            intentos += 1
        elif(tu_numero > numero_bot):
            print("Demasiado alto")
            lista.append(tu_numero)
            intentos += 1

main()
m = str(input("Quieres volver a jugar? \n "))
while m != "no":
    main()
    m = str(input("Quieres volver a jugar? \n "))
