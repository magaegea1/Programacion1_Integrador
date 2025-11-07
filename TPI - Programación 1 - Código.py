print("TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA ")
print ("Trabajo Práctico Integrador – Programación 1 \n")


print("***  Trabajo Práctico Integrador (TPI)  ***\n")

print ("-"*40)
print ("\nGestión de Datos de Países en Python: filtros, ordenamientos y estadísticas\n")
print ("-"*40)

# ******************* Importar módulos: *********************************************************
# Para trabajar con archivos CSV de forma segura y estructurada
import csv  
# Para verificar si el archivo existe sin usar excepciones (que están prohibidas en el parcial)
import os   
# Para ordenar listas de diccionarios por clave (permitido por las reglas del parcial)
from operator import itemgetter  
# Para normalizar texto 
import unicodedata


# *********** Definir el nombre del archivo CSV que almacena el catálogo y mostrarlo al iniciar el programa ******************* 
NOMBRE_ARCHIVO = "datos_paises.csv"
print("Archivo de trabajo:", NOMBRE_ARCHIVO)

# ******************* Funciones que trabajan directamente con el archivo csv **************************************
def cargar_datos_desde_csv(nombre_archivo):
    """
    Carga los datos de países desde un archivo CSV, validando estructura y contenido.

    Si el archivo no existe, lo crea con encabezado vacío. 
    Omite registros con errores de formato o valores no válidos, informando al usuario.

    Cada país válido se transforma en un diccionario con claves normalizadas y se agrega a la lista.

    Parámetros:
    - nombre_archivo: str — nombre del archivo CSV.

    Retorno:
    - lista_paises: list[dict] — lista de países con datos limpios y validados.
    """

    lista_paises = []
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Población", "Superficie en km²", "Continente"])
            escritor.writeheader()
        print("Archivo creado con encabezado.")
        return lista_paises

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["Población"].strip().isdigit() and fila["Superficie en km²"].strip().isdigit():                
                nombre = fila["Nombre"].strip().title()
                poblacion = int(fila["Población"])
                superficie = int(fila["Superficie en km²"])
                continente = fila["Continente"].strip().title()
                if poblacion > 0 and superficie > 0 and nombre and continente:
                    lista_paises.append({
                        "Nombre": nombre,
                        "Población": poblacion,
                        "Superficie en km²": superficie,
                        "Continente": continente
                    })
                else:
                    print("⚠️ Registro inválido, se omite:", fila)
            else:
                print("⚠️ Error en registro CSV, se omite:", fila)
    return lista_paises


# Función para actualizar el archivo datos_paises.csv desde la lista de diccionarios sobreescribiendo 
# todo cada vez que se modifica el inventario

# Se decidió que no hayan más formas de escribir en el catálogo csv (por ejemplo, agregando con "a") porque
# se le da prioridad a la seguridad del archivo csv
# De este modo sólo se cambia el archivo csv sobreescribiendo cuando se termina cada caso del menú en el 
# que se modifique la lista de diccionarios.
def guardar_datos_paises_en_csv(lista_paises):
    """
    Guarda los datos de países en un archivo CSV, sobrescribiendo su contenido.

    Parámetros:
    - lista_paises: list[dict]
      Cada diccionario debe tener las claves: 'Nombre' (str), 'Población' (int), 'Superficie en km²' (int), 'Continente' (str)

    Retorno:
    - No devuelve ningún valor. Imprime un mensaje confirmando la actualización del archivo.
    """
    with open(NOMBRE_ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["Nombre", "Población", "Superficie en km²", "Continente"])
        escritor.writeheader()
        for pais in lista_paises:
            escritor.writerow({
                "Nombre": pais["Nombre"],
                "Población": pais["Población"],
                "Superficie en km²": pais["Superficie en km²"],
                "Continente": pais["Continente"]
            })

    print("\t✅ El archivo datos_países.csv ha sido actualizado correctamente")
    return 

# ******************* Preparar los datos necesarios: *********************************************************
# Para validar, limpiar y normalizar los datos que se usarán después:
# Se unifican o agrupan usando como primera palabra: preparar

# Función para validar que se ingrese una cadena de texto que no esté vacía, limpiar y normalizar con title.

# Función principal para validar y limpiar texto.
def preparar_texto_valido():
    """
    Valida y limpia el texto ingresado por el usuario para su uso como título en el catálogo.

    La función:
    - Verifica que la entrada no esté vacía ni sea numérica.
    - Elimina espacios innecesarios y normaliza el formato con `.title()`.
    - Se utiliza para nombres propios (por ejemplo, países).

    No recibe parámetros. Devuelve una cadena validada y normalizada.
    """
    while True:
        texto = " ".join(input("").strip().split()).title()
        if texto == "":
            print("\tDisculpe, la entrada no puede estar vacía, intente nuevamente: ", end="")

        elif texto.isdigit():
            print("\tDisculpe, no puede ser un número, intente nuevamente: ", end="")
  
        else:         
            return texto


# Para normalizar así se eliminan acentos y caracteres especiales, se usará para comparar los países 
# y que no haya duplicados:
def preparar_texto_normalizado(texto):
    """
    Elimina acentos y caracteres especiales del texto, y lo convierte a minúsculas.

    Parámetros:
    - texto: str

    Retorno:
    - texto normalizado: str
    """
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto



