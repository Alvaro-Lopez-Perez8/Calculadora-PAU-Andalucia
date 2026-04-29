# Copyright © 2026 Álvaro López Pérez
# Este archivo forma parte de "Calculadora PAU Andalucía 2026".

# “Calculadora PAU Andalucía (2026)” se distribuye bajo la Licencia de Uso, Distribución y Adaptación “ALOPPER BY-RC-SA-NAI v1.0”
# Texto completo en LICENSE.txt
# Se permite el uso, copia, distribución gratuita y modificación bajo la misma licencia, con atribución obligatoria y enlace a la versión original gratuita.

# Versión original gratuita: https://drive.google.com/drive/folders/1wqzLrA6vG_kt93CTAKJ6Gax0JJEQPa__
# Repositorio oficial: https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git

# No se permite vender, sublicenciar, explotar comercialmente, poner detrás de pago ni usar este archivo, el programa o sus contenidos para entrenamiento,
# ajuste, evaluación o desarrollo de sistemas de inteligencia artificial sin autorización previa, expresa y por escrito del titular.

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QSizePolicy, QComboBox, QLabel
from PySide6.QtGui import QRegularExpressionValidator, QIcon
from PySide6.QtCore import Qt, QUrl, QRegularExpression

import Functions as F
import DocumentReader as R
import InformGenerator as I
from UI import Ui_MainWindow

#Configurar ordenación española
import locale

