from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QButtonGroup, QHBoxLayout, QLabel, QPushButton, QCheckBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
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

    def calcular_noconjugada():
        global vgm
        try:
            if(raza.lower() == 'caballo'):
              hematocrito = float(campos_comunes[16][1].text())  
              eritrocitos = float(campos_comunes[17][1].text())  
            else:
              hematocrito = float(campos_comunes[17][1].text())  
              eritrocitos = float(campos_comunes[18][1].text()) 
            vgm = hematocrito - eritrocitos  # Fórmula simplificada
            vgm_label.setText(f"{vgm:.2f}")  # Establece el valor en el label
        except ValueError:
            vgm_label.setText("Error")

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
            globulinas = prot - albu  # Fórmula simplificada
            globulinas_label.setText(f"{globulinas:.2f}")  # Establece el valor en el label
        except ValueError:
            globulinas_label.setText("Error")

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
            relacion = albu/glob  # Fórmula simplificada
            relacion_label.setText(f"{relacion:.2f}")  # Establece el valor en el label
        except ValueError:
            relacion_label.setText("Error")

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
            anion = (sodio+pota) - (cloro+bicar)  # Fórmula simplificada
            anion_label.setText(f"{anion:.2f}")  # Establece el valor en el label
        except ValueError:
            anion_label.setText("Error")

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
            iones = sodi - clor  # Fórmula simplificada
            iones_label.setText(f"{iones:.2f}")  # Establece el valor en el label
        except ValueError:
            iones_label.setText("Error")
    
    def calcular_osmolalidad():
        global osmo
        try:
            if(raza.lower() == 'gato'):
              sodi = float(campos_comunes[34][1].text())  
            elif (raza.lower() == 'perro'):
              sodi = float(campos_comunes[33][1].text()) 
            gluc = float(campos_comunes[12][1].text())
            urea = float(campos_comunes[13][1].text())

            osmo = (1.86*sodi) + 9 + gluc + urea  # Fórmula simplificada
            osmo_label.setText(f"{osmo:.2f}")  # Establece el valor en el label
        except ValueError:
            osmo_label.setText("Error")


    # Campos comunes a todos los análisis
    campos_comunes = [
        ("Número de caso:", QLineEdit("Default Case Number")),
        ("Fecha y hora de muestro:", QLineEdit("01/01/2024 12:00")),
        ("Fecha de recepción:", QLineEdit("01/01/2024")),
        ("Fecha de emisión de resultado:", QLineEdit("01/01/2024")),
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
            ("Bilirrubina total:", QLineEdit("0.0")), 
            ("Bilirrubina conjugada:", QLineEdit("0.0")), 
            ("Bilirrubina no conjugada:", None), 
            ("Alaninamino transferasa (ALT):", QLineEdit("0.0")), 
            ("Aspartatoamino transferasa (AST):", QLineEdit("0.0")), 
            ("Fosfatasa alcalina (FA):", QLineEdit("0.0")), 
            ("Creatincinasa (CK):", QLineEdit("0.0")), 
            ("Amilasa:", QLineEdit("0.0")), 
            ("Lipasa:", QLineEdit("0.0")), 
            ("Proteínas totales:", QLineEdit("0.0")), 
            ("Albúmina:", QLineEdit("0.0")), 
            ("Globulinas calculado:", None), 
            ("Relación A/G calculado:", None), 
            ("Calcio total:", QLineEdit("0.0")), 
            ("Fósforo:", QLineEdit("0.0")), 
            ("Potasio:", QLineEdit("0.0")), 
            ("Sodio:", QLineEdit("0.0")), 
            ("Cloro:", QLineEdit("0.0")), 
            ("Bicarbonato:", QLineEdit("0.0")), 
            ("Anion gap calculado:", None), 
            ("Diferencia de iones fuertes calculado:", None), 
            ("Osmolalidad calculada:", None)
        ],
        "gato": [
            ("Glucosa:", QLineEdit("0.0")),
            ("Urea:", QLineEdit("0.0")),
            ("Creatinina:", QLineEdit("0.0")),
            ("Colesterol:", QLineEdit("0.0")),
            ("Triglicéridos:", QLineEdit("0.0")),
            ("Bilirrubina total:", QLineEdit("0.0")),
            ("Bilirrubina conjugada:", QLineEdit("0.0")),
            ("Bilirrubina no conjugada:", None),
            ("Alaninamino transferasa (ALT):", QLineEdit("0.0")),
            ("Aspartatoamino transferasa (AST):", QLineEdit("0.0")),
            ("Fosfatasa alcalina (FA):", QLineEdit("0.0")),
            ("Gammaglutamil transferasa (GGT):", QLineEdit("0.0")),
            ("Creatincinasa (CK):", QLineEdit("0.0")),
            ("Amilasa:", QLineEdit("0.0")),
            ("Lipasa:", QLineEdit("0.0")),
            ("Proteínas totales:", QLineEdit("0.0")),
            ("Albúmina:", QLineEdit("0.0")),
            ("Globulinas calculado:", None),
            ("Relación A/G calculado:", None),
            ("Calcio total:", QLineEdit("0.0")),
            ("Fósforo:", QLineEdit("0.0")),
            ("Potasio:", QLineEdit("0.0")),
            ("Sodio:", QLineEdit("0.0")),
            ("Cloro:", QLineEdit("0.0")),
            ("Bicarbonato:", QLineEdit("0.0")),
            ("Anion gap calculado:", None),
            ("Diferencia de iones fuertes calculado:", None),
            ("Osmolalidad calculada:", None)
        ],
        "caballo": [
            ("Glucosa:", QLineEdit("Glucosa")),
            ("Urea:", QLineEdit("Urea")),
            ("Creatinina:", QLineEdit("Creatinina")),
            ("Colesterol:", QLineEdit("Colesterol")),
            ("Bilirrubina total:", QLineEdit("Total")),
            ("Bilirrubina conjugada:", QLineEdit("Conjugada")),
            ("Bilirrubina no conjugada:", None),
            ("Aspartatoamino transferasa (AST):", QLineEdit("AST")),
            ("Proteínas totales:", QLineEdit("Proteinas")),
            ("Fosfatasa alcalina (FA):", QLineEdit("FA")),
            ("Albúmina:", QLineEdit("Albumina")),
            ("Gamma glutamiltransferasa (GGT):", QLineEdit("GGT")),
            ("Creatincinasa (CK):", QLineEdit("CK")),
            ("Globulinas calculado:", None),
            ("Relación A/G calculado:", None),
            ("Calcio total:", QLineEdit("Calcio")),
            ("Fósforo:", QLineEdit("Fosforo")),
            ("Potasio:", QLineEdit("Potasio")),
            ("Sodio:", QLineEdit("Sodio")),
            ("Cloro:", QLineEdit("Cloro")),
            ("Bicarbonato:", QLineEdit("Bicarbonato")),
            ("Anion gap calculado:", None),
            ("Diferencia de iones fuertes calculado:", None)
        ]
    }

    if raza.lower() == 'perro':
      etiquetas_especificas = {
          "Glucosa:": "3.88 – 6.88",
          "Urea:": "2.1 – 7.9",
          "Creatinina:": "60 – 130",
          "Colesterol:": "2.85 – 7.76",
          "Triglicéridos:": "0.6 – 1.2",
          "Bilirrubina total:": "<5.2",
          "Bilirrubina conjugada:": "-",
          #"Bilirrubina no conjugada:": "-",
          "Alaninamino transferasa (ALT):": "<70",
          "Aspartatoamino transferasa (AST):": "<55",
          "Fosfatasa alcalina (FA):": "<189",
          "Creatincinasa (CK):": "<213",
          "Amilasa:": "<1110",
          "Lipasa:": "<300",
          "Proteínas totales:": "56 – 75",
          "Albúmina:": "29 – 40",
          #"Globulinas calculado:": "23 – 39",
          #"Relación A/G calculado:": "0.78 – 1.46",
          "Calcio total:": "2.17 – 2.94",
          "Fósforo:": "0.80 – 1.80",
          "Potasio:": "3.6 – 5.3",
          "Sodio:": "143 – 158",
          "Cloro:": "110 – 125",
          "Bicarbonato:": "17 – 25",
          #"Anion gap calculado:": "12 – 24",
          #"Diferencia de iones fuertes calculado:": "30 – 40",
          #"Osmolalidakd calculada:": "285 – 320",
        }
    elif raza.lower() == 'gato':
        etiquetas_especificas = {
          "Glucosa:": "3.8 – 7.9",
          "Urea:": "4.1 – 10.8",
          "Creatinina:": "56 – 176",
          "Colesterol:": "1.78 – 3.87",
          "Triglicéridos:": "0.6 – 1.2",
          "Bilirrubina total:": "<6.8",
          "Bilirrubina conjugada:": "-",
          #"Bilirrubina no conjugada:": "-",
          "Alaninamino transferasa (ALT):": "<72",
          "Aspartatoamino transferasa (AST):": "<61",
          "Fosfatasa alcalina (FA):": "<107",
          "Gammaglutamil transferasa (GGT):": "<5",
          "Creatincinasa (CK):": "<277",
          "Amilasa:": "<1800",
          "Lipasa:": "<300",
          "Proteínas totales:": "59 – 81",
          "Albúmina:": "26 – 38",
          #"Globulinas calculado:": "29 – 47",
          #"Relación A/G calculado:": "0.58 – 1.16",
          "Calcio total:": "2.05 – 2.76",
          "Fósforo:": "0.96 – 1.96",
          "Potasio:": "3.6 – 5.3",
          "Sodio:": "143 – 158",
          "Cloro:": "110 – 125",
          "Bicarbonato:": "14 – 24",
          #"Anion gap calculado:": "10 – 27",
          #"Diferencia de iones fuertes calculado:": "30 – 40",
          #"Osmolalidad calculada:": "290 – 330",

        }
    elif raza.lower() == 'caballo':
        etiquetas_especificas = {
          "Glucosa:": "3.4 – 6.2",
          "Urea:": "4.1 – 7.6",
          "Creatinina:": "88 – 156",
          "Colesterol:": "1.81 – 4.65",
          "Bilirrubina total:": "14.0 – 54.0",
          "Bilirrubina conjugada:": "6.0 – 12.0",
          #"Bilirrubina no conjugada:": "4.0 – 44.0",
          "Aspartatoamino transferasa (AST):": "<450",
          "Proteínas totales:": "53 – 71",
          "Fosfatasa alcalina (FA):": "<453",
          "Albúmina:": "31 – 39",
          "Gamma glutamiltransferasa (GGT):": "<22",
          "Creatincinasa (CK):": "<425",
          #"Globulinas calculado:": "20 – 35",
          #"Relación A/G calculado:": "0.89 – 1.65",
          "Calcio total:": "2.79 – 3.22",
          "Fósforo:": "0.89 – 1.77",
          "Potasio:": "3.4 – 5.0",
          "Sodio:": "132 – 141",
          "Cloro:": "98 – 105",
          "Bicarbonato:": "27 – 34",
          #"Anion gap calculado:": "4 – 13",
          #"Diferencia de iones fuertes calculado:": "34 – 43",
        }

    # Agregar campos específicos basados en la raza
    campos_especificos = campos_adicionales[raza]
    for campo in campos_especificos:
        campos_comunes.append(campo)

    campos_comunes.append(("Otros Hallazgos:",QTextEdit("Otros")))
    campos_comunes.append(("Interpretaciones:",QTextEdit("Interpretaciones")))
    campos_comunes.append(("Comentarios extras:",QTextEdit("Comentarios extras")))

    # Añadir todos los campos al layout
    for etiqueta, editor in campos_comunes:
        layout_horizontal = QHBoxLayout()
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)   
        if etiqueta == 'Bilirrubina no conjugada:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_vgm_label = QLabel("Bilirrubina no conjugada:  4.0 – 44.0")
          if raza.lower() == 'perro':
            titulo_vgm_label = QLabel("Bilirrubina no conjugada:  -")
          if raza.lower() == 'gato':
            titulo_vgm_label = QLabel("Bilirrubina no conjugada:  -")
          titulo_vgm_label.setStyleSheet(estilo_label_formulario)
          vgm_label = QLabel("0.0")
          vgm_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_noconjugada) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_vgm_label)
          layout_vgm.addWidget(vgm_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)   

        if etiqueta == 'Globulinas calculado:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_globulina_label = QLabel("Globulinas calculado:  20 – 35")
          if raza.lower() == 'perro':
            titulo_globulina_label = QLabel("Globulinas calculado:  23 – 39")
          if raza.lower() == 'gato':
            titulo_globulina_label = QLabel("Globulinas calculado:  29 – 47")
          titulo_globulina_label.setStyleSheet(estilo_label_formulario)
          globulinas_label = QLabel("0.0")
          globulinas_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_globulinas) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_globulina_label)
          layout_vgm.addWidget(globulinas_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)   

        if etiqueta == 'Relación A/G calculado:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_relacion_label = QLabel("Relación A/G calculado:  0.89 – 1.65")
          if raza.lower() == 'perro':
            titulo_relacion_label = QLabel("Relación A/G calculado:  0.78 – 1.46")
          if raza.lower() == 'gato':
            titulo_relacion_label = QLabel("Relación A/G calculado:  0.58 – 1.16")
          titulo_relacion_label.setStyleSheet(estilo_label_formulario)
          relacion_label = QLabel("0.0")
          relacion_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_relacion) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_relacion_label)
          layout_vgm.addWidget(relacion_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)

        if etiqueta == 'Anion gap calculado:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_anion_label = QLabel("Anion gap calculado:  0.89 – 1.65")
          if raza.lower() == 'perro':
            titulo_anion_label = QLabel("Anion gap calculado:  0.78 – 1.46")
          if raza.lower() == 'gato':
            titulo_anion_label = QLabel("Anion gap calculado:  0.58 – 1.16")
          titulo_anion_label.setStyleSheet(estilo_label_formulario)
          anion_label = QLabel("0.0")
          anion_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_anion) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_anion_label)
          layout_vgm.addWidget(anion_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)

        if etiqueta == 'Diferencia de iones fuertes calculado:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'caballo':
            titulo_iones_label = QLabel("Diferencia de iones fuertes calculado:  34 – 43")
          if raza.lower() == 'perro':
            titulo_iones_label = QLabel("Diferencia de iones fuertes calculado:  30 – 40")
          if raza.lower() == 'gato':
            titulo_iones_label = QLabel("Diferencia de iones fuertes calculado:  30 – 40")
          titulo_iones_label.setStyleSheet(estilo_label_formulario)
          iones_label = QLabel("0.0")
          iones_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_iones) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_iones_label)
          layout_vgm.addWidget(iones_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)  

        if etiqueta == 'Osmolalidad calculada:':
          #################################################### LO QUE SE AGREGA EMPIEZA DESDE AQUI ##########################
          # ESTA SECCION SE ENCARGA DE LA VINCULACION DE ESTILOS Y FUNCIONALIDAD DEL BOTON, LO QUE TIENE QUE VER CON LA INTERFAZ
          # CREACION DE LA FILA VGM, AQUI MANDAMOS A LLAMAR LA FUNCION AL DARLE CLICK AL BOTON
          layout_vgm = QHBoxLayout()
          if raza.lower() == 'perro':
            titulo_osmo_label = QLabel("Osmolalidad calculada:  285 – 320")
          if raza.lower() == 'gato':
            titulo_osmo_label = QLabel("Osmolalidad calculada:  290 – 330")
          titulo_osmo_label.setStyleSheet(estilo_label_formulario)
          osmo_label = QLabel("0.0")
          osmo_label.setStyleSheet(estilo_input_text)
          vgm_button = QPushButton("Calcular")
          vgm_button.clicked.connect(calcular_osmolalidad) #MANDA A LLAMAR LA FUNCION ENCARGADA DE ESTE CALCULO, EN ESA FUNCION SE DEFINE LA VARIABLE GLOBAL
          vgm_button.setStyleSheet(estilo_boton_formulario)
          layout_vgm.addWidget(titulo_osmo_label)
          layout_vgm.addWidget(osmo_label)
          layout_vgm.addWidget(vgm_button)
          layout_principal.addLayout(layout_vgm)            

        if etiqueta == "Sexo:":
            editor = QWidget()  # Container for checkboxes
            layout_sex = QHBoxLayout(editor)
            cb_masculino = QCheckBox("M")
            cb_femenino = QCheckBox("F")
            cb_castrado = QCheckBox("Castrado")
            cb_masculino.setStyleSheet(estilo_checkbox)
            cb_femenino.setStyleSheet(estilo_checkbox)
            cb_castrado.setStyleSheet(estilo_checkbox)

            # Crear un grupo de botones exclusivos
            grupo_sexo = QButtonGroup(widget_principal)
            grupo_sexo.setExclusive(True)  # Asegura que solo uno puede ser seleccionado a la vez
            grupo_sexo.addButton(cb_masculino)
            grupo_sexo.addButton(cb_femenino)
        
            layout_sex.addWidget(cb_masculino)
            layout_sex.addWidget(cb_femenino)
            layout_sex.addWidget(cb_castrado)
            layout_horizontal.addWidget(label)
            layout_horizontal.addWidget(editor)
        elif isinstance(editor, QLineEdit) or isinstance(editor, QTextEdit):
            editor.setStyleSheet(estilo_input_text if isinstance(editor, QLineEdit) else estilo_textedit_formulario)
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
                #"datos_analisis_bilirrubina_no_conjugada": campos_comunes[19][1].text(),
                "datos_analisis_alaninamino_transferasa": campos_comunes[20][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[21][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[22][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[23][1].text(),
                "datos_analisis_amilasa": campos_comunes[24][1].text(),
                "datos_analisis_lipasa": campos_comunes[25][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[26][1].text(),
                "datos_analisis_albumina": campos_comunes[27][1].text(),
                #"datos_analisis_globulinas": campos_comunes[28][1].text(),
                #"datos_analisis_relacion_AG": campos_comunes[29][1].text(),
                "datos_analisis_calcio_total": campos_comunes[30][1].text(),
                "datos_analisis_fosforo": campos_comunes[31][1].text(),
                "datos_analisis_potasio": campos_comunes[32][1].text(),
                "datos_analisis_sodio": campos_comunes[33][1].text(),
                "datos_analisis_cloro": campos_comunes[34][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[35][1].text(),
                #"datos_analisis_anion_gap": campos_comunes[36][1].text(),
                #"datos_analisis_diferencia_iones_fuertes": campos_comunes[37][1].text(),
                #"datos_analisis_osmolalidad": campos_comunes[38][1].text(),
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
                #"datos_analisis_bilirrubina_no_conjugada": campos_comunes[19][1].text(),
                "datos_analisis_alaninamino_transferasa": campos_comunes[20][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[21][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[22][1].text(),
                "datos_analisis_ggt": campos_comunes[23][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[24][1].text(),
                "datos_analisis_amilasa": campos_comunes[25][1].text(),
                "datos_analisis_lipasa": campos_comunes[26][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[27][1].text(),
                "datos_analisis_albumina": campos_comunes[28][1].text(),
                #"datos_analisis_globulinas": campos_comunes[29][1].text(),
                #"datos_analisis_relacion_AG": campos_comunes[30][1].text(),
                "datos_analisis_calcio_total": campos_comunes[31][1].text(),
                "datos_analisis_fosforo": campos_comunes[32][1].text(),
                "datos_analisis_potasio": campos_comunes[33][1].text(),
                "datos_analisis_sodio": campos_comunes[34][1].text(),
                "datos_analisis_cloro": campos_comunes[35][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[36][1].text(),
                #"datos_analisis_anion_gap": campos_comunes[37][1].text(),
                #"datos_analisis_diferencia_iones_fuertes": campos_comunes[38][1].text(),
                #"datos_analisis_osmolalidad": campos_comunes[39][1].text(),
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
                #"datos_analisis_bilirrubina_no_conjugada": campos_comunes[18][1].text(),
                "datos_analisis_aspartatoamino_transferasa": campos_comunes[19][1].text(),
                "datos_analisis_fosfatasa_alcalina": campos_comunes[21][1].text(),
                "datos_analisis_ggt": campos_comunes[23][1].text(),
                "datos_analisis_creatincinasa": campos_comunes[24][1].text(),
                "datos_analisis_proteinas_totales": campos_comunes[20][1].text(),
                "datos_analisis_albumina": campos_comunes[22][1].text(),
                #"datos_analisis_globulinas": campos_comunes[25][1].text(),
                #"datos_analisis_relacion_AG": campos_comunes[26][1].text(),
                "datos_analisis_calcio_total": campos_comunes[27][1].text(),
                "datos_analisis_fosforo": campos_comunes[28][1].text(),
                "datos_analisis_potasio": campos_comunes[29][1].text(),
                "datos_analisis_sodio": campos_comunes[30][1].text(),
                "datos_analisis_cloro": campos_comunes[31][1].text(),
                "datos_analisis_bicarbonato": campos_comunes[32][1].text(),
                #"datos_analisis_anion_gap": campos_comunes[33][1].text(),
                #"datos_analisis_diferencia_iones_fuertes": campos_comunes[34][1].text(),
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
