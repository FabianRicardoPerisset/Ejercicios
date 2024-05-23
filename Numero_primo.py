usuario = int(input("Ingrese un numero y le dire si es primo: "))
numero_primo = usuario % 2
if numero_primo == 0:
    print(f"El numero {usuario} no es primo")
else:
    print(f"El numero {usuario} es primo")
