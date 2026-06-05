def chatbot_principal():
    mostrar_cabecera()

    empleados = cargar_empleados()

    while True:

        opcion = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()

        if opcion.lower() not in ["si", "s", "sí", "iniciar"]:
            continue

        solicitud_activa = True

        id_empleado = ""
        nombre_empleado = ""
        dias_disponibles = 0
        dias_solicitados = 0
        fecha_inicio = ""

        while solicitud_activa:

            id_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip().upper()

            if id_input not in empleados:
                continue

            id_empleado = id_input
            nombre_empleado = empleados[id_input]["nombre"]
            dias_disponibles = empleados[id_input]["disponibles"]

            if dias_disponibles <= 0:
                solicitud_activa = False
                break

            # --- DIAS ---
            while True:

                dias_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()

                try:
                    dias_solicitados = int(dias_input)
                    if dias_solicitados <= 0:
                        continue
                except ValueError:
                    continue

                if dias_solicitados > dias_disponibles:
                    continue

                break

            # --- FECHA ---
            while True:

                fecha_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()

                es_valida, resultado = validar_fecha(fecha_input)

                if es_valida:
                    fecha_inicio = resultado
                    break

            break