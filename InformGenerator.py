# Copyright © 2026 Álvaro López Pérez
# Este archivo forma parte de "Calculadora PAU Andalucía 2026".

# “Calculadora PAU Andalucía (2026)” se distribuye bajo la Licencia de Uso, Distribución y Adaptación “ALOPPER BY-RC-SA-NAI v1.0”
# Texto completo en LICENSE.txt
# Se permite el uso, copia, distribución gratuita y modificación bajo la misma licencia, con atribución obligatoria y enlace a la versión original gratuita.

# Versión original gratuita: https://drive.google.com/drive/folders/1wqzLrA6vG_kt93CTAKJ6Gax0JJEQPa__
# Repositorio oficial: https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git

# No se permite vender, sublicenciar, explotar comercialmente, poner detrás de pago ni usar este archivo, el programa o sus contenidos para entrenamiento,
# ajuste, evaluación o desarrollo de sistemas de inteligencia artificial sin autorización previa, expresa y por escrito del titular.

import locale

import Functions as F

#Configurar ordenación española
try:
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    keyfn = lambda s: locale.strxfrm(s)

except locale.Error:
    keyfn = lambda s: s  # fallback

def imprimir_informe_simple_margen (year, ponderaciones, notas_corte, carreras, nombre, media_1B, media_2B, T, notas_o, ao, notas_ao):
    #Nombre del archivo
    nombre_a = nombre + " (Margen).txt"
    
    #Abrir el archivo
    with open(nombre_a, "w", encoding="utf-8") as doc:
        #Escribimos el título
        doc.write("---------- Informe por Margen de Acceso ----------\n")
        
        notas = {}
        carreras_A = []
        carreras_B = []
        carreras_C = []
        
        #Si en las asignaturas adicionales están "Historia de España" o "Historia de la Filosofía", los eliminamos (y sus notas)
        if "Historia de España" in ao:
            index = ao.index("Historia de España")
            ao.remove("Historia de España")
            del notas_ao[index]
        elif "Historia de la Filosofía" in ao:
            index = ao.index("Historia de la Filosofía")
            ao.remove("Historia de la Filosofía")
            del notas_ao[index]
        
        #Disclaimer
        doc.write("\nLA INFORMACIÓN PROPORCIONADA EN ESTE DOCUMENTO ES PLENAMENTE ORIENTATIVA, NO IMPLICA NI GARANTIZA EL ACCESO REAL A LA UNIVERSIDAD.\n")
        doc.write("\nINFORMACIÓN GENERADA A PARTIR DE LAS PONDERACIONES DEL BOJA Número 192 - Lunes, 6 de octubre de 2025 Y DE LAS NOTAS DE CORTE DEL AÑO " + str(year) + " EXTRAÍDAS DEL DISTRITO ÚNICO ANDALUZ.\n")
        doc.write("\nLAS NOTAS GENERADAS EN ESTE INFORME PUEDEN NO COINCIDIR EXACTAMENTE CON LAS REALES.\n")
        
        doc.write("\n------------------------------------------------------------\n") #Separación
        
        #Calculamos las notas obtenidas de Bachillerato y la Fase de Acceso
        media_B = round((round(media_1B, 3) + round(media_2B, 3))/2, 3)
        nota_B = round(media_B*0.6, 3)
        media_O = round((sum(notas_o)/4), 3)
        nota_O = round((sum(notas_o)*0.1), 3)
        
        #Para aprobar, la media de la fase obligatoria debe salir >= 4
        if media_O < 4:
            doc.write("\n********************** ATENCIÓN **********************\n")
            doc.write("\nLa media de la fase obligatoria es inferior a 4.")
            doc.write("\nPor tanto, has suspendido automáticamente la PAU.\n")
            doc.write("\n******************************************************\n")
        
        #Para aprobar, la nota de Bachillerato + Fase Obligatoria debe ser >= 5
        elif round((nota_B + nota_O), 3) < 5:
            doc.write("\n********************** ATENCIÓN **********************\n")
            doc.write("\nLa nota combinada de Bachillerato y la Fase Obligatoria es inferior a 5.")
            doc.write("\nPor tanto, has suspendido automáticamente la PAU.\n")
            doc.write("\n******************************************************\n")
        
        else:
            #Vamos de carrera en carrera
            for carrera in carreras:
                #Calculamos la nota de corte para esa carrera (sumamos las ponderaciones de las asignaturas opcionales)
                top2, nota_A, notas_pond = F.obtener_nota_opcionales(ponderaciones[carrera], T, notas_o[3], ao, notas_ao)
                nota = round((nota_B + nota_O + nota_A), 3)
                
                #Guardamos la nota en un diccionario (para mostrar luego)
                notas[carrera] = nota
                
                #Calculamos los lugares a los que ha entrado
                lugares = F.buscar_lugar(carrera, notas_corte, nota)
                    
                #Guardamos los lugares en los diccionarios dentro de la carrera
                for clave, margen in lugares[0].items():
                    if clave[1] == "@":
                        lugar = clave[0]
                
                    else:
                        lugar = clave[0] + " (" + clave[1] + ")"
                            
                    carreras_A.append((carrera, lugar, clave[0], clave[1], margen))
                
                for clave, margen in lugares[1].items():
                    if clave[1] == "@":
                        lugar = clave[0]
                
                    else:
                        lugar = clave[0] + " (" + clave[1] + ")"
                            
                    carreras_B.append((carrera, lugar, margen))
                
                for clave, margen in lugares[2].items():
                    if clave[1] == "@":
                        lugar = clave[0]
                
                    else:
                        lugar = clave[0] + " (" + clave[1] + ")"
                            
                    carreras_C.append((carrera, lugar, clave[0], clave[1], margen))
                
            #Ordenamos por margen de menor a mayor (B no es necesario)
            carreras_A.sort(key=lambda x: x[4], reverse=False)
            carreras_C.sort(key=lambda x: x[4], reverse=False)
            
            if carreras_A:
                #Lugares en los que ha entrado con margen
                doc.write("\nCarreras en las que has entrado con margen: \n")
            
                #Mostramos las carreras y lugares a los que ha entrado
                for carrera, lugar, universidad, facultad, margen in carreras_A:
                    doc.write("\n\tHas entrado en " + carrera + " en " + lugar + " (" + str(notas_corte[carrera][universidad][facultad]) + "), con un margen de " + str(margen) + " puntos (tu nota: " + str(notas[carrera]) + ").")

            if carreras_B:
                #Si ya ha mostrado carreras antes, hacemos una separación
                if carreras_A:
                    doc.write("\n\n------------------------------------------------------------\n") #Separación
                
                #Lugares en los que ha entrado justo
                doc.write("\nCarreras en las que has entrado justo: \n")
            
                #Mostramos las carreras y lugares a los que ha entrado justo
                for carrera, lugar, margen in carreras_B:
                    doc.write("\n\tHas alcanzado justo la nota de corte (" + str(notas[carrera]) + ") para " + carrera + " en " + lugar + ".")
            
            if carreras_C:
                #Si ya ha mostrado carreras antes, hacemos una separación
                if carreras_A or carreras_B:
                    doc.write("\n\n------------------------------------------------------------\n") #Separación
                    
                #Lugares en los que no ha entrado
                doc.write("\nCarreras en las que no has entrado: \n")
            
                #Mostramos las carreras y lugares a los que no has entrado
                for carrera, lugar, universidad, facultad, margen in carreras_C:
                    doc.write("\n\tNo has alcanzado la nota de corte (" + str(notas_corte[carrera][universidad][facultad]) + ") para " + carrera + " en " + lugar + ", te has quedado a " + str(margen) + " puntos (tu nota: " + str(notas[carrera]) + ").")
    
    return "OK"

