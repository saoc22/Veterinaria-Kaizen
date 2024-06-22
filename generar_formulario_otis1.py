from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QButtonGroup, QFileDialog,QLineEdit,QTextEdit,QHBoxLayout,QCheckBox
from PyQt5.QtCore import Qt
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

def crear_formato_otis1_completo():
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
        ("Tipo de muestra:", QLineEdit("")),
        ("Microorganismo no.1:", QLineEdit("")),
        ("Microorganismo no.2:", QLineEdit("")),
        ("Microorganismo no.3:", QLineEdit(""))
    ]
    campos_extras = [
        ("Antibiotico no.1:", QLineEdit("")),
        ("A1:", QLineEdit("")),
        ("B1:", QLineEdit("")),
        ("C1:", QLineEdit("")),
        ("Antibiotico no.2:", QLineEdit("")),
        ("A2:", QLineEdit("")),
        ("B2:", QLineEdit("")),
        ("C2:", QLineEdit("")),
        ("Antibiotico no.3:", QLineEdit("")),
        ("A3:", QLineEdit("")),
        ("B3:", QLineEdit("")),
        ("C3:", QLineEdit("")),
        ("Antibiotico no.4:", QLineEdit("")),
        ("A4:", QLineEdit("")),
        ("B4:", QLineEdit("")),
        ("C4:", QLineEdit("")),
        ("Antibiotico no.5:", QLineEdit("")),
        ("A5:", QLineEdit("")),
        ("B5:", QLineEdit("")),
        ("C5:", QLineEdit("")),
        ("Antibiotico no.6:", QLineEdit("")),
        ("A6:", QLineEdit("")),
        ("B6:", QLineEdit("")),
        ("C6:", QLineEdit("")),
        ("Antibiotico no.7:", QLineEdit("")),
        ("A7:", QLineEdit("")),
        ("B7:", QLineEdit("")),
        ("C7:", QLineEdit("")),
        ("Antibiotico no.8:", QLineEdit("")),
        ("A8:", QLineEdit("")),
        ("B8:", QLineEdit("")),
        ("C8:", QLineEdit("")),
    ]

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
    bandera = 0
    for etiqueta, editor in campos:
        layout_horizontal = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        if etiqueta == "Tipo de muestra:" or etiqueta == "Tratamiento:":
          separador = QWidget()
          separador.setFixedHeight(50)
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

              # Crear un grupo de botones exclusivos
              grupo_sexo = QButtonGroup(widget_principal)
              grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
              grupo_sexo.addButton(cb_masculino)
              grupo_sexo.addButton(cb_femenino)
        
              layout_horizontal.addWidget(label)
              layout_horizontal.addWidget(cb_masculino)
              layout_horizontal.addWidget(cb_femenino)
              layout_horizontal.addWidget(cb_castrado)
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


    for i in range(0, 29, 4):
      layout_horizontal1 = QHBoxLayout()
      layout_horizontal2 = QHBoxLayout()
      layout_horizontal3 = QHBoxLayout()
      layout_horizontal4 = QHBoxLayout()
      layout_horizontal5 = QHBoxLayout()

      separador = QWidget()
      separador.setFixedHeight(35)
      separador.setStyleSheet("background-color: transparent;") 

      label1 = QLabel(campos_extras[i+0][0])
      label2 = QLabel(campos_extras[i+1][0])
      label3 = QLabel(campos_extras[i+2][0])
      label4 = QLabel(campos_extras[i+3][0])

      campos_extras[i+0][1].setStyleSheet(estilo_input_text_antibiotico)
      campos_extras[i+1][1].setStyleSheet(estilo_input_text)
      campos_extras[i+2][1].setStyleSheet(estilo_input_text)
      campos_extras[i+3][1].setStyleSheet(estilo_input_text)

      label1.setStyleSheet(estilo_label_formulario)
      label2.setStyleSheet(estilo_label_formulario)
      label3.setStyleSheet(estilo_label_formulario)
      label4.setStyleSheet(estilo_label_formulario)

      layout_horizontal1.addWidget(label1)
      layout_horizontal1.addWidget(campos_extras[i+0][1])
      layout_horizontal2.addWidget(label2)
      layout_horizontal2.addWidget(campos_extras[i+1][1])
      layout_horizontal3.addWidget(label3)
      layout_horizontal3.addWidget(campos_extras[i+2][1])
      layout_horizontal4.addWidget(label4)
      layout_horizontal4.addWidget(campos_extras[i+3][1])

      layout_horizontal5.addLayout(layout_horizontal2)
      layout_horizontal5.addLayout(layout_horizontal3)
      layout_horizontal5.addLayout(layout_horizontal4)

      layout_principal.addWidget(separador) 
      layout_principal.addLayout(layout_horizontal1)
      layout_principal.addWidget(separador) 
      layout_principal.addLayout(layout_horizontal5)
      layout_principal.addWidget(separador)   

    campos_finales = [
      ("Interpretacion:", QTextEdit("")),
      ("Resultado micológico:", QTextEdit("")),
    ]


    # Título y sección de los comentarios
    titulo_paciente = QLabel("Interpretaciones y comentarios")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente)
    titulo_linea = QWidget()#Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)


    for etiqueta, editor in campos_finales:
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        layout_horizontal1.addWidget(label)
        layout_principal.addLayout(layout_horizontal1)
        if editor:
            if isinstance(editor, QLineEdit):
                editor.setStyleSheet(estilo_input_text)
            else:  # Es QTextEdit
                editor.setStyleSheet(estilo_textedit_formulario_otis)
            layout_horizontal2.addWidget(editor)
        layout_principal.addLayout(layout_horizontal2)
        separador = QWidget()
        separador.setFixedHeight(40)
        separador.setStyleSheet("background-color: transparent;") 
        layout_principal.addWidget(separador)



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
          "muestra": campos[12][1].text(),
          "mi1": campos[13][1].text(),
          "mi2": campos[14][1].text(),
          "mi3": campos[15][1].text(),
          "An1": campos_extras[0][1].text(),
          "A1": campos_extras[1][1].text(),
          "B1": campos_extras[2][1].text(),
          "C1": campos_extras[3][1].text(),
          "An2": campos_extras[4][1].text(),
          "A2": campos_extras[5][1].text(),
          "B2": campos_extras[6][1].text(),
          "C2": campos_extras[7][1].text(),
          "An3": campos_extras[8][1].text(),
          "A3": campos_extras[9][1].text(),
          "B3": campos_extras[10][1].text(),
          "C3": campos_extras[11][1].text(),
          "An4": campos_extras[12][1].text(),
          "A4": campos_extras[13][1].text(),
          "B4": campos_extras[14][1].text(),
          "C4": campos_extras[15][1].text(),
          "An5": campos_extras[16][1].text(),
          "A5": campos_extras[17][1].text(),
          "B5": campos_extras[18][1].text(),
          "C5": campos_extras[19][1].text(),
          "An6": campos_extras[20][1].text(),
          "A6": campos_extras[21][1].text(),
          "B6": campos_extras[22][1].text(),
          "C6": campos_extras[23][1].text(),
          "An7": campos_extras[24][1].text(),
          "A7": campos_extras[25][1].text(),
          "B7": campos_extras[26][1].text(),
          "C7": campos_extras[27][1].text(),
          "An8": campos_extras[28][1].text(),
          "A8": campos_extras[29][1].text(),
          "B8": campos_extras[30][1].text(),
          "C8": campos_extras[31][1].text(),
          "firma_path": ruta_firma
      }
      print(valores)
      #generar_urianalisis(valores)
  
    
    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal


