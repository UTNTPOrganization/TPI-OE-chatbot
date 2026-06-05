# INFORME TRABAJO PRÁCTICO INTEGRADOR: ORGANIZACIÓN EMPRESARIAL
**Cátedra:** Organización Empresarial  
**Tecnicatura Universitaria en Programación a Distancia (TUPaD) – UTN**  
**Autores:** [Ingresar Nombre del Estudiante / Integrantes]  
**Año:** 2026  

---

> [!NOTE]
> **Instrucciones para la entrega oficial:** Este documento en Markdown ha sido redactado con el máximo rigor académico requerido por la UTN. Para generar el entregable final en PDF:
> 1. Copiá el contenido de este archivo en un documento de Microsoft Word.
> 2. Seleccioná todo el texto y aplicá la tipografía **Times New Roman** con tamaño **11pt** (interlineado simple o 1.15).
> 3. Asegurá que los títulos principales queden en tamaño **12pt en Negrita y Mayúsculas (BOLD UPPERCASE)**.
> 4. Exportá el documento final a PDF (debe respetar la extensión reglamentaria de entre 4 y 8 páginas A4).

---

## 1. INTRODUCCIÓN Y DEFINICIÓN DEL PROCESO

### 1.0. La Organización como Sistema

Desde la perspectiva de la Teoría General de Sistemas, toda organización puede entenderse como un sistema abierto que interactúa permanentemente con su entorno mediante entradas, procesos, salidas y mecanismos de control.

En el presente trabajo se modela una empresa privada que posee un área de Recursos Humanos responsable de administrar las licencias y vacaciones de los empleados.

**Entradas del sistema:**

* Solicitudes de vacaciones.
* Datos de empleados.
* Políticas internas de RRHH.
* Información proveniente de convenios laborales.

**Procesos:**

* Verificación de identidad del empleado.
* Control de saldo de días disponibles.
* Validación de fechas.
* Registro de solicitudes.
* Actualización de saldos.

**Salidas:**

* Solicitudes aprobadas.
* Solicitudes rechazadas.
* Historial de movimientos.
* Actualización de registros administrativos.

**Subsistemas involucrados:**

* Recursos Humanos.
* Empleados.
* Sistema de información (chatbot).

**Entorno:**

* Legislación laboral vigente.
* Convenios colectivos.
* Políticas organizacionales.

Dentro de este sistema organizacional se seleccionó para su automatización el proceso administrativo de solicitud de vacaciones, debido a su frecuencia de uso y a las oportunidades de mejora detectadas en el análisis del proceso actual.

### 1.1. Identificación del Proceso Administrativo Ineficiente (Flujo "As-Is")
En muchas organizaciones medianas y pequeñas, la gestión de solicitud de vacaciones de los empleados se realiza mediante flujos de trabajo tradicionales, informales y enteramente manuales. El proceso típico analizado bajo el estado actual (**"As-Is"**) se compone de las siguientes etapas:
1. El empleado redacta un correo electrónico informal o llena una planilla física en papel solicitando un rango de fechas de vacaciones.
2. Dicho formulario en papel o correo electrónico es remitido al sector de Recursos Humanos (RRHH).
3. Un analista de RRHH debe suspender sus tareas habituales para buscar manualmente el legajo físico del empleado o consultar planillas de cálculo (Excel) individuales para verificar el saldo de días de vacaciones acumulados de dicho empleado.
4. Si el empleado solicita más días de los que tiene disponibles, el analista de RRHH debe redactar un correo electrónico informándole el rechazo de la solicitud, dando inicio a un intercambio iterativo ineficiente de correos.
5. Si dispone de saldo, se remite la solicitud al supervisor directo del empleado para su firma y autorización.
6. Una vez aprobada, RRHH debe actualizar manualmente el archivo Excel del empleado y archivar físicamente la planilla de solicitud firmada.

