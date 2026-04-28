# Copyright © 2026 Álvaro López Pérez
# Este archivo forma parte de "Calculadora PAU Andalucía 2026".

# “Calculadora PAU Andalucía (2026)” se distribuye bajo la Licencia de Uso, Distribución y Adaptación “ALOPPER BY-RC-SA-NAI v1.0”
# Texto completo en LICENSE.txt
# Se permite el uso, copia, distribución gratuita y modificación bajo la misma licencia, con atribución obligatoria y enlace a la versión original gratuita.

# Versión original gratuita: https://drive.google.com/drive/folders/1wqzLrA6vG_kt93CTAKJ6Gax0JJEQPa__
# Repositorio oficial: https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git

# No se permite vender, sublicenciar, explotar comercialmente, poner detrás de pago ni usar este archivo, el programa o sus contenidos para entrenamiento,
# ajuste, evaluación o desarrollo de sistemas de inteligencia artificial sin autorización previa, expresa y por escrito del titular.

from pathlib import Path
import sys

#Configurar ordenación española
import locale

try:
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    keyfn = lambda s: locale.strxfrm(s)
except locale.Error:
    keyfn = lambda s: s  # fallback
    
def ruta(nombre):
    if getattr(sys, "frozen", False):
        base = Path(sys._MEIPASS)
    else:
        base = Path(__file__).resolve().parent
    return base / nombre

def leer_documento_p (): 
    #Abrir el archivo
    with open(ruta("Ponderaciones.txt"), "r", encoding="utf-8") as f:
        lineas = f.readlines()
    
    #Evitamos lineas vacías
    lineas = [ln.strip() for ln in lineas if ln.strip() != ""]
    
    #Comprobamos que tenga por lo menos 4 lineas
    if (len(lineas) < 4):
        return idiomas, troncales, asignaturas, carreras, ponderaciones, "ERROR. Ponderaciones_S.txt debe tener al menos 4 líneas."

    #Comprobamos que existan idiomas, troncales y asignaturas
    if lineas[0].strip() == "":
        return idiomas, troncales, asignaturas, carreras, ponderaciones, "ERROR. La línea 1 (idiomas) está vacía."
    if lineas[1].strip() == "":
        return idiomas, troncales, asignaturas, carreras, ponderaciones, "ERROR. La línea 2 (troncales) está vacía."
    if lineas[2].strip() == "":
        return idiomas, troncales, asignaturas, carreras, ponderaciones, "ERROR. La línea 3 (asignaturas) está vacía."
    
    #Separamos los datos de las 3 primeras lineas
    idiomas = lineas[0].strip().split("\t")
    idiomas.sort(key=keyfn) #Ordenamos alfabéticamente por si acaso
    
    troncales = lineas[1].strip().split("\t")
    troncales.sort(key=keyfn) #Ordenamos alfabéticamente por si acaso
    
    asignaturas = lineas[2].strip().split("\t")
    
    #Comprobamos que las troncales están dentro de las asignaturas
    for asig in troncales:
        if asig not in asignaturas:
            return idiomas, troncales, asignaturas, carreras, ponderaciones, ("ERROR. La troncal " + asig + " no se encuentra en las asignaturas.")
    
    #Guardamos una lista de índices para reordenar las asignaturas y ponderaciones por orden alfabético
    indices_alfabeticos = sorted(range(len(asignaturas)), key=lambda i: keyfn(asignaturas[i]))
    
    #Reordenamos asignaturas por orden alfabético
    asignaturas = [asignaturas[i] for i in indices_alfabeticos]
    
    # Listas para carreras y ponderaciones
    carreras = []
    ponderaciones = {}

    #Leemos línea por línea a partir de la linea 4
    for linea in lineas[3:]:
        partes = [p for p in linea.strip().split("\t") if p != ""] #Divide por tabuladores y evita errores si hay alguno al final

        #Separamos el nombre de la carrera
        carreras.append(partes[0])
        
        #Añadimos la carrera al diccionario (si no está ya)
        if partes[0] not in ponderaciones:
            ponderaciones[partes[0]] = {}
        
        #Comprobamos que exista el mismo número de ponderaciones que asignaturas
        if (len(partes) - 1) != len(asignaturas):
            return idiomas, troncales, asignaturas, carreras, ponderaciones, ("ERROR. El número de asignaturas y ponderaciones no coincide (" + partes[0] + ").")
        
        fila = []#Lista para las ponderaciones
        for j in range(1, len(partes)):   #Desde el segundo elemento en adelante
            partes[j] = partes[j].replace(',', '.') #Reemplazamos coma (por si acaso)
            partes[j] = float(partes[j]) #Convertimos a float
            
            #Comprobamos que la ponderación esté entre los valores permitidos
            valores = [0.0, 0.1, 0.2] #Valores permitidos para las ponderaciones
            if partes[j] not in valores:
                return idiomas, troncales, asignaturas, carreras, ponderaciones, ("ERROR. Una ponderación no se encuentra entre los valores permitidos (" + partes[0] + ", " + str(j) + ").")
            
            fila.append(partes[j])

        #Reordenamos las ponderaciones en orden alfabético
        fila = [fila[i] for i in indices_alfabeticos]
        
        #Guardamos en el diccionario las asignaturas con su ponderacion
        ponderaciones[partes[0]] = dict(zip(asignaturas, fila))
    
    #Ordenamos las carreras por orden alfabético
    carreras.sort(key=keyfn)
    
    return idiomas, troncales, asignaturas, carreras, ponderaciones, "OK"

def leer_documento_n ():
    #Abrir el archivo
    with open(ruta("Notas de corte.txt"), "r", encoding="utf-8") as f:
        lineas = f.readlines()

    #Evitamos lineas vacías
    lineas = [ln.strip() for ln in lineas if ln.strip() != ""]

    #Listas para carreras y notas de corte
    year = 0
    notas_corte = {}

    #Leer línea por línea
    for i in range(len(lineas)):
        linea = lineas[i].strip() #Separamos cada linea
        partes = linea.split("\t") #Divide por tabuladores
        
        #Si es la primera linea (año de las notas) lo guardamos aparte
        if i == 0:
            year = int(partes[0])
        
        else:
            #Separamos el nombre de la carrera
            carrera = partes[0]
            
            #Separamos la universidad
            universidad = partes[1]
            
            #Separamos la facultad
            facultad = partes[2]
            
            #Separamos la nota de corte (cambiamos comas por puntos por si acaso)
            nota = float(partes[3].replace(',', '.'))
            
            #Si la carrera no existe, la creamos
            if carrera not in notas_corte:
                notas_corte[carrera] = {}
            
            #Si la universidad no existe, la creamos
            if universidad not in notas_corte[carrera]:
                notas_corte[carrera][universidad] = {}
            
            #Guardamos la nota por carrera, universidad y facultad
            notas_corte[carrera][universidad][facultad] = nota
    
    #Una vez hecho todo, extraemos una lista con las carreras que será usada en el programa principal
    carreras = list(notas_corte.keys())
    
    #Ordenamos las carreras por orden alfabético
    carreras.sort(key=keyfn)
    
    return year, carreras, notas_corte, "OK"