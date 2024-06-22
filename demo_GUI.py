from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QScrollArea,QMessageBox,QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from generar_formulario_hemograma import *
from generar_formulario_bioquimica import *
from generar_formulario_urianalisis import *
from generar_formulario_citologia import *
from generar_formulario_koh import *
from generar_formulario_otis1 import *
from generar_formulario_antiograma_2 import *
from pdf_hemograma import *
from firma import *
from estilos import *

#*********************************************
#              Inicializaciones
#*********************************************

grid = QGridLayout()

#*********************************************
#                 WIDGETS
#*********************************************

# Diccionario de widgets
widgets = {
    "button": [],
    "button2": [],
    "button3": [],
    "button4": [],
    "button_generador":[],
    "label": [],
    "scrollarea":[]
}

# Estilo de los botones para las pestañas



# Funcion para limpiar la pantalla de los widgets
def limpiar_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def limpiar_Area():
    # Conserva los widgets de cabecera
    cabecera_widgets = ["button", "button2", "button3", "button4"]
    
    for widget_key in widgets:
        # Si el widget no es uno de los botones de cabecera, entonces limpia
        if widget_key not in cabecera_widgets:
            if widgets[widget_key] != []:
                for widget in widgets[widget_key]:
                    widget.hide()  # Oculta el widget
                widgets[widget_key].clear()  # Limpia la lista de widgets


# Creacion del boton de formato
def crear_boton_formato(nombre,num_imagen):
    boton = QPushButton(nombre)
    ruta_imagen = f'img/botones_formato/Group-{num_imagen}.png'
    boton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    css = f'''
        QPushButton {{
          border: 1.5px solid #C2C2C2; /* Ajusta el color del borde */
          font-size: 18px;
          font-weight: bold; /* Hace el texto en negrita */
          color: #0D1E40; /* Color de las letras azules */
          height: 64px;
          max-width: 600px;
          background-image: url({ruta_imagen});
          background-position: center;
          background-repeat: no-repeat;
          border-radius: 25px; /* Hace el botón redondo */
          margin-top: 35px;
          margin-left: 10px;
          padding-left: 30px; 
        }}
        QPushButton:hover{{
            font-size: 19px;
            border: 4px solid #C2C2C2; /* Ajusta el color del borde */
        }}
    '''
    boton.setStyleSheet(css)
    return boton


######### FORMATOS DE PATOLOGIA CLINICA ###########
#Se manda a llamar la funcion para crear el formulario de hemograma y mostrarlo
def pantalla_hemograma(raza):
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_hemograma_completo(raza)
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

#Se manda a llamar la funcion para crear el formulario de urianalisis y mostrarlo
def pantalla_urianalisis():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_urianalisis_completo() 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

#Se manda a llamar la funcion para crear el formulario de bioquimica y mostrarlo
def pantalla_bioquimica(raza):
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_analisis_clinico(raza) 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def pantalla_citologia():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_citologia_completo() 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

######### FORMATOS DE ENFERMEDADES INFECCIOSAS ###########

def pantalla_otis1():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_otis1_completo() 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def pantalla_antiograma():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_antiograma_completo() 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def pantalla_koh():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formato_KOH_completo() 
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)


def en_progreso():
    limpiar_Area()
    # Crear el layout principal
    layout_principal = QVBoxLayout()
     # Cargar la imagen
    imagen = QPixmap('img/Trabajando.png')
    # Configurar QLabel para mostrar la imagen
    label_imagen = QLabel()
    label_imagen.setPixmap(imagen)
    label_imagen.setScaledContents(True)  # Ajusta la imagen al tamaño del QLabel si es necesario
    # Añadir el QLabel al layout principal
    layout_principal.addWidget(label_imagen)
    # Configurar el layout principal en el widget central si fuera necesario
    central_widget = QWidget()
    central_widget.setLayout(layout_principal)
    grid.addWidget(central_widget, 2, 0, 1, 4)

