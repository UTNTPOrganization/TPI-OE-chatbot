# Trabajo Práctico Integrador: Chatbot de Vacaciones en Python (TFI - UTN)

Este repositorio contiene la resolución completa y formal del **Trabajo Práctico Integrador** para la materia **Organización Empresarial** de la **Tecnicatura Universitaria en Programación a Distancia (TUPaD - UTN)**.

El proyecto consiste en la identificación de un proceso de negocio administrativo manual e ineficiente (la solicitud de vacaciones de empleados) y su optimización integral mediante un **Chatbot Conversacional en Python** con persistencia local en **Archivos de Texto Plano (`.txt`)**, mapeado en base a un modelo de procesos **BPMN 2.0**.

---

Trabajo Colaborativo, Commits y Trazabilidad
Integrantes
Alejandro Fernández (PROY-1)

Responsable principal de:

Diseño e implementación de la máquina de estados conversacional.
Desarrollo del flujo principal del chatbot.
Implementación de los estados del proceso de negocio.
Integración entre el modelo BPMN y el código Python.
Implementación de caminos felices e infelices.
Validación funcional del proceso completo de solicitud de vacaciones.

Prefijo de commits:

[PROY-1]

Ejemplos:

git commit -m "[PROY-1] Implementa estado de validación de empleado"
git commit -m "[PROY-1] Agrega gateway de saldo suficiente"
git commit -m "[PROY-1] Implementa confirmación final de solicitud"
Gabriel Di Lorenzo (PROY-2)

Responsable principal de:

Diseño de las funciones auxiliares del sistema.
Implementación de persistencia mediante archivos de texto.
Gestión de empleados y solicitudes.
Validaciones de fecha utilizando datetime.
Manejo de excepciones mediante try-except.
Implementación de menús, ayuda y presentación en consola.

Prefijo de commits:

[PROY-2]

Ejemplos:

git commit -m "[PROY-2] Implementa carga de empleados desde archivo"
git commit -m "[PROY-2] Agrega persistencia de solicitudes"
git commit -m "[PROY-2] Implementa validación de fechas"
Evidencia de Autoría

La trazabilidad del proyecto puede verificarse mediante:

Historial completo de commits en GitHub.
Uso de prefijos PROY-1 y PROY-2.
Evolución incremental del código.
Relación entre responsabilidades declaradas y componentes desarrollados.

Cada integrante deberá poder explicar durante la defensa oral la parte del sistema bajo su responsabilidad y su relación con el modelo BPMN propuesto.

---

## 📂 Estructura de Archivos del Proyecto

El proyecto está diseñado de forma modular y auto-contenido, utilizando exclusivamente tecnologías estándar y locales de primer año de programación:

*   **`chatbot_vacaciones.py`**: Código fuente principal en Python. Contiene el bucle de la máquina de estados conversacional, validaciones avanzadas (con la librería `datetime`) y gestión de errores mediante `try-except`.
*   **`empleados.txt`**: Archivo plano estructurado con tuberías (`|`) que actúa como base de datos local de la empresa. Almacena los IDs de empleado, nombres, días totales, consumidos y disponibles.
*   **`solicitudes.txt`**: Registro histórico persistente donde el chatbot graba las solicitudes aprobadas en tiempo real.
*   **`bpmn_diagram.svg`**: Diagrama de procesos BPMN 2.0 vectorial de alta resolución. Contiene los carriles de *Empleado* y *Chatbot*, eventos de inicio/fin, compuertas decisorias y tareas de servicio.
*   **`informe_tfi.md`**: Informe académico formal redactado minuciosamente con todas las pautas teóricas y técnicas exigidas por la UTN (análisis As-Is vs To-Be, desglose de carriles, diccionario de datos y justificación de herramientas de IA), listo para copiar a Microsoft Word y exportar a PDF en formato Times New Roman 11pt.

---

## 🚀 Guía de Ejecución

Para iniciar el simulador conversacional en tu computadora local:

1.  Asegúrate de tener instalado **Python 3** en tu sistema.
2.  Abre la terminal o consola de comandos (Command Prompt / PowerShell / Bash) en este directorio.
3.  Ejecuta el siguiente comando:
    ```bash
    python chatbot_vacaciones.py
    ```
4.  ¡Listo! El chatbot se iniciará inmediatamente con una interfaz visual coloreada directamente en la terminal.

---

## 🎮 Comandos Especiales en el Chat

El chatbot está diseñado con un controlador inteligente de comandos que puedes tipear en **cualquier momento** de la conversación para facilitar la simulación y evaluación de los profesores:

*   **`/ayuda`**: Imprime en pantalla la guía de comandos y reglas de uso del chatbot.
*   **`/empleados`**: Lee el archivo `empleados.txt` en tiempo real y muestra una tabla limpia en consola con los días de vacaciones acumulados de cada empleado de prueba.
*   **`/cancelar`**: Cancela y aborta la solicitud en curso de forma segura, limpia la sesión y vuelve al menú de bienvenida del asistente virtual.

---

## 🧪 Escenarios de Prueba para la Defensa Oral

Para demostrar la solidez de tu software ante los profesores en el coloquio final, te recomendamos seguir estos caminos de testeo:

### 🟢 1. El Camino Feliz (Happy Path)
1.  Escribe `si` para iniciar el trámite.
2.  Ingresa el ID `EMP002` (corresponde a Ana López, quien tiene 14 días disponibles).
3.  Solicita **`5`** días de vacaciones.
4.  Ingresa una fecha futura válida, por ejemplo: **`15/12/2026`**.
5.  Confirma escribiendo **`si`** en la pregunta final.
6.  *Verificación:* Observa cómo el sistema descuenta los 5 días de Ana López en `empleados.txt` (pasando a tener 9 disponibles) y registra de forma permanente la transacción en `solicitudes.txt` con el ID autoincremental `SOL001` y la marca de tiempo exacta.

### 🔴 2. Caminos Infelices (Manejo de Errores y Robustez)
*   **ID Inexistente:** Escribe `EMP999` y observa cómo el bot te informa del error al consultar el archivo y te invita a reintentar.
*   **Entrada de Texto Invalida:** Cuando el bot te pregunte los días, escribe `"cinco"` o `"diez"`. Verás cómo el bloque `try-except` captura la excepción sin interrumpir la ejecución del programa y te pide ingresar un entero válido.
*   **Saldo Insuficiente:** Ingresa como empleado `EMP001` (Juan Pérez, con 10 días libres) y solicita **`15`** días. La lógica condicional impedirá el avance y te obligará a pedir un número menor o igual a tu saldo real.
*   **Fecha Pasada:** Intenta ingresar la fecha `01/01/2020` o un formato incorrecto como `15-12-2026`. La validación de `datetime` rechazará la entrada obligándote a cumplir con las normas de negocio establecidas.
