# 🌎 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador (TPI) – Programación I**
📚 _Tecnicatura Universitaria en Programación – UTN_
📅 Año: 2025

---

## 🏫 Datos del trabajo

**Cátedra:** Programación I
**Carrera:** Tecnicatura Universitaria en Programación (a distancia)
**Institución:** Universidad Tecnológica Nacional (UTN)
**Docentes:** Equipo de cátedra de Programación I
**Integrantes:**
👩‍💻 _María Luz Domenicale Dore_
👩‍💻 _Magaly Egea Ruiz_

---

## 💡 Descripción del proyecto

Este proyecto forma parte del **Trabajo Práctico Integrador (TPI)** de la materia _Programación I_.
El objetivo fue desarrollar una aplicación en **Python** que gestione información sobre países, aplicando los temas aprendidos durante el cuatrimestre: **listas, diccionarios, funciones, condicionales, estructuras repetitivas, archivos CSV y estadísticas básicas.**

El programa permite **agregar, modificar, buscar, filtrar, ordenar y analizar datos de países**, mostrando los resultados por consola de manera organizada.
Toda la información se guarda y se actualiza en un archivo `.csv` llamado `datos_paises.csv`.

---

## 🎯 Objetivo del trabajo

El propósito principal fue **aplicar los conceptos teóricos de Programación I en un caso práctico real**, creando una herramienta que gestione datos de forma ordenada, segura y reutilizable.
Se buscó reforzar la comprensión de:

- ✅ Uso de estructuras de datos como **listas** y **diccionarios**.
- ✅ Modularización del código mediante **funciones**.
- ✅ Lectura y escritura en archivos **CSV**.
- ✅ Filtrado, ordenamiento y cálculo de estadísticas.
- ✅ Validaciones y control de errores en la entrada de datos.

---

## 🧠 Marco teórico (resumen aplicado)

Durante la investigación y el desarrollo, se repasaron varios conceptos fundamentales de Python:

- **Listas:** estructuras que permiten guardar varios elementos y recorrerlos fácilmente.
- **Diccionarios:** estructuras clave-valor ideales para representar países con sus datos (nombre, población, superficie, continente).
- **Funciones:** bloques de código reutilizables que facilitan la organización del programa.
- **Condicionales:** decisiones que controlan el flujo del programa según distintas condiciones.
- **Estructuras repetitivas:** permiten recorrer listas, mostrar resultados y pedir datos varias veces.
- **Archivos CSV:** formato simple y estándar para guardar datos de manera persistente.
- **Estadísticas básicas:** cálculo de promedios, máximos y mínimos sobre datos numéricos.

Toda esta teoría fue aplicada directamente en el desarrollo del código.

---

## 🧩 Estructura y desarrollo del proyecto

El trabajo se dividió en etapas siguiendo una metodología ordenada:

1. **Análisis del enunciado:** comprensión de los requerimientos del sistema.
2. **Diseño de la lógica:** definición del flujo principal y de las funciones necesarias.
3. **Creación del archivo CSV:** estructura inicial con encabezados.
4. **Desarrollo modular:** implementación de cada funcionalidad en una función independiente.
5. **Validaciones:** control de entradas y manejo de errores.
6. **Pruebas:** ejecución de distintos casos para garantizar resultados correctos.
7. **Documentación:** creación de este README, conclusiones y video explicativo.

---

## ⚙️ Funcionamiento del programa

Al ejecutar el programa, se carga automáticamente el archivo `datos_paises.csv` y se muestra un **menú principal** con las siguientes opciones:

1. ➕ **Agregar un país nuevo**
   Permite ingresar nombre, población, superficie y continente, validando que no esté duplicado.

2. ✏️ **Actualizar datos de un país existente**
   Se pueden modificar población, superficie y continente, mostrando antes los valores actuales.

3. 🔍 **Buscar un país por coincidencia total o parcial**
   Permite escribir todo o parte del nombre y devuelve los resultados ordenados alfabéticamente.

4. 🅰️ **Buscar países que comienzan con...**
   Devuelve todos los países cuyo nombre empiece con las letras ingresadas.

5. 🎚️ **Filtrar países**
   Permite filtrar por continente, rango de población o rango de superficie.