#Funcion temporal hasta crear todas las interfaces
def prueba():
    elegir_raza_hemograma()

#Pantalla de hemorgrama donde se elige el tipo de raza con la que se trabajara
def elegir_raza_hemograma():
    limpiar_Area()
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    estilo_botones = """
    QPushButton {
      border: 1.5px solid #C2C2C2; /* Ajusta el color del borde */
      font-size: 18px;
      font-weight: bold; /* Hace el texto en negrita */
      color: #0D1E40; /* Color de las letras azules */
      height: 64px;
      max-width: 600px;
      background-position: center;
      background-repeat: no-repeat;
      border-radius: 25px; /* Hace el botón redondo */
      margin-left: 10px;
      padding-left: 30px; 
    }
    QPushButton:hover{
        font-size: 19px;
        border: 4px solid #C2C2C2; /* Ajusta el color del borde */
    }
    """

    # Widget principal para el nuevo formulario
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)

    # Crear botones
    boton_perro = QPushButton("Perro")
    boton_gato = QPushButton("Gato")
    boton_caballo = QPushButton("Caballo")
    boton_cachorro = QPushButton("Cachorro")

    # Aplicar estilos a los botones
    boton_perro.setStyleSheet(estilo_botones)
    boton_gato.setStyleSheet(estilo_botones)
    boton_caballo.setStyleSheet(estilo_botones)
    boton_cachorro.setStyleSheet(estilo_botones)

    # Añadir botones al layout
    layout_principal.addWidget(boton_perro)
    layout_principal.addWidget(boton_gato)
    layout_principal.addWidget(boton_caballo)
    layout_principal.addWidget(boton_cachorro)

    boton_perro.clicked.connect(lambda:pantalla_hemograma("perro"))
    boton_gato.clicked.connect(lambda:pantalla_hemograma("gato"))
    boton_caballo.clicked.connect(lambda:pantalla_hemograma("caballo"))
    boton_cachorro.clicked.connect(lambda:pantalla_hemograma("cachorro"))

    botones_widget = widget_principal

    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

#Pantalla de bioquimica donde se elige el tipo de raza con la que se trabajara
def elegir_raza_bioquimica():
    limpiar_Area()
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    estilo_botones = """
    QPushButton {
      border: 1.5px solid #C2C2C2; /* Ajusta el color del borde */
      font-size: 18px;
      font-weight: bold; /* Hace el texto en negrita */
      color: #0D1E40; /* Color de las letras azules */
      height: 64px;
      max-width: 600px;
      background-position: center;
      background-repeat: no-repeat;
      border-radius: 25px; /* Hace el botón redondo */
      margin-left: 10px;
      padding-left: 30px; 
    }
    QPushButton:hover{
        font-size: 19px;
        border: 4px solid #C2C2C2; /* Ajusta el color del borde */
    }
    """

    # Widget principal para el nuevo formulario
    widget_principal = QWidget()
    layout_principal = QVBoxLayout(widget_principal)

    # Crear botones
    boton_perro = QPushButton("Perro")
    boton_gato = QPushButton("Gato")
    boton_caballo = QPushButton("Caballo")

    # Aplicar estilos a los botones
    boton_perro.setStyleSheet(estilo_botones)
    boton_gato.setStyleSheet(estilo_botones)
    boton_caballo.setStyleSheet(estilo_botones)

    # Añadir botones al layout
    layout_principal.addWidget(boton_perro)
    layout_principal.addWidget(boton_gato)
    layout_principal.addWidget(boton_caballo)

    boton_perro.clicked.connect(lambda:pantalla_bioquimica("perro"))
    boton_gato.clicked.connect(lambda:pantalla_bioquimica("gato"))
    boton_caballo.clicked.connect(lambda:pantalla_bioquimica("caballo"))

    botones_widget = widget_principal

    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def capturar_valores():
    
    popup_confirmacion = QMessageBox()
    popup_confirmacion.setText("¡ PDF GENERADO !")
    popup_confirmacion.setIcon(QMessageBox.Information)
    popup_confirmacion.setInformativeText("El formato ha sido exportado con exito")
    popup_confirmacion.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    popup_confirmacion.setWindowTitle("Confirmacion")
    
    valores = {}

    for child_widget in widgets["scrollarea"][-1].widget().findChildren(QLineEdit):
        if isinstance(child_widget, QLineEdit):
            campo_nombre = child_widget.property("campo_nombre")
            valor = child_widget.text()
            valores[campo_nombre] = valor
    
    #print(valores)
    #valores["imagen_path"] = imagen_path # Utiliza la ruta almacenada
    valor_retorno = popup_confirmacion.exec()
    if(valor_retorno == QMessageBox.Ok):
        pantalla_formatos()

    generar_hemograma(valores)

    #print(valores)  # Imprime los valores capturados en el diccionario

