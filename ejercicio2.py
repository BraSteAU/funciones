#creamos una funcion que determine el mayor numero de tres
def mayor(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} es mayor que {num2} y {num3}")
    elif num2>num3 and num2>num3:
        print(f"{num2} es mayor que {num1} y {num3}")
    else:
        print(f"{num3} es mayor que {num1} y {num2}")

num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
num3=int(input("Ingrese el tercer numero"))
numeros=mayor(num1,num2,num3)