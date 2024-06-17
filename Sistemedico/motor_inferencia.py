# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:49:56 2024

@author: 3PW97LA_RS5
"""

import sqlite3

def obtener_enfermedades_y_sintomas():
    conn = sqlite3.connect('sistema_experto.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT e.id, e.nombre, s.nombre FROM enfermedades e JOIN sintomas s ON e.id = s.enfermedad_id')
    filas = cursor.fetchall()
    
    conn.close()
    
    enfermedades_sintomas = {}
    for fila in filas:
        enfermedad_id, enfermedad, sintoma = fila
        if enfermedad not in enfermedades_sintomas:
            enfermedades_sintomas[enfermedad] = []
        enfermedades_sintomas[enfermedad].append(sintoma)
    
    return enfermedades_sintomas

def preguntar_sintoma(sintoma):
    respuesta = input(f"¿Tiene usted {sintoma}? (si/no): ").strip().lower()
    return respuesta == "si"

def diagnosticar():
    enfermedades_sintomas = obtener_enfermedades_y_sintomas()
    sintomas_presentes = []
    
    print("Por favor, responda las siguientes preguntas con 'si' o 'no':\n")
    
    # Recopilar síntomas presentes
    for enfermedad, sintomas in enfermedades_sintomas.items():
        for sintoma in sintomas:
            if sintoma not in sintomas_presentes and preguntar_sintoma(sintoma):
                sintomas_presentes.append(sintoma)
    
    # Diagnosticar en base a los síntomas presentes
    posibles_enfermedades = {}
    
    for enfermedad, sintomas in enfermedades_sintomas.items():
        sintomas_enfermedad = set(sintomas)
        sintomas_presentes_set = set(sintomas_presentes)
        
        if sintomas_enfermedad.issubset(sintomas_presentes_set):
            posibles_enfermedades[enfermedad] = len(sintomas_enfermedad)
    
    if posibles_enfermedades:
        enfermedad_diagnosticada = max(posibles_enfermedades, key=posibles_enfermedades.get)
        print(f"\nBasado en los síntomas, es probable que usted tenga: {enfermedad_diagnosticada}")
    else:
        print("\nNo se pudo determinar una enfermedad basada en los síntomas proporcionados.")

# Ejecutar el diagnóstico
diagnosticar()