#*********************************************
#     Generacion automatica de los botones
#      que llevan a otros formularios
#         -Patologia Clinica
#         -Enfermedades Infecciosas    
#*********************************************
    
# Creacion de los botones en una area desplazable
def crear_botones_desplazables():
    widget_desplazable = QWidget()
    layout_desplazable = QVBoxLayout(widget_desplazable)
  
    botones_info = [
        ("Hemograma", elegir_raza_hemograma),
        ("Urianálisis", pantalla_urianalisis),
        ("Bioquímica", elegir_raza_bioquimica),
        ("Sub-Bioquimica", en_progreso),
        ("Endocrinología", en_progreso),
        ("Citología", pantalla_citologia),
        ("Líquidos Corporales", en_progreso),
        ("Prot/Creat", en_progreso),
        ("TP/TPPa", en_progreso)
    ]

    for i, (nombre, connect_func) in enumerate(botones_info, start=1):
        boton = crear_boton_formato(nombre,i)
        boton.clicked.connect(connect_func)
        layout_desplazable.addWidget(boton)
    
    return widget_desplazable

def crear_botones_desplazables_enfermedades_infecciosas():
    widget_desplazable = QWidget()
    layout_desplazable = QVBoxLayout(widget_desplazable)
  
    botones_info = [
        ("Análisis Micológico", en_progreso),
        ("Dx Micro Otitis 1 oído", pantalla_otis1),
        ("Dx Micro Otitis 2 oídos", pantalla_otis1),
        ("Diagnóstico Bacteriologico con antiograma 1", pantalla_otis1),
        ("Diagnóstico Bacteriologico con antiograma 2", pantalla_antiograma),
        ("Bacteriología", en_progreso),
        ("Parasitología", en_progreso),
        ("KOH", pantalla_koh),
        ("Patologia molecular", en_progreso),
        ("Urocultivo con antiograma", en_progreso)
    ]

    for i, (nombre, connect_func) in enumerate(botones_info, start=1):
        boton = crear_boton_formato(nombre,i)
        boton.clicked.connect(connect_func)
        layout_desplazable.addWidget(boton)
    
    return widget_desplazable

#*********************************************
#   CONTENIDO DEL SCROLL AREA (FORMULARIOS)
#     -Google Forms
#     -Carga de Firma
#*********************************************



def crear_formulario_google():
    widget_google = QWidget()
    layout_google = QVBoxLayout(widget_google)

    campos_formulario_google = [
        ("Cargar \narchivo:     ", "archivo..."),
        ("Num.Paciente:", "Numero.."),
    ]

    for indice, (etiqueta, placeholder) in enumerate(campos_formulario_google):
        layout_horizontal = QHBoxLayout()
        
        label = QLabel(etiqueta)
        label.setStyleSheet(estilo_label_formulario)  

        input_text = QLineEdit()
        input_text.setPlaceholderText(placeholder)  # Establece un texto de marcador de posición si es necesario
        input_text.setStyleSheet(estilo_input_text)  
        
        layout_horizontal.addWidget(label)
        layout_horizontal.addWidget(input_text)

        # Agregar un botón al lado del primer y cuarto input
        if indice == 0:  # Índices base 0, por lo que 0 y 2 representan el primer y tercer elementos
            boton = QPushButton("Examinar") 
            boton.setStyleSheet(estilo_boton_formulario) 
            layout_horizontal.addWidget(boton)
        
        layout_google.addLayout(layout_horizontal)

    boton_enviar = QPushButton("Buscar")

    boton_enviar.setStyleSheet(estilo_boton_terminar_formulario)

    boton_enviar.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    layout_botones = QHBoxLayout()
    layout_botones.addWidget(boton_enviar)

    layout_google.addLayout(layout_botones)

    return widget_google

