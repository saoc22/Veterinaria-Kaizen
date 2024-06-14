from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QLineEdit, QTextEdit, QButtonGroup, QHBoxLayout, QLabel, QPushButton, QCheckBox, QFileDialog
from PyQt5.QtCore import Qt  # Importa Qt desde QtCore para manejar alineaciones y otros
from PyQt5.QtGui import QFont 
from estilos import *
from pdf_bioquimica import *

def cargar_firma():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Archivos de imagen (*.jpg *.png)")
    file_dialog.setDefaultSuffix("jpg")
    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            return selected_files[0]  # Retorna la ruta del archivo seleccionado
    return None

def crear_formato_analisis_clinico(raza):
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)

    ############### FORMULAS PARA CALCULAR OPERACIONES ###############
    def calcular_noconjugada():
        global vgm
        try:
            if(raza.lower() == 'caballo'):
              hematocrito = float(campos_comunes[16][1].text())  
              eritrocitos = float(campos_comunes[17][1].text())  
            else:
              hematocrito = float(campos_comunes[17][1].text())  
              eritrocitos = float(campos_comunes[18][1].text()) 
            vgm = hematocrito - eritrocitos  
            labels_especiales["Bilirrubina NC:"].setText(f"{vgm:.2f}")  
        except ValueError:
            labels_especiales["Bilirrubina NC:"].setText("Error")

    def calcular_globulinas():
      global globulinas
      try:
          if(raza.lower() == 'caballo'):
            prot = float(campos_comunes[20][1].text())  
            albu = float(campos_comunes[22][1].text())  
          elif (raza.lower() == 'perro'):
            prot = float(campos_comunes[26][1].text())  
            albu = float(campos_comunes[27][1].text()) 
          elif (raza.lower() == 'gato'):
            prot = float(campos_comunes[27][1].text())  
            albu = float(campos_comunes[28][1].text()) 
          globulinas = prot - albu  
          labels_especiales["Globulinas:"].setText(f"{globulinas:.2f}")  
      except ValueError:
          labels_especiales["Globulinas:"].setText("Error")

    def calcular_relacion():
      global relacion
      try:
          if(raza.lower() == 'caballo'):
            albu = float(campos_comunes[22][1].text())  
            glob = float(campos_comunes[20][1].text()) - float(campos_comunes[22][1].text())   
          elif (raza.lower() == 'perro'):
            albu = float(campos_comunes[27][1].text())  
            glob = float(campos_comunes[26][1].text()) - float(campos_comunes[27][1].text()) 
          elif (raza.lower() == 'gato'):
            albu = float(campos_comunes[28][1].text())  
            glob = float(campos_comunes[27][1].text()) - float(campos_comunes[28][1].text()) 
          relacion = albu/glob  
          labels_especiales["Relación A/G:"].setText(f"{relacion:.2f}")  
      except ValueError:
          labels_especiales["Relación A/G:"].setText("Error")

    def calcular_anion():
      global anion
      try:
          if(raza.lower() == 'caballo'):
            sodio = float(campos_comunes[30][1].text())  
            pota = float(campos_comunes[29][1].text())
            cloro = float(campos_comunes[31][1].text())
            bicar = float(campos_comunes[32][1].text())
          elif (raza.lower() == 'perro'):
            sodio = float(campos_comunes[33][1].text())  
            pota = float(campos_comunes[32][1].text())
            cloro = float(campos_comunes[34][1].text())
            bicar = float(campos_comunes[35][1].text())
          elif (raza.lower() == 'gato'):
            sodio = float(campos_comunes[28][1].text())  
            pota = float(campos_comunes[20][1].text())
            cloro = float(campos_comunes[20][1].text())
            bicar = float(campos_comunes[20][1].text())
          anion = (sodio+pota) - (cloro+bicar)  
          labels_especiales["Anion gap:"].setText(f"{anion:.2f}")  
      except ValueError:
          labels_especiales["Anion gap:"].setText("Error")

    def calcular_iones():
      global iones
      try:
          if(raza.lower() == 'caballo'):
            sodi = float(campos_comunes[30][1].text())  
            clor = float(campos_comunes[31][1].text())
          elif (raza.lower() == 'perro'):
            sodi = float(campos_comunes[33][1].text())  
            clor = float(campos_comunes[34][1].text()) 
          elif (raza.lower() == 'gato'):
            sodi = float(campos_comunes[34][1].text())  
            clor = float(campos_comunes[35][1].text())
          iones = sodi - clor  
          labels_especiales["Iones fuertes:"].setText(f"{iones:.2f}")  
      except ValueError:
          labels_especiales["Iones fuertes:"].setText("Error")
    
    def calcular_osmolalidad():
      global osmo
      try:
          if(raza.lower() == 'gato'):
            sodi = float(campos_comunes[34][1].text())  
          elif (raza.lower() == 'perro'):
            sodi = float(campos_comunes[33][1].text()) 
          gluc = float(campos_comunes[12][1].text())
          urea = float(campos_comunes[13][1].text())

          osmo = (1.86*sodi) + 9 + gluc + urea  
          labels_especiales["Osmolalidad:"].setText(f"{osmo:.2f}")  
      except ValueError:
          labels_especiales["Osmolalidad:"].setText("Error")

    def calcular_total():
       calcular_noconjugada()
       calcular_globulinas()
       calcular_relacion()
       calcular_anion()
       calcular_iones()
       if raza.lower() != "caballo":
        calcular_osmolalidad()

    # Campos comunes a todos los análisis
    campos_comunes = [
        ("Número de caso:", QLineEdit("Default Case Number")),
        ("Fecha y hora de muestro:", QLineEdit("01/01/2024 12:00")),
        ("Fecha de recepción:", QLineEdit("01/01/2024")),
        ("Fecha de emisión resultado:", QLineEdit("01/01/2024")),
        ("Nombre paciente:", QLineEdit("Nombre Predeterminado")),
        ("Edad:", QLineEdit("Edad Predeterminada")),
        ("Raza:", QLineEdit(raza)),
        ("Sexo:", None),  # Para los checkboxes de sexo
        ("Nombre del propietario:", QLineEdit("Propietario Predeterminado")),
        ("Hospital/MVZ:", QLineEdit("Hospital Predeterminado")),
        ("Anamnesis:", QTextEdit("Anamnesis Predeterminada")),
        ("Tratamiento:", QTextEdit("Tratamiento Predeterminado"))
    ]

    # Definición de campos adicionales según la raza
    campos_adicionales = {
        "perro": [
            ("Glucosa:", QLineEdit("0.0")), 
            ("Urea:", QLineEdit("0.0")), 
            ("Creatinina:", QLineEdit("0.0")), 
            ("Colesterol:", QLineEdit("0.0")), 
            ("Triglicéridos:", QLineEdit("0.0")), 
            ("Bilirrubina T:", QLineEdit("0.0")), 
            ("Bilirrubina C:", QLineEdit("0.0")), 
            ("Bilirrubina NC:", None), 
            ("ALT:", QLineEdit("0.0")), 
            ("AST:", QLineEdit("0.0")), 
            ("FA:", QLineEdit("0.0")), 
            ("CK:", QLineEdit("0.0")), 
            ("Amilasa:", QLineEdit("0.0")), 
            ("Lipasa:", QLineEdit("0.0")), 
            ("Proteínas:", QLineEdit("0.0")), 
            ("Albúmina:", QLineEdit("0.0")), 
            ("Globulinas:", None), 
            ("Relación A/G:", None), 
            ("Calcio:", QLineEdit("0.0")), 
            ("Fósforo:", QLineEdit("0.0")), 
            ("Potasio:", QLineEdit("0.0")), 
            ("Sodio:", QLineEdit("0.0")), 
            ("Cloro:", QLineEdit("0.0")), 
            ("Bicarbonato:", QLineEdit("0.0")), 
            ("Anion gap:", None), 
            ("Iones fuertes:", None), 
            ("Osmolalidad:", None)
        ],
        "gato": [
            ("Glucosa:", QLineEdit("0.0")),
            ("Urea:", QLineEdit("0.0")),
            ("Creatinina:", QLineEdit("0.0")),
            ("Colesterol:", QLineEdit("0.0")),
            ("Triglicéridos:", QLineEdit("0.0")),
            ("Bilirrubina T:", QLineEdit("0.0")),
            ("Bilirrubina C:", QLineEdit("0.0")),
            ("Bilirrubina NC:", None),
            ("ALT:", QLineEdit("0.0")),
            ("AST:", QLineEdit("0.0")),
            ("FA:", QLineEdit("0.0")),
            ("GGT:", QLineEdit("0.0")),
            ("CK:", QLineEdit("0.0")),
            ("Amilasa:", QLineEdit("0.0")),
            ("Lipasa:", QLineEdit("0.0")),
            ("Proteínas:", QLineEdit("0.0")),
            ("Albúmina:", QLineEdit("0.0")),
            ("Globulinas:", None),
            ("Relación A/G:", None),
            ("Calcio:", QLineEdit("0.0")),
            ("Fósforo:", QLineEdit("0.0")),
            ("Potasio:", QLineEdit("0.0")),
            ("Sodio:", QLineEdit("0.0")),
            ("Cloro:", QLineEdit("0.0")),
            ("Bicarbonato:", QLineEdit("0.0")),
            ("Anion gap:", None),
            ("Iones fuertes:", None),
            ("Osmolalidad:", None)
        ],
        "caballo": [
            ("Glucosa:", QLineEdit("0.0")),
            ("Urea:", QLineEdit("0.0")),
            ("Creatinina:", QLineEdit("0.0")),
            ("Colesterol:", QLineEdit("0.0")),
            ("Bilirrubina T:", QLineEdit("0.0")),
            ("Bilirrubina C:", QLineEdit("0.0")),
            ("Bilirrubina NC:", None),
            ("AST:", QLineEdit("0.0")),
            ("Proteínas:", QLineEdit("0.0")),
            ("FA:", QLineEdit("FA")),
            ("Albúmina:", QLineEdit("0.0")),
            ("GGT:", QLineEdit("0.0")),
            ("CK:", QLineEdit("0.0")),
            ("Globulinas:", None),
            ("Relación A/G:", None),
            ("Calcio:", QLineEdit("0.0")),
            ("Fósforo:", QLineEdit("0.0")),
            ("Potasio:", QLineEdit("0.0")),
            ("Sodio:", QLineEdit("0.0")),
            ("Cloro:", QLineEdit("0.0")),
            ("Bicarbonato:", QLineEdit("0.0")),
            ("Anion gap:", None),
            ("Iones fuertes:", None)
        ]
    }

    campos_comentarios = [
       ("Otros Hallazgos:", QTextEdit("Otros Hallazgos")),
       ("Interpretaciones:", QTextEdit("Interpretaciones")),
       ("Comentarios extras:", QTextEdit("Comentarios extras"))
    ]

    if raza.lower() == 'perro':
      etiquetas_especificas = {
          "Glucosa:": "3.88 – 6.88",
          "Urea:": "2.1 – 7.9",
          "Creatinina:": "60 – 130",
          "Colesterol:": "2.85 – 7.76",
          "Triglicéridos:": "0.6 – 1.2",
          "Bilirrubina T:": "<5.2",
          "Bilirrubina C:": "-",
          "ALT:": "<70",
          "AST:": "<55",
          "FA:": "<189",
          "CK:": "<213",
          "Amilasa:": "<1110",
          "Lipasa:": "<300",
          "Proteínas:": "56 – 75",
          "Albúmina:": "29 – 40",
          "Calcio:": "2.17 – 2.94",
          "Fósforo:": "0.80 – 1.80",
          "Potasio:": "3.6 – 5.3",
          "Sodio:": "143 – 158",
          "Cloro:": "110 – 125",
          "Bicarbonato:": "17 – 25",
          #Calculados
          "Anion gap:": "12 - 24",
          "Iones fuertes:": "30 - 40",
          "Osmolalidad:": "285 - 320",
          "Bilirrubina NC:": "-",
          "Globulinas:": "23 - 39",
          "Relación A/G:": "0.78 - 1.46"
        }
    elif raza.lower() == 'gato':
      etiquetas_especificas = {
        "Glucosa:": "3.8 – 7.9",
        "Urea:": "4.1 – 10.8",
        "Creatinina:": "56 – 176",
        "Colesterol:": "1.78 – 3.87",
        "Triglicéridos:": "0.6 – 1.2",
        "Bilirrubina T:": "<6.8",
        "Bilirrubina C:": "-",
        "ALT:": "<72",
        "AST:": "<61",
        "FA:": "<107",
        "GGT:": "<5",
        "CK:": "<277",
        "Amilasa:": "<1800",
        "Lipasa:": "<300",
        "Proteínas:": "59 – 81",
        "Albúmina:": "26 – 38",
        "Calcio:": "2.05 – 2.76",
        "Fósforo:": "0.96 – 1.96",
        "Potasio:": "3.6 – 5.3",
        "Sodio:": "143 – 158",
        "Cloro:": "110 – 125",
        "Bicarbonato:": "14 – 24",
        "Anion gap:": "10 - 27",
        "Iones fuertes:": "30 - 40",
        "Osmolalidad:": "290 - 330"
      }
    elif raza.lower() == 'caballo':
      etiquetas_especificas = {
        "Glucosa:": "3.4 – 6.2",
        "Urea:": "4.1 – 7.6",
        "Creatinina:": "88 – 156",
        "Colesterol:": "1.81 – 4.65",
        "Bilirrubina T:": "14.0 – 54.0",
        "Bilirrubina C:": "6.0 – 12.0",
        "AST:": "<450",
        "Proteínas:": "53 – 71",
        "FA:": "<453",
        "Albúmina:": "31 – 39",
        "GGT:": "<22",
        "CK:": "<425",
        "Calcio:": "2.79 – 3.22",
        "Fósforo:": "0.89 – 1.77",
        "Potasio:": "3.4 – 5.0",
        "Sodio:": "132 – 141",
        "Cloro:": "98 – 105",
        "Bicarbonato:": "27 – 34",
        "Anion gap:": "4 - 13",
        "Iones fuertes:": "34 - 43",
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
          separador.setFixedHeight(70)
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
    for etiqueta, editor in campos_adicionales[raza]:
      layout_horizontal = QHBoxLayout()
      #Etiqueta del dato a ingresar
      label = QLabel(etiqueta)
      label.setStyleSheet(estilo_label_formulario)
      #Etiqueta del limite del dato
      label_limite = QLabel(etiquetas_especificas[etiqueta])
      label_limite.setStyleSheet(estilo_label_limites)
      #Etiqueta para ingresar los datos
      if editor:
        editor.setStyleSheet(estilo_input_text)
        layout_horizontal.addWidget(label)
        layout_horizontal.addWidget(editor)
        layout_horizontal.addWidget(label_limite)
        layout_principal.addLayout(layout_horizontal)

        #Separador
        separador = QWidget()
        separador.setFixedHeight(50)
        separador.setStyleSheet("background-color: transparent;") 
        layout_principal.addWidget(separador)

    # Título y sección de datos calculados
    titulo_paciente = QLabel("Calculos")
    titulo_paciente.setAlignment(Qt.AlignCenter)  # Centra el título
    titulo_paciente.setStyleSheet("font-size: 20px; font-weight: bold;")
    layout_principal.addWidget(titulo_paciente)
    titulo_linea = QWidget()#Separador
    titulo_linea.setFixedHeight(10)
    titulo_linea.setStyleSheet("background-color: #C2C2C2;") 
    layout_principal.addWidget(titulo_linea)


    #Seccion para juntar ambas listas de datos
    campos_especificos = campos_adicionales[raza]
    for campo in campos_especificos:
        campos_comunes.append(campo)

    labels_especiales = {
      "Bilirrubina NC:": QLabel("0.0"),
      "Globulinas:": QLabel("0.0"),
      "Relación A/G:": QLabel("0.0"),
      "Anion gap:": QLabel("0.0"),
      "Iones fuertes:": QLabel("0.0"),
      "Osmolalidad:": QLabel("0.0")
    }
    # Aplicar estilos a cada QLabel en el diccionario
    for label in labels_especiales.values():
        label.setStyleSheet(estilo_input_text)

    #Seccion del codigo que genera el formulario para los datos de analisis CALCULADOS
    for etiqueta, editor in campos_adicionales[raza]:
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
        # vgm_label = QLabel("0.0")
        # vgm_label.setStyleSheet(estilo_input_text)
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
        separador.setFixedHeight(70)
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
        if raza.lower() == 'perro':
            valores = {
                "datos_caso": campos_comunes[0][1].text(),
                "fecha_muestreo": campos_comunes[1][1].text(),
                "fecha_recepcion": campos_comunes[2][1].text(),
                "fecha_emision": campos_comunes[3][1].text(),
                "datos_paciente_nombre": campos_comunes[4][1].text(),
                "datos_paciente_raza": campos_comunes[6][1].text(),
                "datos_paciente_edad": campos_comunes[5][1].text(),
                "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h",
                "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
                "datos_paciente_propietario": campos_comunes[8][1].text(),
                "datos_paciente_hospital": campos_comunes[9][1].text(),
                "datos_paciente_anamnesis": campos_comunes[10][1].toPlainText(),
                "datos_paciente_tratamiento": campos_comunes[11][1].toPlainText(),
                "datos_analisis_glucosa": campos_comunes[12][1].text(),
                "datos_analisis_urea": campos_comunes[13][1].text(),
                "datos_analisis_creatinina": campos_comunes[14][1].text(),
                "datos_analisis_colesterol": campos_comunes[15][1].text(),
                "datos_analisis_trigliceridos": campos_comunes[16][1].text(),
                "datos_analisis_bilirrubina_total": campos_comunes[17][1].text(),
                "datos_analisis_bilirrubina_conjugada": campos_comunes[18][1].text(),
                "datos_analisis_alaninamino_transferasa": campos_comunes[20][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[21][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[22][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[23][1].text(),
                "datos_analisis_amilasa": campos_comunes[24][1].text(),
                "datos_analisis_lipasa": campos_comunes[25][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[26][1].text(),
                "datos_analisis_albumina": campos_comunes[27][1].text(),
                "datos_analisis_calcio_total": campos_comunes[30][1].text(),
                "datos_analisis_fosforo": campos_comunes[31][1].text(),
                "datos_analisis_potasio": campos_comunes[32][1].text(),
                "datos_analisis_sodio": campos_comunes[33][1].text(),
                "datos_analisis_cloro": campos_comunes[34][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[35][1].text(),
                "datos_analisis_otros_hallazgos": campos_comunes[39][1].toPlainText(),
                "datos_analisis_interpretaciones": campos_comunes[40][1].toPlainText(),
                "datos_analisis_comentarios": campos_comunes[41][1].toPlainText(),
                "firma_path": ruta_firma
            }
            print(valores)
        elif raza.lower() == 'gato':
            valores = {
                "datos_caso": campos_comunes[0][1].text(),
                "fecha_muestreo": campos_comunes[1][1].text(),
                "fecha_recepcion": campos_comunes[2][1].text(),
                "fecha_emision": campos_comunes[3][1].text(),
                "datos_paciente_nombre": campos_comunes[4][1].text(),
                "datos_paciente_raza": campos_comunes[6][1].text(),
                "datos_paciente_edad": campos_comunes[5][1].text(),
                "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h",
                "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
                "datos_paciente_propietario": campos_comunes[8][1].text(),
                "datos_paciente_hospital": campos_comunes[9][1].text(),
                "datos_paciente_anamnesis": campos_comunes[10][1].toPlainText(),
                "datos_paciente_tratamiento": campos_comunes[11][1].toPlainText(),
                "datos_analisis_glucosa": campos_comunes[12][1].text(),
                "datos_analisis_urea": campos_comunes[13][1].text(),
                "datos_analisis_creatinina": campos_comunes[14][1].text(),
                "datos_analisis_colesterol": campos_comunes[15][1].text(),
                "datos_analisis_trigliceridos": campos_comunes[16][1].text(),
                "datos_analisis_bilirrubina_total": campos_comunes[17][1].text(),
                "datos_analisis_bilirrubina_conjugada": campos_comunes[18][1].text(),
                "datos_analisis_alaninamino_transferasa": campos_comunes[20][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[21][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[22][1].text(),
                "datos_analisis_ggt": campos_comunes[23][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[24][1].text(),
                "datos_analisis_amilasa": campos_comunes[25][1].text(),
                "datos_analisis_lipasa": campos_comunes[26][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[27][1].text(),
                "datos_analisis_albumina": campos_comunes[28][1].text(),
                "datos_analisis_calcio_total": campos_comunes[31][1].text(),
                "datos_analisis_fosforo": campos_comunes[32][1].text(),
                "datos_analisis_potasio": campos_comunes[33][1].text(),
                "datos_analisis_sodio": campos_comunes[34][1].text(),
                "datos_analisis_cloro": campos_comunes[35][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[36][1].text(),
                "datos_analisis_otros_hallazgos": campos_comunes[40][1].toPlainText(),
                "datos_analisis_interpretaciones": campos_comunes[41][1].toPlainText(),
                "datos_analisis_comentarios": campos_comunes[42][1].toPlainText(),
                "firma_path": ruta_firma
            }
            print(valores)
        elif raza.lower() == 'caballo':
            valores = {
                "datos_caso": campos_comunes[0][1].text(),
                "fecha_muestreo": campos_comunes[1][1].text(),
                "fecha_recepcion": campos_comunes[2][1].text(),
                "fecha_emision": campos_comunes[3][1].text(),
                "datos_paciente_nombre": campos_comunes[4][1].text(),
                "datos_paciente_raza": campos_comunes[6][1].text(),
                "datos_paciente_edad": campos_comunes[5][1].text(),
                "datos_paciente_sexo": "m" if cb_masculino.isChecked() else "h",
                "datos_paciente_castrado": "Si" if cb_castrado.isChecked() else "no",
                "datos_paciente_propietario": campos_comunes[8][1].text(),
                "datos_paciente_hospital": campos_comunes[9][1].text(),
                "datos_paciente_anamnesis": campos_comunes[10][1].toPlainText(),
                "datos_paciente_tratamiento": campos_comunes[11][1].toPlainText(),
                "datos_analisis_glucosa": campos_comunes[12][1].text(),
                "datos_analisis_urea": campos_comunes[13][1].text(),
                "datos_analisis_creatinina": campos_comunes[14][1].text(),
                "datos_analisis_colesterol": campos_comunes[15][1].text(),
                "datos_analisis_bilirrubina_total": campos_comunes[16][1].text(),
                "datos_analisis_bilirrubina_conjugada": campos_comunes[17][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[19][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[21][1].text(),
                "datos_analisis_ggt": campos_comunes[23][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[24][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[20][1].text(),
                "datos_analisis_albumina": campos_comunes[22][1].text(),
                "datos_analisis_calcio_total": campos_comunes[27][1].text(),
                "datos_analisis_fosforo": campos_comunes[28][1].text(),
                "datos_analisis_potasio": campos_comunes[29][1].text(),
                "datos_analisis_sodio": campos_comunes[30][1].text(),
                "datos_analisis_cloro": campos_comunes[31][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[32][1].text(),
                "datos_analisis_otros_hallazgos": campos_comunes[35][1].toPlainText(),
                "datos_analisis_interpretaciones": campos_comunes[36][1].toPlainText(),
                "datos_analisis_comentarios": campos_comunes[37][1].toPlainText(),
                "firma_path": ruta_firma
            }
            print(valores)
        generar_bioquimica(valores)

    boton_reporte.clicked.connect(boton_reporte_clicked)
    boton_firma.clicked.connect(seleccionar_firma)

    return widget_principal