# Función para validar que se ingrese una cantidad válida como entero positivo.
def preparar_entero_positivo():
    """
    Valida que la entrada sea un entero positivo:
    - No esté vacío
    - Elimina espacios extremos e internos
    - Verifica que sean solo números
    - Convierte a entero

    Devuelve el número entero validado para ser usado como población y superficie.
    """    
    while True:
        cantidad = " ".join(input("").strip().split())
        
        if not cantidad.isdigit():
            print("\tDisculpe, debe ingresar un número entero positivo. Intente nuevamente: ", end="")
        elif int(cantidad)==0:
            print("\tDisculpe, debe no puede ser 0 (cero). Intente nuevamente: ", end="")
        else:
            return int(cantidad)


# Función para validar si el título ingresado está o no dentro de la lista de diccionarios
def preparar_pais_ya_existe(lista_paises, nuevo_pais):
    """
    Verifica si el país ingresado ya existe en la lista de diccionarios lista_paises.

    Recorre la lista y compara los nombres normalizados
    para evitar duplicaciones. La comparación es insensible a mayúsculas, acentos y espacios redundantes.

    Parámetros:
    - lista_paises: lista de diccionarios con los países y sus datos
    - nuevo_pais: texto ingresado por el usuario, ya validado

    Devuelve:
    - True si el país ya existe
    - False si es un país nuevo
    """
    nuevo_pais_normalizado = preparar_texto_normalizado(nuevo_pais)
    for pais in lista_paises:
        pais_normalizado = preparar_texto_normalizado(pais["Nombre"])
        if pais_normalizado == nuevo_pais_normalizado:
            return True
    return False

# Función para que el usuario elija continente, así no hay ambigüedades
def preparar_continentes():
    """
    Solicita al usuario que seleccione un continente desde una lista cerrada y validada.

    La función:
    - Muestra los continentes disponibles con numeración clara.
    - Valida que la entrada sea numérica y esté dentro del rango permitido.
    - Devuelve el nombre del continente seleccionado, normalizado.

    No recibe parámetros. Devuelve una cadena con el continente elegido.
    """

    CONTINENTES_VALIDOS = [
        "Asia",
        "África",
        "Europa",
        "América del Norte",
        "América del Sur",
        "Oceanía",
        "Antártida"
    ]

    while True:
        print("\n\tContinentes disponibles:")
        for i, continente in enumerate(CONTINENTES_VALIDOS, start=1):
            print(f"\t{i}. {continente}")

        print("\n\tIndique el número del continente seleccionado: ", end="")
        entrada = input().strip()

        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(CONTINENTES_VALIDOS):
                return CONTINENTES_VALIDOS[numero - 1]
            else:
                print("\tDisculpe, el número ingresado no está en el rango válido.")
        else:
            print("\tDisculpe, opción inválida. Debe seleccionar el número de la opción deseada...")
            
# Función para mostrar la lista
def mostrar_lista(lista, mensaje):
    """
    Muestra en pantalla la lista de países 

    Parámetros:
    - Una lista (ordenada o filtrada) (list): lista de diccionarios con datos de países.
    - Un mensaje para mostrar
    """
    print(mensaje)
    for i, pais in enumerate(lista, start=1):
        print(f"\t{i}. {pais['Nombre']}: \t{pais['Población']} habitantes,"
              f"\t{pais['Superficie en km²']} Km², \ten {pais['Continente']}")



# Función para salir o seguir:
def salir_seguir(accion="continuar"):
    """
    Pregunta al usuario si desea salir al menú principal o seguir con la acción indicada.

    Parámetros:
    - accion: str, describe la acción que se está realizando (por ejemplo: 'hacer otra búsqueda', 'cargar otro país')

    Retorno:
    - True si desea salir
    - False si desea continuar
    """
    mensaje = f"¿Desea {accion}? Presione 's' para salir:"
    respuesta = input(f"\n\t{mensaje} ").strip().lower()
    if respuesta == "s":
        print("\tVolvemos al menú principal")
        return True
    else:
        print("\tContinuamos...")
        return False

# Función para definir rangos para filtrar.
def rangos_de(clave="habitantes"):
    """
    Solicita al usuario el tipo de filtro (mayor, menor o igual) y luego el límite numérico,
    usando la clave simbólica para personalizar el mensaje.

    Parámetros:
    - clave: str, describe el campo que se está filtrando (por ejemplo: 'habitantes', 'superficie')

    Retorno:
    - tuple: (limite: int, filtro: int)
    """
    print("\tPor favor, indique qué tipo de filtro desea aplicar:")
    print(f"\n\t1. Países con más de x {clave}")
    print(f"\t2. Países con menos de x {clave}")
    print(f"\t3. Países con x {clave}")
    filtro = pedir_opcion_1_a_n(3)

    print(f"\n\tIndique el valor límite de {clave} que desea usar: ", end="")
    limite = preparar_entero_positivo()

    return limite, filtro

# Función para hacer sugerencias de países al usuario
def preparar_sugerencias(pais_normalizado, lista_paises):
    """
    Muestra sugerencias de países cuyo nombre comienza con los primeros caracteres del nombre normalizado.

    Parámetros:
    - pais_normalizado: str, nombre del país ya normalizado
    - lista_paises: list[dict], catálogo de países

    Retorno:
    - No devuelve valores. Imprime sugerencias si las hay.
    """
    sugerencias = [
        pais["Nombre"] for pais in lista_paises
        if preparar_texto_normalizado(pais["Nombre"]).startswith(pais_normalizado[:4])
    ]

    if sugerencias:
        print("\n\t¿Quiso decir alguno de estos?")
        for nombre in sugerencias:
            print(f"\t- {nombre}")

