from fpdf import FPDF
import subprocess
import sys
# -*- coding: utf-8 -*-

def generar_hemograma(valores):

  #print(valores)

  #Header y Footer del documento
  class PDF (FPDF):
      def header(self):
          self.image('img\encabezado.PNG', x=0, y=0, w=210, h=31)
          self.set_font('Arial', 'B', 20)
          self.ln(20)

      def footer(self):
          self.set_y(-30)
          self.image('img\pie.PNG', x=0, w=210, h=30)

  # Variables a crear

  raza = valores.get("datos_paciente_raza", "")

  if raza.lower() == 'caballo':
    numCaso = valores.get("datos_caso", "")
    fechaMuestreo = valores.get("fecha_muestreo", "")
    fechaRecep = valores.get("fecha_recepcion", "")
    fechaResul = valores.get("fecha_emision", "")
    nomPaci = valores.get("datos_paciente_nombre", "")
    raza = valores.get("datos_paciente_raza", "")
    edad = valores.get("datos_paciente_edad", "")
    sexo = valores.get("datos_paciente_sexo", "")
    castrado = valores.get("datos_paciente_castrado", "")
    nomProp = valores.get("datos_paciente_propietario", "")
    hospital = valores.get("datos_paciente_hospital", "")
    anamnesis = valores.get("datos_paciente_anamnesis", "")
    tratamiento = valores.get("datos_paciente_tratamiento", "")
    hematocritoRes = valores.get("datos_analisis_hematrocrito", "")
    hemoglobinaRes = valores.get("datos_analisis_hemoglobina", "")
    eritrocitosRes = valores.get("datos_analisis_eritrocitos", "")
    rdwcRes = valores.get("datos_analisis_rdwc", "")
    plaquetasRes = valores.get("datos_analisis_plaquetas", "")
    vpm = valores.get("datos_analisis_vpm", "")
    solTotal = valores.get("datos_analisis_solidos_totales", "")
    leucocitos = valores.get("datos_analisis_leucocitos", "")
    neutrofilos = valores.get("datos_analisis_neutrofilos", "")
    bandas = valores.get("datos_analisis_bandas", "")
    metamielocitos = valores.get("datos_analisis_metamielocitos", "")
    mielocitos = valores.get("datos_analisis_mielocitos", "")
    linfocitos = valores.get("datos_analisis_linfocitos", "")
    monocitos = valores.get("datos_analisis_monocitos", "")
    eosinofilos = valores.get("datos_analisis_eosinofilos", "")
    basofilos = valores.get("datos_analisis_basofilos", "")
    morfoEri = valores.get("datos_analisis_morfologia_eritrocitos", "")
    morfoLeu = valores.get("datos_analisis_morfologia_leucocitos", "")
    otros = valores.get("datos_analisis_hallazgos", "")
    interpretacion = valores.get("datos_analisis_interpretacion", "")
    comExtras = valores.get("datos_analisis_comentarios", "")
    img = valores.get("firma_path", "")
    fibri = valores.get("datos_analisis_fibrinogeno", "")
    st = valores.get("datos_analisis_relacion", "")
  else:
    numCaso = valores.get("datos_caso", "")
    fechaMuestreo = valores.get("fecha_muestreo", "")
    fechaRecep = valores.get("fecha_recepcion", "")
    fechaResul = valores.get("fecha_emision", "")
    nomPaci = valores.get("datos_paciente_nombre", "")
    raza = valores.get("datos_paciente_raza", "")
    edad = valores.get("datos_paciente_edad", "")
    sexo = valores.get("datos_paciente_sexo", "")
    castrado = valores.get("datos_paciente_castrado", "")
    nomProp = valores.get("datos_paciente_propietario", "")
    hospital = valores.get("datos_paciente_hospital", "")
    anamnesis = valores.get("datos_paciente_anamnesis", "")
    tratamiento = valores.get("datos_paciente_tratamiento", "")
    hematocritoRes = valores.get("datos_analisis_hematrocrito", "")
    hemoglobinaRes = valores.get("datos_analisis_hemoglobina", "")
    eritrocitosRes = valores.get("datos_analisis_eritrocitos", "")
    reticulocitosRes = valores.get("datos_analisis_reticulocitos", "")
    rdwcRes = valores.get("datos_analisis_rdwc", "")
    plaquetasRes = valores.get("datos_analisis_plaquetas", "")
    vpm = valores.get("datos_analisis_vpm", "")
    solTotal = valores.get("datos_analisis_solidos_totales", "")
    leucocitos = valores.get("datos_analisis_leucocitos", "")
    neutrofilos = valores.get("datos_analisis_neutrofilos", "")
    bandas = valores.get("datos_analisis_bandas", "")
    metamielocitos = valores.get("datos_analisis_metamielocitos", "")
    mielocitos = valores.get("datos_analisis_mielocitos", "")
    linfocitos = valores.get("datos_analisis_linfocitos", "")
    monocitos = valores.get("datos_analisis_monocitos", "")
    eosinofilos = valores.get("datos_analisis_eosinofilos", "")
    basofilos = valores.get("datos_analisis_basofilos", "")
    morfoEri = valores.get("datos_analisis_morfologia_eritrocitos", "")
    morfoLeu = valores.get("datos_analisis_morfologia_leucocitos", "")
    otros = valores.get("datos_analisis_hallazgos", "")
    interpretacion = valores.get("datos_analisis_interpretacion", "")
    comExtras = valores.get("datos_analisis_comentarios", "")
    img = valores.get("firma_path", "")

  #Diccionario de los limites de referencia por raza
  parametros_por_raza = {
    'cachorro': {
        'Hematocrito': (0.29, 0.39, '0.29 - 0.39'),
        'Hemoglobina': (0, '0'),
        'Eritrocitos': (4.8, 6.4, '4.8 - 6.4'),
        'VGM': (58, 69, '58 - 69'),
        'CGMH': (0, '0'),
        'Reticulocitos': (60, '<60'),
        'RDWc': (14.0, 20.0, '14.0 - 20.0'),
        'Plaquetas': (350, 800, '350 - 800'),
        'VPM': (39, 111, '39 - 111'),
        'Sólidos totales': (48, 61, '48 - 61'),
        'Leucocitos': (101, 151, '101 - 151'),
        'Neutrófilos': (5.7, 8.3, '5.7 - 8.3'),
        'Bandas': (0, 0.3, '<0.3'),
        'Metamielocitos': (0, '0'),
        'Mielocitos': (0, '0'),
        'Linfocitos': (1.8, 8.7, '1.8 - 8.7'),
        'Monocitos': (0.0, 0.5, '0.0 - 0.5'),
        'Eosinófilos': (0.0, 0.7, '0.0 - 0.7'),
        'Basófilos': (0, '0')
    },
    'gato': {
        'Hematocrito': (0.27, 0.45, '0.27 - 0.45'),
        'Hemoglobina': (80, 150, '80 - 150'),
        'Eritrocitos': (5.0, 10.0, '5.0 - 10.0'),
        'VGM': (39, 55, '39 - 55'),
        'CGMH': (300, 360, '300 - 360'),
        'Reticulocitos': (60, '<60'),
        'RDWc': (18.5, '<18.5'),
        'Plaquetas': (300, 700, '300 - 700'),
        'VPM': (12.0, 170, '12.0 - 170'),
        'Sólidos totales': (60, 80, '60 - 80'),
        'Leucocitos': (5.5, 19.5, '5.5 - 19.5'),
        'Neutrófilos': (2.5, 12.5, '2.5 - 12.5'),
        'Bandas': (0, 0.3, '<0.3'),
        'Metamielocitos': (0, '0'),
        'Mielocitos': (0, '0'),
        'Linfocitos': (1.5, 7.0, '1.5 - 7.0'),
        'Monocitos': (0, 0.8, '0 - 0.8'),
        'Eosinófilos': (0, 0.8, '0 - 0.8'),
        'Basófilos': (0, '0')
    },
    'perro': {
        'Hematocrito': (0.37, 0.55, '0.37 - 0.55'),
        'Hemoglobina': (120, 180, '120 - 180'),
        'Eritrocitos': (5.5, 8.5, '5.5 - 8.5'),
        'VGM': (60, 77, '60 - 77'),
        'CGMH': (320, 360, '320 - 360'),
        'Reticulocitos': (60, '<60'),
        'RDWc': (20, '<20'),
        'Plaquetas': (200, 600, '200 - 600'),
        'VPM': (3.9, 11.1, '3.9 - 11.1'),
        'Sólidos totales': (60, 75, '60 - 75'),
        'Leucocitos': (6.0, 17.0, '6.0 - 17.0'),
        'Neutrófilos': (3.0, 11.5, '3.0 - 11.5'),
        'Bandas': (0, 0.3, '<0.3'),
        'Metamielocitos': (0, '0'),
        'Mielocitos': (0, '0'),
        'Linfocitos': (1.0, 4.8, '1.0 - 4.8'),
        'Monocitos': (0, 1.4, '0 - 1.4'),
        'Eosinófilos': (0, 0.9, '0 - 0.9'),
        'Basófilos': (0, '0')
    },
    'caballo': {
        'Hematocrito': (0.32, 0.52, '0.32 - 0.52'),
        'Hemoglobina': (111, 190, '111 - 190'),
        'Eritrocitos': (6.5, 12.5, '6.5 - 12.5'),
        'VGM': (34, 58, '34 - 58'),
        'CGMH': (310, 370, '310 - 370'),
        'RDWc': (0, '0'),
        'Plaquetas': (100, 600, '100 - 600'),
        'VPM': (0, '0'),
        'Sólidos totales': (60, 80, '60 - 80'),
        'Fibrinógeno': (2, 4, '2 - 4'),
        'Relación': (20, '<20'),
        'Leucocitos': (5.5, 12.5, '5.5 - 12.5'),
        'Neutrófilos': (2.7, 6.7, '2.7 - 6.7'),
        'Bandas': (0, '0'),
        'Metamielocitos': (0, '0'),
        'Mielocitos': (0, '0'),
        'Linfocitos': (1.5, 7.5, '1.5 - 7.5'),
        'Monocitos': (0, 0.8, '0 - 0.8'),
        'Eosinófilos': (0, 0.9, '0 - 0.9'),
        'Basófilos': (0.0, 0.3, '0.0 - 0.3')
    }
  }

  #Forma basica del pdf
  pdf = PDF(format='A4')
  pdf.add_page()
  pdf.add_font('RedditSans-Regular', '', 'font/RedditSans-Regular.ttf', uni=True)
  
  # Registrar una fuente personalizada
  pdf.add_font('Raleway', '', 'font/Raleway-Medium.ttf', uni=True)
  pdf.add_font('RalewayB', '', 'font/Raleway-Bold.ttf', uni=True)

  ##################Titulo
  hemogramas = {
    'gato': 'HEMOGRAMA GATO',
    'perro': 'HEMOGRAMA PERRO',
    'caballo': 'HEMOGRAMA CABALLO',
    'cachorro': 'HEMOGRAMA CACHORRO'
  }   

  pdf.set_font('RalewayB', '', 12)
  if raza.lower() in hemogramas:
    pdf.cell(w=0, h=15, txt=hemogramas[raza], border=0, ln=1, align='C', fill=0)

  ##################Informacion basica
  pdf.set_font('RalewayB', '', 11)
  pdf.cell(w=90, h=9, txt='Numero de caso: '+numCaso, border=0, ln=0, align='C', fill=0)
  pdf.set_font('Raleway', '', 8)
  pdf.multi_cell(w=0, h=3, txt='Fecha y hora de muestreo: '+fechaMuestreo+'\nFecha de recepcion: '+fechaRecep+'\nFecha de emision de resultado: '+fechaResul, border=0, align='L', fill=0)

  ##################Informacion basica del paciente
  #FILA 1
  pdf.set_fill_color(52, 212, 156)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=35, h=5, txt='Nombre Paciente: ', border='TL', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=59, h=5, txt=nomPaci, border='T', ln=0, align='L', fill=1)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=20, h=5, txt='Raza: ', border='T', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=74, h=5, txt=raza, border='TR', ln=1, align='L', fill=1)

  #FILA 2
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=17, h=5, txt='Edad: ', border='L', ln=0, align='L', fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=77, h=5, txt=edad, border='', ln=0, align='L', fill=0)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=19, h=5, txt='Sexo: ', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='M', border='', ln=0, align='L', fill=0)
  if sexo.lower() in ('m', 'macho'):
      pdf.cell(w=13, h=5, txt='X', border='', ln=0, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='H', border='', ln=0, align='L', fill=0)
  if sexo.lower() in ('h', 'hembra'):
      pdf.cell(w=13, h=5, txt='X', border='', ln=0, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='C', border='', ln=0, align='L', fill=0)
  if castrado == 'Si':
      pdf.cell(w=13, h=5, txt='X', border='R', ln=1, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='R', ln=1, align='L', fill=0)

  #FILA 3
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=37, h=5, txt='Nombre propietario: ', border='L', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=57, h=5, txt=nomProp, border='', ln=0, align='L', fill=1)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=27, h=5, txt='Hospital/MVZ:', border='', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=67, h=5, txt=hospital, border='R', ln=1, align='L', fill=1)

  #Fila 4
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=188, h=5, txt='Anamnesis: ', border='TRLB', ln=1, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=188, h=5, txt=anamnesis, border='LBTR',  align='L', fill=0)

  #FILA 5
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=188, h=5, txt='Tratamiento: ', border='TRLB', ln=1, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=188, h=5, txt=tratamiento, border='LBTR',  align='L', fill=0)

  ##################Informacion del analisis
  pdf.cell(w=0, h=8, ln=1)
  x1 = pdf.get_x()  
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)

  #FILA 1 - TITULOS COLUMNAS
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=44, h=5, txt='Analito', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=44, h=5, txt='Resultados', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=44, h=5, txt='Unidades', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=44, h=5, txt='Limites de referencia', border='LRBT', align='C', ln=1, fill=1)

  
  #FILA 2 - HEMATROCITOS
  limites = parametros_por_raza[raza]

  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Hematocrito', border='LR', align='L', ln=0, fill=0)
  min_hema, max_hema, txt_hema = limites['Hematocrito']
  if float(hematocritoRes)<min_hema or float(hematocritoRes)>max_hema:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=hematocritoRes, border='LR', align='C', ln=0, fill=0)
  if float(hematocritoRes)<min_hema:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(hematocritoRes)>max_hema:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='L/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_hema, border='LR', align='C', ln=1, fill=0)

  #FILA 3 - HEMOGLOBINA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Hemoglobina', border='LR', align='L', ln=0, fill=0)
  if raza.lower() == 'cachorro':
    hemo, txt_hemo = limites['Hemoglobina']
    if float(hemoglobinaRes)!=hemo:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=hemoglobinaRes, border='LR', align='C', ln=0, fill=0)
    if float(hemoglobinaRes)!=hemo:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '!', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_hemo, border='LR', align='C', ln=1, fill=0)
  else:
    min_hemo, max_hemo, txt_hemo = limites['Hemoglobina']
    if float(hemoglobinaRes)<min_hemo or float(hemoglobinaRes)>max_hemo:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=hemoglobinaRes, border='LR', align='C', ln=0, fill=0)
    if float(hemoglobinaRes)<min_hemo:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(hemoglobinaRes)>max_hemo:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_hemo, border='LR', align='C', ln=1, fill=0)

  #FILA 4 - ERITROCITOS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Eritrocitos', border='LR', align='L', ln=0, fill=0)
  min_eri, max_eri, txt_eri = limites['Eritrocitos']
  if float(eritrocitosRes)<min_eri or float(eritrocitosRes)>max_eri:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=eritrocitosRes, border='LR', align='C', ln=0, fill=0)
  if float(eritrocitosRes)<min_eri:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(eritrocitosRes)>max_eri:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u00B9\u00B2/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_eri, border='LR', align='C', ln=1, fill=0)

  #FILA 5 - VGM
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='VGM', border='LR', align='L', ln=0, fill=0)
  vgm = (float(hematocritoRes)*1000)/float(eritrocitosRes)
  min_vgm, max_vgm, txt_vgm = limites['VGM']
  if float(vgm)<min_vgm or float(vgm)>max_vgm:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(vgm)), border='LR', align='C', ln=0, fill=0)
  if float(vgm)<min_vgm:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(vgm)>max_vgm:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='fL', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_vgm, border='LR', align='C', ln=1, fill=0)

  #FILA 6 - CGMH
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='CGMH', border='LR', align='L', ln=0, fill=0)
  cgmh = float(hemoglobinaRes)/float(hematocritoRes)
  if raza.lower() == 'cachorro':
    ucgmh, txt_cgmh = limites['CGMH']
    if float(cgmh)!=ucgmh:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(cgmh)), border='LR', align='C', ln=0, fill=0)
    if float(cgmh)!=ucgmh:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '!', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt= '-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_cgmh, border='LR', align='C', ln=1, fill=0)
  else:
    min_cgmh, max_cgmh, txt_cgmh = limites['CGMH']
    if float(cgmh)<min_cgmh or float(cgmh)>max_cgmh:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(cgmh)), border='LR', align='C', ln=0, fill=0)
    if float(cgmh)<min_cgmh:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(cgmh)>max_cgmh:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_cgmh, border='LR', align='C', ln=1, fill=0)

  #FILA 7 - Reticulocitos
  if raza.lower() != 'caballo':
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=44, h=5, txt='Reticulocitos', border='LR', align='L', ln=0, fill=0)
    ureti, txt_reti = limites['Reticulocitos']
    if float(reticulocitosRes)>ureti:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=reticulocitosRes, border='LR', align='C', ln=0, fill=0)
    if float(reticulocitosRes)>ureti:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_reti, border='LR', align='C', ln=1, fill=0)

  #FILA 8 - RDWc
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='RDWc', border='LRB', align='L', ln=0, fill=0)
  if raza.lower() == 'cachorro':
    min_rdwc, max_rdwc, txt_rdwc = limites['RDWc']
    if float(rdwcRes)<min_rdwc or float(rdwcRes)>max_rdwc:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=rdwcRes, border='LRB', align='C', ln=0, fill=0)
    if float(rdwcRes)>max_rdwc:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    elif float(rdwcRes)<min_rdwc:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_rdwc, border='BLR', align='C', ln=1, fill=0)
  elif raza.lower() == 'caballo':
    urdwc, txt_rdwc = limites['RDWc']
    if float(rdwcRes)!=urdwc:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=rdwcRes, border='LRB', align='C', ln=0, fill=0)
    if float(rdwcRes)!=urdwc:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '!', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_rdwc, border='BLR', align='C', ln=1, fill=0)
  else:
    max_rdwc, txt_rdwc = limites['RDWc']
    if float(rdwcRes)>max_rdwc:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=rdwcRes, border='LRB', align='C', ln=0, fill=0)
    if float(rdwcRes)>max_rdwc:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_rdwc, border='BLR', align='C', ln=1, fill=0)

  #FILA 9 - Plaquetas
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Plaquetas', border='LR', align='L', ln=0, fill=0)
  min_pla, max_pla, txt_pla = limites['Plaquetas']
  if float(plaquetasRes)<min_pla or float(plaquetasRes)>max_pla:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=plaquetasRes, border='LR', align='C', ln=0, fill=0)
  if float(plaquetasRes)<min_pla:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(plaquetasRes)>max_pla:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_pla, border='LR', align='C', ln=1, fill=0)

  #FILA 10 - VPM
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='VPM', border='LBR', align='L', ln=0, fill=0)
  if raza.lower() != 'caballo':
    min_vpm, max_vpm, txt_vpm = limites['VPM']
    if float(vpm)<min_vpm or float(vpm)>max_vpm:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=vpm, border='LBR', align='C', ln=0, fill=0)
    if float(vpm)<min_vpm:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LBR', align='C', ln=0, fill=0)
    elif float(vpm)>max_vpm:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='fL', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt= txt_vpm, border='LBR', align='C', ln=1, fill=0)
  else:
    uvpm, txt_vpm = limites['VPM']
    if float(vpm)!=uvpm:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
      pdf.cell(w=39, h=5, txt=vpm, border='LBR', align='C', ln=0, fill=0)
      if float(vpm)!=uvpm:
        pdf.set_font('RedditSans-Regular', '', 10)
        pdf.cell(w=5, h=5, txt= '!', border='LBR', align='C', ln=0, fill=0)
      else:
        pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
      pdf.set_font('Raleway', '', 10)
      pdf.cell(w=44, h=5, txt='fL', border='LBR', align='C', ln=0, fill=0)
      pdf.cell(w=44, h=5, txt=txt_vpm, border='LBR', align='C', ln=1, fill=0)

  #FILA 11 - Solidos totales
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Sólidos totales', border='LBR', align='L', ln=0, fill=0)
  min_soli, max_soli, txt_soli = limites['Sólidos totales']
  if float(solTotal)<min_soli or float(solTotal)>max_soli:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=solTotal, border='LBR', align='C', ln=0, fill=0)
  if float(solTotal)<min_soli:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LBR', align='C', ln=0, fill=0)
  elif float(solTotal)>max_soli:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='g/L', border='LBR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_soli, border='LBR', align='C', ln=1, fill=0)

  ###Seccion exclusiva de caballo
  #Fibrinógeno
  if raza.lower() == 'caballo':
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=44, h=5, txt='Fibrinógeno', border='LBR', align='L', ln=0, fill=0)
    min_fib, max_fib, txt_fib = limites['Fibrinógeno']
    if float(fibri)<min_fib or float(fibri)>max_fib:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=fibri, border='LBR', align='C', ln=0, fill=0)
    if float(fibri)<min_fib:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LBR', align='C', ln=0, fill=0)
    elif float(fibri)>max_fib:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_fib, border='LBR', align='C', ln=1, fill=0)

   #Relacion
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=44, h=5, txt='Relacion ST/FB', border='LBR', align='L', ln=0, fill=0)
    max_rel, txt_rel = limites['Relación']
    if float(st)>max_rel:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=st, border='LBR', align='C', ln=0, fill=0)
    if float(st)>max_rel:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='g/L', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_rel, border='LBR', align='C', ln=1, fill=0) 
  ###Seccion exclusiva de caballo

  #FILA 12 - Leucocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Leucocitos', border='LR', align='L', ln=0, fill=0)
  min_leu, max_leu, txt_leu = limites['Leucocitos']
  if float(leucocitos)<min_leu or float(leucocitos)>max_leu:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=leucocitos, border='LR', align='C', ln=0, fill=0)
  if float(leucocitos)<min_leu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(leucocitos)>max_leu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_leu, border='LR', align='C', ln=1, fill=0)

  #FILA 13 - Neutrófilos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Neutrófilos', border='LR', align='L', ln=0, fill=0)
  neutrofilosRes = float(leucocitos) * (float(neutrofilos)/100)
  min_neu, max_neu, txt_neu = limites['Neutrófilos']
  if float(neutrofilosRes)<min_neu or float(neutrofilosRes)>max_neu:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(neutrofilosRes)), border='LR', align='C', ln=0, fill=0)
  if float(neutrofilosRes)<min_neu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(neutrofilosRes)>max_neu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_neu, border='LR', align='C', ln=1, fill=0)

  #FILA 14 - Bandas
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Bandas', border='LR', align='L', ln=0, fill=0)
  bandasRes = float(leucocitos) * (float(bandas)/100)
  if raza.lower() != 'caballo':
    min_ban, max_ban, txt_ban = limites['Bandas']
    if float(bandasRes)<min_ban or float(bandasRes)>max_ban:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(bandasRes)), border='LR', align='C', ln=0, fill=0)
    if float(bandasRes)<min_ban:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(bandasRes)>max_ban:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_ban, border='LR', align='C', ln=1, fill=0)
  else:
    uban, txt_ban = limites['Bandas']
    if float(bandasRes)!=uban:
      pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(bandasRes)), border='LR', align='C', ln=0, fill=0)
    if float(bandasRes)!=uban:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '!', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_ban, border='LR', align='C', ln=1, fill=0)

  #FILA 15 - Metamielocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Metamielocitos', border='LR', align='L', ln=0, fill=0)
  metamielocitosRes = float(leucocitos) * (float(metamielocitos)/100)
  umet, txt_met = limites['Metamielocitos']
  if float(metamielocitosRes)!=umet:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(metamielocitosRes)), border='LR', align='C', ln=0, fill=0)
  if float(metamielocitosRes)!=umet:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt='!', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_met, border='LR', align='C', ln=1, fill=0)

  #FILA 16 - Mielocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Mielocitos', border='LR', align='L', ln=0, fill=0)
  mielocitosRes = float(leucocitos) * (float(mielocitos)/100)
  umie, txt_mie = limites['Mielocitos']
  if float(mielocitosRes)!=umie:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(mielocitosRes)), border='LR', align='C', ln=0, fill=0)
  if float(metamielocitosRes)!=umie:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt='!', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_mie, border='LR', align='C', ln=1, fill=0)

  #FILA 17 - Linfocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Linfocitos', border='LR', align='L', ln=0, fill=0)
  linfocitosRes = float(leucocitos) * (float(linfocitos)/100)
  min_lin, max_lin, txt_lin = limites['Linfocitos']
  if float(linfocitosRes)<min_lin or float(linfocitosRes)>max_lin:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(linfocitosRes)), border='LR', align='C', ln=0, fill=0)
  if float(linfocitosRes)<min_lin:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(linfocitosRes)>max_lin:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_lin, border='LR', align='C', ln=1, fill=0)

  #FILA 17 - Monocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Monocitos', border='LR', align='L', ln=0, fill=0)
  monocitosRes = float(leucocitos) * (float(monocitos)/100)
  min_mono, max_mono, txt_mono = limites['Monocitos']
  if float(monocitosRes)<min_mono or float(monocitosRes)>max_mono:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(monocitosRes)), border='LR', align='C', ln=0, fill=0)
  if float(monocitosRes)<min_mono:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(monocitosRes)>max_mono:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_mono, border='LR', align='C', ln=1, fill=0)

  #FILA 18 - Eosinófilos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Eosinófilos', border='LR', align='L', ln=0, fill=0)
  eosinofilosRes = float(leucocitos) * (float(eosinofilos)/100)
  min_eos, max_eos, txt_eos = limites['Eosinófilos']
  if float(eosinofilosRes)<min_eos or float(eosinofilosRes)>max_eos:
      pdf.set_font('RalewayB', '', 11)
  else:
      pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(eosinofilosRes)), border='LR', align='C', ln=0, fill=0)
  if float(eosinofilosRes)<min_eos:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(eosinofilosRes)>max_eos:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_eos, border='LR', align='C', ln=1, fill=0)


  #FILA 19 - Basófilos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Basófilos', border='LRB', align='L', ln=0, fill=0)
  basofilosRes= float(leucocitos) * (float(basofilos)/100)
  if raza.lower() != 'caballo':
    ubas, txt_bas = limites['Basófilos']
    if float(basofilosRes)!=ubas:
        pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(basofilosRes)), border='LBR', align='C', ln=0, fill=0)
    if float(basofilosRes)!=ubas:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt='!', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt='Raros', border='BLR', align='C', ln=1, fill=0)
  else:
    min_bas, max_bas, txt_bas = limites['Basófilos']
    if float(basofilosRes)<min_bas or float(basofilosRes)>max_bas:
      pdf.set_font('RalewayB', '', 11)
    else:
        pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(basofilosRes)), border='LBR', align='C', ln=0, fill=0)
    if float(basofilosRes)<min_bas:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt='↓', border='LR', align='C', ln=0, fill=0)
    elif float(basofilosRes)>max_bas:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt='↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '-', border='LR', align='C', ln=0, fill=0)
    #pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=44, h=5, txt='X10\u2079/L', border='LBR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_bas, border='BLR', align='C', ln=1, fill=0)


  #FILA 20 - Morfología de eritrocitos:
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Morfología de eritrocitos:', border='LB', align='L', ln=0, fill=0)
  pdf.cell(w=132, h=5, txt=morfoEri, border='RB', align='L', ln=1, fill=0)

  #FILA 21 - Morfología de leucocitos
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=44, h=5, txt='Morfología de leucocitos:', border='LB', align='L', ln=0, fill=0)
  pdf.cell(w=132, h=5, txt=morfoLeu, border='RB', align='L', ln=1, fill=0)

  #FILA 22 - Otros hallazgos
  if otros!='':
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=44, h=5, txt='Otros hallazgos:', border='LB', align='L', ln=0, fill=0)
    pdf.cell(w=132, h=5, txt=otros, border='RB', align='L', ln=1, fill=0)

  #FILA 23 - Interpretacion
  if interpretacion!='':
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=176, h=5, txt='Interpretacion:', border='LR', align='L', ln=1, fill=0)
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.multi_cell(w=176, h=5, txt=interpretacion, border='RBL', align='L', fill=0)

  #FILA 24 - Comentarios extras
  if comExtras!='':
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.set_font('RalewayB', '', 10)
      pdf.set_text_color(0, 0, 0)
      pdf.cell(w=176, h=5, txt='Comentarios extras:', border='LR', align='L', ln=1, fill=0)
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.multi_cell(w=176, h=5, txt=comExtras, border='RBL', align='L', fill=0)

  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.image(img, x1+55, y1+10, 75, 30)


  ##################Creacion del pdf
  pdfName = numCaso+' '+nomPaci+'.pdf'
  pdf.output(pdfName, 'F')
  if sys.platform == "win32":
      subprocess.run(f'start "" "{pdfName}"', shell=True)
  elif sys.platform == "darwin":
      subprocess.run(['open', pdfName])
  elif sys.platform == "linux":
      subprocess.run(['xdg-open', pdfName])



