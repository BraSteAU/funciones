def par_impar(numero):
    if numero < 0:
        print("Ingresa un numero positivo")
    else:
        if numero%2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

num=int(input("Ingresa un numero"))
numero1=par_impar(num)