try:
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    keyfn = lambda s: locale.strxfrm(s)
except locale.Error:
    keyfn = lambda s: s  # fallback

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Iniciamos la ventana
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Iniciamos Stack al inicio
        self.ui.FAdStackedWidget.setCurrentIndex(0)
        
        #Importamos los datos del documento de ponderaciones
        self.idiomas, self.troncales, self.asignaturas, carreras_p, self.ponderaciones, error = R.leer_documento_p()
        if error != "OK":
            self.error_sistema(error)
        
        #Importamos los datos del documento de notas de corte
        self.year, carreras_n, self.notas_corte, error = R.leer_documento_n()
        if error != "OK":
            self.error_sistema(error)
        
        #Comprobamos que todas las carreras tienen ponderaciones
        for carrera in carreras_n:
            if carrera not in carreras_p:
                    self.error_sistema("ERROR. No se han encontrado coincidencias para la carrera " + carrera +".")
        
        #Una vez comprobado, nos quedamos con las carreras de las notas de corte
        self.carreras = carreras_n
        del carreras_p
        del carreras_n
        
        #A las listas de idiomas, troncales y asignaturas les añadimos una opción de "Seleccionar"
        self.idiomas.insert(0, "Seleccionar")
        self.troncales.insert(0, "Seleccionar")
        self.asignaturas.insert(0, "Seleccionar")
        
        #Configuramos la variable para restaurar los datos al cambiar de fase en el FAdStackedWidget
        self.estado_admision = [{"asignatura": "Seleccionar", "SLE": "Seleccionar", "nota": ""}, {"asignatura": "Seleccionar", "SLE": "Seleccionar", "nota": ""},
                                {"asignatura": "Seleccionar", "SLE": "Seleccionar", "nota": ""}, {"asignatura": "Seleccionar", "SLE": "Seleccionar", "nota": ""}]
        
        #Configuramos los elementos fijos
        self.configurar_validadores()
        self.cargar_comboboxes(self.idiomas, self.troncales)
        
        #Configuramos las comboboxes
        self.actualizar_comboboxes()
        self.actualizar_SLE()
        
        #Configuramos estabilidad del layout
        self.reconfigurar_layout()
        
        #Conectamos los elementos
        self.conectar_elementos()

    def error_sistema(self, mensaje):
        #Esta función se encarga de, si se detecta un error de la aplicación,
        #como si las carreras no coinciden, congelar la aplicación y alertar al ususario
        
        try: #Lo mostramos por el Output
            self.ui.Output.clear()
            self.ui.Output.append(str(mensaje))
            self.ui.Output.append("La aplicación se ha bloqueado.")
        
        except Exception: #Si no, no pasa nada
            pass

        QMessageBox.critical(
            self,
            "ERROR",
            "Ha ocurrido un error inesperado.\n\n"
            "La aplicación quedará bloqueada para evitar resultados incorrectos.\n\n"
            f"{mensaje}")

        # Congela la ventana sin cerrarla
        self.setEnabled(False)
    
    def mostrar_info_programa(self):
        ruta_licencia = R.ruta("LICENSE.txt")
        enlace_licencia = QUrl.fromLocalFile(str(ruta_licencia)).toString()
        
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Acerca de Calculadora PAU Andalucía")
        mensaje.setIcon(QMessageBox.Icon.Information)

        mensaje.setTextFormat(Qt.TextFormat.RichText)
        mensaje.setText(
            f"""
            <h2>Calculadora PAU Andalucía (2026)</h2>

            <p>
                <b>Versión:</b> Beta-1.0
            </p>
            
            <p>
                <b>Creador:</b> Álvaro López Pérez<br>
                <b>Contacto:</b> alopper8@gmail.com
            </p>
            
            <p>
                <b>Licencia:</b> Este programa se distribuye bajo la licencia <b>ALOPPER BY-RC-SA-NAI v1.0</b>
                Puedes consultar el texto <a href="{enlace_licencia}">aquí</a> o la versión en PDF en la carpeta de Drive.
            </p>
            
            <p>
                <b>Manual, licencia y descarga:</b><br>
                <a href="https://drive.google.com/drive/folders/1wqzLrA6vG_kt93CTAKJ6Gax0JJEQPa__">
                    Abrir carpeta de Drive
                </a>
            </p>

            <p>
                <b>Código fuente:</b><br>
                <a href="https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git">
                    Ver repositorio en GitHub
                </a>
            </p>

            <p>
                <b>Aviso:</b><br>
                La información proporcionada por este programa es orientativa y no garantiza el acceso real a la universidad.
            </p>
            """
        )

        for label in mensaje.findChildren(QLabel):
            label.setOpenExternalLinks(True)

        mensaje.exec()
    
    def configurar_validadores(self):
        #Esta función establece las entradas permitidas en los campos de texto
        regex_nombre = QRegularExpression(r'[^<>:"/\\|?*.]*') #Prohíbe caracteres prohibidos en Windows para nombres de archivos
        regex_3_dec = QRegularExpression(r"^(10([.,]\d{0,3})?|[0-9]([.,]\d{0,3})?)?$") #Número de 3 decimales con coma o punto
        regex_2_dec = QRegularExpression(r"^(10([.,]\d{0,2})?|[0-9]([.,]\d{0,2})?)?$") #Número de 2 decimales con coma o punto
        
        #Configurar los validadores
        validador_nombre = QRegularExpressionValidator(regex_nombre, self)
        validador_bach = QRegularExpressionValidator(regex_3_dec, self)
        validador_notas = QRegularExpressionValidator(regex_2_dec, self)
        
        #Nombre
        self.ui.NombreInput.setValidator(validador_nombre)

        # Bachillerato
        self.ui.Bach1Input.setValidator(validador_bach)
        self.ui.Bach2Input.setValidator(validador_bach)

        # Fase de acceso
        self.ui.LenguaInput.setValidator(validador_notas)
        self.ui.HoFInput.setValidator(validador_notas)
        self.ui.IdiomaInput.setValidator(validador_notas)
        self.ui.TroncalInput.setValidator(validador_notas)

        # Fase de admisión
        self.ui.F1OptInput.setValidator(validador_notas)

        self.ui.F2Opt1Input.setValidator(validador_notas)
        self.ui.F2Opt2Input.setValidator(validador_notas)

        self.ui.F3Opt1Input.setValidator(validador_notas)
        self.ui.F3Opt2Input.setValidator(validador_notas)
        self.ui.F3Opt3Input.setValidator(validador_notas)

        self.ui.F4Opt1Input.setValidator(validador_notas)
        self.ui.F4Opt2Input.setValidator(validador_notas)
        self.ui.F4Opt3Input.setValidator(validador_notas)
        self.ui.F4Opt4Input.setValidator(validador_notas)

    def reconfigurar_layout(self):
        #Columnas principales del mismo tamaño (50/50)
        self.ui.GeneralH1Layout.setStretch(0, 1)
        self.ui.GeneralH1Layout.setStretch(1, 1)
        
        #Columna de la izquierda (25/25/50)
        self.ui.NombreCampo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.BachilleratoCampo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.FAcCampo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.ui.GeneralV1Layout.setStretch(0, 1)
        self.ui.GeneralV1Layout.setStretch(1, 1)
        self.ui.GeneralV1Layout.setStretch(2, 2)
        
        #Columna de la derecha (50/50)
        self.ui.GeneralV2Layout.setStretch(0, 1)
        self.ui.GeneralV2Layout.setStretch(1, 1)

        self.ui.FAdStackedWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        #Dentro de VCalculoLayout (25/50/25)
        self.ui.VCalculoLayout.setStretch(0, 1)
        self.ui.VCalculoLayout.setStretch(1, 2)
        self.ui.VCalculoLayout.setStretch(2, 1)

        self.ui.EjecutarButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.Output.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.AutorLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        #Función que permite a los widgets expandirse horizontalmente
        def permitir_expansion(*widgets):
            for w in widgets:
                w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        #Dentro de la Fase de Acceso (75/25)
        permitir_expansion(self.ui.LenguaLabel, self.ui.LenguaInput)
        permitir_expansion(self.ui.HoFCombo, self.ui.HoFInput)
        permitir_expansion(self.ui.IdiomaCombo, self.ui.IdiomaInput)
        permitir_expansion(self.ui.TroncalCombo, self.ui.TroncalInput)
        
        self.ui.FAcH1Layout.setStretch(0, 3)
        self.ui.FAcH1Layout.setStretch(1, 1)

        self.ui.FAcH2Layout.setStretch(0, 3)
        self.ui.FAcH2Layout.setStretch(1, 1)

        self.ui.FAcH3Layout.setStretch(0, 3)
        self.ui.FAcH3Layout.setStretch(1, 1)

        self.ui.FAcH4Layout.setStretch(0, 3)
        self.ui.FAcH4Layout.setStretch(1, 1)
        
        #Dentro de la Fase de Admisión (filas 1-3)
        #Función que establece el tamaño de los widgets
        def escalar_admision(layout, opt_combo, sle_combo, input_line):
            permitir_expansion(opt_combo, sle_combo, input_line) #Permitimos que se expandan

            if sle_combo.isVisible(): #Si SLE visible (50, 25, 25)
                layout.setStretch(0, 2)
                layout.setStretch(1, 1)
                layout.setStretch(2, 1)
            
            else: #Si SLE invisible (75/25)
                layout.setStretch(0, 3)
                layout.setStretch(1, 0)
                layout.setStretch(2, 1)
        
        escalar_admision(self.ui.FAd1H1Layout, self.ui.F1OptCombo, self.ui.F1SLECombo, self.ui.F1OptInput)
        
        escalar_admision(self.ui.FAd2H1Layout, self.ui.F2Opt1Combo, self.ui.F2SLE1Combo, self.ui.F2Opt1Input)
        escalar_admision(self.ui.FAd2H2Layout, self.ui.F2Opt2Combo, self.ui.F2SLE2Combo, self.ui.F2Opt2Input)
        
        escalar_admision(self.ui.FAd3H1Layout, self.ui.F3Opt1Combo, self.ui.F3SLE1Combo, self.ui.F3Opt1Input)
        escalar_admision(self.ui.FAd3H2Layout, self.ui.F3Opt2Combo, self.ui.F3SLE2Combo, self.ui.F3Opt2Input)
        escalar_admision(self.ui.FAd3H3Layout, self.ui.F3Opt3Combo, self.ui.F3SLE3Combo, self.ui.F3Opt3Input)
        
        escalar_admision(self.ui.FAd4H1Layout, self.ui.F4Opt1Combo, self.ui.F4SLE1Combo, self.ui.F4Opt1Input)
        escalar_admision(self.ui.FAd4H2Layout, self.ui.F4Opt2Combo, self.ui.F4SLE2Combo, self.ui.F4Opt2Input)
        escalar_admision(self.ui.FAd4H3Layout, self.ui.F4Opt3Combo, self.ui.F4SLE3Combo, self.ui.F4Opt3Input)
        
        #En la última fila de la Fase de Admisión
        #Permitimos que se expandan
        permitir_expansion(self.ui.F4SLELabel, self.ui.F4Opt4Combo, self.ui.F4SLE4Combo, self.ui.F4Opt4Input)
        
        if self.ui.F4SLELabel.isVisible(): #Si SLE visible (50/0/25/25)
            self.ui.Fad4H4Layout.setStretch(0, 2)
            self.ui.Fad4H4Layout.setStretch(1, 0)
            self.ui.Fad4H4Layout.setStretch(2, 1)
            self.ui.Fad4H4Layout.setStretch(3, 1)
        
        else: #Si SLE invisible (0/75/0/25)
            self.ui.Fad4H4Layout.setStretch(0, 0)
            self.ui.Fad4H4Layout.setStretch(1, 3)
            self.ui.Fad4H4Layout.setStretch(2, 0)
            self.ui.Fad4H4Layout.setStretch(3, 1)
        
        #Botones Añadir/Quitar en la Fase de Admisión
        permitir_expansion(self.ui.F1LessButton, self.ui.F1AddButton)
        permitir_expansion(self.ui.F2LessButton, self.ui.F2AddButton)
        permitir_expansion(self.ui.F3LessButton, self.ui.F3AddButton)

        self.ui.FAd1H2Layout.setStretch(0, 1)
        self.ui.FAd1H2Layout.setStretch(1, 1)

        self.ui.FAd2H3Layout.setStretch(0, 1)
        self.ui.FAd2H3Layout.setStretch(1, 1)

        self.ui.FAd3H4Layout.setStretch(0, 1)
        self.ui.FAd3H4Layout.setStretch(1, 1)

        self.ui.F4LessButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        #Forzamos al programa a recalcular la interfaz
        self.ui.centralwidget.layout().invalidate()
        self.ui.centralwidget.layout().activate()
        
    def cargar_comboboxes(self, idiomas, troncales):
        #Esta función rellena las comboboxes que no dependen de otras
        self.ui.HoFCombo.addItems(["Historia de España", "Historia de la Filosofía"])

        self.ui.IdiomaCombo.addItems(idiomas)

        self.ui.TroncalCombo.addItems(troncales)
  
    def conectar_elementos(self):
        #Esta función conecta los elementos con sus respectivas acciones
        #Los botones Add y Less controlan la fase del Stack
        self.ui.F0AddButton.clicked.connect(lambda: self.cambiar_fase_admision(1))
        self.ui.F1LessButton.clicked.connect(lambda: self.cambiar_fase_admision(0))
        self.ui.F1AddButton.clicked.connect(lambda: self.cambiar_fase_admision(2))
        self.ui.F2LessButton.clicked.connect(lambda: self.cambiar_fase_admision(1))
        self.ui.F2AddButton.clicked.connect(lambda: self.cambiar_fase_admision(3))
        self.ui.F3LessButton.clicked.connect(lambda: self.cambiar_fase_admision(2))
        self.ui.F3AddButton.clicked.connect(lambda: self.cambiar_fase_admision(4))
        self.ui.F4LessButton.clicked.connect(lambda: self.cambiar_fase_admision(3))

        self.ui.EjecutarButton.clicked.connect(self.calcular) #Boton CALCULAR
        self.ui.InfoButton.clicked.connect(self.mostrar_info_programa) #Botón Información
        
        #Cualquier cambio en las comboboxes provoca que se actualicen todas
        self.ui.TroncalCombo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.IdiomaCombo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.HoFCombo.currentIndexChanged.connect(self.actualizar_comboboxes)

        self.ui.F1OptCombo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F2Opt1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F2Opt2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3Opt1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3Opt2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3Opt3Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4Opt1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4Opt2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4Opt3Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4Opt4Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F1SLECombo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F2SLE1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F2SLE2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3SLE1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3SLE2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F3SLE3Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4SLE1Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4SLE2Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4SLE3Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
        self.ui.F4SLE4Combo.currentIndexChanged.connect(self.actualizar_comboboxes)
    
    def cambiar_fase_admision(self, nuevo_indice):
        #Esta función cambia entre páginas en la fase de admisión
        self.guardar_estado_admision()
        self.ui.FAdStackedWidget.setCurrentIndex(nuevo_indice)
        self.actualizar_comboboxes()
        self.actualizar_SLE()
        self.restaurar_estado_admision()
        self.actualizar_comboboxes()
        self.actualizar_SLE()
    
    def guardar_estado_admision(self):
        #Esta función guarda los estados de la fase de admisión para poner recuperarlos después de cambiar
        indice = self.ui.FAdStackedWidget.currentIndex()

        if indice == 1:
            self.estado_admision[0]["asignatura"] = self.ui.F1OptCombo.currentText()
            self.estado_admision[0]["SLE"] = self.ui.F1SLECombo.currentText()
            self.estado_admision[0]["nota"] = self.ui.F1OptInput.text()

        elif indice == 2:
            self.estado_admision[0]["asignatura"] = self.ui.F2Opt1Combo.currentText()
            self.estado_admision[0]["SLE"] = self.ui.F2SLE1Combo.currentText()
            self.estado_admision[0]["nota"] = self.ui.F2Opt1Input.text()

            self.estado_admision[1]["asignatura"] = self.ui.F2Opt2Combo.currentText()
            self.estado_admision[1]["SLE"] = self.ui.F2SLE2Combo.currentText()
            self.estado_admision[1]["nota"] = self.ui.F2Opt2Input.text()

        elif indice == 3:
            self.estado_admision[0]["asignatura"] = self.ui.F3Opt1Combo.currentText()
            self.estado_admision[0]["SLE"] = self.ui.F3SLE1Combo.currentText()
            self.estado_admision[0]["nota"] = self.ui.F3Opt1Input.text()

            self.estado_admision[1]["asignatura"] = self.ui.F3Opt2Combo.currentText()
            self.estado_admision[1]["SLE"] = self.ui.F3SLE2Combo.currentText()
            self.estado_admision[1]["nota"] = self.ui.F3Opt2Input.text()

            self.estado_admision[2]["asignatura"] = self.ui.F3Opt3Combo.currentText()
            self.estado_admision[2]["SLE"] = self.ui.F3SLE3Combo.currentText()
            self.estado_admision[2]["nota"] = self.ui.F3Opt3Input.text()

        elif indice == 4:
            self.estado_admision[0]["asignatura"] = self.ui.F4Opt1Combo.currentText()
            self.estado_admision[0]["SLE"] = self.ui.F4SLE1Combo.currentText()
            self.estado_admision[0]["nota"] = self.ui.F4Opt1Input.text()

            self.estado_admision[1]["asignatura"] = self.ui.F4Opt2Combo.currentText()
            self.estado_admision[1]["SLE"] = self.ui.F4SLE2Combo.currentText()
            self.estado_admision[1]["nota"] = self.ui.F4Opt2Input.text()

            self.estado_admision[2]["asignatura"] = self.ui.F4Opt3Combo.currentText()
            self.estado_admision[2]["SLE"] = self.ui.F4SLE3Combo.currentText()
            self.estado_admision[2]["nota"] = self.ui.F4Opt3Input.text()

            self.estado_admision[3]["asignatura"] = self.ui.F4Opt4Combo.currentText()
            self.estado_admision[3]["SLE"] = self.ui.F4SLE4Combo.currentText()
            self.estado_admision[3]["nota"] = self.ui.F4Opt4Input.text()
    
    def restaurar_estado_admision(self):
        #Esta función restaura los datos guardados antes de pasar página
        #Bloqueamos las comboboxes
        self.bloquear_combos(True)
        
        indice = self.ui.FAdStackedWidget.currentIndex()

        if indice == 1:
            self.ui.F1OptCombo.setCurrentText(self.estado_admision[0]["asignatura"])
            self.ui.F1SLECombo.setCurrentText(self.estado_admision[0]["SLE"])
            self.ui.F1OptInput.setText(self.estado_admision[0]["nota"])

        elif indice == 2:
            self.ui.F2Opt1Combo.setCurrentText(self.estado_admision[0]["asignatura"])
            self.ui.F2SLE1Combo.setCurrentText(self.estado_admision[0]["SLE"])
            self.ui.F2Opt1Input.setText(self.estado_admision[0]["nota"])

            self.ui.F2Opt2Combo.setCurrentText(self.estado_admision[1]["asignatura"])
            self.ui.F2SLE2Combo.setCurrentText(self.estado_admision[1]["SLE"])
            self.ui.F2Opt2Input.setText(self.estado_admision[1]["nota"])

        elif indice == 3:
            self.ui.F3Opt1Combo.setCurrentText(self.estado_admision[0]["asignatura"])
            self.ui.F3SLE1Combo.setCurrentText(self.estado_admision[0]["SLE"])
            self.ui.F3Opt1Input.setText(self.estado_admision[0]["nota"])

            self.ui.F3Opt2Combo.setCurrentText(self.estado_admision[1]["asignatura"])
            self.ui.F3SLE2Combo.setCurrentText(self.estado_admision[1]["SLE"])
            self.ui.F3Opt2Input.setText(self.estado_admision[1]["nota"])

            self.ui.F3Opt3Combo.setCurrentText(self.estado_admision[2]["asignatura"])
            self.ui.F3SLE3Combo.setCurrentText(self.estado_admision[2]["SLE"])
            self.ui.F3Opt3Input.setText(self.estado_admision[2]["nota"])

        elif indice == 4:
            self.ui.F4Opt1Combo.setCurrentText(self.estado_admision[0]["asignatura"])
            self.ui.F4SLE1Combo.setCurrentText(self.estado_admision[0]["SLE"])
            self.ui.F4Opt1Input.setText(self.estado_admision[0]["nota"])

            self.ui.F4Opt2Combo.setCurrentText(self.estado_admision[1]["asignatura"])
            self.ui.F4SLE2Combo.setCurrentText(self.estado_admision[1]["SLE"])
            self.ui.F4Opt2Input.setText(self.estado_admision[1]["nota"])

            self.ui.F4Opt3Combo.setCurrentText(self.estado_admision[2]["asignatura"])
            self.ui.F4SLE3Combo.setCurrentText(self.estado_admision[2]["SLE"])
            self.ui.F4Opt3Input.setText(self.estado_admision[2]["nota"])

            self.ui.F4Opt4Combo.setCurrentText(self.estado_admision[3]["asignatura"])
            self.ui.F4SLE4Combo.setCurrentText(self.estado_admision[3]["SLE"])
            self.ui.F4Opt4Input.setText(self.estado_admision[3]["nota"])
        
        #Desbloqueamos las comboboxes
        self.bloquear_combos(False)
    
    def bloquear_combos(self, bloquear):
        #Esta función bloquea (y desbloquea) las comboboxes para que al cambiarlas no creen un bucle infinito
        self.ui.F1OptCombo.blockSignals(bloquear)
        self.ui.F2Opt1Combo.blockSignals(bloquear)
        self.ui.F2Opt2Combo.blockSignals(bloquear)
        self.ui.F3Opt1Combo.blockSignals(bloquear)
        self.ui.F3Opt2Combo.blockSignals(bloquear)
        self.ui.F3Opt3Combo.blockSignals(bloquear)
        self.ui.F4Opt1Combo.blockSignals(bloquear)
        self.ui.F4Opt2Combo.blockSignals(bloquear)
        self.ui.F4Opt3Combo.blockSignals(bloquear)
        self.ui.F4Opt4Combo.blockSignals(bloquear)
        
        self.ui.F1SLECombo.blockSignals(bloquear)
        self.ui.F2SLE1Combo.blockSignals(bloquear)
        self.ui.F2SLE2Combo.blockSignals(bloquear)
        self.ui.F3SLE1Combo.blockSignals(bloquear)
        self.ui.F3SLE2Combo.blockSignals(bloquear)
        self.ui.F3SLE3Combo.blockSignals(bloquear)
        self.ui.F4SLE1Combo.blockSignals(bloquear)
        self.ui.F4SLE2Combo.blockSignals(bloquear)
        self.ui.F4SLE3Combo.blockSignals(bloquear)
        self.ui.F4SLE4Combo.blockSignals(bloquear)

    def obtener_combos_activos(self):
        #Esta función devuelve al programa una lista con los combobox de la fase en uso
        indice = self.ui.FAdStackedWidget.currentIndex()

        if indice == 0:
            return [], []

        elif indice == 1:
            return [self.ui.F1OptCombo], [self.ui.F1SLECombo]

        elif indice == 2:
            return [self.ui.F2Opt1Combo, self.ui.F2Opt2Combo], [self.ui.F2SLE1Combo, self.ui.F2SLE2Combo]

        elif indice == 3:
            return [self.ui.F3Opt1Combo, self.ui.F3Opt2Combo, self.ui.F3Opt3Combo], [self.ui.F3SLE1Combo, self.ui.F3SLE2Combo, self.ui.F3SLE3Combo]

        elif indice == 4:
            return [self.ui.F4Opt1Combo, self.ui.F4Opt2Combo, self.ui.F4Opt3Combo, self.ui.F4Opt4Combo], [self.ui.F4SLE1Combo, self.ui.F4SLE2Combo, self.ui.F4SLE3Combo, self.ui.F4SLE4Combo]

    def actualizar_SLE (self):
        #Esta función se encarga de monitorizar la SLE y mostrar y ocultar las comboboxes correspondientes
        #Bloqueamos las comboboxes
        self.bloquear_combos(True)
        
        indice = self.ui.FAdStackedWidget.currentIndex()

        if indice == 1:
            if self.ui.F1OptCombo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F1SLECombo.show()
            else:
                self.ui.F1SLECombo.hide()

        elif indice == 2:
            if self.ui.F2Opt1Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F2SLE1Combo.show()
                self.ui.F2SLE2Combo.hide()
            elif self.ui.F2Opt2Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F2SLE1Combo.hide()
                self.ui.F2SLE2Combo.show()
            else:
                self.ui.F2SLE1Combo.hide()
                self.ui.F2SLE2Combo.hide()

        elif indice == 3:
            if self.ui.F3Opt1Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F3SLE1Combo.show()
                self.ui.F3SLE2Combo.hide()
                self.ui.F3SLE3Combo.hide()
                self.ui.F3AddButton.setText("Añadir")
            elif self.ui.F3Opt2Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F3SLE1Combo.hide()
                self.ui.F3SLE2Combo.show()
                self.ui.F3SLE3Combo.hide()
                self.ui.F3AddButton.setText("Añadir")
            elif self.ui.F3Opt3Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F3SLE1Combo.hide()
                self.ui.F3SLE2Combo.hide()
                self.ui.F3SLE3Combo.show()
                self.ui.F3AddButton.setText("Añadir")
            else:
                self.ui.F3SLE1Combo.hide()
                self.ui.F3SLE2Combo.hide()
                self.ui.F3SLE3Combo.hide()
                self.ui.F3AddButton.setText("Añadir Segunda Lengua Extranjera")
            
        elif indice == 4:
            if self.ui.F4Opt1Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F4SLE1Combo.show()
                self.ui.F4SLE2Combo.hide()
                self.ui.F4SLE3Combo.hide()
                self.ui.F4SLELabel.hide()
                self.ui.F4Opt4Combo.show()
                self.ui.F4SLE4Combo.hide()
                self.ui.F4LessButton.setText("Quitar")
            elif self.ui.F4Opt2Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F4SLE1Combo.hide()
                self.ui.F4SLE2Combo.show()
                self.ui.F4SLE3Combo.hide()
                self.ui.F4SLELabel.hide()
                self.ui.F4Opt4Combo.show()
                self.ui.F4SLE4Combo.hide()
                self.ui.F4LessButton.setText("Quitar")
            elif self.ui.F4Opt3Combo.currentText() == "Segunda Lengua Extranjera":
                self.ui.F4SLE1Combo.hide()
                self.ui.F4SLE2Combo.hide()
                self.ui.F4SLE3Combo.show()
                self.ui.F4SLELabel.hide()
                self.ui.F4Opt4Combo.show()
                self.ui.F4SLE4Combo.hide()
                self.ui.F4LessButton.setText("Quitar")
            else:
                self.ui.F4SLE1Combo.hide()
                self.ui.F4SLE2Combo.hide()
                self.ui.F4SLE3Combo.hide()
                self.ui.F4SLELabel.show()
                self.ui.F4Opt4Combo.hide()
                self.ui.F4SLE4Combo.show()
                self.ui.F4LessButton.setText("Quitar Segunda Lengua Extranjera")
            
        #Desbloqueamos las comboboxes
        self.bloquear_combos(False)
        
        #Reconfiguramos la interfaz para adaptarla a los cambios en visibilidad
        self.reconfigurar_layout()

    def actualizar_comboboxes(self):
        lenguas_extranjeras = self.idiomas.copy()
        opciones = self.asignaturas.copy()
        
        #Actualizamos la comboboxes de la SLE
        self.actualizar_SLE()
        
        #Bloqueamos las comboboxes
        self.bloquear_combos(True)
        
        #Obtenemos la opción de "Historia de España" o "Historia de la Filosofía" y añadimos la opuesta
        HoF = self.ui.HoFCombo.currentText()
        if HoF == "Historia de España":
            opciones.append("Historia de la Filosofía")
        else:
            opciones.append("Historia de España")
        opciones.sort(key=keyfn) #Ordenamos alfabéticamente
        opciones.remove("Seleccionar") #"Seleccionar" se ha desplazado al ordenar alfabéticamente
        opciones.insert(0, "Seleccionar") #Volver a añadirlo al principio
        
        #Obtenemos el idioma actual y lo eliminamos de la lista (si no es "Seleccionar")
        idioma = self.ui.IdiomaCombo.currentText()
        if idioma != "Seleccionar":
            lenguas_extranjeras.remove(idioma)
        
        #Obtenemos la troncal actual y la eliminamos de la lista (si no es "Seleccionar")
        troncal = self.ui.TroncalCombo.currentText()
        if troncal != "Seleccionar":
            opciones.remove(troncal)
        
        #Lista con todas las comboboxes
        combos_Opt, combos_SLE = self.obtener_combos_activos()
        
        #Vamos de combobox en combobox para las asignaturas
        for combo in combos_Opt:
            #Obtenemos el valor actual
            opcion = combo.currentText()
            
            #Limpiamos la combobox
            combo.clear()
            
            #Si está en "Seleccionar" rellenamos las opciones y dejamos en el primero
            if opcion == "Seleccionar":
                combo.addItems(opciones)
                combo.setCurrentIndex(0)
            
            #Si está en una opción no ocupada previamente (pertenece a la lista disponible)
            elif opcion in opciones:
                combo.addItems(opciones)
                combo.setCurrentText(opcion)
                
                opciones.remove(opcion) #Eliminamos de la lista disponible
            
            #Si está en una opción ya ocupada (no está en la lista disponible)
            elif opcion not in opciones:
                combo.addItems(opciones)
                combo.setCurrentIndex(0)
        
        #Vamos de combobox en combobox para la Segunda Lengua Extranjera
        for combo in combos_SLE:
            #Obtenemos el valor actual
            lengua = combo.currentText()
            
            #Limpiamos la combobox
            combo.clear()
            
            #Si está en "Seleccionar" rellenamos las opciones y dejamos en el primero
            if lengua == "Seleccionar":
                combo.addItems(lenguas_extranjeras)
                combo.setCurrentIndex(0)
            
            #Si está en una opción no ocupada previamente (pertenece a la lista disponible)
            elif lengua in lenguas_extranjeras:
                combo.addItems(lenguas_extranjeras)
                combo.setCurrentText(lengua)
                
                #Si está visible, eliminamos su valor de la lista disponible
                if combo.isVisible():
                    lenguas_extranjeras.remove(lengua) #Eliminamos de la lista disponible
            
            #Si está en una opción ya ocupada (no está en la lista disponible)
            elif lengua not in lenguas_extranjeras:
                combo.addItems(lenguas_extranjeras)
                combo.setCurrentIndex(0)

        #Desbloqueamos las comboboxes
        self.bloquear_combos(False)
        
        #Reconfiguramos la interfaz para adaptarla a los cambios en visibilidad
        self.reconfigurar_layout()

    def texto_a_float(self, texto):
        texto = texto.strip().replace(",", ".")
        
        if texto == "":
            return None
        
        try: #Intentamos convertir la entrada en float
            return float(texto)
        
        except ValueError: #Si falla
            return("ERROR")
        
    def leer_datos(self):
        #Esta función lee todos los datos de la interfaz y los comprueba
        #Nombre
        nombre = self.ui.NombreInput.text().strip()
        if nombre == "":
            self.ui.Output.append("ATENCIÓN. Falta el nombre.")
        
        #Bachillerato
        media_1B = self.texto_a_float(self.ui.Bach1Input.text())
        if media_1B is None:
            self.ui.Output.append("ATENCIÓN. Falta la media de 1º de Bachillerato.")
        elif media_1B == "ERROR":
            self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la media de 1º de Bachillerato.")
        
        media_2B = self.texto_a_float(self.ui.Bach2Input.text())
        if media_2B is None:
            self.ui.Output.append("ATENCIÓN. Falta la media de 2º de Bachillerato.")
        elif media_2B == "ERROR":
            self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la media de 2º de Bachillerato.")

        #Fase de Acceso
        notas_o = []
        
        aux = self.texto_a_float(self.ui.LenguaInput.text())
        if aux is None:
            self.ui.Output.append("ATENCIÓN. Falta la nota de Lengua Castellana y Literatura.")
        elif aux == "ERROR":
            self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de Lengua Castellana y Literatura.")
        else:
            notas_o.append(aux)
        
        FoH = self.ui.HoFCombo.currentText()
        
        aux = self.texto_a_float(self.ui.HoFInput.text())
        if aux is None:
            self.ui.Output.append("ATENCIÓN. Falta la nota de " + FoH +".")
        elif aux == "ERROR":
            self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + FoH + ".")
        else:
            notas_o.append(aux)
        
        LE = self.ui.IdiomaCombo.currentText()
        if LE == "Seleccionar":
            self.ui.Output.append("ATENCIÓN. Selecciona una lengua extranjera.")
        
        aux = self.texto_a_float(self.ui.IdiomaInput.text())
        if aux is None:
            if LE == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Falta la nota de la lengua extranjera.")
            else:
                self.ui.Output.append("ATENCIÓN. Falta la nota de " + LE +".")
        elif aux == "ERROR":
            if LE == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de la lengua extranjera.")
            else:
                self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + LE + ".")
        else:
            notas_o.append(aux)
        
        T = self.ui.TroncalCombo.currentText()
        if T == "Seleccionar":
            self.ui.Output.append("ATENCIÓN. Selecciona una asignatura troncal.")
        
        aux = self.texto_a_float(self.ui.TroncalInput.text())
        if aux is None:
            if T == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Falta la nota de la asignatura troncal.")
            else:
                self.ui.Output.append("ATENCIÓN. Falta la nota de " + T +" (troncal).")
        elif aux == "ERROR":
            if T == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de la asignatura troncal.")
            else:
                self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + T + " (troncal).")
        else:
            notas_o.append(aux)
        
        #Fase de Admisión
        ao = []
        notas_ao = []
        SLE = None

        indice = self.ui.FAdStackedWidget.currentIndex()

        if indice == 1:
            aux1 = self.ui.F1OptCombo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la primera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F1SLECombo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F1OptInput.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)

        elif indice == 2:
            aux1 = self.ui.F2Opt1Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la primera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F2SLE1Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F2Opt1Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            aux1 = self.ui.F2Opt2Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la segunda asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F2SLE2Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F2Opt2Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)

        elif indice == 3:
            aux1 = self.ui.F3Opt1Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la primera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F3SLE1Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F3Opt1Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            aux1 = self.ui.F3Opt2Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la segunda asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F3SLE2Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F3Opt2Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            aux1 = self.ui.F3Opt3Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la tercera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F3SLE3Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F3Opt3Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)

        elif indice == 4:
            aux1 = self.ui.F4Opt1Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la primera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F4SLE1Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F4Opt1Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            aux1 = self.ui.F4Opt2Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la segunda asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F4SLE2Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F4Opt2Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            aux1 = self.ui.F4Opt3Combo.currentText()
            if aux1 == "Seleccionar":
                self.ui.Output.append("ATENCIÓN. Selecciona la tercera asignatura adicional.")
            else:
                ao.append(aux1)
                
                if aux1 == "Segunda Lengua Extranjera":
                    auxSLE = self.ui.F4SLE3Combo.currentText()
                    if auxSLE == "Seleccionar":
                        self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                    else:
                        SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F4Opt3Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                else:
                    notas_ao.append(aux2)
            
            if self.ui.F4SLELabel.isVisible():
                ao.append("Segunda Lengua Extranjera")
                
                auxSLE = self.ui.F4SLE4Combo.currentText()
                if auxSLE == "Seleccionar":
                    self.ui.Output.append("ATENCIÓN. Seleccione el idioma para la Segunda Lengua Extranjera.")
                else:
                    SLE = auxSLE
                
                aux2 = self.texto_a_float(self.ui.F4Opt4Input.text())
                if aux2 is None:
                    self.ui.Output.append("ATENCIÓN. Falta la nota de la Segunda Lengua Extranjera.")
                elif aux2 == "ERROR":
                    self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de la Segunda Lengua Extranjera.")
                else:
                    notas_ao.append(aux2)
            
            else:
                aux1 = self.ui.F4Opt4Combo.currentText()
                if aux1 == "Seleccionar":
                    self.ui.Output.append("ATENCIÓN. Selecciona la cuarta asignatura adicional.")
                else:
                    ao.append(aux1)
                    
                    aux2 = self.texto_a_float(self.ui.F4Opt4Input.text())
                    if aux2 is None:
                        self.ui.Output.append("ATENCIÓN. Falta la nota de " + aux1 + ".")
                    elif aux2 == "ERROR":
                        self.ui.Output.append("ATENCIÓN. Introduce un número decimal correcto en la nota de " + aux1 + ".")
                    else:
                        notas_ao.append(aux2)

        return nombre, media_1B, media_2B, FoH, LE, T, notas_o, ao, notas_ao, SLE
    
    def confirmar_informes(self, nombre):
        #Esta función comprueba que los archivos no existan antes de hacer el informe
        #Archivos que se van a generar
        archivos = [Path(nombre + " (Completo).txt"), Path(nombre + " (Margen).txt")]

        #Comprobamos cuáles existen ya
        existentes = [archivo for archivo in archivos if archivo.exists()]

        #Si no existe ninguno, se puede continuar directamente
        if not existentes:
            return True

        #Preparamos el texto de la advertencia
        lista_archivos = "\n".join(f"• {archivo.name}" for archivo in existentes)
        
        #Preguntamos qué se quiere hacer
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("GENERADOR DE ARCHIVOS")
        mensaje.setIcon(QMessageBox.Icon.Warning)

        mensaje.setText(
            "Ya existe uno o más informes con el nombre:\n\n"
            f"{lista_archivos}\n\n"
            "Si continúas, se sobrescribirán los archivos existentes.\n\n"
            "¿Quieres continuar de todas formas?"
        )

        boton_si = mensaje.addButton("Sí", QMessageBox.ButtonRole.YesRole)
        boton_no = mensaje.addButton("No", QMessageBox.ButtonRole.NoRole)

        mensaje.setDefaultButton(boton_no)

        mensaje.exec()

        if mensaje.clickedButton() == boton_si:
            return True

        self.ui.Output.append("Proceso interrumpido. No se han generado los informes.")
        return False
    
    def calcular(self):
        #Dejamos el Output en blanco
        self.ui.Output.clear()
        
        nombre, media_1B, media_2B, FoH, LE, T, notas_o, ao, notas_ao, SLE = self.leer_datos()
        
        #Si todo ha ido bien (Output vacío), generamos los informes
        if not self.ui.Output.toPlainText().strip():
            
            #Comprobamos si ya existen informes con ese nombre
            if not self.confirmar_informes(nombre):
                return
            
            self.ui.Output.append("Generando informe completo por carreras...")
            
            error = I.imprimir_informe_completo_carreras(self.year, self.ponderaciones, self.notas_corte, self.carreras, nombre, media_1B, media_2B, FoH, LE, T, notas_o, ao, notas_ao, SLE)
            if error == "OK":
                self.ui.Output.append("Informe completo generado con éxito.")
            else:
                self.error_sistema("ERROR. No se ha podido generar informe completo (motivo desconocido).")
            
            self.ui.Output.append("Generando informe simple por margen de acceso...")
            
            error = I.imprimir_informe_simple_margen(self.year, self.ponderaciones, self.notas_corte, self.carreras, nombre, media_1B, media_2B, T, notas_o, ao, notas_ao)
            if error == "OK":
                self.ui.Output.append("Informe simple por margen de acceso generado con éxito.")
            else:
                self.error_sistema("ERROR. No se ha podido generar informe por margen (motivo desconocido).")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    
    ventana.setWindowTitle("Calculadora PAU Andalucía") #Cambiamos el título de la ventana principal
    ventana.setWindowIcon(QIcon(str(R.ruta("Icono.ico")))) #Cambiamos el icono de la ventana
    
    ventana.show()
    sys.exit(app.exec())