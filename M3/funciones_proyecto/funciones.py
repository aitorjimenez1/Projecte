

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

#texto_prueba = id_by_steps[1]["Description"]
#resultado = formatText(texto_prueba, longitud_linea=50, separador="\n")
#print(resultado)


def getHeader(texto,largo):
    resultado = "".center(largo,"*") + "\n" + texto.center(largo,"=") + "\n" + "".center(largo,"*") + "\n"
    return resultado

#resultado = getHeader("Pato",50)
#print(resultado)

def menu_opc(opciones):
    numero = 1
    resultado = ""
    for opcion in opciones:
        resultado += str(numero)+") " + str(opcion) + "\n"
        numero += 1
    return resultado

#print(menu_opc(["s","asa","dds"]))

def validar_opcion(maximo):
    opc = input("Opción: ")
    if not opc.isdigit():
        print("\nNumeric Entries Only")
        input("Enter to continue\n")
        return None
    elif int(opc) not in range(1, len(maximo)+1):
        print("\nOption out of Range")
        input("Enter to continue\n")
        return None
    else:
        return int(opc)

def login():
    nombre = input("Introduce tu nombre de usuario: ")
    password = input("Introduce tu contraseña: ")


def create_user_nombre(nombre):
    nombre_solo_letras = nombre.replace(" ", "")
    if nombre.count("  ") > 0 or len(nombre) > 20 or nombre_solo_letras.isalpha() == False:
        if nombre.count("  ") > 0:
            print("El nombre no puede tener 2 espacios seguidos")
        if len(nombre) > 20:
            print("El nombre es demasiado largo (max 20 letras)")
        if nombre_solo_letras.isalpha() == False:
            print("El nombre solo puede contener letras")
        return ""
    else:
        print("Nombre aceptado")
    return nombre

def create_user_password(password):
    if len(password) < 8:
        print("Contraseña muy corta (minim 8 letras)")
        return ""
    print("Contraseña aceptada")
    return password