# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:07:05 2024

@author: 3PW97LA_RS5
"""
import json

# Cargar el conocimiento desde un archivo JSON si existe
try:
    with open('knowledge_base.json', 'r') as file:
        knowledge_base = json.load(file)
except FileNotFoundError:
    # Si el archivo no existe, usar un conocimiento inicial
    knowledge_base = {
        'hola': '¡Hola!',
        'como estas': 'Estoy bien, ¿y tú?',
        'de que te gustaria hablar': 'Puedo hablar de muchos temas. ¿Hay algo específico que te interese?'
    }

def chat(message):
    message_lower = message.lower()

    # Buscar coincidencias en el diccionario de conocimiento
    response = knowledge_base.get(message_lower, None)

    if response:
        return response
    else:
        # Si no hay coincidencia, preguntar al usuario y aprender
        new_response = input(f"No sé cómo responder a '{message}'. ¿Cómo debería responder? ")
        knowledge_base[message_lower] = new_response

        # Guardar el conocimiento actualizado en el archivo JSON
        with open('knowledge_base.json', 'w') as file:
            json.dump(knowledge_base, file)

        return f"Gracias por enseñarme. Ahora puedo responder a '{message}'."

# Ejemplo de uso
while True:
    user_input = input("Usuario: ")
    if user_input.lower() == 'salir':
        break
    else:
        bot_response = chat(user_input)
        print("Bot:", bot_response)