Este proceso **"As-Is"** presenta ineficiencias críticas:
*   **Desperdicio de Tiempo Operativo:** Búsquedas manuales de legajos y saldos en planillas aisladas.
*   **Alta Propensión al Error Humano:** Fallas al transcribir manualmente los días consumidos en planillas Excel compartidas, lo que puede provocar liquidaciones incorrectas o superposición de descansos.
*   **Falta de Trazabilidad:** Las solicitudes pueden perderse en bandejas de entrada de correo electrónico o carpetas físicas sin dejar un log auditable del estado de aprobación.
*   **Demoras en la Respuesta:** El empleado no posee autogestión y depende 100% de la disponibilidad temporal del área de RRHH para conocer su saldo y estado de trámite.

### 1.2. Propuesta de Optimización Automatizada (Flujo "To-Be")
Con el propósito de mitigar estas ineficiencias, el modelo rediseñado (**"To-Be"**) introduce un **Chatbot de Autogestión Conversacional** desarrollado en **Python** con persistencia en **Archivos de Texto Plano (.txt)**. 

En este nuevo flujo de negocio:
1. El empleado interactúa en tiempo real con un asistente virtual de RRHH (HR-Bot) por consola.
2. El chatbot solicita el ID del empleado y realiza una **consulta de servicio automática e instantánea** al archivo físico `empleados.txt` (que actúa como base de datos de saldos).
3. El chatbot realiza la validación matemática de días solicitados frente a los disponibles y la consistencia de la fecha mediante lógica integrada, resolviendo de forma inmediata aprobaciones y rechazos.
4. Al confirmar la solicitud, el sistema descuenta automáticamente los días en `empleados.txt` y registra la transacción en el archivo histórico `solicitudes.txt`, garantizando persistencia y trazabilidad de punta a punta en segundos.

---

## 2. PERSPECTIVA DE NEGOCIO (MODELADO BPMN 2.0)

El modelado del proceso se estructuró siguiendo el estándar internacional **BPMN 2.0 (Business Process Model and Notation)**. Para representar con total precisión la interacción entre los actores, el diagrama de procesos se divide en dos canales o carriles principales:

### 2.1. Desglose de Carriles (Lanes)
*   **Carril Empleado (Usuario):** Representa todas las acciones de interacción directa del solicitante. Contiene las tareas manuales y de entrada de datos: inicio del proceso, tipeo del ID, ingreso de cantidad de días requeridos, entrada de la fecha de inicio en el formato establecido, y decisión de confirmación final.
*   **Carril Chatbot de RRHH (Sistema):** Contempla el procesamiento computacional de las solicitudes. Representa las tareas automatizadas de servicio: validación de existencia del ID del empleado en la base de datos física, evaluación de saldo disponible, procesamiento y formateo de la fecha, control de excepciones del flujo infeliz, cálculo matemático de actualización de saldos, y persistencia (escritura) de datos en los archivos de texto correspondientes.

### 2.2. Eventos y Compuertas Decisorias (Gateways)
El modelo cuenta con un **Evento de Inicio** (Empleado decide solicitar vacaciones) y **Eventos de Fin** que marcan la culminación del proceso (Solicitud Aprobada y Guardada, o Solicitud Cancelada por el Usuario). 

Para gobernar el flujo de negocio, se han implementado **cuatro compuertas lógicas exclusivas (XOR Gateways)**:
1.  **¿ID Válido?:** Evalúa si el ID ingresado por el empleado existe en la base de datos (`empleados.txt`). De ser negativo (Camino Infeliz), desvía el flujo de vuelta a la tarea de ingreso con un mensaje de alerta. De ser positivo (Camino Feliz), avanza.
2.  **¿Tiene Saldo Suficiente?:** Evalúa matemáticamente si los días solicitados son menores o iguales a los días disponibles en sesión. Si excede el saldo (Camino Infeliz), el bot rechaza la petición, expone los saldos reales y solicita un nuevo valor. Si es adecuado (Camino Feliz), continúa.
3.  **¿Fecha Válida?:** Comprueba si la fecha cumple con el patrón sintáctico `DD/MM/AAAA` y si cronológicamente es futura. Si es inválida o en el pasado (Camino Infeliz), notifica y exige reingreso. Si es correcta (Camino Feliz), avanza a la confirmación.
4.  **¿Acepta/Confirma?:** Pregunta de control final al usuario para confirmar o cancelar la transacción. Si confirma (Sí), se guardan los archivos y finaliza con éxito. Si declina (No), se registra la cancelación en el histórico de auditoría sin tocar el saldo de días y finaliza el proceso.

