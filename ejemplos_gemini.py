"""
Ejemplos de uso de la API de Gemini con Python
==============================================

Este archivo contiene ejemplos prácticos de cómo utilizar la API de Gemini
con la biblioteca oficial de Python para diversos casos de uso.

Autor: @luispizarrom
Fecha: Mayo 2025
"""

import os
import google.generativeai as genai
from IPython.display import display, Markdown
from PIL import Image
import pathlib
import requests
from io import BytesIO

# Configuración de la API
def configurar_api(api_key=None):
    """
    Configura la API de Gemini con la clave proporcionada o desde variables de entorno.
    
    Args:
        api_key: Clave de API opcional. Si no se proporciona, se intentará obtener de GOOGLE_API_KEY.
    """
    if api_key is None:
        api_key = os.getenv('GOOGLE_API_KEY')
        if api_key is None:
            raise ValueError("No se ha proporcionado una clave de API. Especifique una o configure GOOGLE_API_KEY.")
    
    genai.configure(api_key=api_key)
    
    # Verificación de modelos disponibles
    for model in genai.list_models():
        if "gemini" in model.name:
            print(f"Modelo disponible: {model.name}")
            print(f"    Capacidades: {model.supported_generation_methods}")
            print(f"    Soporte multimodal: {hasattr(model, 'multimodal') and model.multimodal}")
            print("---")

# Ejemplo 1: Generación de texto básica
def generar_texto(prompt, modelo="gemini-1.5-pro"):
    """
    Genera texto utilizando el modelo Gemini especificado.
    
    Args:
        prompt: Texto de entrada para el modelo
        modelo: Identificador del modelo a utilizar
        
    Returns:
        Texto generado por el modelo
    """
    modelo_gemini = genai.GenerativeModel(modelo)
    respuesta = modelo_gemini.generate_content(prompt)
    
    return respuesta.text

# Ejemplo 2: Procesamiento multimodal (texto + imagen)
def procesar_imagen_texto(texto, ruta_imagen=None, url_imagen=None, modelo="gemini-1.5-pro"):
    """
    Procesa una combinación de texto e imagen.
    
    Args:
        texto: Texto descriptivo o pregunta sobre la imagen
        ruta_imagen: Ruta local a la imagen (opcional)
        url_imagen: URL de la imagen en línea (opcional)
        modelo: Identificador del modelo a utilizar
        
    Returns:
        Texto generado por el modelo
    """
    if ruta_imagen is None and url_imagen is None:
        raise ValueError("Se debe proporcionar al menos una ruta de imagen o URL")
    
    # Cargar imagen
    if ruta_imagen:
        imagen = Image.open(ruta_imagen)
    else:
        respuesta = requests.get(url_imagen)
        imagen = Image.open(BytesIO(respuesta.content))
    
    # Configurar modelo
    modelo_vision = genai.GenerativeModel(modelo)
    
    # Crear prompt multimodal
    prompt_multimodal = [texto, imagen]
    
    # Generar respuesta
    respuesta = modelo_vision.generate_content(prompt_multimodal)
    
    return respuesta.text

# Ejemplo 3: Chat interactivo
def iniciar_chat(modelo="gemini-1.5-pro", temperatura=0.7):
    """
    Inicia una sesión de chat interactiva con Gemini.
    
    Args:
        modelo: Identificador del modelo a utilizar
        temperatura: Valor de temperatura para la generación (0.0-1.0)
        
    Returns:
        Objeto de chat para interacción continua
    """
    modelo_gemini = genai.GenerativeModel(
        modelo,
        generation_config=genai.GenerationConfig(temperature=temperatura)
    )
    
    chat = modelo_gemini.start_chat(history=[])
    print("Chat iniciado. Envíe mensajes o 'salir' para terminar.")
    
    return chat

def enviar_mensaje_chat(chat, mensaje):
    """
    Envía un mensaje al chat y devuelve la respuesta.
    
    Args:
        chat: Objeto de chat de Gemini
        mensaje: Mensaje a enviar
        
    Returns:
        Texto de respuesta del modelo
    """
    respuesta = chat.send_message(mensaje)
    return respuesta.text

# Ejemplo 4: Análisis de código
def analizar_codigo(codigo, instruccion, modelo="gemini-1.5-pro"):
    """
    Analiza código fuente con instrucciones específicas.
    
    Args:
        codigo: Código fuente a analizar
        instruccion: Instrucciones específicas para el análisis
        modelo: Identificador del modelo a utilizar
        
    Returns:
        Análisis generado por el modelo
    """
    modelo_gemini = genai.GenerativeModel(modelo)
    
    prompt = f"""
    {instruccion}
    
    ```
    {codigo}
    ```
    """
    
    respuesta = modelo_gemini.generate_content(prompt)
    return respuesta.text

# Ejemplo 5: Función con streaming de respuesta
def generar_con_streaming(prompt, modelo="gemini-1.5-pro"):
    """
    Genera contenido con streaming de respuesta en tiempo real.
    
    Args:
        prompt: Texto de entrada para el modelo
        modelo: Identificador del modelo a utilizar
        
    Returns:
        Iterador sobre fragmentos de respuesta
    """
    modelo_gemini = genai.GenerativeModel(modelo)
    
    respuesta_stream = modelo_gemini.generate_content(
        prompt,
        stream=True
    )
    
    # En lugar de devolver directamente, podríamos procesar:
    texto_completo = ""
    for fragmento in respuesta_stream:
        if fragmento.text:
            texto_completo += fragmento.text
            # En un entorno interactivo:
            # print(fragmento.text, end="", flush=True)
    
    return texto_completo

# Ejemplo de uso
if __name__ == "__main__":
    # Recuerde configurar su API key antes de ejecutar
    # configurar_api("SU_API_KEY_AQUÍ")
    
    # Ejemplo básico
    configurar_api()
    resultado = generar_texto("Explica la arquitectura multimodal de Gemini en 3 párrafos")
    print(resultado)