# Función para pedir opciones:
# Validar pedir opción de 1 a n posibilidades
def pedir_opcion_1_a_n(n):
    """
    Solicita al usuario una opción válida entre 1 y n posibilidades.

    Valida que la entrada sea un número entero dentro del rango permitido.
    Si la opción no es válida, solicita nuevamente.

    Retorno:
    - int: número de opción elegida por el usuario
    """
    while True:
        opcion = input("\n\tPor favor, ingrese la opción deseada: ").strip()
        if opcion.isdigit() and 1<=int(opcion)<=n:
            return int(opcion)
        else:
            print("\n\tDisculpe, pero la opción ingresada no es válida, intente nuevamente...")


# ******************* Funciones de las Opciones del Menú: *********************************************************
#******************* case 1*******************
# 1. Función: Agregar país: alta de un pais individual con población y superficie iniciales y continente
def agregar_pais(lista_paises):
    """
    Permite ingresar un nuevo país con todos sus datos.
    Valida duplicados y entradas vacías.
    Actualiza la lista y el archivo CSV.
    """
    print("\n\t1. Agregar un país")
    print("\tDebe indicar:")
    print("\t- Nombre del país")
    print("\t- Población (entero positivo)")
    print("\t- Superficie en km² (entero positivo)")
    print("\t- Continente")

    #Bucle para agregar países, uno por uno, hasta que el usuario decida salir
    salir = False
    while not salir:
        print("\n\tPor favor, indique el nombre del país que desea cargar: ", end="")
        pais_nuevo=preparar_texto_valido()
        pais_nuevo_normalizado = preparar_texto_normalizado(pais_nuevo)
        if preparar_pais_ya_existe(lista_paises , pais_nuevo):
            print("\tDisculpe, pero ese país ya está registrado")
            if salir_seguir("cargar otro país"):
                return

        else:
            print(f"\n\tPor favor, indique la Población de {pais_nuevo}: ", end="")
            poblacion=preparar_entero_positivo()
            print(f"\n\tPor favor, indique la Superficie en km² de {pais_nuevo}: ", end="")
            superficie=preparar_entero_positivo()
            print(f"\n\tPor favor, indique el Continente donde se encuentra {pais_nuevo}: ", end="")
            continente=preparar_continentes()

            lista_paises.append({
                "Nombre": pais_nuevo,
                "Población": poblacion,
                "Superficie en km²": superficie,
                "Continente": continente
            })
           
            guardar_datos_paises_en_csv(lista_paises)        
            print(f"\n\t✅ Se ha actualizado el archivo con los datos de {pais_nuevo}.")
            print(f"\tDel país: {pais_nuevo} se ha registrado:")
            print(f"\t{poblacion}: Población")
            print(f"\t{superficie}: Superficie en km²")
            print(f"\t{continente}: Continente") 
            if salir_seguir("cargar otro país"):
                return

#******************* case 2 *******************
# 2. Función: Actualizar los datos de Población y Superfice de un Pais.
def actualizar_pais(lista_paises):
    """
    Actualiza la población y superficie de un país existente en la lista.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Modifica la lista en memoria y actualiza el archivo CSV mediante guardar_datos_paises_en_csv().
    """
    while True:
        if not lista_paises:
            print("\tEl catálogo de países está vacío.")
            return

        print("\n\t2. Actualizar datos de un país existente.")            
        print("\tDebe indicar los nuevos valores de población y superficie (reemplazarán los anteriores).")

        print("\n\tPor favor, indique el nombre del país que desea actualizar: ", end="")
        pais_existente = preparar_texto_valido()
        pais_existente_normalizado = preparar_texto_normalizado(pais_existente)

        encontrado = None
        for pais in lista_paises:
            if preparar_texto_normalizado(pais["Nombre"]) == pais_existente_normalizado:
                encontrado = pais
                break

        if encontrado:
            print(f"\n\tDatos actuales de {encontrado['Nombre']}:")
            print(f"\tPoblación: {encontrado['Población']}")
            print(f"\tSuperficie: {encontrado['Superficie en km²']} km²")
            print(f"\tContinente: {encontrado['Continente']}")

            print(f"\n\tPor favor, indique la nueva Población de {pais_existente}: ", end="")
            poblacion_nueva = preparar_entero_positivo()
            print(f"\n\tPor favor, indique la nueva Superficie en km² de {pais_existente}: ", end="")
            superficie_nueva = preparar_entero_positivo()

            encontrado["Población"] = poblacion_nueva
            encontrado["Superficie en km²"] = superficie_nueva

            print("\n\t¿Desea actualizar también el continente? (s/n): ", end="")
            respuesta = input().strip().lower()
            if respuesta == "s":
                nuevo_continente = preparar_continentes()
                encontrado["Continente"] = nuevo_continente
                print(f"\tDel país: {pais_existente}, se actualizó este continente: {nuevo_continente}\n")


            guardar_datos_paises_en_csv(lista_paises)
            print(f"\n\t✅ Se ha actualizado el archivo con los datos de {pais_existente}.")
            print(f"\tDel país: {pais_existente}, tenemos estos datos:")
            print(f"\t{poblacion_nueva}: Población")
            print(f"\t{superficie_nueva}: Superficie en km²")
            print(f"\t{encontrado['Continente']}: Continente")
            if salir_seguir("actualizar otro país"):
                return

        else:
            print("\tEse país no está registrado.")
            preparar_sugerencias(pais_existente_normalizado, lista_paises)
            print("\tSi no lo encontró en la lista de sugerencias y desea agregarlo debe hacerlo desde la opción 1 del menú principal")

            
            if salir_seguir("actualizar otro país"):
                return