---

## 3. PERSPECTIVA TÉCNICA Y PROGRAMACIÓN

La traducción del modelo conceptual BPMN a software funcional se realizó mediante un script ejecutable en **Python** de alta portabilidad que corre de manera local.

### 3.1. Selección del Stack Tecnológico
Se seleccionó **Python** como lenguaje de programación debido a su legibilidad, robustez en el tipado dinámico y potencia nativa para procesar archivos y lógica condicional. 
*   **Sin dependencias externas:** Para asegurar la máxima compatibilidad en cualquier entorno académico y alinearse al 1er cuatrimestre de la tecnicatura, el desarrollo utiliza exclusivamente módulos estándar incorporados en Python: `os` (para manipulación de rutas y limpieza de pantalla), `time` (para simular tiempos de espera y dotar de naturalidad a la conversación del bot) y `datetime` (para procesamiento temporal avanzado).
*   **Persistencia en Archivos de Texto Plano (`.txt`):** Se implementó una base de datos simulada mediante archivos estructurados separados por caños (`|`). Esto permite prescindir de motores SQL complejos o dependencias avanzadas de JSON, manteniendo el código transparente, legible y 100% defendible bajo los conceptos de manejo de flujos de archivos nativos de primer año (`open(..., "r")` y `open(..., "w")`).

### 3.2. Implementación de la Máquina de Estados
El chatbot emula una máquina de estados finitos mediante una arquitectura secuencial controlada por bucles `while` anidados. Cada bucle representa un estado conversacional específico que no permite al usuario avanzar al siguiente paso hasta que la entrada de datos satisfaga estrictamente las reglas de negocio del estándar BPMN. 

Esto garantiza que el código sea estructuralmente coherente con el diagrama de procesos: las decisiones lógicas del diagrama se ejecutan de forma exacta mediante sentencias `if/elif/else` en Python.

---

## 4. DICCIONARIO DE DATOS Y MANUAL DE USUARIO

### 4.1. Diccionario de Datos del Sistema

#### A. Estructura de la Base de Datos de Empleados (`empleados.txt`)
Almacena el registro maestro de empleados y sus vacaciones acumuladas. Cada línea representa un empleado con campos separados por tuberías (`|`):

| Campo | Tipo de Datos | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **IDEmpleado** | Cadena (String) | Clave primaria. Código único del empleado. | `EMP002` |
| **Nombre** | Cadena (String) | Nombre y apellido completo del trabajador. | `Ana Lopez` |
| **DiasTotales** | Entero (Integer) | Vacaciones totales asignadas por convenio. | `20` |
| **DiasConsumidos** | Entero (Integer) | Días de vacaciones ya usufructuados. | `6` |
| **DiasDisponibles** | Entero (Integer) | Saldo de días restantes para solicitar. | `14` |

#### B. Estructura de Registro de Solicitudes (`solicitudes.txt`)
Almacena el registro histórico de transacciones del chatbot para auditoría:

| Campo | Tipo de Datos | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **IDSolicitud** | Cadena (String) | Clave primaria autoincremental (`SOL001`, `SOL002`). | `SOL001` |
| **IDEmpleado** | Cadena (String) | Clave foránea referenciada al empleado. | `EMP002` |
| **Nombre** | Cadena (String) | Nombre del empleado al momento del registro. | `Ana Lopez` |
| **DiasSolicitados**| Entero (Integer) | Cantidad de días de vacaciones pedidos. | `5` |
| **FechaInicio** | Cadena (String) | Fecha pactada para el inicio (DD/MM/AAAA). | `15/12/2026` |
| **Estado** | Cadena (String) | Estado final de la solicitud (`APROBADA` o `CANCELADA`).| `APROBADA` |
| **FechaRegistro** | Cadena (String) | Marca de tiempo exacta de la transacción. | `27/05/2026 01:42:00` |

