# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI Pyside6.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(824, 445)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setMaximumSize(QSize(16777215, 16777215))
        self.Titulo.setTabletTracking(True)
        self.Titulo.setLineWidth(1)

        self.verticalLayout.addWidget(self.Titulo)

        self.GeneralH1Layout = QHBoxLayout()
        self.GeneralH1Layout.setSpacing(40)
        self.GeneralH1Layout.setObjectName(u"GeneralH1Layout")
        self.GeneralH1Layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.GeneralV1Layout = QVBoxLayout()
        self.GeneralV1Layout.setSpacing(10)
        self.GeneralV1Layout.setObjectName(u"GeneralV1Layout")
        self.NombreCampo = QGroupBox(self.centralwidget)
        self.NombreCampo.setObjectName(u"NombreCampo")
        self.verticalLayout_2 = QVBoxLayout(self.NombreCampo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.NombreInput = QLineEdit(self.NombreCampo)
        self.NombreInput.setObjectName(u"NombreInput")

        self.verticalLayout_2.addWidget(self.NombreInput)


        self.GeneralV1Layout.addWidget(self.NombreCampo)

        self.BachilleratoCampo = QGroupBox(self.centralwidget)
        self.BachilleratoCampo.setObjectName(u"BachilleratoCampo")
        self.verticalLayout_3 = QVBoxLayout(self.BachilleratoCampo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BachH1Layout = QHBoxLayout()
        self.BachH1Layout.setObjectName(u"BachH1Layout")
        self.Bach1Label = QLabel(self.BachilleratoCampo)
        self.Bach1Label.setObjectName(u"Bach1Label")

        self.BachH1Layout.addWidget(self.Bach1Label)

        self.Bach1Input = QLineEdit(self.BachilleratoCampo)
        self.Bach1Input.setObjectName(u"Bach1Input")

        self.BachH1Layout.addWidget(self.Bach1Input)


        self.verticalLayout_3.addLayout(self.BachH1Layout)

        self.BachH2Layout = QHBoxLayout()
        self.BachH2Layout.setObjectName(u"BachH2Layout")
        self.Bach2Label = QLabel(self.BachilleratoCampo)
        self.Bach2Label.setObjectName(u"Bach2Label")

        self.BachH2Layout.addWidget(self.Bach2Label)

        self.Bach2Input = QLineEdit(self.BachilleratoCampo)
        self.Bach2Input.setObjectName(u"Bach2Input")

        self.BachH2Layout.addWidget(self.Bach2Input)


        self.verticalLayout_3.addLayout(self.BachH2Layout)


        self.GeneralV1Layout.addWidget(self.BachilleratoCampo)

        self.FAcCampo = QGroupBox(self.centralwidget)
        self.FAcCampo.setObjectName(u"FAcCampo")
        self.verticalLayout_5 = QVBoxLayout(self.FAcCampo)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.FAcH1Layout = QHBoxLayout()
        self.FAcH1Layout.setObjectName(u"FAcH1Layout")
        self.LenguaLabel = QLabel(self.FAcCampo)
        self.LenguaLabel.setObjectName(u"LenguaLabel")

        self.FAcH1Layout.addWidget(self.LenguaLabel)

        self.LenguaInput = QLineEdit(self.FAcCampo)
        self.LenguaInput.setObjectName(u"LenguaInput")

        self.FAcH1Layout.addWidget(self.LenguaInput)


        self.verticalLayout_5.addLayout(self.FAcH1Layout)

        self.FAcH2Layout = QHBoxLayout()
        self.FAcH2Layout.setObjectName(u"FAcH2Layout")
        self.HoFCombo = QComboBox(self.FAcCampo)
        self.HoFCombo.setObjectName(u"HoFCombo")
        self.HoFCombo.setMinimumSize(QSize(89, 0))

        self.FAcH2Layout.addWidget(self.HoFCombo)

        self.HoFInput = QLineEdit(self.FAcCampo)
        self.HoFInput.setObjectName(u"HoFInput")

        self.FAcH2Layout.addWidget(self.HoFInput)


        self.verticalLayout_5.addLayout(self.FAcH2Layout)

        self.FAcH3Layout = QHBoxLayout()
        self.FAcH3Layout.setObjectName(u"FAcH3Layout")
        self.IdiomaCombo = QComboBox(self.FAcCampo)
        self.IdiomaCombo.setObjectName(u"IdiomaCombo")

        self.FAcH3Layout.addWidget(self.IdiomaCombo)

        self.IdiomaInput = QLineEdit(self.FAcCampo)
        self.IdiomaInput.setObjectName(u"IdiomaInput")

        self.FAcH3Layout.addWidget(self.IdiomaInput)


        self.verticalLayout_5.addLayout(self.FAcH3Layout)

        self.FAcH4Layout = QHBoxLayout()
        self.FAcH4Layout.setObjectName(u"FAcH4Layout")
        self.TroncalCombo = QComboBox(self.FAcCampo)
        self.TroncalCombo.setObjectName(u"TroncalCombo")

        self.FAcH4Layout.addWidget(self.TroncalCombo)

        self.TroncalInput = QLineEdit(self.FAcCampo)
        self.TroncalInput.setObjectName(u"TroncalInput")

        self.FAcH4Layout.addWidget(self.TroncalInput)


        self.verticalLayout_5.addLayout(self.FAcH4Layout)


        self.GeneralV1Layout.addWidget(self.FAcCampo)

        self.GeneralV1Layout.setStretch(0, 1)
        self.GeneralV1Layout.setStretch(1, 2)

        self.GeneralH1Layout.addLayout(self.GeneralV1Layout)

        self.GeneralV2Layout = QVBoxLayout()
        self.GeneralV2Layout.setSpacing(10)
        self.GeneralV2Layout.setObjectName(u"GeneralV2Layout")
        self.FAdStackedWidget = QStackedWidget(self.centralwidget)
        self.FAdStackedWidget.setObjectName(u"FAdStackedWidget")
        self.FAd0 = QWidget()
        self.FAd0.setObjectName(u"FAd0")
        self.horizontalLayout = QHBoxLayout(self.FAd0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FAdCampo0 = QGroupBox(self.FAd0)
        self.FAdCampo0.setObjectName(u"FAdCampo0")
        self.verticalLayout_6 = QVBoxLayout(self.FAdCampo0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.F0AddButton = QPushButton(self.FAdCampo0)
        self.F0AddButton.setObjectName(u"F0AddButton")

        self.verticalLayout_6.addWidget(self.F0AddButton)


        self.horizontalLayout.addWidget(self.FAdCampo0)

        self.FAdStackedWidget.addWidget(self.FAd0)
        self.FAd1 = QWidget()
        self.FAd1.setObjectName(u"FAd1")
        self.horizontalLayout_2 = QHBoxLayout(self.FAd1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FAdCampo1 = QGroupBox(self.FAd1)
        self.FAdCampo1.setObjectName(u"FAdCampo1")
        self.verticalLayout_7 = QVBoxLayout(self.FAdCampo1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.FAd1H1Layout = QHBoxLayout()
        self.FAd1H1Layout.setObjectName(u"FAd1H1Layout")
        self.F1OptCombo = QComboBox(self.FAdCampo1)
        self.F1OptCombo.setObjectName(u"F1OptCombo")
        self.F1OptCombo.setMaximumSize(QSize(16777215, 16777215))

        self.FAd1H1Layout.addWidget(self.F1OptCombo)

        self.F1SLECombo = QComboBox(self.FAdCampo1)
        self.F1SLECombo.setObjectName(u"F1SLECombo")

        self.FAd1H1Layout.addWidget(self.F1SLECombo)

        self.F1OptInput = QLineEdit(self.FAdCampo1)
        self.F1OptInput.setObjectName(u"F1OptInput")

        self.FAd1H1Layout.addWidget(self.F1OptInput)


        self.verticalLayout_7.addLayout(self.FAd1H1Layout)

        self.FAd1H2Layout = QHBoxLayout()
        self.FAd1H2Layout.setObjectName(u"FAd1H2Layout")
        self.F1LessButton = QPushButton(self.FAdCampo1)
        self.F1LessButton.setObjectName(u"F1LessButton")

        self.FAd1H2Layout.addWidget(self.F1LessButton)

        self.F1AddButton = QPushButton(self.FAdCampo1)
        self.F1AddButton.setObjectName(u"F1AddButton")

        self.FAd1H2Layout.addWidget(self.F1AddButton)


        self.verticalLayout_7.addLayout(self.FAd1H2Layout)


        self.horizontalLayout_2.addWidget(self.FAdCampo1)

        self.FAdStackedWidget.addWidget(self.FAd1)
        self.FAd2 = QWidget()
        self.FAd2.setObjectName(u"FAd2")
        self.horizontalLayout_5 = QHBoxLayout(self.FAd2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.FAdCampo2 = QGroupBox(self.FAd2)
        self.FAdCampo2.setObjectName(u"FAdCampo2")
        self.verticalLayout_8 = QVBoxLayout(self.FAdCampo2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.FAd2H1Layout = QHBoxLayout()
        self.FAd2H1Layout.setObjectName(u"FAd2H1Layout")
        self.F2Opt1Combo = QComboBox(self.FAdCampo2)
        self.F2Opt1Combo.setObjectName(u"F2Opt1Combo")

        self.FAd2H1Layout.addWidget(self.F2Opt1Combo)

        self.F2SLE1Combo = QComboBox(self.FAdCampo2)
        self.F2SLE1Combo.setObjectName(u"F2SLE1Combo")

        self.FAd2H1Layout.addWidget(self.F2SLE1Combo)

        self.F2Opt1Input = QLineEdit(self.FAdCampo2)
        self.F2Opt1Input.setObjectName(u"F2Opt1Input")

        self.FAd2H1Layout.addWidget(self.F2Opt1Input)


        self.verticalLayout_8.addLayout(self.FAd2H1Layout)

        self.FAd2H2Layout = QHBoxLayout()
        self.FAd2H2Layout.setObjectName(u"FAd2H2Layout")
        self.F2Opt2Combo = QComboBox(self.FAdCampo2)
        self.F2Opt2Combo.setObjectName(u"F2Opt2Combo")

        self.FAd2H2Layout.addWidget(self.F2Opt2Combo)

        self.F2SLE2Combo = QComboBox(self.FAdCampo2)
        self.F2SLE2Combo.setObjectName(u"F2SLE2Combo")

        self.FAd2H2Layout.addWidget(self.F2SLE2Combo)

        self.F2Opt2Input = QLineEdit(self.FAdCampo2)
        self.F2Opt2Input.setObjectName(u"F2Opt2Input")

        self.FAd2H2Layout.addWidget(self.F2Opt2Input)


        self.verticalLayout_8.addLayout(self.FAd2H2Layout)

        self.FAd2H3Layout = QHBoxLayout()
        self.FAd2H3Layout.setObjectName(u"FAd2H3Layout")
        self.F2LessButton = QPushButton(self.FAdCampo2)
        self.F2LessButton.setObjectName(u"F2LessButton")

        self.FAd2H3Layout.addWidget(self.F2LessButton)

        self.F2AddButton = QPushButton(self.FAdCampo2)
        self.F2AddButton.setObjectName(u"F2AddButton")

        self.FAd2H3Layout.addWidget(self.F2AddButton)


        self.verticalLayout_8.addLayout(self.FAd2H3Layout)


        self.horizontalLayout_5.addWidget(self.FAdCampo2)

        self.FAdStackedWidget.addWidget(self.FAd2)
        self.FAd3 = QWidget()
        self.FAd3.setObjectName(u"FAd3")
        self.horizontalLayout_10 = QHBoxLayout(self.FAd3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.FAdCampo3 = QGroupBox(self.FAd3)
        self.FAdCampo3.setObjectName(u"FAdCampo3")
        self.verticalLayout_9 = QVBoxLayout(self.FAdCampo3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.FAd3H1Layout = QHBoxLayout()
        self.FAd3H1Layout.setObjectName(u"FAd3H1Layout")
        self.F3Opt1Combo = QComboBox(self.FAdCampo3)
        self.F3Opt1Combo.setObjectName(u"F3Opt1Combo")

        self.FAd3H1Layout.addWidget(self.F3Opt1Combo)

        self.F3SLE1Combo = QComboBox(self.FAdCampo3)
        self.F3SLE1Combo.setObjectName(u"F3SLE1Combo")

        self.FAd3H1Layout.addWidget(self.F3SLE1Combo)

        self.F3Opt1Input = QLineEdit(self.FAdCampo3)
        self.F3Opt1Input.setObjectName(u"F3Opt1Input")

        self.FAd3H1Layout.addWidget(self.F3Opt1Input)


        self.verticalLayout_9.addLayout(self.FAd3H1Layout)

        self.FAd3H2Layout = QHBoxLayout()
        self.FAd3H2Layout.setObjectName(u"FAd3H2Layout")
        self.F3Opt2Combo = QComboBox(self.FAdCampo3)
        self.F3Opt2Combo.setObjectName(u"F3Opt2Combo")

        self.FAd3H2Layout.addWidget(self.F3Opt2Combo)

        self.F3SLE2Combo = QComboBox(self.FAdCampo3)
        self.F3SLE2Combo.setObjectName(u"F3SLE2Combo")

        self.FAd3H2Layout.addWidget(self.F3SLE2Combo)

        self.F3Opt2Input = QLineEdit(self.FAdCampo3)
        self.F3Opt2Input.setObjectName(u"F3Opt2Input")

        self.FAd3H2Layout.addWidget(self.F3Opt2Input)


        self.verticalLayout_9.addLayout(self.FAd3H2Layout)

        self.FAd3H3Layout = QHBoxLayout()
        self.FAd3H3Layout.setObjectName(u"FAd3H3Layout")
        self.F3Opt3Combo = QComboBox(self.FAdCampo3)
        self.F3Opt3Combo.setObjectName(u"F3Opt3Combo")

        self.FAd3H3Layout.addWidget(self.F3Opt3Combo)

        self.F3SLE3Combo = QComboBox(self.FAdCampo3)
        self.F3SLE3Combo.setObjectName(u"F3SLE3Combo")

        self.FAd3H3Layout.addWidget(self.F3SLE3Combo)

        self.F3Opt3Input = QLineEdit(self.FAdCampo3)
        self.F3Opt3Input.setObjectName(u"F3Opt3Input")

        self.FAd3H3Layout.addWidget(self.F3Opt3Input)


        self.verticalLayout_9.addLayout(self.FAd3H3Layout)

        self.FAd3H4Layout = QHBoxLayout()
        self.FAd3H4Layout.setObjectName(u"FAd3H4Layout")
        self.F3LessButton = QPushButton(self.FAdCampo3)
        self.F3LessButton.setObjectName(u"F3LessButton")

        self.FAd3H4Layout.addWidget(self.F3LessButton)

        self.F3AddButton = QPushButton(self.FAdCampo3)
        self.F3AddButton.setObjectName(u"F3AddButton")

        self.FAd3H4Layout.addWidget(self.F3AddButton)


        self.verticalLayout_9.addLayout(self.FAd3H4Layout)


        self.horizontalLayout_10.addWidget(self.FAdCampo3)

        self.FAdStackedWidget.addWidget(self.FAd3)
        self.FAd4 = QWidget()
        self.FAd4.setObjectName(u"FAd4")
        self.horizontalLayout_15 = QHBoxLayout(self.FAd4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.FAdCampo4 = QGroupBox(self.FAd4)
        self.FAdCampo4.setObjectName(u"FAdCampo4")
        self.verticalLayout_10 = QVBoxLayout(self.FAdCampo4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.FAd4H1Layout = QHBoxLayout()
        self.FAd4H1Layout.setObjectName(u"FAd4H1Layout")
        self.F4Opt1Combo = QComboBox(self.FAdCampo4)
        self.F4Opt1Combo.setObjectName(u"F4Opt1Combo")

        self.FAd4H1Layout.addWidget(self.F4Opt1Combo)

        self.F4SLE1Combo = QComboBox(self.FAdCampo4)
        self.F4SLE1Combo.setObjectName(u"F4SLE1Combo")

        self.FAd4H1Layout.addWidget(self.F4SLE1Combo)

        self.F4Opt1Input = QLineEdit(self.FAdCampo4)
        self.F4Opt1Input.setObjectName(u"F4Opt1Input")

        self.FAd4H1Layout.addWidget(self.F4Opt1Input)


        self.verticalLayout_10.addLayout(self.FAd4H1Layout)

        self.FAd4H2Layout = QHBoxLayout()
        self.FAd4H2Layout.setObjectName(u"FAd4H2Layout")
        self.F4Opt2Combo = QComboBox(self.FAdCampo4)
        self.F4Opt2Combo.setObjectName(u"F4Opt2Combo")
        self.F4Opt2Combo.setMaximumSize(QSize(16777215, 16777215))

        self.FAd4H2Layout.addWidget(self.F4Opt2Combo)

        self.F4SLE2Combo = QComboBox(self.FAdCampo4)
        self.F4SLE2Combo.setObjectName(u"F4SLE2Combo")

        self.FAd4H2Layout.addWidget(self.F4SLE2Combo)

        self.F4Opt2Input = QLineEdit(self.FAdCampo4)
        self.F4Opt2Input.setObjectName(u"F4Opt2Input")

        self.FAd4H2Layout.addWidget(self.F4Opt2Input)


        self.verticalLayout_10.addLayout(self.FAd4H2Layout)

        self.FAd4H3Layout = QHBoxLayout()
        self.FAd4H3Layout.setObjectName(u"FAd4H3Layout")
        self.F4Opt3Combo = QComboBox(self.FAdCampo4)
        self.F4Opt3Combo.setObjectName(u"F4Opt3Combo")
        self.F4Opt3Combo.setMaximumSize(QSize(16777215, 16777215))

        self.FAd4H3Layout.addWidget(self.F4Opt3Combo)

        self.F4SLE3Combo = QComboBox(self.FAdCampo4)
        self.F4SLE3Combo.setObjectName(u"F4SLE3Combo")

        self.FAd4H3Layout.addWidget(self.F4SLE3Combo)

        self.F4Opt3Input = QLineEdit(self.FAdCampo4)
        self.F4Opt3Input.setObjectName(u"F4Opt3Input")

        self.FAd4H3Layout.addWidget(self.F4Opt3Input)


        self.verticalLayout_10.addLayout(self.FAd4H3Layout)

        self.Fad4H4Layout = QHBoxLayout()
        self.Fad4H4Layout.setObjectName(u"Fad4H4Layout")
        self.F4SLELabel = QLabel(self.FAdCampo4)
        self.F4SLELabel.setObjectName(u"F4SLELabel")

        self.Fad4H4Layout.addWidget(self.F4SLELabel)

        self.F4Opt4Combo = QComboBox(self.FAdCampo4)
        self.F4Opt4Combo.setObjectName(u"F4Opt4Combo")

        self.Fad4H4Layout.addWidget(self.F4Opt4Combo)

        self.F4SLE4Combo = QComboBox(self.FAdCampo4)
        self.F4SLE4Combo.setObjectName(u"F4SLE4Combo")
        self.F4SLE4Combo.setMaximumSize(QSize(16777215, 16777215))

        self.Fad4H4Layout.addWidget(self.F4SLE4Combo)

        self.F4Opt4Input = QLineEdit(self.FAdCampo4)
        self.F4Opt4Input.setObjectName(u"F4Opt4Input")

        self.Fad4H4Layout.addWidget(self.F4Opt4Input)


        self.verticalLayout_10.addLayout(self.Fad4H4Layout)

        self.F4LessButton = QPushButton(self.FAdCampo4)
        self.F4LessButton.setObjectName(u"F4LessButton")

        self.verticalLayout_10.addWidget(self.F4LessButton)


        self.verticalLayout_4.addWidget(self.FAdCampo4)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)

        self.FAdStackedWidget.addWidget(self.FAd4)

        self.GeneralV2Layout.addWidget(self.FAdStackedWidget)

        self.VCalculoLayout = QVBoxLayout()
        self.VCalculoLayout.setObjectName(u"VCalculoLayout")
        self.EjecutarButton = QPushButton(self.centralwidget)
        self.EjecutarButton.setObjectName(u"EjecutarButton")

        self.VCalculoLayout.addWidget(self.EjecutarButton)

        self.Output = QTextEdit(self.centralwidget)
        self.Output.setObjectName(u"Output")
        self.Output.setReadOnly(True)

        self.VCalculoLayout.addWidget(self.Output)

        self.AutorLayout = QHBoxLayout()
        self.AutorLayout.setObjectName(u"AutorLayout")
        self.AutorLabel = QLabel(self.centralwidget)
        self.AutorLabel.setObjectName(u"AutorLabel")

        self.AutorLayout.addWidget(self.AutorLabel)

        self.InfoButton = QPushButton(self.centralwidget)
        self.InfoButton.setObjectName(u"InfoButton")

        self.AutorLayout.addWidget(self.InfoButton)


        self.VCalculoLayout.addLayout(self.AutorLayout)


        self.GeneralV2Layout.addLayout(self.VCalculoLayout)


        self.GeneralH1Layout.addLayout(self.GeneralV2Layout)

        self.GeneralH1Layout.setStretch(0, 1)
        self.GeneralH1Layout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.GeneralH1Layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.FAdStackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700; text-decoration: underline;\">CALCULADORA PAU ANDALUC\u00cdA</span></p></body></html>", None))
        self.NombreCampo.setTitle(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.BachilleratoCampo.setTitle(QCoreApplication.translate("MainWindow", u"Bachillerato", None))
        self.Bach1Label.setText(QCoreApplication.translate("MainWindow", u"Media de 1\u00ba", None))
        self.Bach2Label.setText(QCoreApplication.translate("MainWindow", u"Media de 2\u00ba", None))
        self.FAcCampo.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Acceso", None))
        self.LenguaLabel.setText(QCoreApplication.translate("MainWindow", u"Lengua Castellana y Literatura", None))
        self.FAdCampo0.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Admisi\u00f3n", None))
        self.F0AddButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir asignatura", None))
        self.FAdCampo1.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Admisi\u00f3n", None))
        self.F1LessButton.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
        self.F1AddButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.FAdCampo2.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Admisi\u00f3n", None))
        self.F2LessButton.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
        self.F2AddButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.FAdCampo3.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Admisi\u00f3n", None))
        self.F3LessButton.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
        self.F3AddButton.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.FAdCampo4.setTitle(QCoreApplication.translate("MainWindow", u"Fase de Admisi\u00f3n", None))
        self.F4SLELabel.setText(QCoreApplication.translate("MainWindow", u"Segunda Lengua Extranjera", None))
        self.F4LessButton.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
        self.EjecutarButton.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.AutorLabel.setText(QCoreApplication.translate("MainWindow", u"Creador: \u00c1lvaro L\u00f3pez P\u00e9rez", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
    # retranslateUi