#******************* case 3 *******************
# 3. Función:  Buscar un país por nombre (coincidencia parcial o exacta).
# Función auxiliar para obtener el nombre de un país
def obtener_nombre(pais):
    """
    Devuelve el valor de la clave 'Nombre' de un diccionario que representa un país.
    """
    return pais["Nombre"]

# Función central de la opción 3 del menú
def buscar_pais_por_nombre(lista_paises):
    """
    Busca países por coincidencia parcial o exacta en el nombre.

    La búsqueda es insensible a mayúsculas, acentos y espacios redundantes.
    Muestra los resultados ordenados alfabéticamente.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados encontrados.
    """
    if not lista_paises:
        print("\tEl catálogo de países está vacío.")
        return []

    while True:
        print("\n\t3. Cuál es el país que desea buscar? Puede ser una coincidencia parcial o exacta: ", end="")
        nombre = preparar_texto_valido()
        nombre_normalizado = preparar_texto_normalizado(nombre)
        print("\tHemos encontrado lo siguiente:")
        resultados = []

        for i, pais in enumerate(sorted(lista_paises, key=obtener_nombre)):
            if nombre_normalizado in preparar_texto_normalizado(pais["Nombre"]):
                resultados.append(pais)
                print(
                    f"\t{i + 1}. {pais['Nombre']}: \t{pais['Población']} habitantes,"
                    f"\t{pais['Superficie en km²']} Km², \ten {pais['Continente']}"
                )

        if not resultados:
            print("\tDisculpe, no se encontró ninguna coincidencia")

        if salir_seguir("hacer otra búsqueda"):
            return

#******************* case 4 *******************
# 4. Función:  Buscar un país que comience con... (esta opción extra se agrega porque consideramos que es muy útil).
def buscar_paises_que_comienzan_con(lista_paises):
    """
    Busca países cuyo nombre comienza con el texto ingresado por el usuario.

    La búsqueda es insensible a mayúsculas, acentos y espacios.
    Muestra los resultados ordenados alfabéticamente.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados encontrados.
    """
    if not lista_paises:
        print("\tEl catálogo de países está vacío.")
        return []

    while True:
        print("\n\t4. Ingrese la letra o texto inicial del país que desea buscar: ", end="")
        inicio = preparar_texto_valido()
        inicio_normalizado = preparar_texto_normalizado(inicio)
        print("\tHemos encontrado lo siguiente:")
        resultados = []

        for i, pais in enumerate(sorted(lista_paises, key=obtener_nombre)):
            nombre_normalizado = preparar_texto_normalizado(pais["Nombre"])
            if nombre_normalizado.startswith(inicio_normalizado):
                resultados.append(pais)
                print(
                    f"\t{i + 1}. {pais['Nombre']}: \t{pais['Población']} habitantes,"
                    f"\t{pais['Superficie en km²']} Km², \ten {pais['Continente']}"
                )

        if not resultados:
            print("\tDisculpe, no se encontró ninguna coincidencia")

        if salir_seguir("hacer otra búsqueda"):
            return


#******************* case 5 *******************
# 5. Filtrar Países (Continente, rango de Población y rango de Superficie).
# Por continente
def filtrar_por_continente(lista_paises):
    """
    Filtra la lista de países según el continente indicado por el usuario.

    Pregunta si desea aplicar el filtro. Si el usuario acepta, solicita el nombre del continente
    y devuelve una lista con los países que pertenecen a ese continente.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - list[dict]: lista filtrada por continente (o la misma si no se aplica filtro)
    """
    print("\n\tSe va a filtrar por continente... Presione 's' para saltar este filtro: ", end="")
    respuesta = input().strip().lower()
    if respuesta == "s":
        return lista_paises

    print("\n\tPor favor, indique el continente que desea filtrar: ", end="")
    continente = preparar_continentes()
    continente_normalizado = preparar_texto_normalizado(continente)

    lista_filtrada = []
    for pais in lista_paises:
        if preparar_texto_normalizado(pais["Continente"]) == continente_normalizado:
            lista_filtrada.append(pais)
    
    if not lista_filtrada:
        print("\tNo se encontraron países en ese continente.")
    else:
        print(f"\tSe encontraron {len(lista_filtrada)} países en {continente}.")

    return lista_filtrada

# Por Población
def filtrar_por_poblacion(lista_paises):
    """
    Filtra la lista de países según un rango de población indicado por el usuario.

    Pregunta si desea aplicar el filtro. Si el usuario acepta, solicita los valores mínimo y máximo
    y devuelve una lista con los países cuya población está dentro del rango.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - list[dict]: lista filtrada por población (o la misma si no se aplica filtro)
    """
    print("\n\t¿Desea filtrar por población? Presione 's' para saltar este filtro: ", end="")
    respuesta = input().strip().lower()
    if respuesta == "s":
        return lista_paises

    limite_poblacion, filtro = rangos_de("habitantes")

    lista_filtrada = []

    if filtro==1:
        for pais in lista_paises:
            if pais["Población"]>limite_poblacion:
                lista_filtrada.append(pais)
            
        print(f"\tSe encontraron {len(lista_filtrada)} países con una población mayor que {limite_poblacion}.")

    elif filtro==2:
        for pais in lista_paises:
            if pais["Población"]<limite_poblacion:
                lista_filtrada.append(pais)
        print(f"\tSe encontraron {len(lista_filtrada)} países con una población menor que {limite_poblacion}.")

    elif filtro==3:
        for pais in lista_paises:
            if pais["Población"]==limite_poblacion:
                lista_filtrada.append(pais)
        print(f"\tSe encontraron {len(lista_filtrada)} países con una población igual a {limite_poblacion}.")

    return lista_filtrada

# Por superficie
def filtrar_por_superficie(lista_paises):
    """
    Filtra la lista de países según un rango de superficie indicado por el usuario.

    Pregunta si desea aplicar el filtro. Si el usuario acepta, solicita los valores mínimo y máximo
    y devuelve una lista con los países cuya superficie está dentro del rango.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - list[dict]: lista filtrada por superficie (o la misma si no se aplica filtro)
    """

    print("\n\t¿Desea filtrar por superficie? Presione 's' para saltar este filtro: ", end="")
    respuesta = input().strip().lower()
    if respuesta == "s":
        return lista_paises

    limite_superficie, filtro = rangos_de("km²")

    lista_filtrada = []
    if filtro==1:
        for pais in lista_paises:
            if pais["Superficie en km²"]>limite_superficie:
                lista_filtrada.append(pais)
            
        print(f"\tSe encontraron {len(lista_filtrada)} países con una superficie mayor que {limite_superficie}.")

    elif filtro==2:
        for pais in lista_paises:
            if pais["Superficie en km²"]<limite_superficie:
                lista_filtrada.append(pais)
        print(f"\tSe encontraron {len(lista_filtrada)} países con una superficie menor que {limite_superficie}.")

    elif filtro==3:
        for pais in lista_paises:
            if pais["Superficie en km²"]==limite_superficie:
                lista_filtrada.append(pais)
        print(f"\tSe encontraron {len(lista_filtrada)} países con una superficie igual a {limite_superficie}.")

    return lista_filtrada

# Función central de filtrar países
def filtrar_paises(lista_paises):
    """
    Aplica filtros sobre la lista de países según los criterios elegidos por el usuario.

    Los filtros disponibles son:
    - Continente
    - Rango de población
    - Rango de superficie

    Se aplican en cascada, en el orden definido por el programa. Al finalizar, se muestra la lista filtrada.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados filtrados.
    """
    if not lista_paises:
        print("\tEl catálogo de países está vacío.")
        return

    lista_filtrada = lista_paises.copy()

    while True:
        print("\n\t5. A continuación se le ofrecerá filtrar por una o varias opciones," 
              "\n\telija la que desee (una a la vez) y vaya omitiendo la que no desee usar...")
        print("\n\t¿Qué filtro desea aplicar ahora?")
        print("\t1. por Continente")
        print("\t2. por Población")
        print("\t3. por Superficie")

        opcion = pedir_opcion_1_a_n(3)

        if opcion == 1:
            lista_filtrada = filtrar_por_continente(lista_filtrada)
        elif opcion == 2:
            lista_filtrada = filtrar_por_poblacion(lista_filtrada)
        elif opcion == 3:
            lista_filtrada = filtrar_por_superficie(lista_filtrada)

        # Aquí se ofrece salir del bucle
        if salir_seguir("aplicar otro filtro"):
            break

    # Mostrar resultados finales
    print("\n\tResultados filtrados:")
    for i, pais in enumerate(sorted(lista_filtrada, key=obtener_nombre)):
        print(
            f"\t{i + 1}. {pais['Nombre']}: \t{pais['Población']} habitantes,"
            f"\t{pais['Superficie en km²']} Km², \ten {pais['Continente']}"
        )

#******************* case 6 *******************
# 6. Funciones para Ordenar

#Menor a mayor y mayor a menor

#Auxiliares para función siguiente
def obtener_nombre(pais):
    return preparar_texto_normalizado(pais["Nombre"])

def obtener_continente(pais):
    return preparar_texto_normalizado(pais["Continente"])


# Función para ordenar de mayor a menor o al revés. 
def ordenar_mayor_o_menor(lista, clave,n=None):
    """
    Ordena la lista de países según la clave indicada.
    Permite elegir entre orden ascendente (1) y descendente (2).

    Parámetros:
    - lista (list): lista de diccionarios con datos de países.
    - clave (str): campo del diccionario por el cual se desea ordenar.
    - n (int): número de elementos a usar
    """
    print("\t\t1. De menor a mayor")
    print("\t\t2. De mayor a menor")
    print("\tSeleccione 1 o 2: ", end="")
    ordenado = pedir_opcion_1_a_n(2)

    # Si clave es string → usar itemgetter
    if isinstance(clave, str):
        lista_ordenada = sorted(lista, key=itemgetter(clave), reverse=(ordenado == 2))
    else:
        # Si clave es función → usarla directamente
        lista_ordenada = sorted(lista, key=clave, reverse=(ordenado == 2))

    if n is not None:
        lista_ordenada = lista_ordenada[:n]

    mostrar_lista(lista_ordenada, "\n\tLista ordenada:")


