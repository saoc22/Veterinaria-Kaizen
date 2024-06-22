from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QScrollArea,QMessageBox,QHBoxLayout,QLineEdit
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from pathlib import Path
import sys
import json
import shutil

from estilos import *

imagen_path = ""  # Variable para almacenar la ruta de la imagen  
input_text_1 = None  # Variable para almacenar el widget de entrada de imagen

nombre_doctor = None

cedulas = {}
cedula_input = None

titulo_input = None

json_file_path = "doctores.json"

def cargar_json():
    if not Path(json_file_path).exists():
        with open(json_file_path, 'w') as file:
            json.dump({}, file)
    with open(json_file_path, 'r') as file:
        return json.load(file)

def guardar_json(data):
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)



def generar_popup(titulo,encabezado,cuerpo):
    popup = QMessageBox()
    popup.setText(encabezado)
    popup.setIcon(QMessageBox.Information)
    popup.setInformativeText(cuerpo)
    popup.setStandardButtons(QMessageBox.Ok)
    popup.setWindowTitle(titulo)
    return popup

def cargar_firma():
    global imagen_path
    
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Archivos de imagen (*.jpg)")
    file_dialog.setDefaultSuffix("jpg")
    
    if file_dialog.exec_():
        selected_files = file_dialog.selectedFiles()
        if selected_files:
            imagen_path = selected_files[0]
            input_text_1.setText(imagen_path)

def crear_directorio_doctor():
    global nombre_doctor
    #Revisar si ya hay un directorio con ese nombre
    #Validar el nombre
    nombre = nombre_doctor.text()
    directory_path = Path.cwd() / "Firmas" / nombre
    directory_path.mkdir()
    print(f"Successfully made the '{directory_path}' directory.")

def añadir_nueva_celula():
    global cedula_input
    global cedulas
    global titulo_input
    global nombre_doctor
    global imagen_path
    global input_text_1

    popup = None

    cedula = cedula_input.text()
    titulo = titulo_input.text()
    nombre = nombre_doctor.text()

    if not nombre or not cedula or not titulo or not imagen_path:
        popup = generar_popup("Error", "Todos los campos son obligatorios", "")
    else:
        data = cargar_json()
        if nombre not in data:
            data[nombre] = {"cedulas": [], "firma": ""}

        # Si la firma ya está agregada, no agregarla de nuevo
        if data[nombre]["firma"] == "":
            # Mueve la imagen a la carpeta "Firmas" dentro del proyecto
            firma_dir = Path.cwd() / "Firmas" / nombre
            firma_dir.mkdir(parents=True, exist_ok=True)
            firma_destino = firma_dir / Path(imagen_path).name
            shutil.copy(imagen_path, firma_destino)
            data[nombre]["firma"] = str(firma_destino)

        # Añade la nueva cédula al registro del doctor
        data[nombre]["cedulas"].append({"titulo": titulo, "cedula": cedula})
        guardar_json(data)

        cedulas[cedula] = titulo
        cedula_input.setText("")

        # Bloquear los campos de nombre y firma después de la primera adición
        nombre_doctor.setDisabled(True)
        input_text_1.setDisabled(True)

        popup = generar_popup("Confirmación", "Cédula y título agregados!", f"Se han registrado {len(cedulas)} cédulas")

    if popup:
        popup.exec()
    print(cedulas)


def mostrar_informacion_doctor():
    global nombre_doctor

    nombre = nombre_doctor.text()
    data = cargar_json()

    if nombre in data:
        info = data[nombre]
        cedulas_info = "\n".join([f"Cédula: {cedula['cedula']}, Título: {cedula['titulo']}" for cedula in info["cedulas"]])
        firma_info = f"Firma: {info['firma']}" if info["firma"] else "Firma: No registrada"
        mensaje = f"Nombre: {nombre}\n\nCédulas:\n{cedulas_info}\n\n{firma_info}"
        popup = generar_popup("Información del Doctor", "Información agregada:", mensaje)
        popup.exec()
    else:
        popup = generar_popup("Error", "Doctor no encontrado", "No se encontró información para el doctor especificado.")
        popup.exec()

def crear_formulario_firma():
    global imagen_path
    global input_text_1
    global nombre_doctor
    global cedula_input
    global titulo_input

    widget_formulario = QWidget()
    layout_formulario = QVBoxLayout(widget_formulario)

    # Primer elemento: Cargar archivos
    layout_horizontal_1 = QHBoxLayout()

    label_1 = QLabel("Cargar \narchivos:")
    label_1.setStyleSheet(estilo_label_formulario)

    input_text_1 = QLineEdit()
    input_text_1.setPlaceholderText("Archivo..")
    input_text_1.setStyleSheet(estilo_input_text)

    boton_1 = QPushButton("Examinar")
    boton_1.setStyleSheet(estilo_boton_formulario)
    boton_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    boton_1.clicked.connect(cargar_firma)

    layout_horizontal_1.addWidget(label_1)
    layout_horizontal_1.addWidget(input_text_1)
    layout_horizontal_1.addWidget(boton_1)

    layout_formulario.addLayout(layout_horizontal_1)

    # Tercer elemento: Nombre
    layout_horizontal_3 = QHBoxLayout()

    label_3 = QLabel("Nombre:")
    label_3.setStyleSheet(estilo_label_formulario)

    input_text_3 = QLineEdit()
    input_text_3.setPlaceholderText("Nombre...")
    input_text_3.setStyleSheet(estilo_input_text)

    layout_horizontal_3.addWidget(label_3)
    layout_horizontal_3.addWidget(input_text_3)

    layout_formulario.addLayout(layout_horizontal_3)

    # Segundo elemento: Títulos
    layout_horizontal_2 = QHBoxLayout()

    label_2 = QLabel("Titulos:  ")
    label_2.setStyleSheet(estilo_label_formulario)

    input_text_2 = QLineEdit()
    input_text_2.setPlaceholderText("Titulos...")
    input_text_2.setStyleSheet(estilo_input_text)

    layout_horizontal_2.addWidget(label_2)
    layout_horizontal_2.addWidget(input_text_2)

    layout_formulario.addLayout(layout_horizontal_2)

    # Cuarto elemento: Cedula
    layout_horizontal_4 = QHBoxLayout()

    label_4 = QLabel("Cedula:  ")
    label_4.setStyleSheet(estilo_label_formulario)

    input_text_4 = QLineEdit()
    input_text_4.setPlaceholderText("Cedula...")
    input_text_4.setStyleSheet(estilo_input_text)

    boton_4 = QPushButton("+")
    boton_4.setStyleSheet(estilo_boton_formulario)
    boton_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    boton_4.clicked.connect(añadir_nueva_celula)

    layout_horizontal_4.addWidget(label_4)
    layout_horizontal_4.addWidget(input_text_4)
    layout_horizontal_4.addWidget(boton_4)

    layout_formulario.addLayout(layout_horizontal_4)

    # Agregar botones al final del formulario
    boton_enviar = QPushButton("Añadir")
    boton_cancelar = QPushButton("Cancelar")

    boton_enviar.setStyleSheet(estilo_boton_terminar_formulario)
    boton_cancelar.setStyleSheet(estilo_boton_terminar_formulario)

    boton_enviar.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    boton_cancelar.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    nombre_doctor = input_text_3
    cedula_input = input_text_4
    titulo_input = input_text_2

    boton_enviar.clicked.connect(mostrar_informacion_doctor)

    layout_botones = QHBoxLayout()
    layout_botones.addWidget(boton_enviar)
    layout_botones.addWidget(boton_cancelar)

    layout_formulario.addLayout(layout_botones)

    return widget_formulario
