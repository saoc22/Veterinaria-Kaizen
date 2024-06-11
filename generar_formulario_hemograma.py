from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QButtonGroup, QWidget, QFileDialog, QGridLayout, QScrollArea,QLineEdit,QFormLayout,QTextEdit,QHBoxLayout,QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from estilos import *
from pdf_hemograma import *

def cargar_firma():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Archivos de imagen (*.jpg *.png)")
    file_dialog.setDefaultSuffix("jpg")

    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            return selected_files[0]  # Retorna la ruta del archivo seleccionado
    return None

def crear_formato_hemograma_completo(raza):
    # Widget principal del formulario
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)

    ############### LAS FUNCIONES DEBEN IR DENTRO DE LA CREACION DEL FORMULARIO ##########################
    def calcular_vgm():
        global vgm
        try:
            hematocrito = float(campos[12][1].text())  # Asume que hematocrito está en posición 12
            eritrocitos = float(campos[14][1].text())  # Asume que eritrocitos está en posición 14
            vgm = hematocrito *1000/ eritrocitos  # Fórmula simplificada
            vgm_label.setText(f"{vgm:.2f}")  # Establece el valor en el label
        except ValueError:
            vgm_label.setText("Error")

    def calcular_cgmh():
        global cgmh
        try:
            hemoglobina = float(campos[13][1].text())  # Asume que hemoglobina está en posición 13
            hematocrito = float(campos[12][1].text())  # Asume que hematocrito está en posición 12
            cgmh = (hemoglobina / hematocrito)  # Fórmula simplificada
            cgmh_label.setText(f"{cgmh:.2f}")  # Establece el valor en el label
        except ValueError:
            cgmh_label.setText("Error")
    ##################### AQUI TERMINAN LAS FUNCIONES DE CALCULO, ASI ES COMO FUNCIONAA ################
    
    # Crear campos de formulario con etiquetas y entradas
    if raza.lower() != 'caballo':
      campos = [
          ("Número de caso:", QLineEdit("Default Case Number")),
          ("Fecha y hora de muestro:", QLineEdit("01/01/2024 12:00")),
          ("Fecha de recepción:", QLineEdit("01/01/2024")),
          ("Fecha de emisión de resultado:", QLineEdit("01/01/2024")),
          ("Nombre paciente:", QLineEdit("Nombre Predeterminado")),
          ("Raza:", QLineEdit(raza)),
          ("Edad:", QLineEdit("Edad Predeterminada")),
          ("Sexo:", None),  # Para los checkboxes de sexo
          ("Nombre del propietario:", QLineEdit("Propietario Predeterminado")),
          ("Hospital/MVZ:", QLineEdit("Hospital Predeterminado")),
          ("Anamnesis:", QTextEdit("Anamnesis Predeterminada")),
          ("Tratamiento:", QTextEdit("Tratamiento Predeterminado")),
          ("Hematocrito:", QLineEdit("1.0")),
          ("Hemoglobina:", QLineEdit("0.0")),
          ("Eritrocitos:", QLineEdit("1.0")),
          ("VGM:", None), 
          ("CGMH:", None), 
          ("Reticulocitos:", QLineEdit("0.0")),
          ("RDWc:", QLineEdit("0.0")),
          ("Plaquetas:", QLineEdit("0")),
          ("VPM:", QLineEdit("0.0")),
          ("Sólidos totales:", QLineEdit("0.0")),
          ("Leucocitos:", QLineEdit("0.0")),
          ("Neutrófilos:", QLineEdit("0.0")),
          ("Bandas:", QLineEdit("0.0")),
          ("Metamielocitos:", QLineEdit("0.0")),
          ("Mielocitos:", QLineEdit("0.0")),
          ("Linfocitos:", QLineEdit("0.0")),
          ("Monocitos:", QLineEdit("0.0")),
          ("Eosinófilos:", QLineEdit("0.0")),
          ("Basófilos:", QLineEdit("0.0")),
          ("Morfología de eritrocitos:", QTextEdit("Morfología Predeterminada")),
          ("Morfología de leucocitos:", QTextEdit("Morfología Predeterminada")),
          ("Otros hallazgos:", QTextEdit("Hallazgos Predeterminados")),
          ("Interpretación:", QTextEdit("Interpretación Predeterminada")),
          ("Comentarios:", QTextEdit("Comentarios")) #34
      ]
    else:
       campos = [
          ("Número de caso:", QLineEdit("")),
          ("Fecha y hora de muestro:", QLineEdit("")),
          ("Fecha de recepción:", QLineEdit("")),
          ("Fecha de emisión de resultado:", QLineEdit("")),
          ("Nombre paciente:", QLineEdit("")),
          ("Raza:", QLineEdit(raza)),
          ("Edad:", QLineEdit("")),
          ("Sexo:", None),  # Para los checkboxes de sexo
          ("Nombre del propietario:", QLineEdit("")),
          ("Hospital/MVZ:", QLineEdit("")),
          ("Anamnesis:", QTextEdit("")),
          ("Tratamiento:", QTextEdit("")),
          ("Hematocrito:", QLineEdit("")),
          ("Hemoglobina:", QLineEdit("")),
          ("Eritrocitos:", QLineEdit("")),
          ("VGM:", None), 
          ("CGMH:", None), 
          ("RDWc:", QLineEdit("")),
          ("Plaquetas:", QLineEdit("")),
          ("VPM:", QLineEdit("")),
          ("Sólidos totales:", QLineEdit("")),
          ("Fibrinógeno:", QLineEdit("")),
          ("Relación ST/Fb:", QLineEdit("")),
          ("Leucocitos:", QLineEdit("")),
          ("Neutrófilos:", QLineEdit("")),
          ("Bandas:", QLineEdit("")),
          ("Metamielocitos:", QLineEdit("")),
          ("Mielocitos:", QLineEdit("")),
          ("Linfocitos:", QLineEdit("")),
          ("Monocitos:", QLineEdit("")),
          ("Eosinófilos:", QLineEdit("")),
          ("Basófilos:", QLineEdit("")),
          ("Morfología de eritrocitos:", QTextEdit("")),
          ("Morfología de leucocitos:", QTextEdit("")),
          ("Otros hallazgos:", QTextEdit("")),
          ("Interpretación:", QTextEdit("")),
          ("Comentarios:", QTextEdit("")) #35
      ]
    
    #DISCCIONARIOS PARA LIMITES DEL FORMULARIO
    if raza.lower() == 'perro':
       etiquetas_especificas = {
          "Hematocrito:": "0.37 – 0.55",
          "Hemoglobina:": "120 – 180",
          "Eritrocitos:": "5.5 – 8.5",
          "Reticulocitos:": "<60",
          "RDWc:": "<20.0",
          "Plaquetas:": "200 – 600",
          "VPM:": "3.9 – 11.1",
          "Sólidos totales:": "60 – 75",
          "Leucocitos:": "6.0 – 17.0",
          "Neutrófilos:": "3.0 – 11.5",
          "Bandas:": "<0.3",
          "Metamielocitos:": "0",
          "Mielocitos:": "0",
          "Linfocitos:": "1.0 – 4.8",
          "Monocitos:": "0 – 1.4",
          "Eosinófilos:": "0 – 0.9",
          "Basófilos:": "raros",
       }
    elif raza.lower() == 'gato':
       etiquetas_especificas = {
          "Hematocrito:": "0.27 – 0.45",
          "Hemoglobina:": "80 – 150",
          "Eritrocitos:": "5.0 – 10.0",
          "Reticulocitos:": "<60",
          "RDWc:": "<18.5",
          "Plaquetas:": "300 – 700",
          "VPM:": "12.0 – 17.0",
          "Sólidos totales:": "60 – 80",
          "Leucocitos:": "5.5 – 19.5",
          "Neutrófilos:": "2.5 – 12.5",
          "Bandas:": "0 – 0.3",
          "Metamielocitos:": "0",
          "Mielocitos:": "0",
          "Linfocitos:": "1.5 – 7.0",
          "Monocitos:": "0 – 0.8",
          "Eosinófilos:": "0 – 0.8",
          "Basófilos:": "Raros",
       }
    elif raza.lower() == 'cachorro':
       etiquetas_especificas = {
          "Hematocrito:": "0.29 – 0.39",
          "Hemoglobina:": "-",
          "Eritrocitos:": "4.8 – 6.4",
          "Reticulocitos:": "<60",
          "RDWc:": "14.0 – 20.0",
          "Plaquetas:": "350-800",
          "VPM:": "3.9 – 11.1",
          "Sólidos totales:": "48-61",
          "Leucocitos:": "10.1 – 15.1",
          "Neutrófilos:": "5.7 – 8.3",
          "Bandas:": "<0.3",
          "Metamielocitos:": "0",
          "Mielocitos:": "0",
          "Linfocitos:": "1.8 – 8.7",
          "Monocitos:": "0.0 – 0.5",
          "Eosinófilos:": "0.0 – 0.7",
          "Basófilos:": "0",
       }
    elif raza.lower() == 'caballo':
       etiquetas_especificas = {
          "Hematocrito:": "0.32 – 0.52",
          "Hemoglobina:": "111 – 190",
          "Eritrocitos:": "6.5 – 12.5",
          "RDWc:": "–",
          "Plaquetas:": "100 – 600",
          "VPM:": "–",
          "Sólidos totales:": "60 – 80",
          "Fibrinógeno:": "2 – 4",
          "Relación ST/Fb:": "<20",
          "Leucocitos:": "5.5 – 12.5",
          "Neutrófilos:": "2.7 – 6.7",
          "Bandas:": "0",
          "Metamielocitos:": "0",
          "Mielocitos:": "0",
          "Linfocitos:": "1.5 – 7.5",
          "Monocitos:": "0 – 0.8",
          "Eosinófilos:": "0 – 0.9",
          "Basófilos:": "0 – 0.3",
       }

    # Iterar sobre cada campo y agregarlo al layout principal
    for etiqueta, editor in campos:
        layout_horizontal = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        if editor:
            if isinstance(editor, QLineEdit):
                editor.setStyleSheet(estilo_input_text)
            else:  # Es QTextEdit
                editor.setStyleSheet(estilo_textedit_formulario)
            layout_horizontal.addWidget(label)
            layout_horizontal.addWidget(editor)
        
        ################### EN ESTA PARTE ES DONDE SE AGREGAAAN LOS LIMITEEEES CON BASE AL DICCIONARIO ####################
        # Añadir etiqueta específica si el campo está en el diccionario
        if etiqueta in etiquetas_especificas:
            texto_etiqueta = etiquetas_especificas[etiqueta]
            label_especifico = QLabel(texto_etiqueta)
            label_especifico.setStyleSheet(estilo_label_limites)  # Estilo opcional para la etiqueta específica
            layout_horizontal.addWidget(label_especifico)
        ###################### HASTA AQUI ##################################################################            
        if etiqueta == 'VGM:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_vgm_label = QLabel("VGM:  34 – 58")
          if raza.lower() == 'perro':
            titulo_vgm_label = QLabel("VGM:  60 – 77")
          if raza.lower() == 'gato':
            titulo_vgm_label = QLabel("VGM:  39 – 55")
          if raza.lower() == 'cachorro':
            titulo_vgm_label = QLabel("VGM:  58 – 69")
          titulo_vgm_label.setStyleSheet(estilo_label_formulario)
          vgm_label = QLabel("0.0")
          vgm_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular VGM")
          vgm_button.clicked.connect(calcular_vgm) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_vgm_label)
          layout_vgm.addWidget(vgm_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)
        if etiqueta == 'CGMH:':
          # CREACION DE LA FILA CGMH, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_cgmh = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_cgmh_label = QLabel("CGMH:  310 – 370")
          if raza.lower() == 'perro':
            titulo_cgmh_label = QLabel("CGMH:  320 – 360")
          if raza.lower() == 'gato':
            titulo_cgmh_label = QLabel("CGMH:  300 – 360")
          if raza.lower() == 'cachorro':
            titulo_cgmh_label = QLabel("CGMH:  -")
          titulo_cgmh_label.setStyleSheet(estilo_label_formulario)
          cgmh_label = QLabel("0.0")
          cgmh_label.setStyleSheet(estilo_input_text)  #MANDA A LLAMAR LA FUNCION ENCARGA DEL CALCULO
          cgmh_button = QPushButton("Calcular CGMH")
          cgmh_button.clicked.connect(calcular_cgmh)
          cgmh_button.setStyleSheet(estilo_boton_formulario)
          layout_cgmh.addWidget(titulo_cgmh_label)
          layout_cgmh.addWidget(cgmh_label)
          layout_cgmh.addWidget(cgmh_button)
          layout_principal.addLayout(layout_cgmh)
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
      if raza.lower() == "caballo":
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
            "datos_paciente_tratamiento": campos[11][1].toPlainText(),
            "datos_analisis_hematrocrito": campos[12][1].text(),
            "datos_analisis_hemoglobina": campos[13][1].text(),
            "datos_analisis_eritrocitos": campos[14][1].text(),
            "datos_analisis_rdwc": campos[17][1].text(),
            "datos_analisis_plaquetas": campos[18][1].text(),
            "datos_analisis_vpm": campos[19][1].text(),
            "datos_analisis_solidos_totales": campos[20][1].text(),
            "datos_analisis_fibrinogeno": campos[21][1].text(),
            "datos_analisis_relacion": campos[22][1].text(),
            "datos_analisis_leucocitos": campos[23][1].text(),
            "datos_analisis_neutrofilos": campos[24][1].text(),
            "datos_analisis_bandas": campos[25][1].text(),
            "datos_analisis_metamielocitos": campos[26][1].text(),
            "datos_analisis_mielocitos": campos[27][1].text(),
            "datos_analisis_linfocitos": campos[28][1].text(),
            "datos_analisis_monocitos": campos[29][1].text(),
            "datos_analisis_eosinofilos": campos[30][1].text(),
            "datos_analisis_basofilos": campos[31][1].text(), #se queda igual
            "datos_analisis_morfologia_eritrocitos": campos[32][1].toPlainText(), #aqui esta
            "datos_analisis_morfologia_leucocitos": campos[33][1].toPlainText(),
            "datos_analisis_hallazgos": campos[34][1].toPlainText(),
            "datos_analisis_interpretacion": campos[35][1].toPlainText(),
            "datos_analisis_comentarios": campos[36][1].toPlainText(),
            "firma_path": ruta_firma
        }
        print(valores)
        generar_hemograma(valores)
      else:
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
            "datos_paciente_tratamiento": campos[11][1].toPlainText(),
            "datos_analisis_hematrocrito": campos[12][1].text(),
            "datos_analisis_hemoglobina": campos[13][1].text(),
            "datos_analisis_eritrocitos": campos[14][1].text(),
            "datos_analisis_reticulocitos": campos[17][1].text(),
            "datos_analisis_rdwc": campos[18][1].text(),
            "datos_analisis_plaquetas": campos[19][1].text(),
            "datos_analisis_vpm": campos[20][1].text(),
            "datos_analisis_solidos_totales": campos[21][1].text(),
            "datos_analisis_leucocitos": campos[22][1].text(),
            "datos_analisis_neutrofilos": campos[23][1].text(),
            "datos_analisis_bandas": campos[24][1].text(),
            "datos_analisis_metamielocitos": campos[25][1].text(),
            "datos_analisis_mielocitos": campos[26][1].text(),
            "datos_analisis_linfocitos": campos[27][1].text(),
            "datos_analisis_monocitos": campos[28][1].text(),
            "datos_analisis_eosinofilos": campos[29][1].text(),
            "datos_analisis_basofilos": campos[30][1].text(),
            "datos_analisis_morfologia_eritrocitos": campos[31][1].toPlainText(),
            "datos_analisis_morfologia_leucocitos": campos[32][1].toPlainText(),
            "datos_analisis_hallazgos": campos[33][1].toPlainText(),
            "datos_analisis_interpretacion": campos[34][1].toPlainText(),
            "datos_analisis_comentarios": campos[35][1].toPlainText(),
            "firma_path": ruta_firma
        }
        print(valores)
        generar_hemograma(valores)
    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal


