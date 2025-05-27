def celsius_fahrenheit(celcius):
    f=celcius*1.8+32
    print(f"Grados celcius: {celcius} / grados fahrenheit: {f}")

grado=float(input("Ingrese temperatura en grados celcius: "))
celsius_fahrenheit(grado)