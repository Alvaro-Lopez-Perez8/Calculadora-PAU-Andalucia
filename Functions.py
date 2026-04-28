# Copyright © 2026 Álvaro López Pérez
# Este archivo forma parte de "Calculadora PAU Andalucía 2026".

# “Calculadora PAU Andalucía (2026)” se distribuye bajo la Licencia de Uso, Distribución y Adaptación “ALOPPER BY-RC-SA-NAI v1.0”
# Texto completo en LICENSE.txt
# Se permite el uso, copia, distribución gratuita y modificación bajo la misma licencia, con atribución obligatoria y enlace a la versión original gratuita.

# Versión original gratuita: https://drive.google.com/drive/folders/1wqzLrA6vG_kt93CTAKJ6Gax0JJEQPa__
# Repositorio oficial: https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git

# No se permite vender, sublicenciar, explotar comercialmente, poner detrás de pago ni usar este archivo, el programa o sus contenidos para entrenamiento,
# ajuste, evaluación o desarrollo de sistemas de inteligencia artificial sin autorización previa, expresa y por escrito del titular.

def obtener_nota_opcionales (Pond, T, nota_T, ao, notas_ao):
    #Calculamos la cantidad de nota a obtener de las asignaturas opcionales (max=4)
    #Buscamos las notas ya ponderadas
    notas_pond = []

    #Nota de la troncal ponderada (si está aprobada)
    if(nota_T >= 5):
        notas_pond.append((T, Pond[T]*nota_T))

    #Añadimos las notas de las opcionales
    for i in range(len(ao)):
        if notas_ao[i] >= 5:
            notas_pond.append((ao[i], round((Pond[ao[i]]*notas_ao[i]), 3)))

    #Ordenamos la lista de mayor a menor según el segundo elemento
    notas_pond.sort(key=lambda x:x[1], reverse=True)
    
    #Eliminamos todas las asignaturas que no ponderen
    notas_pond = [x for x in notas_pond if x[1] != 0] #Eliminamos las que no ponderen
    
    #Separamos los dos mayores (2 primeros elementos)
    top2 = notas_pond[:2]

    #Sumamos los segundos valores de los dos elementos
    nota_ao = round(sum([x[1] for x in top2]), 3)

    #Devolvemos la tupla, la lista y la suma
    return top2, nota_ao, notas_pond

def buscar_lugar(carrera, notas_corte, nota):
    #Creeamos una lista que será la salida
    lugares = []
    
    #Creamos un diccionario de lugares donde entra, otros donde entra justo, y otros donde no entra
    lugares_A = {}
    lugares_B = {}
    lugares_C = {}
    
    #Vamos de universidad en universidad
    for universidad in notas_corte[carrera].keys():
        #Vamos de facultad en facultad
        for facultad in notas_corte[carrera][universidad].keys():
            clave = (universidad, facultad)
            
            nota_c = float(notas_corte[carrera][universidad][facultad])
            
            if nota > nota_c:
                lugares_A[clave] = round((nota - nota_c), 3)
            elif nota == nota_c:
                lugares_B[clave] = 0
            else:
                lugares_C[clave] = round((nota_c - nota), 3)
    
    #Ordenamos de mayor a menor segun el margen (lugares_B es innecesario)
    lugares_A = dict(sorted(lugares_A.items(), key=lambda x: x[1], reverse=False))
    lugares_C = dict(sorted(lugares_C.items(), key=lambda x: x[1], reverse=False))

    #Guardamos todo en lugares
    lugares.append(lugares_A)
    lugares.append(lugares_B)
    lugares.append(lugares_C)
    
    #Devolvemos lugares
    return lugares