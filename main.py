import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga las variables de entorno del archivo .env
load_dotenv()

# Inicializa el cliente de OpenAI con la API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_correo_profesional(tu_nombre, destinatario, tema, tono, contexto):
    """
    Genera un correo profesional utilizando un modelo de lenguaje de IA.

    Args:
        tu_nombre (str): Nombre del remitente.
        destinatario (str): Nombre del destinatario.
        tema (str): El tema principal del correo.
        tono (str): El tono deseado para el correo.
        contexto (str): Detalles adicionales para la redacción.
    
    Returns:
        str: El borrador del correo generado.
    """
    
    # Prompt dinámico que incluye todas las variables de contexto
    prompt_completo = f"""Actúa como un asistente experto en redacción de correos profesionales.
    Tu tarea es redactar un borrador de correo electrónico.
    
    Remitente: {tu_nombre}
    Destinatario: {destinatario}
    Tema: {tema}
    Tono deseado: {tono}
    
    Contexto adicional: {contexto}
    
    El borrador debe ser claro, conciso, profesional y adaptarse a la información proporcionada.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un redactor de correos profesionales."},
                {"role": "user", "content": prompt_completo}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Ocurrió un error al generar el correo: {e}"

if __name__ == "__main__":
    print("--- Bienvenido al Asistente de Correos Profesionales con IA ---")
    print("Por favor, ingresa los siguientes datos para generar tu correo.")

    # Pide al usuario la nueva información
    mi_nombre = input("\nIngresa tu nombre: ")
    destinatario = input("Ingresa el nombre del destinatario: ")
    tema_usuario = input("Ingresa el tema del correo: ")
    tono_usuario = input("Ingresa el tono deseado (formal, informal, conciliador, firme): ")
    contexto_usuario = input("Describe el contexto o los puntos clave del correo: ")

    # Genera el correo y lo muestra en la consola
    borrador_correo = generar_correo_profesional(mi_nombre, destinatario, tema_usuario, tono_usuario, contexto_usuario)

    print("\n--- Borrador generado ---")
    print(borrador_correo)
    print("\n-------------------------")
