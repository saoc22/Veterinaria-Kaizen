from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QScrollArea,QLineEdit,QFormLayout,QTextEdit,QHBoxLayout,QCheckBox, QButtonGroup
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from estilos import *
from pdf_urianalisis import *

def cargar_firma():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Archivos de imagen (*.jpg *.png)")
    file_dialog.setDefaultSuffix("jpg")

    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            return selected_files[0]  # Retorna la ruta del archivo seleccionado
    return None

def crear_formato_urianalisis_completo():
    # Widget principal del formulario
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)
    
    # Crear campos de formulario con etiquetas y entradas
    campos = [
        ("Número de caso:", QLineEdit("")),
        ("Fecha y hora de muestro:", QLineEdit("")),
        ("Fecha de recepción:", QLineEdit("")),
        ("Fecha de emisión resultado:", QLineEdit("")),
        ("Nombre paciente:", QLineEdit("")),
        ("Raza:", QLineEdit("")),
        ("Edad:", QLineEdit("")),
        ("Sexo:", None),  # Para los checkboxes de sexo
        ("Nombre del propietario:", QLineEdit("")),
        ("Hospital/MVZ:", QLineEdit("")),
        ("Anamnesis:", QTextEdit("")),
        ("Tratamiento:", QTextEdit("")), ####Hasta aqui informacion basica
        ("Metodo de obtencion:", None),
        ("Aporte previo liquidos:", None),
        ("Apariencia:", QLineEdit("")),
        ("Color:", QLineEdit("")),
        ("Densidad:", QLineEdit("")),
        ("pH:", QLineEdit("")),
        ("Proteinas:", QLineEdit("")),
        ("Glucosa:", QLineEdit("")),
        ("Cetonas:", QLineEdit("")),
        ("Bilirrubina:", QLineEdit("")),
        ("Sangre/Hg:", QLineEdit("")),
        ("Eritrocitos:", QLineEdit("")),
        ("Leucocitos:", QLineEdit("")),
        ("Celulas renales:", QLineEdit("")),
        ("Celulas transitorias:", QLineEdit("")),
        ("Celulas escamosas:", QLineEdit("")),
        ("Cilindros:", QLineEdit("")),
        ("Cristales:", QLineEdit("")),
        ("Bacterias:", QLineEdit("")),
        ("Lipidos:", QLineEdit("")),
        ("Otros hallazgos:", QTextEdit("")),
        ("Interpretación:", QTextEdit("")),
        ("Comentarios Extras:", QTextEdit(""))
    ]

    # Iterar sobre cada campo y agregarlo al layout principal
    bandera = 0
    for etiqueta, editor in campos:
        layout_horizontal = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        if etiqueta == "Metodo de obtencion:" or etiqueta == "Tratamiento:":
          separador = QWidget()
          separador.setFixedHeight(15)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)
        if editor:
            if isinstance(editor, QLineEdit):
                editor.setStyleSheet(estilo_input_text)
            else:  # Es QTextEdit
                editor.setStyleSheet(estilo_textedit_formulario)
            layout_horizontal.addWidget(label)
            layout_horizontal.addWidget(editor)
        else:
            if etiqueta == 'Sexo:':
              # Crear checkboxes para el sexo
              cb_masculino = QCheckBox("M")
              cb_femenino = QCheckBox("H")
              cb_castrado = QCheckBox("Castrado")
              cb_masculino.setStyleSheet(estilo_checkbox)
              cb_femenino.setStyleSheet(estilo_checkbox)
              cb_castrado.setStyleSheet(estilo_checkbox)

              grupo_sexo = QButtonGroup(widget_principal)
              grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
              grupo_sexo.addButton(cb_masculino)
              grupo_sexo.addButton(cb_femenino)

              layout_horizontal.addWidget(label)
              layout_horizontal.addWidget(cb_masculino)
              layout_horizontal.addWidget(cb_femenino)
              layout_horizontal.addWidget(cb_castrado)
            if  etiqueta == 'Metodo de obtencion:':
              # Crear checkboxes para el sexo
              cb_mic = QCheckBox("Miccion")
              cb_cat = QCheckBox("Catete")
              cb_cis = QCheckBox("Cisto")
              cb_nr1 = QCheckBox("NR")
              cb_mic.setStyleSheet(estilo_checkbox)
              cb_cat.setStyleSheet(estilo_checkbox)
              cb_cis.setStyleSheet(estilo_checkbox)
              cb_nr1.setStyleSheet(estilo_checkbox)

              # Crear un grupo de botones exclusivos
              grupo_sexo = QButtonGroup(widget_principal)
              grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
              grupo_sexo.addButton(cb_mic)
              grupo_sexo.addButton(cb_cat)
              grupo_sexo.addButton(cb_cis)
              grupo_sexo.addButton(cb_nr1)

              layout_horizontal.addWidget(label)
              layout_horizontal.addWidget(cb_mic)
              layout_horizontal.addWidget(cb_cat)
              layout_horizontal.addWidget(cb_cis)
              layout_horizontal.addWidget(cb_nr1)
              bandera = 2
            if etiqueta == "Aporte previo liquidos:":
              # Crear checkboxes para el sexo
              cb_si = QCheckBox("Si")
              cb_no = QCheckBox("No")
              cb_nr2 = QCheckBox("NR")
              cb_si.setStyleSheet(estilo_checkbox)
              cb_no.setStyleSheet(estilo_checkbox)
              cb_nr2.setStyleSheet(estilo_checkbox)

              # Crear un grupo de botones exclusivos
              grupo_sexo = QButtonGroup(widget_principal)
              grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
              grupo_sexo.addButton(cb_si)
              grupo_sexo.addButton(cb_no)
              grupo_sexo.addButton(cb_nr2)
        
              layout_horizontal.addWidget(label)
              layout_horizontal.addWidget(cb_si)
              layout_horizontal.addWidget(cb_no)
              layout_horizontal.addWidget(cb_nr2)
              bandera = 0
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
      
      #Determinar el checkbox de obtencion
      if cb_mic.isChecked():
          obtencion = "miccion"
      elif cb_cat.isChecked():
          obtencion = "catete"
      elif cb_cis.isChecked():
          obtencion = "Cisco"
      elif cb_nr1.isChecked():
          obtencion = "NR"
      else:
           obtencion = "NR"

      #Determinar el checkbox de liquidos
      if cb_si.isChecked():
        liquidos = "si"
      elif cb_no.isChecked():
        liquidos = "no"
      elif cb_nr2.isChecked():
        liquidos = "NR"
      else:
        liquidos = "NR"

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
          "datos_analisis_metodo_de_obtencion": obtencion,
          "datos_analisis_aporte_previo_de_liquidos": liquidos,
          "datos_analisis_apariencia": campos[14][1].text(),
          "datos_analisis_color": campos[15][1].text(),
          "datos_analisis_densidad": campos[16][1].text(),
          "datos_analisis_ph": campos[17][1].text(),
          "datos_analisis_proteinas": campos[18][1].text(),
          "datos_analisis_glucosa": campos[19][1].text(),
          "datos_analisis_cetonas": campos[20][1].text(),
          "datos_analisis_bilirrubina": campos[21][1].text(),
          "datos_analisis_sangre_hg": campos[22][1].text(),
          "datos_analisis_eritrocitos": campos[23][1].text(),
          "datos_analisis_leucocitos": campos[24][1].text(),
          "datos_analisis_celulas_renales": campos[25][1].text(),
          "datos_analisis_celulas_transitorias": campos[26][1].text(),
          "datos_analisis_celulas_escamosas": campos[27][1].text(),
          "datos_analisis_cilindros": campos[28][1].text(),
          "datos_analisis_cristales": campos[29][1].text(),
          "datos_analisis_bacterias": campos[30][1].text(),
          "datos_analisis_lipidos": campos[31][1].text(),
          "datos_analisis_otros": campos[32][1].toPlainText(),
          "datos_analisis_interpretacion": campos[33][1].toPlainText(),
          "datos_analisis_comentarios": campos[34][1].toPlainText(),
          "firma_path": ruta_firma
      }
      print(valores)
      generar_urianalisis(valores)
  
    
    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal


