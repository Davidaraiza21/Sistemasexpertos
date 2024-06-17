# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:41:39 2024

@author: 3PW97LA_RS5
"""

import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('sistema_experto.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS enfermedades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sintomas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enfermedad_id INTEGER,
    nombre TEXT NOT NULL,
    FOREIGN KEY (enfermedad_id) REFERENCES enfermedades(id)
)
''')

conn.commit()
conn.close()
