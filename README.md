# Propuesta de Proyecto Final: Asistente de correos profesionales con IA

## Datos del curso
**Nombre del proyecto:** Asistente de correos profesionales con IA
**Curso:** Inteligencia Artificial Generación de Prompts
**N° de comisión:** 84180
**Alumno:** Leonardo Hugo Griffone

---

## 1. Introducción

### Presentación del problema a abordar
En mi trabajo, la redacción de correos con el tono adecuado (formal, conciliador, firme, etc.) es un desafío diario que consume tiempo y esfuerzo. La falta de una herramienta que simplifique este proceso es la problemática central que este proyecto busca resolver. El objetivo es crear un asistente que genere borradores de correos adaptados a cada situación, mejorando la eficiencia y la calidad de la comunicación profesional.

### Desarrollo de la propuesta de solución
La solución consiste en un script de Python que interactúa con una API de IA. A través de un prompt dinámico, el usuario proporciona su nombre, el destinatario, el tema, el tono y un contexto detallado, y el modelo de IA genera un borrador de correo personalizado. Este enfoque permite generar respuestas más precisas y útiles, optimizando el tiempo y la calidad de la redacción.

### Justificación de la viabilidad del proyecto
Este proyecto es altamente viable porque aborda una necesidad laboral real y cotidiana con una solución tecnológica accesible y de bajo costo. Los modelos de lenguaje generativo han demostrado ser excepcionalmente efectivos para la redacción de texto, y la implementación no requiere de grandes recursos. Es un proyecto práctico y escalable que puede ser aplicado directamente en el ámbito profesional.

---

## 2. Objetivos

* **Objetivo principal:** Desarrollar un asistente funcional que genere borradores de correos profesionales, aplicando técnicas de **Prompt Engineering** para obtener resultados precisos y de alta calidad.
* **Objetivo secundario:** Analizar la viabilidad técnica y económica de la solución, evaluando el rendimiento del modelo de IA y el costo asociado al consumo de tokens.

---

## 3. Metodología

El proyecto se desarrolló de forma iterativa, siguiendo estos pasos clave:
1.  **Diseño del prompt:** Se creó un prompt dinámico y modular que permite incluir múltiples variables de contexto (remitente, destinatario, tono, tema). Se utilizó la técnica de **Role Prompting** para instruir a la IA a que actúe como un experto en redacción de correos, mejorando la coherencia y el estilo.
2.  **Implementación del código:** Se desarrolló un script en Python para interactuar con la API de OpenAI, permitiendo al usuario ingresar los datos de manera interactiva a través de la consola.
3.  **Análisis de viabilidad:** Se evaluaron tanto la capacidad técnica de las herramientas como la rentabilidad económica de la solución.

---

## 4. Herramientas y Tecnologías

* **Lenguaje de Programación:** Python
* **Técnica de Prompting:** **Role Prompting** para la optimización de respuestas.
* **API:** Se utilizó la API de OpenAI con el modelo `gpt-3.5-turbo`, elegido por su buen desempeño y eficiencia de costos.
* **Librerías de Python:**
    * `openai`: Para la interacción con la API de OpenAI.
    * `python-dotenv`: Para la gestión segura de las variables de entorno.
* **Entorno de Desarrollo:** Visual Studio Code.

---

## 5. Implementación

La solución se encuentra en el archivo `main.py`, un script interactivo que guía al usuario. El corazón de la solución es el siguiente prompt principal, diseñado para ser dinámico y adaptable a la entrada del usuario:

Actúa como un asistente experto en redacción de correos profesionales.
Tu tarea es redactar un borrador de correo electrónico.
Remitente: {tu_nombre}
Destinatario: {destinatario}
Tema: {tema}
Tono deseado: {tono}
Contexto adicional: {contexto}
El borrador debe ser claro, conciso, profesional y adaptarse a la información proporcionada.

Este enfoque modular permite generar correos altamente personalizados sin necesidad de un prompt inicial excesivamente largo, presentando la información de manera organizada al modelo.

### **Viabilidad económica y técnica**

Se realizó un análisis de costos para demostrar la rentabilidad del proyecto:
-   **Costo del modelo:** El precio del modelo `gpt-3.5-turbo` es de **$0.0015 USD por cada 1,000 tokens de entrada** y **$0.002 USD por cada 1,000 tokens de salida**.
-   **Análisis del costo por borrador:** Un correo típico, con un prompt de **aproximadamente 50 tokens de entrada** y una respuesta de **150 tokens de salida**, tiene un costo total de **$0.000375 USD**. Este costo sumamente bajo por cada borrador generado demuestra la viabilidad económica de la solución para un uso diario.

---

## 6. Advertencia de seguridad

Este proyecto utiliza un archivo `.env` para almacenar la API key de manera segura. Este archivo **