from variables import *

texto_prueba = id_by_steps[1]["Description"]


def formatText(texto, longitud_linea, separador):
    resultado = ""          # Texto final formateado
    linea_actual = ""       # Línea que estamos construyendo
    palabra = ""            # Palabra que estamos leyendo letra por letra
    for letra in texto:     # Recorremos cada carácter del texto
        if not letra == " ":    # Si no es espacio, agregamos la letra a la palabra
            palabra += letra
        else:               # Si encontramos un espacio, la palabra terminó
            if linea_actual == "":  # Línea vacía
                linea_actual = palabra
            else:
                # Verificar si cabe la palabra en la línea
                if len(linea_actual) + 1 + len(palabra) <= longitud_linea:
                    linea_actual = linea_actual + " " + palabra
                else:
                    if resultado == "":
                        resultado = linea_actual
                    else:
                        resultado = resultado + separador + linea_actual
                    linea_actual = palabra
            palabra = ""     # Reiniciamos palabra
    # Añadir la última palabra que quedó después del último espacio
    if not palabra == "":
        if linea_actual == "":
            linea_actual = palabra
        else:
            if len(linea_actual) + 1 + len(palabra) <= longitud_linea:
                linea_actual = linea_actual + " " + palabra
            else:
                if resultado == "":
                    resultado = linea_actual
                else:
                    resultado = resultado + separador + linea_actual
                linea_actual = palabra
    # Añadir la última línea al resultado
    if resultado == "":
        resultado = linea_actual
    else:
        resultado = resultado + separador + linea_actual
    return resultado

resultado = formatText(texto_prueba, longitud_linea=50, separador="\n")
print(resultado)


def getHeader(texto):
    resultado = "".center(50,"*") + "\n" + texto.center(50,"=") + "\n" + "".center(50,"*") + "\n"
    return resultado

resultado = getHeader("Pato")
print(resultado)