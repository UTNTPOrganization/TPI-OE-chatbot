# -*- coding: utf-8 -*-
"""
Trabajo Práctico Integrador — Organización Empresarial
Cátedra: Organización Empresarial (TUPaD - UTN)
Tema: Simulador de Chatbot de Vacaciones con Persistencia en Archivos de Texto (.txt)
"""

import os
import time
from datetime import datetime

# --- PALETA DE COLORES ANSI PARA CONSOLA PREMIUM ---
# Proporciona una interfaz visual de alto nivel directamente en la terminal
COLOR_RESET = "\033[0m"
COLOR_BOT = "\033[1;36m"       # Cian brillante para el Bot
COLOR_USER = "\033[1;32m"      # Verde para el Usuario
COLOR_SYS = "\033[1;35m"       # Violeta/Muted para acciones del Sistema
COLOR_ALERT = "\033[1;33m"     # Amarillo para Advertencias
COLOR_ERROR = "\033[1;31m"     # Rojo para Errores y Cancelaciones
COLOR_TITLE = "\033[1;37;44m"  # Blanco con fondo Azul para Títulos

# --- FUNCIONES DE PERSISTENCIA (MANEJO DE ARCHIVOS .TXT) ---

def cargar_empleados():
    """
    Lee la base de datos de empleados del archivo 'empleados.txt'
    Formato del archivo: ID|Nombre|DiasTotales|DiasConsumidos|DiasDisponibles
    """
    empleados = {}
    if not os.path.exists("empleados.txt"):
        # Crear archivo con datos por defecto si no existe
        crear_empleados_defecto()
        
    try:
        with open("empleados.txt", "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split('|')
                if len(partes) == 5:
                    emp_id, nombre, totales, consumidos, disponibles = partes
                    empleados[emp_id] = {
                        "id": emp_id,
                        "nombre": nombre,
                        "totales": int(totales),
                        "consumidos": int(consumidos),
                        "disponibles": int(disponibles)
                    }
    except Exception as e:
        print(f"{COLOR_ERROR}Error al leer empleados.txt: {e}{COLOR_RESET}")
    return empleados

def guardar_empleados(empleados):
    """
    Guarda los datos actualizados de los empleados en 'empleados.txt'
    """
    try:
        with open("empleados.txt", "w", encoding="utf-8") as f:
            for emp in empleados.values():
                linea = f"{emp['id']}|{emp['nombre']}|{emp['totales']}|{emp['consumidos']}|{emp['disponibles']}\n"
                f.write(linea)
    except Exception as e:
        print(f"{COLOR_ERROR}Error al guardar en empleados.txt: {e}{COLOR_RESET}")

def registrar_solicitud(emp_id, nombre, dias, fecha_inicio, estado="APROBADA"):
    """
    Registra una solicitud de vacaciones en el archivo histórico 'solicitudes.txt'.
    Genera un ID correlativo SOL001, SOL002, etc.
    """
    if not os.path.exists("solicitudes.txt"):
        with open("solicitudes.txt", "w", encoding="utf-8") as f:
            f.write("IDSolicitud|IDEmpleado|Nombre|DiasSolicitados|FechaInicio|Estado|FechaRegistro\n")
            
    try:
        # Contar líneas existentes para generar el ID correlativo
        with open("solicitudes.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            # Cantidad de solicitudes = Total de líneas menos la cabecera
            cant_sols = len(lineas) - 1 if len(lineas) > 0 else 0
            
        sol_id = f"SOL{cant_sols + 1:03d}"
        fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Escribir la solicitud al final del archivo (modo 'a' de append)
        with open("solicitudes.txt", "a", encoding="utf-8") as f:
            linea = f"{sol_id}|{emp_id}|{nombre}|{dias}|{fecha_inicio}|{estado}|{fecha_registro}\n"
            f.write(linea)
            
        return sol_id
    except Exception as e:
        print(f"{COLOR_ERROR}Error al registrar en solicitudes.txt: {e}{COLOR_RESET}")
        return "SOL999"

def crear_empleados_defecto():
    """
    Crea el archivo inicial 'empleados.txt' con datos semilla de la UTN
    """
    datos_semilla = [
        "EMP001|Juan Perez|10|0|10\n",
        "EMP002|Ana Lopez|20|6|14\n",
        "EMP003|Carlos Gomez|15|15|0\n",
        "EMP004|Maria Rodriguez|30|12|18\n",
        "EMP005|Sofia Martinez|14|4|10\n"
    ]
    with open("empleados.txt", "w", encoding="utf-8") as f:
        f.writelines(datos_semilla)

# --- FUNCIONES DE SOPORTE DEL CHATBOT ---

def bot_imprimir(mensaje):
    """
    Imprime un mensaje simulando el efecto de escritura del Bot
    """
    print(f"\n{COLOR_BOT}[HR-Bot]:{COLOR_RESET}", end=" ")
    # Simular una pequeña pausa para simular escritura y dar fluidez
    time.sleep(0.4)
    print(mensaje)

def sys_imprimir(mensaje):
    """
    Imprime mensajes técnicos del sistema
    """
    print(f"{COLOR_SYS}[Sistema-DB]: {mensaje}{COLOR_RESET}")

def validar_fecha(fecha_str):
    """
    Valida el formato de fecha (DD/MM/AAAA) y que sea estrictamente futura.
    Utiliza try-except para robustecer el control de errores de la biblioteca datetime.
    """
    try:
        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
        hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if fecha_obj <= hoy:
            return False, "La fecha de inicio de vacaciones debe ser estrictamente en el futuro."
        return True, fecha_str
    except ValueError:
        return False, "Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/12/2026)."

# --- MENÚS DE INFORMACIÓN RAPIDA EN CONSOLA ---

def mostrar_cabecera():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 65)
    print(f"{COLOR_TITLE}    UTN TUPaD - TRABAJO PRÁCTICO INTEGRADOR - ORGANIZACIÓN EMPRESARIAL    {COLOR_RESET}")
    print("=" * 65)
    print(f" {COLOR_SYS}* Base de Datos persistida localmente en archivos de texto (.txt){COLOR_RESET}")
    print(f" {COLOR_SYS}* Comandos globales en el chat: /ayuda, /empleados, /cancelar{COLOR_RESET}")
    print("=" * 65)

def mostrar_ayuda():
    print(f"\n{COLOR_ALERT}--- 🛠️ GUÍA DE COMANDOS DEL CHATBOT ---{COLOR_RESET}")
    print(" Puedes escribir estos comandos en cualquier momento de la charla:")
    print("  • /empleados  -> Muestra la lista de empleados y sus días disponibles.")
    print("  • /cancelar   -> Cancela la solicitud en curso y vuelve al menú inicial.")
    print("  • /ayuda      -> Muestra esta guía informativa de soporte.")
    print("-" * 45)

def mostrar_empleados_consola(empleados):
    print(f"\n{COLOR_SYS}--- 📋 ESTADO DE DÍAS DE VACACIONES DE EMPLEADOS (empleados.txt) ---{COLOR_RESET}")
    print(f"{'ID':<8} | {'Nombre y Apellido':<18} | {'Totales':<7} | {'Consumidos':<10} | {'Disponibles':<11}")
    print("-" * 65)
    for emp in empleados.values():
        disponibles_color = COLOR_USER if emp['disponibles'] > 0 else COLOR_ERROR
        print(f"{emp['id']:<8} | {emp['nombre']:<18} | {emp['totales']:^7} | {emp['consumidos']:^10} | {disponibles_color}{emp['disponibles']:^11}{COLOR_RESET}")
    print("-" * 65)



# --- FLUJO PRINCIPAL Conversacional (MÁQUINA DE ESTADOS) ---

def chatbot_principal():
    mostrar_cabecera()
    
    # Carga de la BD inicial desde archivos
    empleados = cargar_empleados()
    
    bot_imprimir("👋 ¡Hola! Soy el asistente virtual de Recursos Humanos de la empresa.")
    bot_imprimir("Estoy acá para ayudarte a registrar tu **Solicitud de Vacaciones** de forma digital.")
    
    while True:
        # --- ESTADO 1: INICIO DEL PROCESO ---
        bot_imprimir("¿Querés registrar una nueva solicitud de vacaciones? (Escribí 'si' para iniciar, o '/ayuda'):")
        
        opcion = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()
        
        # Procesar comandos globales
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
            bot_imprimir("Entendido. Quedo a tu disposición si cambiás de opinión. ¡Que tengas un buen día!")
            time.sleep(1.5)
            continue
            
        # --- ESTADO 2: SOLICITUD DE ID DE EMPLEADO (BPMN: Tarea Usuario) ---
        solicitud_activa = True
        id_empleado = ""
        nombre_empleado = ""
        dias_disponibles = 0
        
        while solicitud_activa:
            bot_imprimir("Excelente. Comencemos el trámite. Por favor, **ingresá tu ID de empleado** (ej: EMP002) o '/cancelar' para salir:")
            id_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip().upper()
            
            if id_input == "/CANCELAR":
                bot_imprimir("❌ Solicitud abortada por el usuario.")
                solicitud_activa = False
                break
            elif id_input == "/AYUDA":
                mostrar_ayuda()
                continue
            elif id_input == "/EMPLEADOS":
                mostrar_empleados_consola(empleados)
                continue
            
            # BPMN: Tarea Servicio - Validar ID en archivo de texto
            sys_imprimir(f"Validando ID '{id_input}' en empleados.txt...")
            time.sleep(0.6)
            
            if id_input in empleados:
                # ID Correcto - Gateway Sí
                id_empleado = id_input
                nombre_empleado = empleados[id_input]["nombre"]
                dias_disponibles = empleados[id_input]["disponibles"]
                
                bot_imprimir(f"✅ ID Verificado con éxito.")
                bot_imprimir(f"Empleado: {nombre_empleado}.")
                bot_imprimir(f"Saldo disponible: {dias_disponibles} días de vacaciones.")
                
                # Camino infeliz automático: Tiene 0 días
                if dias_disponibles <= 0:
                    bot_imprimir("⚠️ Rechazo Automático: Tu saldo de días es 0. No podés continuar con la solicitud.")
                    solicitud_activa = False
                    break
                break
            else:
                # ID Incorrecto - Gateway No (Camino Infeliz / Robustez)
                bot_imprimir(f"❌ Error: El ID de empleado '{id_input}' no figura en el archivo. Por favor, reintentalo.")
        
        if not solicitud_activa:
            continue
            
        # --- ESTADO 3: SOLICITUD DE CANTIDAD DE DÍAS (BPMN: Tarea Usuario) ---
        dias_solicitados = 0
        while solicitud_activa:
            bot_imprimir("¿**Cuántos días** de vacaciones querés solicitar?")
            dias_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()
            
            if dias_input.upper() == "/CANCELAR":
                bot_imprimir("❌ Solicitud abortada por el usuario.")
                solicitud_activa = False
                break
            elif dias_input.upper() == "/AYUDA":
                mostrar_ayuda()
                continue
            elif dias_input.upper() == "/EMPLEADOS":
                mostrar_empleados_consola(empleados)
                continue
                
            # ROBUSTEZ: Validar que sea un número entero (try-except)
            try:
                dias_solicitados = int(dias_input)
                if dias_solicitados <= 0:
                    bot_imprimir("⚠️ El número de días debe ser un entero positivo mayor a 0.")
                    continue
            except ValueError:
                bot_imprimir("⚠️ Entrada inválida. Por favor, ingresá únicamente números enteros (ej: 5).")
                continue
                
            # BPMN: Tarea Servicio - Validar Saldo de Días
            sys_imprimir(f"Validando saldo: Solicitados {dias_solicitados} vs. Disponibles {dias_disponibles}...")
            time.sleep(0.5)
            
            if dias_solicitados <= dias_disponibles:
                # Saldo Suficiente - Gateway Sí
                bot_imprimir(f"✅ Saldo suficiente. Se pre-autorizan {dias_solicitados} días.")
                break
            else:
                # Saldo Insuficiente - Gateway No (Camino Infeliz)
                bot_imprimir(f"❌ Rechazo: No tenés saldo de días suficiente.")
                bot_imprimir(f"Pediste {dias_solicitados} días pero solo disponés de {dias_disponibles} días.")
                bot_imprimir("Por favor, ingresá una cantidad menor o igual a tu saldo.")

        if not solicitud_activa:
            continue

        # --- ESTADO 4: SOLICITUD DE FECHA DE INICIO (BPMN: Tarea Usuario) ---
        fecha_inicio = ""
        while solicitud_activa:
            bot_imprimir("¿En qué fecha querés iniciar tus vacaciones? (Formato: **DD/MM/AAAA**, ej: 15/12/2026):")
            fecha_input = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip()
            
            if fecha_input.upper() == "/CANCELAR":
                bot_imprimir("❌ Solicitud abortada por el usuario.")
                solicitud_activa = False
                break
            elif fecha_input.upper() == "/AYUDA":
                mostrar_ayuda()
                continue
            elif fecha_input.upper() == "/EMPLEADOS":
                mostrar_empleados_consola(empleados)
                continue
                
            # ROBUSTEZ: Validar fecha (Formato y Futura)
            sys_imprimir("Validando fecha ingresada...")
            time.sleep(0.5)
            es_valida, resultado = validar_fecha(fecha_input)
            
            if es_valida:
                # Fecha Correcta - Gateway Sí
                fecha_inicio = resultado
                bot_imprimir(f"✅ Fecha fijada correctamente para el: {fecha_inicio}.")
                break
            else:
                # Fecha Incorrecta - Gateway No (Camino Infeliz)
                bot_imprimir(f"❌ Error en fecha: {resultado}")

        if not solicitud_activa:
            continue

        # --- ESTADO 5: CONFIRMACIÓN FINAL (BPMN: Gateway ¿Acepta?) ---
        while solicitud_activa:
            bot_imprimir("Por favor, confirmá los datos de tu solicitud antes de grabarla:")
            print(f"  {COLOR_SYS}• Empleado:{COLOR_RESET} {nombre_empleado} ({id_empleado})")
            print(f"  {COLOR_SYS}• Días Solicitados:{COLOR_RESET} {dias_solicitados} días")
            print(f"  {COLOR_SYS}• Fecha de Inicio:{COLOR_RESET} {fecha_inicio}")
            print("-" * 35)
            
            bot_imprimir("¿Son correctos los datos? (Escribí **SI** para confirmar y grabar, o **NO** para cancelar):")
            confirmar = input(f"{COLOR_USER}[Vos]: {COLOR_RESET}").strip().lower()
            
            if confirmar in ["si", "s", "sí", "confirmar", "correcto"]:
                # CONFIRMADO - GUARDAR EN ARCHIVOS Y ACTUALIZAR SALDOS
                sys_imprimir("Conectando con base de datos en archivos planos...")
                time.sleep(0.8)
                
                # 1. Registrar Solicitud en solicitudes.txt
                sol_id = registrar_solicitud(id_empleado, nombre_empleado, dias_solicitados, fecha_inicio)
                
                # 2. Descontar saldo del empleado en el diccionario y reescribir empleados.txt
                empleados[id_empleado]["consumidos"] += dias_solicitados
                empleados[id_empleado]["disponibles"] -= dias_solicitados
                guardar_empleados(empleados)
                
                sys_imprimir("Registros actualizados exitosamente en los archivos.")
                time.sleep(0.5)
                
                bot_imprimir(f"🎉 ¡Felicidades **{nombre_empleado}**! Tu solicitud ha sido grabada.")
                bot_imprimir(f"Se generó el comprobante número {sol_id}.")
                bot_imprimir(f"Tus días de vacaciones restantes son: {empleados[id_empleado]['disponibles']} días.")
                
                solicitud_activa = False
                break
                
            elif confirmar in ["no", "n", "cancelar"]:
                # CANCELADO
                bot_imprimir("❌ Decidiste cancelar la solicitud. No se han modificado tus saldos ni guardado archivos.")
                
                # Registrar cancelación en solicitudes.txt para histórico simulado
                registrar_solicitud(id_empleado, nombre_empleado, dias_solicitados, fecha_inicio, estado="CANCELADA")
                
                solicitud_activa = False
                break
            else:
                bot_imprimir("⚠️ Entrada incorrecta. Escribí únicamente 'SI' para confirmar la solicitud, o 'NO' para abortarla.")

        print(f"\n{COLOR_SYS}====================== PROCESO FINALIZADO ======================{COLOR_RESET}\n")
        time.sleep(1.5)

# --- EJECUCIÓN DEL SCRIPT ---
chatbot_principal()
    