#*********************************************
#       PANTALLAS DEL SISTEMA
#*********************************************
# Pantalla de Patologia Clinica, es la primera que se visualiza en el sistema
def pantalla_formatos():
    limpiar_widgets()

    #Boton de Patologia clinica
    button = QPushButton("Patología \n clinica")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(estilo_boton_pestaña)
    button.clicked.connect(pantalla_formatos)
    widgets["button"].append(button)

    #Boton de Enfermedades infecciosas
    button2 = QPushButton("Enfermedades \n infecciosas")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2.setStyleSheet(estilo_boton_pestaña)
    button2.clicked.connect(pantalla_enfermedades_infecciosas)
    widgets["button2"].append(button2)

    #Boton de Google Forms
    button3 = QPushButton("Google \n Forms")
    button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button3.setStyleSheet(estilo_boton_pestaña)
    button3.clicked.connect(pantalla_google_forms)
    widgets["button3"].append(button3)

    #Boton de Cargar Firma
    button4 = QPushButton("Cargar \n Firma")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4.setStyleSheet(estilo_boton_pestaña)
    button4.clicked.connect(pantalla_firmas)
    widgets["button4"].append(button4)

    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_botones_desplazables()
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["button"][-1], 0, 0)
    grid.addWidget(widgets["button2"][-1], 0, 1)
    grid.addWidget(widgets["button3"][-1], 0, 2)
    grid.addWidget(widgets["button4"][-1], 0, 3)
    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

#Pantalla de los formlarios de google Forms,
def pantalla_google_forms():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formulario_google()
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def pantalla_firmas():
    limpiar_Area()
    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_formulario_firma()
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)

def pantalla_enfermedades_infecciosas():
    limpiar_widgets()

    #Boton de Patologia clinica
    button = QPushButton("Patologia \n clinica")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(estilo_boton_pestaña)
    button.clicked.connect(pantalla_formatos)
    widgets["button"].append(button)

    #Boton de Enfermedades infecciosas
    button2 = QPushButton("Enfermedades \n infecciosas")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2.setStyleSheet(estilo_boton_pestaña)
    button2.clicked.connect(pantalla_enfermedades_infecciosas)
    widgets["button2"].append(button2)

    #Boton de Google Forms
    button3 = QPushButton("Google \n Forms")
    button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button3.setStyleSheet(estilo_boton_pestaña)
    button3.clicked.connect(pantalla_google_forms)
    widgets["button3"].append(button3)

    #Boton de Cargar Firma
    button4 = QPushButton("Cargar \n Firma")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4.setStyleSheet(estilo_boton_pestaña)
    button4.clicked.connect(pantalla_firmas)
    widgets["button4"].append(button4)

    #Scroll area para los botones
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    botones_widget = crear_botones_desplazables_enfermedades_infecciosas()
    scroll_area.setWidget(botones_widget)
    scroll_area.setStyleSheet(estilo_scroll_area)
    widgets["scrollarea"].append(scroll_area) 

    grid.addWidget(widgets["button"][-1], 0, 0)
    grid.addWidget(widgets["button2"][-1], 0, 1)
    grid.addWidget(widgets["button3"][-1], 0, 2)
    grid.addWidget(widgets["button4"][-1], 0, 3)
    grid.addWidget(widgets["scrollarea"][-1], 2, 0,1,4)