# Ordenar por país
def ordenar_por_pais(lista_paises):
    """
    Ordena la lista de países alfabéticamente por nombre.

    El usuario puede elegir ver:
    - La lista completa ordenada
    - Solo los primeros n países

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados ordenados por pantalla.
    """
    print("\t¿Cuántos elementos desea ver?")
    print("\t\t1. Todos")
    print("\t\t2. Los primeros n elementos")
    print("\tSeleccione 1 o 2: ", end="")
    opcion=pedir_opcion_1_a_n(2)
    if opcion==1:
        # Mostrar resultados finales
        n=None
        ordenar_mayor_o_menor(lista_paises, obtener_nombre)
    else:
        print("\t¿Cuántos elementos desea ver?: ", end="")
        n=preparar_entero_positivo()
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, obtener_nombre,n)


# Ordenar por Población
def ordenar_por_poblacion(lista_paises):
    """
    Ordena la lista de países por cantidad de población (de menor a mayor).

    El usuario puede elegir ver:
    - La lista completa ordenada
    - Solo los primeros n países

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados ordenados por pantalla.
    """
    print("\t¿Cuántos elementos desea ver?")
    print("\t\t1. Todos")
    print("\t\t2. Los primeros n elementos")
    print("\tSeleccione 1 o 2: ", end="")
    opcion=pedir_opcion_1_a_n(2)
    if opcion==1:
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, "Población")
    else:
        print("\t¿Cuántos elementos desea ver?: ", end="")
        n=preparar_entero_positivo()
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, "Población",n)

# Ordenar por Superficie
def ordenar_por_superficie(lista_paises):
    """
    Ordena la lista de países por superficie en km² (de menor a mayor).

    El usuario puede elegir ver:
    - La lista completa ordenada
    - Solo los primeros n países

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados ordenados por pantalla.
    """
    print("\t¿Cuántos elementos desea ver?")
    print("\t\t1. Todos")
    print("\t\t2. Los primeros n elementos")
    print("\tSeleccione 1 o 2: ", end="")
    opcion=pedir_opcion_1_a_n(2)
    if opcion==1:
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, "Superficie en km²")
    else:
        print("\t¿Cuántos elementos desea ver?: ", end="")
        n=preparar_entero_positivo()
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, "Superficie en km²",n)


# Ordenar por continente
def ordenar_por_continente(lista_paises):
    """
    Ordena la lista de países alfabéticamente por continente.

    El usuario puede elegir ver:
    - La lista completa ordenada
    - Solo los primeros n países

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime los resultados ordenados por pantalla.
    """
    print("\t¿Cuántos elementos desea ver?")
    print("\t\t1. Todos")
    print("\t\t2. Los primeros n elementos")
    print("\tSeleccione 1 o 2: ", end="")
    opcion=pedir_opcion_1_a_n(2)
    if opcion==1:
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, obtener_continente)
    else:
        print("\t¿Cuántos elementos desea ver?: ", end="")
        n=preparar_entero_positivo()
        # Mostrar resultados finales
        ordenar_mayor_o_menor(lista_paises, obtener_continente,n)

# Ordenar lista completa:
def ordenar_paises(lista_paises):
    """
    Permite ordenar la lista de países según un criterio elegido por el usuario.

    Criterios disponibles:
    - Nombre
    - Población
    - Superficie
    - Continente

    Dentro de cada criterio, el usuario puede elegir:
    - Ver la lista completa ordenada
    - Ver solo los primeros n elementos

    Parámetros:
    - lista_paises: list[dict]
      Lista de diccionarios con los datos de países.

    Retorno:
    - No devuelve valores. Imprime los resultados ordenados por pantalla.
    """
    print(f"\n\t6. Por favor, indique bajo qué criterio quiere ordenar la lista completa:")
    print(f"\t1. País:")
    print(f"\t2. Población:")
    print(f"\t3. Superficie:")
    print(f"\t4. Continente:")
    opcion = pedir_opcion_1_a_n(4)
    match opcion:
        case 1:
            lista_ordenada = ordenar_por_pais(lista_paises)
        case 2:
            lista_ordenada = ordenar_por_poblacion(lista_paises)
        case 3:
            lista_ordenada = ordenar_por_superficie(lista_paises)
        case 4:
            lista_ordenada = ordenar_por_continente(lista_paises)

#******************* case 7 *******************
# Funciones estadísticas:

#Calcula promedio aplicando filtros:
def calcular_promedio_filtrado(lista, clave):
    """
    Calcula el promedio de una clave numérica (como 'Población' o 'Superficie en km²')
    sobre una lista filtrada según los criterios elegidos por el usuario.

    Parámetros:
    - lista: list[dict]
    - clave: str

    Retorno:
    - float: promedio calculado, o 0 si la lista está vacía.
    """
    print(f"\n\t¿Desea aplicar filtros antes de calcular el promedio de {clave.lower()}?")
    print("\t1. Filtrar por continente")
    print("\t2. Filtrar por rango de población")
    print("\t3. Filtrar por rango de superficie")
    print("\t4. No aplicar filtros (usar lista completa)")
    opcion = pedir_opcion_1_a_n(4)

    lista_filtrada = lista.copy()
    if opcion == 1:
        lista_filtrada = filtrar_por_continente(lista_filtrada)
    elif opcion == 2:
        lista_filtrada = filtrar_por_poblacion(lista_filtrada)
    elif opcion == 3:
        lista_filtrada = filtrar_por_superficie(lista_filtrada)

    if not lista_filtrada:
        print("\t⚠️ No hay países que cumplan con los filtros seleccionados.")
        return 0

    suma = 0
    for diccionario in lista_filtrada:
        suma += diccionario[clave]

    promedio = suma / len(lista_filtrada)
    print(f"\n\t✅ Promedio de {clave.lower()} calculado sobre {len(lista_filtrada)} países: {promedio:.2f}")
    return promedio



