from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QButtonGroup, QWidget, QLineEdit, QTextEdit, QHBoxLayout, QCheckBox, QComboBox
from estilos import *
from pdf_citologia import *
from PyQt5.QtCore import Qt
import json
from pathlib import Path

# Ruta del archivo JSON
json_file_path = "doctores.json"

def cargar_json():
    if not Path(json_file_path).exists():
        with open(json_file_path, 'w') as file:
            json.dump({}, file)
    with open(json_file_path, 'r') as file:
        return json.load(file)

def crear_formato_endocrinologia_completo():
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
        ("Raza:", QLineEdit()),
        ("Edad:", QLineEdit("")),
        ("Sexo:", None),  # Para los checkboxes de sexo
        ("Nombre del propietario:", QLineEdit("")),
        ("Hospital/MVZ:", QLineEdit("")),
        ("Anamnesis:", QTextEdit("")),
        ("Tratamiento:", QTextEdit("")), ####Hasta aqui informacion basica
    ]

    campos_adicionales = [
       ("Metodo:", QLineEdit("")),
       ("Tipo de muestra:", QLineEdit("")),
    ]

    campos_analitos = [
       ("Cortisol Basal:", QLineEdit(""), QLineEdit("")),
       ("Cortisol 1 hora:", QLineEdit(""), QLineEdit("")),
       ("Cortisol 3 horas:", QLineEdit(""), QLineEdit("")),
       ("Cortisol 4 horas:", QLineEdit(""), QLineEdit("")),
       ("Cortisol 8 horas:", QLineEdit(""), QLineEdit("")),
       ("TSH:", QLineEdit(""), QLineEdit("")),
       ("T4 Total:", QLineEdit(""), QLineEdit("")),
       ("T4 Libre:", QLineEdit(""), QLineEdit("")),
       ("ACTH:", QLineEdit(""), QLineEdit("")),
       ("Aldosterona:", QLineEdit(""), QLineEdit("")),
       ("Cortisol en orina:", QLineEdit(""), QLineEdit("")),
       ("Creatinina:", QLineEdit(""), QLineEdit("")),
       ("Cortisol/Creatin:", QLineEdit(""), QLineEdit("")),
       ("HDL:", QLineEdit(""), QLineEdit("")),
       ("LDL:", QLineEdit(""), QLineEdit("")),
       ("Colerterol:", QLineEdit(""), QLineEdit("")),
       ("Progesterona:", QLineEdit(""), QLineEdit("")),
       ("Fructosamina:", QLineEdit(""), QLineEdit("")),
    ]

    campos_comentarios = [
       ("Otros Hallazgos:", QTextEdit("Otros Hallazgos")),
       ("Interpretaciones:", QTextEdit("Interpretaciones")),
       ("Comentarios extras:", QTextEdit("Comentarios extras"))
    ]

    bandera = 0

    # Título y sección de datos del paciente
    titulo_paciente = QLabel("Datos del paciente")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente) 
    titulo_linea = QWidget() #Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)


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
    
    # Título y sección de datos del analisis
    titulo_paciente = QLabel("Analitos")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente)
    titulo_linea = QWidget()#Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)

    #Estos son los campos adicionales
    for etiqueta, editor in campos_adicionales:
      layout_horizontal = QHBoxLayout()
      label = QLabel(etiqueta)
      label.setStyleSheet(estilo_label_formulario)
      editor.setStyleSheet(estilo_input_text)
      layout_horizontal.addWidget(label)
      layout_horizontal.addWidget(editor)
      layout_principal.addLayout(layout_horizontal)

    layout_horizontal = QHBoxLayout()
    label1 = QLabel("Analitos")
    label2 = QLabel("Resultado")
    label3 = QLabel("Referencia")
    label1.setStyleSheet(estilo_label_formulario_subtitulo)
    label2.setStyleSheet(estilo_label_formulario_subtitulo)
    label3.setStyleSheet(estilo_label_formulario_subtitulo)
    label1.setAlignment(Qt.AlignCenter)
    label2.setAlignment(Qt.AlignCenter)
    label3.setAlignment(Qt.AlignCenter)
    layout_horizontal.addWidget(label1)
    layout_horizontal.addWidget(label2)
    layout_horizontal.addWidget(label3)
    layout_principal.addLayout(layout_horizontal)

    #Estos son los analitos
    for etiqueta, editor1, editor2 in campos_analitos:
      layout_horizontal = QHBoxLayout()
      label = QLabel(etiqueta)
      label.setStyleSheet(estilo_label_formulario)
      editor1.setStyleSheet(estilo_input_text_endocri)
      editor2.setStyleSheet(estilo_input_text_endocri)
      layout_horizontal.addWidget(label)
      layout_horizontal.addWidget(editor1)
      layout_horizontal.addWidget(editor2)
      layout_principal.addLayout(layout_horizontal)
    

    # Título y sección de los comentarios
    titulo_paciente = QLabel("Interpretaciones y comentarios")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente)
    titulo_linea = QWidget()#Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)
    
    #Seccion del codigo para agregar el formulario de comentarios
    for etiqueta, editor in campos_comentarios:
      layout_horizontal = QHBoxLayout()
      label = QLabel(etiqueta)
      label.setStyleSheet(estilo_label_formulario)
      if editor:
        editor.setStyleSheet(estilo_textedit_formulario_citologia)
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal.addWidget(label)
        layout_horizontal2.addWidget(editor)
        layout_principal.addLayout(layout_horizontal)
        layout_principal.addLayout(layout_horizontal2)
        #Separador
        separador = QWidget()
        separador.setFixedHeight(30)
        separador.setStyleSheet("background-color: transparent;") 
        layout_principal.addWidget(separador)


    separador = QWidget()
    separador.setFixedHeight(30)
    separador.setStyleSheet("background-color: transparent;") 
    layout_principal.addWidget(separador)

    # Añadir el combo box para seleccionar firma
    layout_horizontal_firma = QHBoxLayout()
    label_firma = QLabel("Seleccionar firma del doctor:")
    label_firma.setStyleSheet(estilo_label_formulario)
    combo_box_firma = QComboBox()
    combo_box_firma.setStyleSheet(estilo_input_text)

    # Cargar los nombres de los doctores desde el JSON
    data = cargar_json()
    for doctor in data.keys():
        combo_box_firma.addItem(doctor)

    layout_horizontal_firma.addWidget(label_firma)
    layout_horizontal_firma.addWidget(combo_box_firma)
    layout_principal.addLayout(layout_horizontal_firma)

    # Añadir botones al final del formulario
    layout_botones = QHBoxLayout()
    boton_reporte = QPushButton("Generar reporte")
    boton_reporte.setStyleSheet(estilo_boton_formulario)
    layout_botones.addWidget(boton_reporte)
    layout_principal.addLayout(layout_botones)

    def boton_reporte_clicked():
      # Crear diccionario con los valores del formulario
      doctor_seleccionado = combo_box_firma.currentText()
      firma_path = data[doctor_seleccionado]["firma"] if doctor_seleccionado in data else ""

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
          "firma_path": firma_path,
      }
      print(valores)
      generar_citologia(valores)
  
    boton_reporte.clicked.connect(boton_reporte_clicked)

    return widget_principal