def imprimir_informe_completo_carreras (year, ponderaciones, notas_corte, carreras, nombre, media_1B, media_2B, FoH, LE, T, notas_o, ao, notas_ao, SLE): 
    #Nombre del archivo
    nombre_a = nombre + " (Completo).txt"
    
    #Abrir el archivo
    with open(nombre_a, "w", encoding="utf-8") as doc:
        #Escribimos el título
        doc.write("-------------------- Informe Completo por Carreras --------------------\n")
        
        #Disclaimer
        doc.write("\nLA INFORMACIÓN PROPORCIONADA EN ESTE DOCUMENTO ES PLENAMENTE ORIENTATIVA, NO IMPLICA NI GARANTIZA EL ACCESO REAL A LA UNIVERSIDAD.\n")
        doc.write("\nINFORMACIÓN GENERADA A PARTIR DE LAS PONDERACIONES DEL BOJA Número 192 - Lunes, 6 de octubre de 2025 Y DE LAS NOTAS DE CORTE DEL AÑO " + str(year) + " EXTRAÍDAS DEL DISTRITO ÚNICO ANDALUZ.\n")
        doc.write("\nLAS NOTAS GENERADAS EN ESTE INFORME PUEDEN NO COINCIDIR EXACTAMENTE CON LAS REALES.\n")
        
        #Mostramos la media y la nota de Bachillerato
        doc.write("\n------------ Bachillerato (Max. 6 puntos) ------------\n")
        doc.write("\nMedia de 1º de Bachillerato: " + str(media_1B))
        doc.write("\nMedia de 2º de Bachillerato (2ª evaluación): " + str(media_2B))
        
        #Calculamos la media de Bachillerato
        media_B = round((round(media_1B, 3) + round(media_2B, 3))/2, 3)
        doc.write("\n\nMedia de Bachillerato: " + str(media_B))
        
        #Calulamos la nota obtenida de Bachillerato
        nota_B = round(media_B*0.6, 3)
        doc.write("\nNota obtenida de Bachillerato: " + str(nota_B))
        
        #Mostramos las notas de la Fase de Acceso
        doc.write("\n\n------------ Fase de Acceso (Max. 4 puntos) ------------\n")
        doc.write("\nLengua Castellana y Literatura: " + str(notas_o[0]))
        
        if FoH == "Historia de la Filosofía":
            doc.write("\nHistoria de la Filosofía: " + str(notas_o[1]))
        elif FoH == "Historia de España":
            doc.write("\nHistoria de España: " + str(notas_o[1]))
        
        doc.write("\n" + LE + ": " + str(notas_o[2]))
        
        doc.write("\n" + T + ": " + str(notas_o[3]))
        if notas_o[3] < 5: #Si suspende la troncal, no cuenta para ponderar
            doc.write("\n*AVISO. Al estar suspensa, la asignatura troncal (" + T + "), no ponderará para la Fase de Admisión.*")
        
        #Calculamos la media de la fase obligatoria
        media_O = round((sum(notas_o)/4), 3)
        doc.write("\n\nMedia de la Fase Obligatoria: " + str(media_O))
        
        #Calculamos la nota a obtener de la fase obligatoria
        nota_O = round((sum(notas_o)*0.1), 3)
        doc.write("\nNota de la Fase Obligatoria: " + str(nota_O))
        doc.write("\n\nNota de Bachillerato + Fase Obligatoria: " + str(round((nota_B + nota_O), 3)))
        
        #Mostramos las notas de la Fase de Admisión
        doc.write("\n\n------------ Fase de Admisión (Max. 4 puntos) ------------\n")
        
        if ao: #Si se ha presentado a asignaturas opcionales
            doc.write("\nTe has presentado a las siguientes asignaturas: ")
            
            for i in range(len(ao)):
                if ao[i] == "Segunda Lengua Extranjera":
                    doc.write("\n\tSegunda Lengua Extranjera (" + SLE + "): " + str(notas_ao[i]))
                
                    if notas_ao[i] < 5: #Si suspende el examen, la asignatura no ponderará
                        doc.write("\n\t*AVISO. Al estar suspensa, Segunda Lengua Extranjera (" + SLE + ") no ponderará.*")
                
                elif ao[i] == "Historia de España" or ao[i] == "Historia de la Filosofía":
                    doc.write("\n\t" + ao[i] + ": " + str(notas_ao[i]))
                    
                    doc.write("\n\t*AVISO. La asignatura " + ao[i] + " solo sirve para otras Comunidades Autónomas. Por tanto, aquí no ponderará en absoluto.")
                
                else:
                    doc.write("\n\t" + ao[i] + ": " + str(notas_ao[i]))
                    
                    if notas_ao[i] < 5: #Si suspende el examen, la asignatura no ponderará
                        doc.write("\n\t*AVISO. Al estar suspensa, " + ao[i] + " no ponderará.*")
                      
        else: #Si no se ha presentado a ninguna opcional
            doc.write("\nNo te has presentado a ninguna asignatura adicional.")
        
        #Si en las asignaturas adicionales están "Historia de España" o "Historia de la Filosofía", los eliminamos (y sus notas)
        if "Historia de España" in ao:
            index = ao.index("Historia de España")
            ao.remove("Historia de España")
            del notas_ao[index]
        elif "Historia de la Filosofía" in ao:
            index = ao.index("Historia de la Filosofía")
            ao.remove("Historia de la Filosofía")
            del notas_ao[index]
        
        #Para aprobar, la media de la fase obligatoria debe salir >= 4
        if media_O < 4:
            doc.write("\n\n********************** ATENCIÓN **********************\n")
            doc.write("\nLa media de la fase obligatoria es inferior a 4.")
            doc.write("\nPor tanto, has suspendido automáticamente la PAU.\n")
            doc.write("\n******************************************************\n")
        
        #Para aprobar, la nota de Bachillerato + Fase Obligatoria debe ser >= 5
        elif round((nota_B + nota_O), 3) < 5:
            doc.write("\n\n********************** ATENCIÓN **********************\n")
            doc.write("\nLa nota combinada de Bachillerato y la Fase Obligatoria es inferior a 5.")
            doc.write("\nPor tanto, has suspendido automáticamente la PAU.\n")
            doc.write("\n******************************************************\n")
        
        else:
            doc.write("\n\n----------------- Desglose por carreras -----------------\n")
            
            #Vamos de carrera en carrera
            for carrera in carreras:
                
                doc.write("\nPara la carrera de " + carrera + ":\n")
                
                #Calculamos la nota de corte para esa carrera (sumamos las ponderaciones de las asignaturas opcionales)
                top2, nota_A, notas_pond = F.obtener_nota_opcionales(ponderaciones[carrera], T, notas_o[3], ao, notas_ao)
                nota = round((nota_B + nota_O + nota_A), 3)
                
                #Mostramos su nota de selectividad para la carrera
                doc.write("\n\tTu nota sería de " + str(nota) + " puntos.")
                
                if notas_pond: #Si al menos 1 asignatura ha subido nota
                    doc.write("\n\n\tLas asignaturas que te han subido nota son:")
                    
                    for i, j in top2:
                        J = round(j, 3) #Redondeamos otra vez por si acaso
                        if i != "Segunda Lengua Extranjera":
                            doc.write("\n\t\t" + i + " con ponderación " + str(ponderaciones[carrera][i]) + " y valor " + str(J) + " puntos.")
                        
                        else:
                            doc.write("\n\t\tSegunda Lengua Extranjera (" + SLE + ") con ponderación " + str(ponderaciones[carrera][i]) + " y valor " + str(J) + " puntos.")
                    
                    #Otras asignaturas que ponderan, pero no han subido nota
                    del notas_pond[:2] #Eliminamos el top2
                   
                    if notas_pond: #Mostramos las otras asignaturas
                        doc.write("\n\n\tOtras asignaturas que ponderan pero no te han subido nota son: ")
                    
                        for i, j in notas_pond:
                            J = round(j, 3) #Redondeamos otra vez por si acaso
                            if i != "Segunda Lengua Extranjera":
                                doc.write("\n\t\t" + i + " con ponderación " + str(ponderaciones[carrera][i]) + " y valor " + str(J) + " puntos.")
                            else:
                                doc.write("\n\t\tSegunda Lengua Extranjera (" + SLE + ") con ponderación " + str(ponderaciones[carrera][i]) + " y valor " + str(J) + " puntos.")

                #Calculamos los lugares a los que ha entrado
                lugares = F.buscar_lugar(carrera, notas_corte, nota)
                
                #Lugares en los que has entrado con margen
                if len(lugares[0].items()) > 0:
                    doc.write("\n") #Separación
                    
                    for clave, margen in lugares[0].items():
                        if clave[1] == "@":
                            lugar = clave[0]
            
                        else:
                            lugar = clave[0] + " (" + clave[1] + ")"
                        
                        doc.write("\n\tHas entrado en " + lugar + " (" + str(notas_corte[carrera][clave[0]][clave[1]]) + "), con un margen de " + str(margen) + " puntos.")
                
                #Lugares en los que has entrado justo
                if len(lugares[1].items()) > 0:
                    doc.write("\n") #Separación
                    
                    for clave, margen in lugares[1].items():
                        if clave[1] == "@":
                            lugar = clave[0]
            
                        else:
                            lugar = clave[0] + " (" + clave[1] + ")"
                        
                        doc.write("\n\tHas alcanzado justo la nota de corte en " + lugar + " (" + str(notas_corte[carrera][clave[0]][clave[1]]) + ").")
                
                #Lugares en los que no has entrado
                if len(lugares[2].items()) > 0:
                    doc.write("\n") #Separación
                    
                    for clave, margen in lugares[2].items():
                        if clave[1] == "@":
                            lugar = clave[0]
            
                        else:
                            lugar = clave[0] + " (" + clave[1] + ")"
                        
                        doc.write("\n\tNo has alcanzado la nota de corte en " + lugar + " (" + str(notas_corte[carrera][clave[0]][clave[1]]) + "), te has quedado a " + str(margen) + " puntos.")
                
                #Si no es la última carrera, ponemos una separación
                if carrera != carreras[-1]:
                    doc.write("\n\n------------------------------------------------------------\n")
    
    return "OK"