6. 🧮 **Ordenar países**
   Se puede ordenar por nombre, población, superficie o continente, mostrando la lista completa o los primeros _n_ resultados.

7. 📊 **Ver estadísticas**
   Calcula promedios de población o superficie y muestra los países con valores máximos o mínimos.

8. 🗑️ **Eliminar un país**
   Opción extra que permite borrar un registro, con confirmación previa.

9. 🚪 **Salir del programa**
   Finaliza la ejecución guardando todos los cambios.

---

## 🛡️ Validaciones y manejo de errores

Durante todo el desarrollo se implementaron validaciones para mejorar la experiencia del usuario y evitar errores:

- 🚫 No se aceptan campos vacíos ni valores negativos.
- 🔢 Solo se permiten números enteros en población y superficie.
- 🔁 Se evita registrar países duplicados.
- ⚠️ Si el archivo CSV no existe, se crea automáticamente.
- 🔍 Cuando no hay coincidencias, se informa al usuario sin interrumpir el programa.

Estas medidas garantizan que los datos se mantengan limpios y que el programa sea robusto ante errores comunes.

---

## 📊 Resultados obtenidos

- ✅ El programa funciona correctamente con todas las opciones del menú.
- 💾 Los datos se guardan y actualizan sin perder información.
- 🧩 Las funciones son claras, separadas y reutilizables.
- 🧠 Los filtros y ordenamientos permiten analizar los datos desde distintos enfoques.
- 🗣️ La comunicación entre integrantes fue constante, repartiendo tareas de forma equilibrada.
- 🐞 Los errores encontrados se resolvieron con pruebas y revisión de pares.

---

## 💬 Conclusiones

Con este proyecto pudimos **consolidar todo lo aprendido** en Programación I.
Aprendimos a planificar, estructurar y programar una aplicación completa, modular y con persistencia de datos.
Además, comprendimos la importancia de las validaciones, el trabajo colaborativo y la documentación clara.

Estas herramientas son fundamentales para cualquier proyecto futuro, ya que permiten crear programas confiables, ordenados y fáciles de mantener.

---

## 🧰 Librerías utilizadas

El programa utiliza solo módulos estándar de Python:

- `csv` → para leer y escribir archivos CSV.
- `os` → para verificar la existencia de archivos.
- `unicodedata` → para normalizar texto (eliminar acentos).
- `operator` → para ordenar listas de diccionarios.

---

## 💾 Instrucciones de ejecución

1. Asegurarse de tener **Python 3.x** instalado.
2. Descargar el archivo `TPI - Programación 1 - Código.py` (o el código del repositorio).
3. Colocar el archivo `datos_paises.csv` en la misma carpeta.
4. Ejecutar el programa desde consola:

   ```bash
   python "TPI - Programación 1 - Código.py
   ```
 
5. Seguir las instrucciones del menú interactivo.

---

## 📂 Estructura del repositorio

```
📁 TPI_Programacion1/
├── 📁 Capturas de Pantalla
├── 📄 Diagrama del flujo del programa.png
├── 📘 Programación 1 - TPI.pdf
├── 📄 TPI - Programación 1 - Código.py
├── 🎥 Video - Programación 1 - TPI.pdf: Guía de Países TPI Programación 1 -.mp4
├── 📄 datos_paises.csv
└── 📄 README.md
```

---

## 🌐 Repositorio y exposición

🔗 **Repositorio GitHub:** [https://github.com/magaegea1/Programacion1_Integrador]
🎥 **Video explicativo:** [https://drive.google.com/file/d/1onQlgumxodV6bT3sGvlo2wC2vRD1zWS5/view?usp=sharing]

---

## 📚 Fuentes y referencias

- Documentación oficial de Python: [https://docs.python.org/es/3/](https://docs.python.org/es/3/)
- Tutoriales y guías de Python en español.
- Apuntes de cátedra de Programación I – UTN.
- Ejemplos prácticos del curso.

---

### ✨ _“El código puede ser correcto, pero la documentación es lo que cuenta su historia.”_

📘 Trabajo realizado por **María Luz Domenicale Dore** y **Magaly Egea Ruiz**
💻 _Tecnicatura Universitaria en Programación – UTN_
