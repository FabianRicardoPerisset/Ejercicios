hora_actual = int(input("Introduzca la hora actual en formato 24 horas: "))
numero_entero = int(input("Introduzca un numero entero:"))
nueva_hora = hora_actual + numero_entero % 24
print(f"En {numero_entero} horas, seran las {nueva_hora} horas.")