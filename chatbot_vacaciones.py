# --- FLUJO PRINCIPAL Conversacional (MÁQUINA DE ESTADOS) ---

def chatbot_principal():
    mostrar_cabecera()

    empleados = cargar_empleados()

    bot_imprimir("👋 ¡Hola! Soy el asistente virtual de Recursos Humanos de la empresa.")
    bot_imprimir("Estoy acá para ayudarte a registrar tu **Solicitud de Vacaciones** de forma digital.")

    while True:

        # --- ESTADO 1: INICIO DEL PROCESO ---
        bot_imprimir("¿Querés registrar una nueva solicitud de vacaciones? (si / /ayuda):")

        opcion = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()

        if opcion.lower() == "/ayuda":
            mostrar_ayuda()
            continue

        elif opcion.lower() == "/empleados":
            mostrar_empleados_consola(empleados)
            continue

        elif opcion.lower() == "/cancelar":
            bot_imprimir("No hay ninguna solicitud activa para cancelar actualmente.")
            continue

        if opcion.lower() not in ["si", "s", "sí", "iniciar"]:
            bot_imprimir("Entendido. Quedo a tu disposición.")
            continue

        solicitud_activa = True