from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QSpacerItem, QVBoxLayout, QSizePolicy, QButtonGroup, QWidget, QFileDialog, QGridLayout, QScrollArea,QLineEdit,QFormLayout,QTextEdit,QHBoxLayout,QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from estilos import *
from pdf_citologia import *

def cargar_firma():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Archivos de imagen (*.jpg *.png)")
    file_dialog.setDefaultSuffix("jpg")

    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            return selected_files[0]  # Retorna la ruta del archivo seleccionado
    return None

def crear_formato_citologia_completo():
    # Widget principal del formulario
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)
    
    # Crear campos de formulario con etiquetas y entradas
    campos = [
        ("Número de caso:", QLineEdit("")),
        ("Fecha y hora de muestro:", QLineEdit("")),
        ("Fecha de recepción:", QLineEdit("")),
        ("Fecha de emisión de resultado:", QLineEdit("")),
        ("Nombre paciente:", QLineEdit("")),
        ("Raza:", QLineEdit()),
        ("Edad:", QLineEdit("")),
        ("Sexo:", None),  # Para los checkboxes de sexo
        ("Nombre del propietario:", QLineEdit("")),
        ("Hospital/MVZ:", QLineEdit("")),
        ("Anamnesis:", QTextEdit("")),
        ("Tratamiento:", QTextEdit("")), ####Hasta aqui informacion basica
        ("Metodo de muestreo:", None),
        ("Descripcion macroscópica:", QTextEdit("")),
        ("Descripcion microscópica:", QTextEdit("")),
        ("Interpretación:", QTextEdit("")),
        ("Diagnostico:", QTextEdit("")),
        ("Comentarios:", QTextEdit(""))
    ]
    bandera = 0
    # Iterar sobre cada campo y agregarlo al layout principal
    for etiqueta, editor in campos:
        layout_horizontal = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        if editor:
            if isinstance(editor, QLineEdit):
                editor.setStyleSheet(estilo_input_text)
                layout_horizontal.addWidget(label)
                layout_horizontal.addWidget(editor)
            else:  # Es QTextEdit
                editor.setStyleSheet(estilo_textedit_formulario_citologia)
                layout_horizontal2 = QHBoxLayout()
                layout_horizontal.addWidget(label)
                layout_horizontal2.addWidget(editor)
                layout_principal.addLayout(layout_horizontal)
                layout_principal.addLayout(layout_horizontal2)
                bandera = 1
        else:
            if etiqueta == 'Metodo de muestreo:':
              layout_horizontal2 = QHBoxLayout()
              # Crear checkboxes para el sexo
              cb_paf = QCheckBox("PAF/PAD")
              cb_acaf = QCheckBox("ACAF/ACAD")
              cb_impro = QCheckBox("Impronta")
              cb_hisopado = QCheckBox("Hisopado")
              cb_raspado = QCheckBox("Raspado")

              cb_paf.setStyleSheet(estilo_checkbox)
              cb_acaf.setStyleSheet(estilo_checkbox)
              cb_impro.setStyleSheet(estilo_checkbox)
              cb_hisopado.setStyleSheet(estilo_checkbox)
              cb_raspado.setStyleSheet(estilo_checkbox)
        
              layout_horizontal.addWidget(label)
              layout_horizontal2.addWidget(cb_paf)
              layout_horizontal2.addWidget(cb_acaf)
              layout_horizontal2.addWidget(cb_impro)
              layout_horizontal2.addWidget(cb_hisopado)
              layout_horizontal2.addWidget(cb_raspado)
              bandera = 1
              # spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
              # layout_horizontal2.addItem(spacer)  # Añade el spacer al inicio para empujar a la derecha
              layout_principal.addLayout(layout_horizontal)
              layout_principal.addLayout(layout_horizontal2)

            if etiqueta == 'Sexo:':
              # Crear checkboxes para el sexo
              cb_masculino = QCheckBox("M")
              cb_femenino = QCheckBox("H")
              cb_castrado = QCheckBox("Castrado")
              cb_masculino.setStyleSheet(estilo_checkbox)
              cb_femenino.setStyleSheet(estilo_checkbox)
              cb_castrado.setStyleSheet(estilo_checkbox)

              # Crear un grupo de botones exclusivos
              grupo_sexo = QButtonGroup(widget_principal)
              grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
              grupo_sexo.addButton(cb_masculino)
              grupo_sexo.addButton(cb_femenino)
        
              layout_horizontal.addWidget(label)
              layout_horizontal.addWidget(cb_masculino)
              layout_horizontal.addWidget(cb_femenino)
              layout_horizontal.addWidget(cb_castrado)
        if bandera == 1:
          bandera = 0
        else:
          layout_principal.addLayout(layout_horizontal)

    separador = QWidget()
    separador.setFixedHeight(30)
    separador.setStyleSheet("background-color: transparent;") 
    layout_principal.addWidget(separador)

    # Añadir botones al final del formulario
    layout_botones = QHBoxLayout()
    boton_firma = QPushButton("Seleccionar firma")
    boton_reporte = QPushButton("Generar reporte")
    boton_firma.setStyleSheet(estilo_boton_formulario)
    boton_reporte.setStyleSheet(estilo_boton_formulario)
    layout_botones.addWidget(boton_firma)
    layout_botones.addWidget(boton_reporte)
    layout_principal.addLayout(layout_botones)

    
    def seleccionar_firma():
      global ruta_firma
      ruta_firma = cargar_firma()

    def boton_reporte_clicked():
      # Crear diccionario con los valores del formulario

      valores = {
          "datos_caso": campos[0][1].text(),
          "fecha_muestreo": campos[1][1].text(),
          "fecha_recepcion": campos[2][1].text(),
          "fecha_emision": campos[3][1].text(),
          "datos_paciente_nombre": campos[4][1].text(),
          "datos_paciente_raza": campos[5][1].text(),
          "datos_paciente_edad": campos[6][1].text(),
          "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h" ,
          "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
          "datos_paciente_propietario": campos[8][1].text(),
          "datos_paciente_hospital": campos[9][1].text(),
          "datos_paciente_anamnesis": campos[10][1].toPlainText(),
          "datos_paciente_tratamiento": campos[11][1].toPlainText(), #A partir de aqui es lo nuevo
          #"muestreo": campos[12][1].toPlainText(),
          "macros": campos[13][1].toPlainText(),
          "micros": campos[14][1].toPlainText(),
          "inter": campos[15][1].toPlainText(),
          "diag": campos[16][1].toPlainText(),
          "comen": campos[17][1].toPlainText(),
          "firma_path": ruta_firma,
          "paf": "y" if cb_paf.isChecked() else "n",
          "acaf": "y" if cb_acaf.isChecked() else "n",
          "impro": "y" if cb_impro.isChecked() else "n",
          "raspado": "y" if cb_raspado.isChecked() else "n",
          "hisopado": "y" if cb_hisopado.isChecked() else "n",
      }
      print(valores)
      generar_citologia(valores)
  
    
    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal


