def factorial(n):
    f=1
    for num in range(1,n+1):
        f*=num
    print(f"El factorial de {n} es: {f}")

numero=int(input("Ingrese un numero: "))
factorial(numero)