### 4.2. Manual de Usuario y Comandos del Chatbot
El programa interactúa enteramente a través de la consola estándar del sistema operativo. Para ejecutar el chatbot:
1. Abrir la terminal o consola del sistema en la carpeta del proyecto.
2. Ejecutar el comando: `python chatbot_vacaciones.py`.

#### 🎮 Comandos Globales Interactivos
El sistema cuenta con un controlador de comandos globales que pueden ser escritos por el usuario en cualquier pregunta del chat para alterar el flujo ordinario del sistema:
*   **`/ayuda`:** Muestra en pantalla el manual de ayuda técnica y el listado de comandos disponibles.
*   **`/empleados`:** Realiza una lectura al instante de `empleados.txt` y plasma en la terminal una tabla formateada con los saldos actualizados de los empleados para facilitar el testeo del sistema.
*   **`/cancelar`:** Aborta de inmediato cualquier solicitud activa en curso, limpia las variables temporales de sesión, registra opcionalmente la cancelación en el archivo y devuelve al chatbot a su estado inicial.

---

## 5. PRUEBAS DE ROBUSTEZ Y CAMINOS INFELICES (EVIDENCIA)

Para garantizar la calidad de software requerida en la pauta "Robustez (Camino Infeliz)", el script fue sometido a pruebas de estrés de entrada de datos simulando errores comunes de usuarios.

### 5.1. Prueba de Error en ID de Empleado (ID No Existente)
*   **Entrada de Usuario:** `EMP999`
*   **Acción del Bot:** Al validar en `empleados.txt`, el bot no localiza la clave.
*   **Respuesta en Consola:**  
    `[Sistema-DB]: Validando ID 'EMP999' en empleados.txt...`  
    `[HR-Bot]: ❌ Error: El ID de empleado 'EMP999' no figura en el archivo. Por favor, reintentalo.`
*   **Resultado:** El sistema se mantiene en bucle solicitando el ID sin caerse ni registrar datos corruptos.

### 5.2. Prueba de Entrada No Numérica en Días (Control de Excepciones)
*   **Entrada de Usuario:** `"cinco"` o `"5.5"`
*   **Acción del Bot:** La función `int()` de Python genera una excepción `ValueError`. El bloque `try-except` captura el error.
*   **Respuesta en Consola:**  
    `[HR-Bot]: ⚠️ Entrada inválida. Por favor, ingresá únicamente números enteros (ej: 5).`
*   **Resultado:** Excepción controlada de forma elegante, evitando el crash del script y re-preguntando la cantidad.

### 5.3. Prueba de Saldo de Días Insuficiente (Gateway de Negocio)
*   **Entrada de Usuario:** `25` (para el empleado `EMP002` que posee únicamente `14` días disponibles).
*   **Acción del Bot:** Compara matemáticamente la entrada (`25`) con el campo `disponibles` (`14`).
*   **Respuesta en Consola:**  
    `[Sistema-DB]: Validando saldo: Solicitados 25 vs. Disponibles 14...`  
    `[HR-Bot]: ❌ Rechazo: No tenés saldo de días suficiente.`  
    `[HR-Bot]: Pediste 25 días pero solo disponés de 14 días.`  
    `[HR-Bot]: Por favor, ingresá una cantidad menor o igual a tu saldo.`
*   **Resultado:** El Gateway detecta la violación de la regla de negocio y rechaza la solicitud.

### 5.4. Prueba de Fecha Pasada o Formato Incorrecto
*   **Entradas de Prueba:** `15-12-2026` (formato guiones) o `01/01/2020` (fecha del pasado).
*   **Acción del Bot:** La librería `datetime` evalúa la sintaxis y compara cronológicamente la fecha con el día actual (`datetime.now()`).
*   **Respuesta en Consola (Formato incorrecto):**  
    `[HR-Bot]: ❌ Error en fecha: Formato incorrecto. Debe ser DD/MM/AAAA (ej: 15/12/2026).`
*   **Respuesta en Consola (Fecha pasada):**  
    `[HR-Bot]: ❌ Error en fecha: La fecha de inicio de vacaciones debe ser estrictamente en el futuro.`