# Calcular el máximo
def buscar_maximo(lista, clave):
    """
    Busca el país con el valor máximo en la clave indicada.

    Parámetros:
    - lista: list[dict]
    - clave: str (por ejemplo: 'Población' o 'Superficie en km²')

    Retorno:
    - dict: país con el valor máximo
    """
    if not lista:
        return None
    return max(lista, key=itemgetter(clave))


def buscar_maximo_filtrado(lista, clave):
    """
    Busca el país con el valor máximo en la clave indicada.

    Parámetros:
    - lista: list[dict]
      Lista de diccionarios con datos de países.
    - clave: str
      Clave numérica sobre la cual se desea encontrar el valor máximo.

    Retorno:
    - dict: diccionario del país con el valor máximo.
    """
    print(f"\n\t¿Desea aplicar filtros antes de calcular el máximo de {clave.lower()}?")
    print("\t1. Filtrar por continente")
    print("\t2. Filtrar por rango de población")
    print("\t3. Filtrar por rango de superficie")
    print("\t4. No aplicar filtros (usar lista completa)")
    opcion = pedir_opcion_1_a_n(4)

    lista_filtrada = lista.copy()
    if opcion == 1:
        lista_filtrada = filtrar_por_continente(lista_filtrada)
    elif opcion == 2:
        lista_filtrada = filtrar_por_poblacion(lista_filtrada)
    elif opcion == 3:
        lista_filtrada = filtrar_por_superficie(lista_filtrada)

    if not lista_filtrada:
        print("\t⚠️ No hay países que cumplan con los filtros seleccionados.")
        return 0

    pais_max = buscar_maximo(lista_filtrada, clave)

    if pais_max:
        print(f"\n\t✅ País con mayor {clave.lower()}: {pais_max['Nombre']} ({pais_max[clave]})")

    return pais_max


# Calcular el mínimo
def buscar_minimo(lista, clave):
    """
    Busca el país con el valor mínimo en la clave indicada.

    Parámetros:
    - lista: list[dict]
      Lista de diccionarios con datos de países.
    - clave: str
      Clave numérica sobre la cual se desea encontrar el valor mínimo.

    Retorno:
    - dict: diccionario del país con el valor mínimo.
    """
    if not lista:
        return None
    return min(lista, key=itemgetter(clave))

def buscar_minimo_filtrado(lista, clave):
    """
    Busca el país con el valor mínimo en la clave indicada.

    Parámetros:
    - lista: list[dict]
      Lista de diccionarios con datos de países.
    - clave: str
      Clave numérica sobre la cual se desea encontrar el valor máximo.

    Retorno:
    - dict: diccionario del país con el valor mínimo.
    """
    print(f"\n\t¿Desea aplicar filtros antes de calcular el mínimo de {clave.lower()}?")
    print("\t1. Filtrar por continente")
    print("\t2. Filtrar por rango de población")
    print("\t3. Filtrar por rango de superficie")
    print("\t4. No aplicar filtros (usar lista completa)")
    opcion = pedir_opcion_1_a_n(4)

    lista_filtrada = lista.copy()
    if opcion == 1:
        lista_filtrada = filtrar_por_continente(lista_filtrada)
    elif opcion == 2:
        lista_filtrada = filtrar_por_poblacion(lista_filtrada)
    elif opcion == 3:
        lista_filtrada = filtrar_por_superficie(lista_filtrada)

    if not lista_filtrada:
        print("\t⚠️ No hay países que cumplan con los filtros seleccionados.")
        return 0

    pais_min = buscar_minimo(lista_filtrada, clave)
    if pais_min:
        print(f"\n\t✅ País con menor {clave.lower()}: {pais_min['Nombre']} ({pais_min[clave]})")

    return pais_min

# Función: cantidad de países por continente
def cantidad_paises_por_continente(lista_paises):
    """
    Calcula y muestra la cantidad de países por continente.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - dict: continentes como claves y cantidad de países como valores.
    """
    if not lista_paises:
        print("\tEl catálogo de países está vacío.")
        return {}

    conteo = {}
    for pais in lista_paises:
        continente = pais["Continente"]
        conteo[continente] = conteo.get(continente, 0) + 1

    print("\n\t✅ Cantidad de países por continente:")
    for continente, cantidad in conteo.items():
        print(f"\t{continente}: {cantidad} países")

    return conteo

# Función central estadística
def mostrar_estadisticas(lista_paises):
    """
    Muestra estadísticas generales sobre la lista de países.

    El usuario puede elegir calcular:
    - Promedio de población
    - Promedio de superficie
    - País con mayor población
    - País con menor población
    - País con mayor superficie
    - País con menor superficie

    En cada caso, puede aplicar filtros antes de calcular.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Imprime las estadísticas por pantalla.
    """
    while True:
        print("\n\t7. ¿Qué estadística desea calcular?")
        print("\n\t1. Promedio de población")
        print("\t2. Promedio de superficie")
        print("\t3. País con mayor población")
        print("\t4. País con menor población")
        print("\t5. País con mayor superficie")
        print("\t6. País con menor superficie")
        print("\t7. Cantidad de países por continente")
        print("\t8. Volver al menú principal")
        opcion = pedir_opcion_1_a_n(8)
        
        match opcion:
            case 1:
                calcular_promedio_filtrado(lista_paises, "Población")
            case 2:
                calcular_promedio_filtrado(lista_paises, "Superficie en km²")
            case 3:
                buscar_maximo_filtrado(lista_paises, "Población")
            case 4: 
                buscar_minimo_filtrado(lista_paises, "Población")
            case 5:
                buscar_maximo_filtrado(lista_paises, "Superficie en km²")
            case 6:
                buscar_minimo_filtrado(lista_paises, "Superficie en km²")
            case 7:
                cantidad_paises_por_continente(lista_paises)
            case 8:
                print("\n\tVolviendo al menú principal...")
                break

