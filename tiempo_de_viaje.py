def tiempo_de_viaje():
    total_de_minutos = 0
    while True:
        usuario = int(input("Ingrese el tiempo por tramos en minutos, "
                            "0 cuando llegue a destino: "))
        if usuario == 0:
            break
        total_de_minutos += usuario
    horas = total_de_minutos // 60
    minutos = total_de_minutos % 60
    print(f"El tiempo total de viaje es de {horas} horas y {minutos} minutos.")


tiempo_de_viaje()