# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:24:01 2024

@author: 3PW97LA_RS5
"""

import json

def main():
    while True:
        # Intenta cargar los datos desde el archivo JSON
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        tipo_animal = data.get("tipo_animal", input("¿El animal es un mamífero? (si/no): ").lower())
        if tipo_animal == "si":
            tipo_animal = "mamífero"
        elif tipo_animal == "no":
            tipo_animal = data.get("tipo_animal_no", input("¿El animal es un ave? (si/no): ").lower())
            if tipo_animal == "si":
                tipo_animal = "ave"
            elif tipo_animal == "no":
                tipo_animal = "reptil"
            else:
                print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                continue
        else:
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
            continue

        color_pelaje = data.get("color_pelaje", input("¿El pelaje o plumaje del animal es de color marrón? (si/no): ").lower())
        if color_pelaje == "si":
            color_pelaje = "marrón"
        elif color_pelaje == "no":
            color_pelaje = data.get("color_pelaje_no", input("¿El pelaje o plumaje del animal es de color negro? (si/no): ").lower())
            if color_pelaje == "si":
                color_pelaje = "negro"
            elif color_pelaje == "no":
                color_pelaje = data.get("color_pelaje_no_no", input("¿El pelaje o plumaje del animal es de color blanco? (si/no): ").lower())
                if color_pelaje == "si":
                    color_pelaje = "blanco"
                elif color_pelaje == "no":
                    print("No se puede determinar el personaje con las respuestas dadas.")
                    continue
                else:
                    print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                    continue
            else:
                print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                continue
        else:
            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
            continue

        especie = "no aplica"
        if tipo_animal == "mamífero":
            especie = data.get("especie", input("¿El animal tiene melena? (si/no): ").lower())
            if especie == "si":
                especie = "león"
            elif especie == "no":
                especie = data.get("especie_no", input("¿El animal tiene rayas en su pelaje? (si/no): ").lower())
                if especie == "si":
                    especie = "tigre"
                elif especie == "no":
                    especie = data.get("especie_no_no", input("¿El animal es de gran tamaño y tiene garras poderosas? (si/no): ").lower())
                    if especie == "si":
                        especie = "oso"
                    elif especie == "no":
                        print("No se puede determinar la especie del animal con las respuestas dadas.")
                        continue
                    else:
                        print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                        continue
                else:
                    print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                    continue
            else:
                print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                continue

        personaje = determinar_personaje(tipo_animal, color_pelaje, especie)
        if personaje:
            print("Tu personaje es", personaje)
        else:
            print("No se puede determinar el personaje con las respuestas dadas.")
            # Si no se puede determinar el personaje, solicita al usuario el nombre del animal y lo guarda en el archivo JSON
            nuevo_animal = input("¿En qué animal estás pensando? ")
            data["nuevo_animal"] = nuevo_animal

        # Guarda los datos actualizados en el archivo JSON
        with open("data.json", "w") as file:
            json.dump(data, file)

        respuesta = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if respuesta != "si":
            print("¡Gracias por jugar! Hasta luego.")
            break

def determinar_personaje(tipo_animal, color_pelaje, especie):
    if tipo_animal == "mamífero" and color_pelaje == "marrón" and especie == "león":
        return "León"
    elif tipo_animal == "mamífero" and color_pelaje == "negro" and especie == "oso":
        return "Oso Negro"
    elif tipo_animal == "mamífero" and color_pelaje == "blanco" and especie == "tigre":
        return "Tigre Blanco"
    elif tipo_animal == "ave" and color_pelaje == "negro":
        return "Cuervo"
    elif tipo_animal == "ave" and color_pelaje == "blanco":
        return "Gaviota"
    elif tipo_animal == "reptil" and color_pelaje == "verde":
        return "Serpiente"
    else:
        return None

if __name__ == "__main__":
    main()