*   **Resultado:** Evita el registro de solicitudes con fechas imposibles o formatos inconsistentes.

---

## 6. HERRAMIENTAS DE IA UTILIZADAS Y PROMPTS APLICADOS

### Alejandro Fernández (PROY-1)

#### Rol en el Proyecto

Responsable principal del diseño e implementación de la máquina de estados conversacional, integración del flujo BPMN con Python, validaciones funcionales y gestión de caminos felices e infelices.

#### Uso de Inteligencia Artificial

Se utilizó Gemini como herramienta de consulta técnica y apoyo metodológico durante el diseño del flujo conversacional.

La IA fue utilizada para:

* Analizar alternativas de implementación de máquinas de estados.
* Diseñar validaciones robustas para entradas de usuario.
* Evaluar estrategias de persistencia utilizando archivos de texto.
* Revisar mecanismos de validación de fechas mediante la librería datetime.
* Contrastar diferentes formas de implementar gateways y caminos alternativos presentes en el BPMN.

Las respuestas obtenidas fueron evaluadas críticamente y adaptadas a las restricciones del proyecto y a los contenidos desarrollados durante la cursada.

#### Prompts Utilizados

**Prompt 1 – Diseño de Máquina de Estados**

> "Necesito diseñar una máquina de estados conversacional en Python para un chatbot de vacaciones de UTN. Solo puedo utilizar estructuras vistas en primer año (condicionales, ciclos, funciones y archivos de texto). ¿Cómo puedo modelar el flujo para que represente correctamente un proceso BPMN?"

**Aplicación:**

Sirvió como referencia conceptual para estructurar el flujo principal del chatbot.

---

**Prompt 2 – Persistencia de Información**

> "¿Cómo puedo leer y actualizar un archivo de texto con registros de empleados utilizando el formato id|nombre|total|consumidos|disponibles manteniendo la integridad de los datos?"

**Aplicación:**

Se utilizó como apoyo para comprender estrategias de lectura y actualización de archivos planos.

---

**Prompt 3 – Validación de Fechas**

> "¿Cómo puedo validar una fecha ingresada en formato DD/MM/AAAA utilizando datetime y verificar además que corresponda a una fecha futura?"

**Aplicación:**

Se tomó como referencia para la implementación de la validación de fechas utilizada por el sistema.

---

**Prompt 4 – Manejo de Errores y Robustez**

> "¿Qué mecanismos simples pueden utilizarse para evitar que un chatbot en consola falle cuando el usuario ingresa datos inválidos?"

**Aplicación:**

Permitió analizar distintas estrategias de control de errores mediante validaciones y estructuras try-except.

#### Evaluación Crítica

Durante el proceso se descartaron diversas sugerencias generadas por la IA debido a que utilizaban conceptos no contemplados dentro del alcance de la materia (bases de datos, programación orientada a objetos o librerías externas).

La implementación final fue desarrollada y adaptada manualmente para respetar los contenidos trabajados en Programación I y Organización Empresarial.

---

### Gabriel Di Lorenzo (PROY-2)

[Completar con las herramientas de IA utilizadas, prompts aplicados y evaluación crítica correspondiente a las funciones auxiliares, persistencia, manejo de archivos y validaciones implementadas por el integrante.]

---

## 7. CONCLUSIÓN Y APRENDIZAJES

El desarrollo de este Trabajo Práctico Integrador ha permitido consolidar de forma práctica la unión entre el modelado de procesos de negocio (perspectiva administrativa/organizacional) y la programación lógica (perspectiva técnica). 

La implementación del chatbot en **Python** con persistencia en **archivos de texto plano (.txt)** demostró de forma empírica que es posible erradicar ineficiencias de procesos burocráticos manuales utilizando tecnologías sencillas, locales y accesibles. 

La correcta gestión de los "caminos infelices" y las excepciones de entrada resalta la importancia de la robustez en el diseño de software para evitar la degradación de datos en sistemas reales, proveyendo al futuro programador una valiosa experiencia práctica sobre el comportamiento de sistemas en entornos de producción.
