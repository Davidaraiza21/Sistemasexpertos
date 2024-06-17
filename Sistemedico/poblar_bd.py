# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:48:49 2024

@author: 3PW97LA_RS5
"""

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('sistema_experto.db')
cursor = conn.cursor()

# Insertar enfermedades
enfermedades = [
    ("Gripe",),
    ("Resfriado",),
    ("Neumonía",),
    ("Bronquitis",),
    ("Asma",),
    ("Migraña",),
    ("Amigdalitis",),
    ("Gastroenteritis",),
    ("Sinusitis",),
    ("Meningitis",),
    ("COVID-19",),
    ("Dengue",),
    ("Hepatitis",),
    ("Tuberculosis",),
    ("Malaria",)
]

cursor.executemany('INSERT INTO enfermedades (nombre) VALUES (?)', enfermedades)

# Obtener ids de enfermedades para insertar síntomas
cursor.execute('SELECT id, nombre FROM enfermedades')
enfermedades_ids = {nombre: id for id, nombre in cursor.fetchall()}

# Insertar síntomas
sintomas = [
    (enfermedades_ids["Gripe"], "fiebre"),
    (enfermedades_ids["Gripe"], "tos"),
    (enfermedades_ids["Gripe"], "dolor de garganta"),
    (enfermedades_ids["Resfriado"], "congestión nasal"),
    (enfermedades_ids["Resfriado"], "tos"),
    (enfermedades_ids["Resfriado"], "dolor de cabeza"),
    (enfermedades_ids["Neumonía"], "fiebre"),
    (enfermedades_ids["Neumonía"], "escalofríos"),
    (enfermedades_ids["Neumonía"], "dolor en el pecho"),
    (enfermedades_ids["Bronquitis"], "tos"),
    (enfermedades_ids["Bronquitis"], "producción de moco"),
    (enfermedades_ids["Bronquitis"], "dificultad para respirar"),
    (enfermedades_ids["Asma"], "dificultad para respirar"),
    (enfermedades_ids["Asma"], "sibilancias"),
    (enfermedades_ids["Asma"], "opresión en el pecho"),
    (enfermedades_ids["Migraña"], "dolor de cabeza"),
    (enfermedades_ids["Migraña"], "náuseas"),
    (enfermedades_ids["Migraña"], "sensibilidad a la luz"),
    (enfermedades_ids["Amigdalitis"], "dolor de garganta"),
    (enfermedades_ids["Amigdalitis"], "dificultad para tragar"),
    (enfermedades_ids["Amigdalitis"], "fiebre"),
    (enfermedades_ids["Gastroenteritis"], "diarrea"),
    (enfermedades_ids["Gastroenteritis"], "vómitos"),
    (enfermedades_ids["Gastroenteritis"], "dolor abdominal"),
    (enfermedades_ids["Sinusitis"], "dolor facial"),
    (enfermedades_ids["Sinusitis"], "congestión nasal"),
    (enfermedades_ids["Sinusitis"], "dolor de cabeza"),
    (enfermedades_ids["Meningitis"], "fiebre"),
    (enfermedades_ids["Meningitis"], "dolor de cabeza"),
    (enfermedades_ids["Meningitis"], "rigidez en el cuello"),
    (enfermedades_ids["COVID-19"], "fiebre"),
    (enfermedades_ids["COVID-19"], "tos seca"),
    (enfermedades_ids["COVID-19"], "dificultad para respirar"),
    (enfermedades_ids["Dengue"], "fiebre alta"),
    (enfermedades_ids["Dengue"], "dolor de cabeza severo"),
    (enfermedades_ids["Dengue"], "dolor detrás de los ojos"),
    (enfermedades_ids["Hepatitis"], "ictericia"),
    (enfermedades_ids["Hepatitis"], "fatiga"),
    (enfermedades_ids["Hepatitis"], "dolor abdominal"),
    (enfermedades_ids["Tuberculosis"], "tos persistente"),
    (enfermedades_ids["Tuberculosis"], "pérdida de peso"),
    (enfermedades_ids["Tuberculosis"], "sudores nocturnos"),
    (enfermedades_ids["Malaria"], "fiebre"),
    (enfermedades_ids["Malaria"], "escalofríos"),
    (enfermedades_ids["Malaria"], "dolor muscular")
]

cursor.executemany('INSERT INTO sintomas (enfermedad_id, nombre) VALUES (?, ?)', sintomas)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
