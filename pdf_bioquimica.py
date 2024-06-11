from fpdf import FPDF
import subprocess
import sys
# -*- coding: utf-8 -*-

def generar_bioquimica(valores):

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

  parametros_por_raza = {
    'caballo': {
        'Glucosa': (3.4, 6.2, '3.4 – 6.2'),
        'Urea': (4.1, 7.6, '4.1 – 7.6'),
        'Creatinina': (88, 156, '88 – 156'),
        'Colesterol': (1.81, 4.65, '1.81 – 4.65'),
        'total': (14.0, 54.0, '14.0 – 54.0'),
        'conjugada': (6.0, 12.0, '6.0 – 12.0'),
        'no conjugada': (4.0, 44.0, '4.0 – 44.0'),
        'AST': (0, 450, '<450'),
        'GGT': (0, 22, '<22'),
        'FA': (0, 453, '<453'),
        'CK': (0, 425, '<425'),
        'Proteínas': (53, 71, '53 – 71'),
        'Albúmina': (31, 39, '31 – 39'),
        'Globulinas': (20, 35, '20 – 35'),
        'AG': (0.89, 1.65, '0.89 – 1.65'),
        'Calcio': (2.79, 3.22, '2.79 – 3.22'),
        'Fósforo': (0.89, 1.77, '0.89 – 1.77'),
        'Potasio': (3.4, 5.0, '3.4 – 5.0'),
        'Sodio': (132, 141, '132 – 141'),
        'Cloro': (98, 105, '98 – 105'),
        'Bicarbonato': (27, 34, '27 – 34'),
        'Anion': (4, 13, '4 – 13'),
        'iones': (34, 43, '34 – 43')
    },
    'gato': {
      'Glucosa': (3.8, 7.9, '3.8 – 7.9'),
      'Urea': (4.1, 10.8, '4.1 – 10.8'),
      'Creatinina': (56, 176, '56 – 176'),
      'Colesterol': (1.78, 3.87, '1.78 – 3.87'),
      'Triglicéridos': (0.6, 1.2, '0.6 – 1.2'),
      'total': (0, 6.8, '<6.8'),
      'conjugada': (0, 0, '–'),
      'no conjugada': (0, 0, '–'),
      'ALT': (0, 72, '<72'),
      'AST': (0, 61, '<61'),
      'FA': (0, 107, '<107'),
      'GGT': (0, 5, '<5'),
      'CK': (0, 277, '<277'),
      'Amilasa': (0, 1800, '<1800'),
      'Lipasa': (0, 300, '<300'),
      'Proteínas': (59, 81, '59 – 81'),
      'Albúmina': (26, 38, '26 – 38'),
      'Globulinas': (29, 47, '29 – 47'),
      'AG': (0.58, 1.16, '0.58 – 1.16'),
      'Calcio': (2.05, 2.76, '2.05 – 2.76'),
      'Fósforo': (0.96, 1.96, '0.96 – 1.96'),
      'Potasio': (3.6, 5.3, '3.6 – 5.3'),
      'Sodio': (143, 158, '143 – 158'),
      'Cloro': (110, 125, '110 – 125'),
      'Bicarbonato': (14, 24, '14 – 24'),
      'Anion': (10, 27, '10 – 27'),
      'iones': (30, 40, '30 – 40'),
      'Osmolalidad': (290, 330, '290 – 330')
    },
    'perro': {
      'Glucosa': (3.88, 6.88, '3.88 – 6.88'),
      'Urea': (2.1, 7.9, '2.1 – 7.9'),
      'Creatinina': (60, 130, '60 – 130'),
      'Colesterol': (2.85, 7.76, '2.85 – 7.76'),
      'Triglicéridos': (0.6, 1.2, '0.6 – 1.2'),
      'total': (0, 5.2, '<5.2'),
      'conjugada': (0, 0, '–'),
      'no conjugada': (0, 0, '–'),
      'ALT': (0, 70, '<70'),
      'AST': (0, 55, '<55'),
      'FA': (0, 189, '<189'),
      'CK': (0, 213, '<213'),
      'Amilasa': (0, 1110, '<1110'),
      'Lipasa': (0, 300, '<300'),
      'Proteínas': (56, 75, '56 – 75'),
      'Albúmina': (29, 40, '29 – 40'),
      'Globulinas': (23, 39, '23 – 39'),
      'AG': (0.78, 1.46, '0.78 – 1.46'),
      'Calcio': (2.17, 2.94, '2.17 – 2.94'),
      'Fósforo': (0.80, 1.80, '0.80 – 1.80'),
      'Potasio': (3.6, 5.3, '3.6 – 5.3'),
      'Sodio': (143, 158, '143 – 158'),
      'Cloro': (110, 125, '110 – 125'),
      'Bicarbonato': (17, 25, '17 – 25'),
      'Anion': (12, 24, '12 – 24'),
      'iones': (30, 40, '30 – 40'),
      'Osmolalidad': (285, 320, '285 – 320')
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
  bioquimica = {
    'gato': 'BIOQUIMICA GATO',
    'perro': 'BIOQUIMICA PERRO',
    'caballo': 'BIOQUIMICA CABALLO',
  }   

  pdf.set_font('RalewayB', '', 12)
  if valores['datos_paciente_raza'].lower() in bioquimica:
    pdf.cell(w=0, h=15, txt=bioquimica[valores['datos_paciente_raza']], border=0, ln=1, align='C', fill=0)

  ##################Informacion basica
  pdf.set_font('RalewayB', '', 11)
  pdf.cell(w=90, h=9, txt='Numero de caso: '+valores['datos_caso'], border=0, ln=0, align='C', fill=0)
  pdf.set_font('Raleway', '', 8)
  pdf.multi_cell(w=0, h=3, txt='Fecha y hora de muestreo: '+valores['fecha_muestreo']+'\nFecha de recepcion: '+valores['fecha_recepcion']+'\nFecha de emision de resultado: '+valores['fecha_emision'], border=0, align='L', fill=0)

  ##################Informacion basica del paciente
  #FILA 1
  pdf.set_fill_color(52, 212, 156)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=35, h=5, txt='Nombre Paciente: ', border='TL', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=59, h=5, txt=valores['datos_paciente_nombre'], border='T', ln=0, align='L', fill=1)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=20, h=5, txt='Raza: ', border='T', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=74, h=5, txt=valores['datos_paciente_raza'], border='TR', ln=1, align='L', fill=1)

  #FILA 2
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=17, h=5, txt='Edad: ', border='L', ln=0, align='L', fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=77, h=5, txt=valores['datos_paciente_edad'], border='', ln=0, align='L', fill=0)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=19, h=5, txt='Sexo: ', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='M', border='', ln=0, align='L', fill=0)
  if valores['datos_paciente_sexo'].lower() in ('m', 'macho'):
      pdf.cell(w=13, h=5, txt='X', border='', ln=0, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='H', border='', ln=0, align='L', fill=0)
  if valores['datos_paciente_sexo'].lower() in ('h', 'hembra'):
      pdf.cell(w=13, h=5, txt='X', border='', ln=0, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='', ln=0, align='L', fill=0)
  pdf.cell(w=12, h=5, txt='C', border='', ln=0, align='L', fill=0)
  if valores['datos_paciente_castrado'] == 'Si':
      pdf.cell(w=13, h=5, txt='X', border='R', ln=1, align='L', fill=0)
  else:
      pdf.cell(w=13, h=5, txt='', border='R', ln=1, align='L', fill=0)

  #FILA 3
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=37, h=5, txt='Nombre propietario: ', border='L', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=57, h=5, txt=valores['datos_paciente_propietario'], border='', ln=0, align='L', fill=1)
  pdf.set_font('RalewayB', '', 10)
  pdf.cell(w=27, h=5, txt='Hospital/MVZ:', border='', ln=0, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=67, h=5, txt=valores['datos_paciente_hospital'], border='R', ln=1, align='L', fill=1)

  #Fila 4
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=188, h=5, txt='Anamnesis: ', border='TRLB', ln=1, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=188, h=5, txt=valores['datos_paciente_anamnesis'], border='LBTR',  align='L', fill=0)

  #FILA 5
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=188, h=5, txt='Tratamiento: ', border='TRLB', ln=1, align='L', fill=1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=188, h=5, txt=valores['datos_paciente_tratamiento'], border='LBTR',  align='L', fill=0)

  ##################Informacion del analisis
  pdf.cell(w=0, h=8, ln=1)
  x1 = pdf.get_x()  
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)

  #FILA 1 - TITULOS COLUMNAS
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=64, h=5, txt='Analito', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=44, h=5, txt='Resultados', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=24, h=5, txt='Unidades', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=44, h=5, txt='Limites de referencia', border='LRBT', align='C', ln=1, fill=1)

  limites = parametros_por_raza[valores['datos_paciente_raza']]

  #FILA 2 - GLUCOSA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Glucosa', border='LR', align='L', ln=0, fill=0)
  min_glu, max_glu, txt_glu = limites['Glucosa']
  if float(valores['datos_analisis_glucosa'])<min_glu or float(valores['datos_analisis_glucosa'])>max_glu:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_glucosa'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_glucosa'])<min_glu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_glucosa'])>max_glu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_glu, border='LR', align='C', ln=1, fill=0)

  #FILA 3 - UREA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Urea', border='LR', align='L', ln=0, fill=0)
  min_ur, max_ur, txt_ur = limites['Urea']
  if float(valores['datos_analisis_urea'])<min_ur or float(valores['datos_analisis_urea'])>max_ur:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_urea'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_urea'])<min_ur:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_urea'])>max_ur:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ur, border='LR', align='C', ln=1, fill=0)

  #FILA 4 - CREATININA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Creatinina', border='LR', align='L', ln=0, fill=0)
  min_crea, max_crea, txt_crea = limites['Creatinina']
  if float(valores['datos_analisis_creatinina'])<min_crea or float(valores['datos_analisis_creatinina'])>max_crea:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_creatinina'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_creatinina'])<min_crea:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_creatinina'])>max_crea:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_crea, border='LR', align='C', ln=1, fill=0)

  #FILA 4 - COLESTEROL
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Colesterol', border='LR', align='L', ln=0, fill=0)
  min_col, max_col, txt_col = limites['Colesterol']
  if float(valores['datos_analisis_colesterol'])<min_col or float(valores['datos_analisis_colesterol'])>max_col:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_colesterol'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_colesterol'])<min_col:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_colesterol'])>max_col:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_col, border='LR', align='C', ln=1, fill=0)

  if(valores['datos_paciente_raza'].lower()!='caballo'):
    #FILA 5 - TRIGLICERIDOS
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Triglicéridos', border='LR', align='L', ln=0, fill=0)
    min_tri, max_tri, txt_tri = limites['Triglicéridos']
    if float(valores['datos_analisis_trigliceridos'])<min_tri or float(valores['datos_analisis_trigliceridos'])>max_tri:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=valores['datos_analisis_trigliceridos'], border='LR', align='C', ln=0, fill=0)
    if float(valores['datos_analisis_trigliceridos'])<min_tri:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(valores['datos_analisis_trigliceridos'])>max_tri:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_tri, border='LR', align='C', ln=1, fill=0)

  #FILA 6 - BILIRRUBINA TOTAL
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Bilirrubina total', border='LR', align='L', ln=0, fill=0)
  min_btot, max_btot, txt_btot = limites['total']
  if float(valores['datos_analisis_bilirrubina_total'])<min_btot or float(valores['datos_analisis_bilirrubina_total'])>max_btot:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_bilirrubina_total'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_bilirrubina_total'])<min_btot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_bilirrubina_total'])>max_btot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_btot, border='LR', align='C', ln=1, fill=0)

  #FILA 7 - BILIRRUBINA CONJUGADA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Bilirrubina conjugada', border='LR', align='L', ln=0, fill=0)
  min_con, max_con, txt_con = limites['conjugada']
  if float(valores['datos_analisis_bilirrubina_conjugada'])<min_con or float(valores['datos_analisis_bilirrubina_conjugada'])>max_con:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_bilirrubina_conjugada'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_bilirrubina_conjugada'])<min_con:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_bilirrubina_conjugada'])>max_con:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_con, border='LR', align='C', ln=1, fill=0)

  #FILA 9 - BILIRRUBINA NO CONJUGADA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Bilirrubina no conjugada', border='LR', align='L', ln=0, fill=0)
  min_ncon, max_ncon, txt_ncon = limites['no conjugada']
  noConjugada = float(valores['datos_analisis_bilirrubina_total']) - float(valores['datos_analisis_bilirrubina_conjugada'])
  if float(noConjugada)<min_ncon or float(noConjugada)>max_ncon:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(noConjugada)), border='LR', align='C', ln=0, fill=0)
  if float(noConjugada)<min_ncon:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(noConjugada)>max_ncon:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ncon, border='LR', align='C', ln=1, fill=0)

  if (valores['datos_paciente_raza'].lower() != 'caballo'):
    #FILA 10 - ALANINAMINO TRANSFERASA ALT
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Alaninamino transferasa (ALT)', border='LR', align='L', ln=0, fill=0)
    min_alt, max_ALT, txt_ALT = limites['ALT']
    if float(valores['datos_analisis_alaninamino_transferasa'])<min_alt or float(valores['datos_analisis_alaninamino_transferasa'])>max_ALT:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=valores['datos_analisis_alaninamino_transferasa'], border='LR', align='C', ln=0, fill=0)
    if float(valores['datos_analisis_alaninamino_transferasa'])<min_alt:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(valores['datos_analisis_alaninamino_transferasa'])>max_ALT:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_ALT, border='LR', align='C', ln=1, fill=0)

  #FILA 11 - ASPARTATOAMINO TRANSFERASA (AST)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Aspartatoamino transferasa (AST)', border='LR', align='L', ln=0, fill=0)
  min_ast, max_ast, txt_ast = limites['AST']
  if float(valores['datos_analisis_aspartatoamino_transferasa'])<min_ast or float(valores['datos_analisis_aspartatoamino_transferasa'])>max_ast:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_aspartatoamino_transferasa'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_aspartatoamino_transferasa'])<min_ast:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_aspartatoamino_transferasa'])>max_ast:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ast, border='LR', align='C', ln=1, fill=0)

  #FILA 12 - FOSFATASA ALCALINA (FA)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Fosfatasa alcalina (FA)', border='LR', align='L', ln=0, fill=0)
  min_fa, max_fa, txt_fa = limites['FA']
  if float(valores['datos_analisis_fosfatasa_alcalina'])<min_fa or float(valores['datos_analisis_fosfatasa_alcalina'])>max_fa:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_fosfatasa_alcalina'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_fosfatasa_alcalina'])<min_fa:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_fosfatasa_alcalina'])>max_fa:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_fa, border='LR', align='C', ln=1, fill=0)

  if (valores['datos_paciente_raza'].lower() != 'perro'):
    #FILA 13 - GAMMAGLUTAMIL TRANSFERASA (GGT)
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Gammaglutamil transferasa (GGT)', border='LR', align='L', ln=0, fill=0)
    min_ggt, max_ggt, txt_ggt = limites['GGT']
    if float(valores['datos_analisis_ggt'])<min_ggt or float(valores['datos_analisis_ggt'])>max_ggt:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=valores['datos_analisis_ggt'], border='LR', align='C', ln=0, fill=0)
    if float(valores['datos_analisis_ggt'])<min_ggt:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(valores['datos_analisis_ggt'])>max_ggt:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_ggt, border='LR', align='C', ln=1, fill=0)

  #FILA 14 - CREATINCINASA CK
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Creatincinasa (CK)', border='LR', align='L', ln=0, fill=0)
  min_ck, max_ck, txt_ck = limites['CK']
  if float(valores['datos_analisis_creatincinasa'])<min_ck or float(valores['datos_analisis_creatincinasa'])>max_ck:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_creatincinasa'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_creatincinasa'])<min_ck:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_creatincinasa'])>max_ck:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ck, border='LR', align='C', ln=1, fill=0)

  if (valores['datos_paciente_raza'].lower() != 'caballo'):
    #FILA 15 - AMILASA
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Amilasa', border='LR', align='L', ln=0, fill=0)
    min_ami, max_ami, txt_ami = limites['Amilasa']
    if float(valores['datos_analisis_amilasa'])<min_ami or float(valores['datos_analisis_amilasa'])>max_ami:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=valores['datos_analisis_amilasa'], border='LR', align='C', ln=0, fill=0)
    if float(valores['datos_analisis_amilasa'])<min_ami:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(valores['datos_analisis_amilasa'])>max_ami:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_ami, border='LR', align='C', ln=1, fill=0)

    #FILA 16 - LIPASA
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Lipasa', border='LR', align='L', ln=0, fill=0)
    min_lip, max_lip, txt_lip = limites['Lipasa']
    if float(valores['datos_analisis_lipasa'])<min_lip or float(valores['datos_analisis_lipasa'])>max_lip:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=valores['datos_analisis_lipasa'], border='LR', align='C', ln=0, fill=0)
    if float(valores['datos_analisis_lipasa'])<min_lip:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
    elif float(valores['datos_analisis_lipasa'])>max_lip:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='U/L', border='LR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_lip, border='LR', align='C', ln=1, fill=0)

  #FILA 17 - PROTEINAS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Proteinas totales', border='LR', align='L', ln=0, fill=0)
  min_prot, max_prot, txt_prot = limites['Proteínas']
  if float(valores['datos_analisis_proteinas_totales'])<min_prot or float(valores['datos_analisis_proteinas_totales'])>max_prot:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_proteinas_totales'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_proteinas_totales'])<min_prot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_proteinas_totales'])>max_prot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_prot, border='LR', align='C', ln=1, fill=0)

  #FILA 18 - ALBUMINA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Albúmina', border='LR', align='L', ln=0, fill=0)
  min_albu, max_albu, txt_albu = limites['Albúmina']
  if float(valores['datos_analisis_albumina'])<min_albu or float(valores['datos_analisis_albumina'])>max_albu:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_albumina'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_albumina'])<min_albu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_albumina'])>max_albu:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_albu, border='LR', align='C', ln=1, fill=0)

  #FILA 19 - GLOBULINAS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Globulina calculada', border='LR', align='L', ln=0, fill=0)
  min_glo, max_glo, txt_glo = limites['Globulinas']
  globulinas = float(valores['datos_analisis_proteinas_totales']) - float(valores['datos_analisis_albumina'])
  if globulinas<min_glo or globulinas>max_glo:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(globulinas)), border='LR', align='C', ln=0, fill=0)
  if globulinas<min_glo:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif globulinas>max_glo:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='g/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_glo, border='LR', align='C', ln=1, fill=0)

  #FILA 20 - RELACION A/G
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Relacion A/G', border='LR', align='L', ln=0, fill=0)
  min_rel, max_rel, txt_rel = limites['AG']
  relacionAG = float(valores['datos_analisis_albumina'])/globulinas
  if relacionAG<min_rel or relacionAG>max_rel:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(relacionAG)), border='LR', align='C', ln=0, fill=0)
  if relacionAG<min_rel:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif relacionAG>max_rel:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_rel, border='LR', align='C', ln=1, fill=0)

  #FILA 21 - CALCIO TOTAL
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Calcio total', border='LR', align='L', ln=0, fill=0)
  min_cal, max_cal, txt_cal = limites['Calcio']
  if float(valores['datos_analisis_calcio_total'])<min_cal or float(valores['datos_analisis_calcio_total'])>max_cal:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_calcio_total'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_calcio_total'])<min_cal:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_calcio_total'])>max_cal:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_cal, border='LR', align='C', ln=1, fill=0)

  #FILA 22 - FOSFORO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Fosforo', border='LR', align='L', ln=0, fill=0)
  min_fos, max_fos, txt_fos = limites['Fósforo']
  if float(valores['datos_analisis_fosforo'])<min_fos or float(valores['datos_analisis_fosforo'])>max_fos:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_fosforo'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_fosforo'])<min_fos:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_fosforo'])>max_fos:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_fos, border='LR', align='C', ln=1, fill=0)

  #FILA 23 - POTASIO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Potasio', border='LR', align='L', ln=0, fill=0)
  min_pot, max_pot, txt_pot = limites['Potasio']
  if float(valores['datos_analisis_potasio'])<min_pot or float(valores['datos_analisis_potasio'])>max_pot:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_potasio'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_potasio'])<min_pot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_potasio'])>max_pot:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_pot, border='LR', align='C', ln=1, fill=0)

  #FILA 24 - SODIO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Sodio', border='LR', align='L', ln=0, fill=0)
  min_sod, max_sod, txt_sod = limites['Sodio']
  if float(valores['datos_analisis_sodio'])<min_sod or float(valores['datos_analisis_sodio'])>max_sod:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_sodio'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_sodio'])<min_sod:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_sodio'])>max_sod:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_sod, border='LR', align='C', ln=1, fill=0)

  #FILA 25 - CLORO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Cloro', border='LR', align='L', ln=0, fill=0)
  min_clo, max_clo, txt_clo = limites['Cloro']
  if float(valores['datos_analisis_cloro'])<min_clo or float(valores['datos_analisis_cloro'])>max_clo:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_cloro'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_cloro'])<min_clo:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_cloro'])>max_clo:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_clo, border='LR', align='C', ln=1, fill=0)

  #FILA 26 - BICARBONATO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Bicarbonato', border='LR', align='L', ln=0, fill=0)
  min_bic, max_bic, txt_bic = limites['Bicarbonato']
  if float(valores['datos_analisis_bicarbonato'])<min_bic or float(valores['datos_analisis_bicarbonato'])>max_bic:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=valores['datos_analisis_bicarbonato'], border='LR', align='C', ln=0, fill=0)
  if float(valores['datos_analisis_bicarbonato'])<min_bic:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif float(valores['datos_analisis_bicarbonato'])>max_bic:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_bic, border='LR', align='C', ln=1, fill=0)

  #FILA 27 - ANION GAP
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Anion gap calculado', border='LR', align='L', ln=0, fill=0)
  min_ani, max_ani, txt_ani = limites['Anion']
  anion = (float(valores['datos_analisis_sodio'])+float(valores['datos_analisis_potasio'])) - (float(valores['datos_analisis_cloro'])+float(valores['datos_analisis_bicarbonato']))
  if anion<min_ani or anion>max_ani:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(anion)), border='LR', align='C', ln=0, fill=0)
  if anion<min_ani:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border='LR', align='C', ln=0, fill=0)
  elif anion>max_ani:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border='LR', align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border='LR', align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border='LR', align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ani, border='LR', align='C', ln=1, fill=0)

  #FILA 28 - DIFERENCIA DE IONES
  if(valores['datos_paciente_raza'].lower()=='caballo'):
    bordes = 'LRB'
  else:
    bordes = "LR"
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=64, h=5, txt='Diferencia de iones fuertes calculada', border=bordes, align='L', ln=0, fill=0)
  min_ion, max_ion, txt_ion = limites['iones']
  ion = (float(valores['datos_analisis_sodio'])-float(valores['datos_analisis_cloro']))
  if ion<min_ion or ion>max_ion:
    pdf.set_font('RalewayB', '', 11)
  else:
    pdf.set_font('Raleway', '', 10)
  pdf.cell(w=39, h=5, txt=str("{:.2f}".format(ion)), border=bordes, align='C', ln=0, fill=0)
  if ion<min_ion:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↓', border=bordes, align='C', ln=0, fill=0)
  elif ion>max_ion:
    pdf.set_font('RedditSans-Regular', '', 10)
    pdf.cell(w=5, h=5, txt= '↑', border=bordes, align='C', ln=0, fill=0)
  else:
    pdf.cell(w=5, h=5, txt='-', border=bordes, align='C', ln=0, fill=0)
  pdf.set_font('Raleway', '', 10)
  pdf.cell(w=24, h=5, txt='mmol/L', border=bordes, align='C', ln=0, fill=0)
  pdf.cell(w=44, h=5, txt=txt_ion, border=bordes, align='C', ln=1, fill=0)

  if(valores['datos_paciente_raza'].lower()!='caballo'):
    #FILA 29 - OSMOLALIDAD
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=64, h=5, txt='Osmolalidad calculada', border='LBR', align='L', ln=0, fill=0)
    min_osmo, max_osmo, txt_osmo = limites['Osmolalidad']
    osmo = (1.86*float(valores['datos_analisis_sodio']))+float(valores['datos_analisis_glucosa'])+float(valores['datos_analisis_urea'])
    if osmo<min_osmo or osmo>max_osmo:
      pdf.set_font('RalewayB', '', 11)
    else:
      pdf.set_font('Raleway', '', 10)
    pdf.cell(w=39, h=5, txt=str("{:.2f}".format(osmo)), border='LBR', align='C', ln=0, fill=0)
    if osmo<min_osmo:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↓', border='LBR', align='C', ln=0, fill=0)
    elif osmo>max_osmo:
      pdf.set_font('RedditSans-Regular', '', 10)
      pdf.cell(w=5, h=5, txt= '↑', border='LBR', align='C', ln=0, fill=0)
    else:
      pdf.cell(w=5, h=5, txt='-', border='LBR', align='C', ln=0, fill=0)
    pdf.set_font('Raleway', '', 10)
    pdf.cell(w=24, h=5, txt='mmol/L', border='BLR', align='C', ln=0, fill=0)
    pdf.cell(w=44, h=5, txt=txt_osmo, border='LRB', align='C', ln=1, fill=0)

  #FILA 30 - OTROS HALLAZGOS
  if valores['datos_analisis_otros_hallazgos']!='':
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.set_font('RalewayB', '', 10)
      pdf.set_text_color(0, 0, 0)
      pdf.cell(w=176, h=5, txt='Otros hallazgos:', border='LR', align='L', ln=1, fill=0)
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.multi_cell(w=176, h=5, txt=valores['datos_analisis_otros_hallazgos'], border='RBL', align='L', fill=0)

  #FILA 31 - INTERPRETACIONES
  if valores['datos_analisis_interpretaciones']!='':
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.set_font('RalewayB', '', 10)
      pdf.set_text_color(0, 0, 0)
      pdf.cell(w=176, h=5, txt='Interpretaciones:', border='LR', align='L', ln=1, fill=0)
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.multi_cell(w=176, h=5, txt=valores['datos_analisis_interpretaciones'], border='RBL', align='L', fill=0)

  #FILA 30 - COMENTARIOS EXTRA
  if valores['datos_analisis_comentarios']!='':
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.set_font('RalewayB', '', 10)
      pdf.set_text_color(0, 0, 0)
      pdf.cell(w=176, h=5, txt='Comentarios extra:', border='LR', align='L', ln=1, fill=0)
      y1 = pdf.get_y()
      pdf.set_xy(x1+6, y1)
      pdf.multi_cell(w=176, h=5, txt=valores['datos_analisis_comentarios'], border='RBL', align='L', fill=0)

  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.image(valores['firma_path'], x1+55, y1+10, 75, 30)








  ##################Creacion del pdf
  pdfName = valores['datos_caso']+' '+valores['datos_paciente_nombre']+'.pdf'
  pdf.output(pdfName, 'F')
  if sys.platform == "win32":
      subprocess.run(f'start "" "{pdfName}"', shell=True)
  elif sys.platform == "darwin":
      subprocess.run(['open', pdfName])
  elif sys.platform == "linux":
      subprocess.run(['xdg-open', pdfName])
