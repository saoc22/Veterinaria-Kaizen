from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QButtonGroup, QWidget, QFileDialog, QLineEdit, QTextEdit, QHBoxLayout, QCheckBox
from PyQt5.QtCore import Qt 
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
            hematocrito = float(campos_comunes[12][1].text())  # Asume que hematocrito está en posición 12
            eritrocitos = float(campos_comunes[14][1].text())  # Asume que eritrocitos está en posición 14
            vgm = int(hematocrito *1000/ eritrocitos)  # Fórmula simplificada
            labels_especiales["VGM:"].setText(str(vgm))  # Establece el valor en el label
        except ValueError:
            labels_especiales["VGM:"].setText("Error")

    def calcular_cgmh():
        global cgmh
        try:
            hemoglobina = float(campos_comunes[13][1].text())  # Asume que hemoglobina está en posición 13
            hematocrito = float(campos_comunes[12][1].text())  # Asume que hematocrito está en posición 12
            cgmh = int((hemoglobina / hematocrito))  # Fórmula simplificada
            labels_especiales["CGMH:"].setText(str(cgmh))  # Establece el valor en el label
        except ValueError:
            labels_especiales["CGMH:"].setText("Error")

    def calcular_leucocitos():
        global leucocito
        try:
            if raza.lower() != "caballo":
              leuc = float(campos_comunes[23][1].text())  
              eritr = float(campos_comunes[22][1].text())  
              leucocito = (leuc * 100)/(eritr + 100)  # Fórmula simplificada
              labels_especiales2["Leu. Corregido:"].setText(f"{leucocito:.2f}")  # Establece el valor en el label
            else:
              leuc = float(campos_comunes[24][1].text())  
              eritr = float(campos_comunes[23][1].text())  
              leucocito = (leuc * 100)/(eritr + 100)  # Fórmula simplificada
              labels_especiales2["Leu. Corregido:"].setText(f"{leucocito:.2f}")
        except ValueError:
            labels_especiales2["Leu. Corregido:"].setText("Error")

    def calcular_datos():
        global netro, banda, meta, miel, linfo, mono, eosin, baso
        try:
            if raza.lower() != "caballo":
              leuc = float(campos_comunes[23][1].text())  
              ne = float(campos_comunes[24][1].text())  
              ba = float(campos_comunes[25][1].text())
              me = float(campos_comunes[26][1].text())
              mi = float(campos_comunes[27][1].text())
              li = float(campos_comunes[28][1].text())
              mo = float(campos_comunes[29][1].text())
              eo = float(campos_comunes[30][1].text())
              bs = float(campos_comunes[31][1].text())
              netro = (leuc) * (ne/100)
              banda = (leuc) * (ba/100)
              meta = (leuc) * (me/100)
              miel = (leuc) * (mi/100)
              linfo = (leuc) * (li/100)
              mono = (leuc) * (mo/100)
              eosin = (leuc) * (eo/100)
              baso = (leuc) * (bs/100)
              labels_especiales2["Neutrófilos:"].setText(f"{netro:.2f}")
              labels_especiales2["Bandas:"].setText(f"{banda:.2f}")
              labels_especiales2["Metamielocitos:"].setText(f"{meta:.2f}")
              labels_especiales2["Mielocitos:"].setText(f"{miel:.2f}")
              labels_especiales2["Linfocitos:"].setText(f"{linfo:.2f}")
              labels_especiales2["Monocitos:"].setText(f"{mono:.2f}")
              labels_especiales2["Eosinófilos:"].setText(f"{eosin:.2f}")
              labels_especiales2["Basófilos:"].setText(f"{baso:.2f}")
            else:
              leuc = float(campos_comunes[24][1].text())  
              ne = float(campos_comunes[25][1].text())  
              ba = float(campos_comunes[26][1].text())
              me = float(campos_comunes[27][1].text())
              mi = float(campos_comunes[28][1].text())
              li = float(campos_comunes[29][1].text())
              mo = float(campos_comunes[30][1].text())
              eo = float(campos_comunes[31][1].text())
              bs = float(campos_comunes[32][1].text())
              netro = (leuc) * (ne/100)
              banda = (leuc) * (ba/100)
              meta = (leuc) * (me/100)
              miel = (leuc) * (mi/100)
              linfo = (leuc) * (li/100)
              mono = (leuc) * (mo/100)
              eosin = (leuc) * (eo/100)
              baso = (leuc) * (bs/100)
              labels_especiales2["Neutrófilos:"].setText(f"{netro:.2f}")
              labels_especiales2["Bandas:"].setText(f"{banda:.2f}")
              labels_especiales2["Metamielocitos:"].setText(f"{meta:.2f}")
              labels_especiales2["Mielocitos:"].setText(f"{miel:.2f}")
              labels_especiales2["Linfocitos:"].setText(f"{linfo:.2f}")
              labels_especiales2["Monocitos:"].setText(f"{mono:.2f}")
              labels_especiales2["Eosinófilos:"].setText(f"{eosin:.2f}")
              labels_especiales2["Basófilos:"].setText(f"{baso:.2f}")
        except ValueError:
            labels_especiales2["Leu. Corregido:"].setText("Error")


    def calcular_total():
       calcular_vgm()
       calcular_cgmh()
       calcular_leucocitos()
       calcular_datos()
    ##################### AQUI TERMINAN LAS FUNCIONES DE CALCULO, ASI ES COMO FUNCIONAA ################
    
    campos_comunes = [
      ("Número de caso:", QLineEdit("Default Case Number")),
      ("Fecha y hora de muestro:", QLineEdit("01/01/2024 12:00")),
      ("Fecha de recepción:", QLineEdit("01/01/2024")),
      ("Fecha de emisión resultado:", QLineEdit("01/01/2024")),
      ("Nombre paciente:", QLineEdit("Nombre Predeterminado")),
      ("Raza:", QLineEdit(raza)),
      ("Edad:", QLineEdit("Edad Predeterminada")),
      ("Sexo:", None),  # Para los checkboxes de sexo
      ("Nombre del propietario:", QLineEdit("Propietario Predeterminado")),
      ("Hospital/MVZ:", QLineEdit("Hospital Predeterminado")),
      ("Anamnesis:", QTextEdit("Anamnesis Predeterminada")),
      ("Tratamiento:", QTextEdit("Tratamiento Predeterminado"))
    ]

    # Crear campos de formulario con etiquetas y entradas
    if raza.lower() != 'caballo':
      campos_adicionales = [
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
          ("Eri. Nucleados:", QLineEdit("0.0")),
          ("Leucocitos:", QLineEdit("0.0")),
          ("Neutrófilos:", QLineEdit("0.0")),
          ("Bandas:", QLineEdit("0.0")),
          ("Metamielocitos:", QLineEdit("0.0")),
          ("Mielocitos:", QLineEdit("0.0")),
          ("Linfocitos:", QLineEdit("0.0")),
          ("Monocitos:", QLineEdit("0.0")),
          ("Eosinófilos:", QLineEdit("0.0")),
          ("Basófilos:", QLineEdit("0.0")),
      ]
    else:
      campos_adicionales = [
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
          ("Eri. Nucleados:", QLineEdit("0.0")),
          ("Leucocitos:", QLineEdit("")),
          ("Neutrófilos:", QLineEdit("")),
          ("Bandas:", QLineEdit("")),
          ("Metamielocitos:", QLineEdit("")),
          ("Mielocitos:", QLineEdit("")),
          ("Linfocitos:", QLineEdit("")),
          ("Monocitos:", QLineEdit("")),
          ("Eosinófilos:", QLineEdit("")),
          ("Basófilos:", QLineEdit(""))
      ]
    
    campos_comentarios = [
      ("Morfología de eritrocitos:", QTextEdit("Morfología Predeterminada")),
      ("Morfología de leucocitos:", QTextEdit("Morfología Predeterminada")),
      ("Otros hallazgos:", QTextEdit("Hallazgos Predeterminados")),
      ("Interpretación:", QTextEdit("Interpretación Predeterminada")),
      ("Comentarios:", QTextEdit("Comentarios"))
    ]
    
    campos_leucocitos = [
       ("Leu. Corregido:", None),
       ("Neutrófilos:", None),
       ("Bandas:", None),
       ("Metamielocitos:", None),
       ("Mielocitos:", None),
       ("Linfocitos:", None),
       ("Monocitos:", None),
       ("Eosinófilos:", None),
       ("Basófilos:", None),
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
          "VGM:": "60 - 77",
          "CGMH:": "320 - 360",
          "Leu. Corregido:": "6.0 - 17.0"
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
          "VGM:": "39 - 55",
          "CGMH:": "300 - 360",
          "Leu. Corregido:": "5.5 - 19.5"
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
          "VGM:": "58 - 69",
          "CGMH:": "-",
          "Leu. Corregido:": "10.1 - 15.1" 
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
          "VGM:": "34 - 58", 
          "CGMH:": "310 - 370",
          "Leu. Corregido:": "5.5 - 12.5"
       }

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

    #Seccion del codigo que genera el formulario para los datos del paciente
    for etiqueta, editor in campos_comunes:
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
          #Separador
          separador = QWidget()
          separador.setFixedHeight(50)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)
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
      if(bandera == 1):
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

    #Seccion del codigo que genera el formulario para los datos de analisis segun la raza
    for etiqueta, editor in campos_adicionales:
      if etiqueta == "Eri. Nucleados:":
        layout_horizontal = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        #Etiqueta del dato a ingresar
        label = QLabel(etiqueta)
        decim = QLabel('Decimales')
        cb_uno = QCheckBox("1")
        cb_dos = QCheckBox("2")

        label.setStyleSheet(estilo_label_formulario)
        decim.setStyleSheet(estilo_label_formulario)
        cb_uno.setStyleSheet(estilo_checkbox)
        cb_dos.setStyleSheet(estilo_checkbox)

        # Crear un grupo de botones exclusivos
        grupo_decim = QButtonGroup(widget_principal)
        grupo_decim.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
        grupo_decim.addButton(cb_uno)
        grupo_decim.addButton(cb_dos)
        
        editor.setStyleSheet(estilo_input_text_nucleados)
        layout_horizontal.addWidget(label)
        layout_horizontal.addWidget(editor)
        layout_horizontal.addWidget(decim)
        layout_horizontal.addWidget(cb_uno)
        layout_horizontal.addWidget(cb_dos)
        layout_principal.addLayout(layout_horizontal)

        #Separador
        separador = QWidget()
        separador.setFixedHeight(50)
        separador.setStyleSheet("background-color: transparent;") 
        layout_principal.addWidget(separador)
      elif etiqueta in ("Neutrófilos:", "Bandas:", "Metamielocitos:", "Mielocitos:", "Linfocitos:", "Monocitos:", "Eosinófilos:", "Basófilos:"):
        layout_horizontal = QHBoxLayout()
        #Etiqueta del dato a ingresar
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        #Etiqueta del limite del dato
        label_limite = QLabel("")
        label_limite.setStyleSheet(estilo_label_limites)
        #Etiqueta para ingresar los datos
        if editor:
          editor.setStyleSheet(estilo_input_text_hemograma)
          layout_horizontal.addWidget(label)
          layout_horizontal.addWidget(editor)
          layout_horizontal.addWidget(label_limite)
          layout_principal.addLayout(layout_horizontal)

          #Separador
          separador = QWidget()
          separador.setFixedHeight(50)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)
      else:
        layout_horizontal = QHBoxLayout()
        #Etiqueta del dato a ingresar
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        #Etiqueta del limite del dato
        label_limite = QLabel(etiquetas_especificas[etiqueta])
        label_limite.setStyleSheet(estilo_label_limites)
        #Etiqueta para ingresar los datos
        if editor:
          editor.setStyleSheet(estilo_input_text_hemograma)
          layout_horizontal.addWidget(label)
          layout_horizontal.addWidget(editor)
          layout_horizontal.addWidget(label_limite)
          layout_principal.addLayout(layout_horizontal)

          #Separador
          separador = QWidget()
          separador.setFixedHeight(50)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)

    #Seccion para juntar las primeras listas
    for campo in campos_adicionales:
       campos_comunes.append(campo)

    # Título y sección de datos calculados
    titulo_paciente = QLabel("Calculos")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente)
    titulo_linea = QWidget()#Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)

    labels_especiales = {
      "VGM:": QLabel("0"),
      "CGMH:": QLabel("0"),
    }

    labels_especiales2 = {
      "Leu. Corregido:": QLabel("0.0"),
      "Neutrófilos:": QLabel("0.0"),
      "Bandas:": QLabel("0.0"),
      "Metamielocitos:": QLabel("0.0"),
      "Mielocitos:": QLabel("0.0"),
      "Linfocitos:": QLabel("0.0"),
      "Monocitos:": QLabel("0.0"),
      "Eosinófilos:": QLabel("0.0"),
      "Basófilos:": QLabel("0.0"),
    }

    # Aplicar estilos a cada QLabel en el diccionario
    for label in labels_especiales.values():
        label.setStyleSheet(estilo_input_text_hemograma)
    # Aplicar estilos a cada QLabel en el diccionario
    for label in labels_especiales2.values():
        label.setStyleSheet(estilo_input_text_hemograma)

    #Seccion del codigo que genera el formulario para los datos de analisis CALCULADOS
    for etiqueta, editor in campos_adicionales:
      if etiqueta != "Eri. Nucleados:":
        layout_horizontal = QHBoxLayout()
        #Etiqueta del dato a ingresar
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        #Etiqueta del limite del dato
        label_limite = QLabel(etiquetas_especificas[etiqueta])
        label_limite.setStyleSheet(estilo_label_limites)
        #Etiqueta para ingresar los datos
        if editor is None and etiqueta in labels_especiales:
          label_especial = labels_especiales[etiqueta]
          layout_horizontal.addWidget(label)
          layout_horizontal.addWidget(label_especial)
          layout_horizontal.addWidget(label_limite)
          layout_principal.addLayout(layout_horizontal)

          #Separador
          separador = QWidget()
          separador.setFixedHeight(50)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)
    
    #Seccion del codigo que genera el formulario para los datos de analisis CALCULADOS
    for etiqueta, editor in campos_leucocitos:
      if etiqueta != "Eri. Nucleados:":
        layout_horizontal = QHBoxLayout()
        #Etiqueta del dato a ingresar
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)
        #Etiqueta del limite del dato
        label_limite = QLabel(etiquetas_especificas[etiqueta])
        label_limite.setStyleSheet(estilo_label_limites)
        #Etiqueta para ingresar los datos
        if editor is None and etiqueta in labels_especiales2:
          label_especial = labels_especiales2[etiqueta]
          layout_horizontal.addWidget(label)
          layout_horizontal.addWidget(label_especial)
          layout_horizontal.addWidget(label_limite)
          layout_principal.addLayout(layout_horizontal)

          #Separador
          separador = QWidget()
          separador.setFixedHeight(50)
          separador.setStyleSheet("background-color: transparent;") 
          layout_principal.addWidget(separador)

    calculos_button = QPushButton("Calcular")
    calculos_button.clicked.connect(calcular_total)
    calculos_button.setStyleSheet(estilo_boton_formulario)
    layout_principal.addWidget(calculos_button)

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
        separador.setFixedHeight(50)
        separador.setStyleSheet("background-color: transparent;") 
        layout_principal.addWidget(separador)
    
    #Seccion para juntar ambas listas de datos
    for campo in campos_comentarios:
      campos_comunes.append(campo)

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
            "datos_caso": campos_comunes[0][1].text(),
            "fecha_muestreo": campos_comunes[1][1].text(),
            "fecha_recepcion": campos_comunes[2][1].text(),
            "fecha_emision": campos_comunes[3][1].text(),
            "datos_paciente_nombre": campos_comunes[4][1].text(),
            "datos_paciente_raza": campos_comunes[5][1].text(),
            "datos_paciente_edad": campos_comunes[6][1].text(),
            "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h" ,
            "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
            "datos_paciente_propietario": campos_comunes[8][1].text(),
            "datos_paciente_hospital": campos_comunes[9][1].text(),
            "datos_paciente_anamnesis": campos_comunes[10][1].toPlainText(),
            "datos_paciente_tratamiento": campos_comunes[11][1].toPlainText(),
            "datos_analisis_hematrocrito": campos_comunes[12][1].text(),
            "datos_analisis_hemoglobina": campos_comunes[13][1].text(),
            "datos_analisis_eritrocitos": campos_comunes[14][1].text(),
            "datos_analisis_rdwc": campos_comunes[17][1].text(),
            "datos_analisis_plaquetas": campos_comunes[18][1].text(),
            "datos_analisis_vpm": campos_comunes[19][1].text(),
            "datos_analisis_solidos_totales": campos_comunes[20][1].text(),
            "datos_analisis_fibrinogeno": campos_comunes[21][1].text(),
            "datos_analisis_relacion": campos_comunes[22][1].text(),
            "datos_analisis_leucocitos": campos_comunes[24][1].text(),
            "datos_analisis_neutrofilos": campos_comunes[25][1].text(),
            "datos_analisis_bandas": campos_comunes[26][1].text(),
            "datos_analisis_metamielocitos": campos_comunes[27][1].text(),
            "datos_analisis_mielocitos": campos_comunes[28][1].text(),
            "datos_analisis_linfocitos": campos_comunes[29][1].text(),
            "datos_analisis_monocitos": campos_comunes[30][1].text(),
            "datos_analisis_eosinofilos": campos_comunes[31][1].text(),
            "datos_analisis_basofilos": campos_comunes[32][1].text(), #se queda igual
            "datos_analisis_morfologia_eritrocitos": campos_comunes[33][1].toPlainText(), #aqui esta
            "datos_analisis_morfologia_leucocitos": campos_comunes[34][1].toPlainText(),
            "datos_analisis_hallazgos": campos_comunes[35][1].toPlainText(),
            "datos_analisis_interpretacion": campos_comunes[37][1].toPlainText(),
            "datos_analisis_comentarios": campos_comunes[37][1].toPlainText(),
            "firma_path": ruta_firma,
            "decimales": "d" if cb_dos.isChecked() else "u" ,
        }
        print(valores)
        generar_hemograma(valores)
      else:
        valores = {
            "datos_caso": campos_comunes[0][1].text(),
            "fecha_muestreo": campos_comunes[1][1].text(),
            "fecha_recepcion": campos_comunes[2][1].text(),
            "fecha_emision": campos_comunes[3][1].text(),
            "datos_paciente_nombre": campos_comunes[4][1].text(),
            "datos_paciente_raza": campos_comunes[5][1].text(),
            "datos_paciente_edad": campos_comunes[6][1].text(),
            "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h" ,
            "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
            "datos_paciente_propietario": campos_comunes[8][1].text(),
            "datos_paciente_hospital": campos_comunes[9][1].text(),
            "datos_paciente_anamnesis": campos_comunes[10][1].toPlainText(),
            "datos_paciente_tratamiento": campos_comunes[11][1].toPlainText(),
            "datos_analisis_hematrocrito": campos_comunes[12][1].text(),
            "datos_analisis_hemoglobina": campos_comunes[13][1].text(),
            "datos_analisis_eritrocitos": campos_comunes[14][1].text(),
            "datos_analisis_reticulocitos": campos_comunes[17][1].text(),
            "datos_analisis_rdwc": campos_comunes[18][1].text(),
            "datos_analisis_plaquetas": campos_comunes[19][1].text(),
            "datos_analisis_vpm": campos_comunes[20][1].text(),
            "datos_analisis_solidos_totales": campos_comunes[21][1].text(),
            "datos_analisis_leucocitos": campos_comunes[23][1].text(),
            "datos_analisis_neutrofilos": campos_comunes[24][1].text(),
            "datos_analisis_bandas": campos_comunes[25][1].text(),
            "datos_analisis_metamielocitos": campos_comunes[26][1].text(),
            "datos_analisis_mielocitos": campos_comunes[27][1].text(),
            "datos_analisis_linfocitos": campos_comunes[28][1].text(),
            "datos_analisis_monocitos": campos_comunes[29][1].text(),
            "datos_analisis_eosinofilos": campos_comunes[30][1].text(),
            "datos_analisis_basofilos": campos_comunes[31][1].text(),
            "datos_analisis_morfologia_eritrocitos": campos_comunes[32][1].toPlainText(),
            "datos_analisis_morfologia_leucocitos": campos_comunes[33][1].toPlainText(),
            "datos_analisis_hallazgos": campos_comunes[34][1].toPlainText(),
            "datos_analisis_interpretacion": campos_comunes[35][1].toPlainText(),
            "datos_analisis_comentarios": campos_comunes[36][1].toPlainText(),
            "firma_path": ruta_firma,
            "decimales": "d" if cb_dos.isChecked() else "u" ,
        }
        print(valores)
        generar_hemograma(valores)
    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal


