def año_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False


usuario = int(input("Ingrese un año: "))
if año_bisiesto(usuario):
    print(f"{usuario} es un año bisiesto.")
else:
    print(f"{usuario} no es un año bisiesto.")
