import pymysql

from variables import *

"""
def conectar_BDD():
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="aws",
            database="adventure_game",
            port=3306
        )
        print("Conectado a la BDD")
        return conexion
    except pymysql.MySQLError as e:
        print("Error al conectar con la BDD:\n", e)
        return ""
"""
"""
def get_table(query):
    try:
        with conectar_BDD().cursor() as cursor:
            cursor.execute(query)
            filas = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return (tuple(columnas), filas)
    finally:
        conectar_BDD().close()
"""

def get_answers_bystep_adventure():
    resultado = {}
    for clave in idAnswers_ByStep_Adventure:
        if clave[1] == 1:
            resultado[clave] = idAnswers_ByStep_Adventure[clave]
    return resultado

print(get_answers_bystep_adventure())

def get_adventures_with_chars():
    resultado = adventures
    return resultado

def get_id_bystep_adventure():
    resultado = {}
    referencia = get_answers_bystep_adventure()
    for clave in referencia:
        valor = referencia[clave]  # Ejemplo: {"NextStep_Adventure": 1}
        next_step = valor["NextStep_Adventure"]
        if next_step in id_by_steps:
            resultado[next_step] = id_by_steps[next_step]
    return resultado

def get_first_step_adventure():
    print()

def get_characters():
    resultado = characters
    return resultado
def getReplayAdventures():
    resultado = replayAdventures
    return resultado

def getChoices():
    print()

print(get_id_bystep_adventure())