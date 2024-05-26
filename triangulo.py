numero = int(input("Ingrese un numero entero:"))
renglones = int(input("Ingrese la cantidad de renglones del triangulo: "))
for i in range(renglones + 1):
    print(f"{numero} " * i)