#******************* case 8 *******************
# 8. Función para eliminar un país del catálogo, esta opción es extra a las consignas, se considera 
# importante para dar la posibilidad de borrar algo que se haya cargado mal o por error 
# (por ejemplo, si se cargó mal el nombre del país: Argentian en vez de Argentina y se encuentra ahora duplicado
#  con esos dos nombres)
def eliminar_pais(lista_paises):
    """
    Elimina un país del catálogo si existe y el usuario lo confirma.

    Parámetros:
    - lista_paises: list[dict]

    Retorno:
    - No devuelve valores. Modifica la lista en memoria y actualiza el archivo CSV mediante guardar_datos_paises_en_csv().
    """
    while True:
        if not lista_paises:
            print("\tEl catálogo de países está vacío.")
            return

        print("\n\t8. Eliminar un país del catálogo.")
        print("\t¡CUIDADO! Luego de borrar un país del catálogo no podrá deshacer esta acción. Se le pedirá confirmación...")
        print("\tPor favor, indique el nombre del país que desea eliminar: ", end="")
        pais_a_eliminar = preparar_texto_valido()
        pais_normalizado = preparar_texto_normalizado(pais_a_eliminar)

        encontrado = None
        for pais in lista_paises:
            if preparar_texto_normalizado(pais["Nombre"]) == pais_normalizado:
                encontrado = pais
                break

        if encontrado:
            print(f"\n\tSe encontró el país: {encontrado['Nombre']}")
            print(f"\tPoblación: {encontrado['Población']}")
            print(f"\tSuperficie: {encontrado['Superficie en km²']} km²")
            print(f"\tContinente: {encontrado['Continente']}")
            print("\n\t¿Está seguro de que desea eliminar este país? ⚠️  Esta acción no se puede deshacer. (s/n): ", end="")
            confirmacion = input().strip().lower()
            if confirmacion == "s":
                lista_paises.remove(encontrado)
                print(f"\n\t✅ El país {encontrado['Nombre']} ha sido eliminado del catálogo.")
                guardar_datos_paises_en_csv(lista_paises)
            
            else:
                print("\n\tOperación cancelada. El país no fue eliminado.")

            if salir_seguir("eliminar otro país"):
                return

        else:
            print("\tEse país no está registrado.")
            preparar_sugerencias(pais_normalizado, lista_paises)
            if salir_seguir("eliminar otro país"):
                return


# ******************* Funciones de la estructura del Menú *********************************************************

def mostrar_menu():
    """
    Muestra las opciones disponibles del menú principal.

    No recibe parámetros ni devuelve valores.
    Su propósito es guiar al usuario en la navegación del sistema.
    """
    # Opciones del menú
    print ("-"*40)
    print("1. Agregar un país nuevo con todos sus datos (Nombre, Población, Superficie y Continente).") 
    print("2. Actualizar la población y superficie de un país del catálogo.")
    print("3. Buscar un país por coincidencia total o parcial.")
    print("4. Buscar países que comiencen por...")
    print("5. Filtrar Países (Continente, rango de Población y rango de Superficie)")
    print("6. Ordenar Países (lista completa, primeros n elementos y por filtros).")
    print("7. Estadísticas, generales y filtradas:")
    print("8. Eliminar un país del catálogo (De forma definitiva):")
    print("9. Salir: finalizar la aplicación.")
    print ("-"*40)


def menu_principal(lista_paises):
    """
    Controla el flujo principal del programa, mostrando el menú y ejecutando la opción elegida.

    Parámetros:
    - lista_paises: list[dict], catálogo de países cargado desde el archivo CSV

    Retorno:
    - No devuelve valores. Ejecuta funciones según la opción seleccionada por el usuario.
    """
    while True:
        mostrar_menu()
        # Interacción con el usuario para que ingrese la opción que desea
        num_opcion=pedir_opcion_1_a_n(9)

        match num_opcion: 
            case 1:
                agregar_pais(lista_paises)
                
            case 2:
                actualizar_pais(lista_paises)
                
            case 3:
                buscar_pais_por_nombre(lista_paises)

            case 4:
                buscar_paises_que_comienzan_con(lista_paises)

            case 5:
                filtrar_paises(lista_paises)
                
            case 6:
                ordenar_paises(lista_paises)
                
            case 7:
                mostrar_estadisticas(lista_paises)

            case 8:
                eliminar_pais(lista_paises)

            case 9:
                print("¡Gracias por usar el sistema! \n¡Hasta Pronto!")
                break



# ******************* Para ejecutar el programa **************************************

lista_paises=cargar_datos_desde_csv(NOMBRE_ARCHIVO)
print("\n\tVerificando datos antes de filtrar por población:")
for pais in lista_paises:
    print(f"\t{pais['Nombre']}: \t{pais['Población']} habitantes, \t{pais['Superficie en km²']} km², \t{pais['Continente']}" )

menu_principal(lista_paises)
