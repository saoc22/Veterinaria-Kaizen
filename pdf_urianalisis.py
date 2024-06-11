from fpdf import FPDF
import subprocess
import sys
# -*- coding: utf-8 -*-

def generar_urianalisis(valores):

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
  obtencion = valores.get("datos_analisis_metodo_de_obtencion", "")
  liquidos = valores.get("datos_analisis_aporte_previo_de_liquidos", "")
  apariencia = valores.get("datos_analisis_apariencia", "")
  color = valores.get("datos_analisis_color", "")
  densidad = valores.get("datos_analisis_densidad", "")
  ph = valores.get("datos_analisis_ph", "")
  proteinas = valores.get("datos_analisis_proteinas", "")
  glucosa = valores.get("datos_analisis_glucosa", "")
  cetonas = valores.get("datos_analisis_cetonas", "")
  bilirrubina = valores.get("datos_analisis_bilirrubina", "")
  sangre = valores.get("datos_analisis_sangre_hg", "")
  eritrocitos = valores.get("datos_analisis_eritrocitos", "")
  leucocitos = valores.get("datos_analisis_leucocitos", "")
  renales = valores.get("datos_analisis_celulas_renales", "")
  transitorias = valores.get("datos_analisis_celulas_transitorias", "")
  escamosas = valores.get("datos_analisis_celulas_escamosas", "")
  cilindros = valores.get("datos_analisis_cilindros", "")
  cristales = valores.get("datos_analisis_cristales", "")
  bacterias = valores.get("datos_analisis_bacterias", "")
  lipidos = valores.get("datos_analisis_lipidos", "")
  otros = valores.get("datos_analisis_otros", "")
  interpretacion = valores.get("datos_analisis_interpretacion", "")
  comentarios = valores.get("datos_analisis_comentarios", "")
  img = valores.get("firma_path", "")

  #Forma basica del pdf
  pdf = PDF(format='A4')
  pdf.add_page()
  pdf.add_font('RedditSans-Regular', '', 'font/RedditSans-Regular.ttf', uni=True)
  
  # Registrar una fuente personalizada
  pdf.add_font('Raleway', '', 'font/Raleway-Medium.ttf', uni=True)
  pdf.add_font('RalewayB', '', 'font/Raleway-Bold.ttf', uni=True)

  pdf.set_font('RalewayB', '', 12)
  pdf.cell(w=0, h=15, txt='URIANALISIS', border=0, ln=1, align='C', fill=0)

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

  #FILA 1 - OBTENCION
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=44, h=5, txt='Metodo de obtencion', border='LRBT', align='L', ln=0, fill=1)
  pdf.cell(w=22, h=5, txt='Miccion', border='LRBT', align='C', ln=0, fill=1)
  if obtencion == 'miccion':
    pdf.cell(w=11, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=11, h=5, txt=' ', border='LRBT', align='C', ln=0, fill=1)
  
  pdf.cell(w=22, h=5, txt='Cateterismo', border='LRBT', align='C', ln=0, fill=1)
  if obtencion == 'catete':
    pdf.cell(w=11, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=11, h=5, txt=' ', border='LRBT', align='C', ln=0, fill=1)

  pdf.cell(w=22, h=5, txt='Cistocentesis ', border='LRBT', align='C', ln=0, fill=1)
  if obtencion == 'Cisco':
    pdf.cell(w=11, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=11, h=5, txt=' ', border='LRBT', align='C', ln=0, fill=1)

  pdf.cell(w=22, h=5, txt='NR', border='LRBT', align='C', ln=0, fill=1)
  if obtencion == 'NR':
    pdf.cell(w=11, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=11, h=5, txt=' ', border='LRBT', align='C', ln=1, fill=1)
  
  #FILA 2 - LIQUIDOS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=56, h=5, txt='Aporte previo de liquidos', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=30, h=5, txt='Si', border='LRBT', align='C', ln=0, fill=1)
  if liquidos == 'si':
    pdf.cell(w=10, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=10, h=5, txt=' ', border='LRBT', align='C', ln=0, fill=1)
  
  pdf.cell(w=30, h=5, txt='No', border='LRBT', align='C', ln=0, fill=1)
  if liquidos == 'no':
    pdf.cell(w=10, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=10, h=5, txt=' ', border='LRBT', align='C', ln=0, fill=1)

  pdf.cell(w=30, h=5, txt='NR ', border='LRBT', align='C', ln=0, fill=1)
  if liquidos == 'NR':
    pdf.cell(w=10, h=5, txt='X', border='LRBT', align='C', ln=0, fill=1)
  else:
    pdf.cell(w=10, h=5, txt=' ', border='LRBT', align='C', ln=1, fill=1)

  #FILA 3 - TITULOS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=78, h=5, txt='EXAMEN FISICO', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=98, h=5, txt='EXAMEN MICROSCOPICO', border='LRBT', align='C', ln=1, fill=1)

  #FILA 4 - APARIENCIA/ERITROCITOS
  #APARIENCIA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=30, h=5, txt='Apariencia', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=48, h=5, txt=apariencia, border='R', align='C', ln=0, fill=0)

  #ERITROCITOS
  pdf.cell(w=39, h=5, txt='Eritrocitos', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=eritrocitos, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo400X', border='R', align='L', ln=1, fill=0)

  #FILA 5 - COLOR/LEUCOCITOS
  #COLOR
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=30, h=5, txt='Color', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=48, h=5, txt=color, border='R', align='C', ln=0, fill=0)

  #LEUCOCITOS
  pdf.cell(w=39, h=5, txt='Leucocitos', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=leucocitos, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo400X', border='R', align='L', ln=1, fill=0)

  #FILA 6 - DENSIDAD/RENALES
  #DENSIDAD
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=30, h=5, txt='Densidad', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=48, h=5, txt=densidad, border='R', align='C', ln=0, fill=0)

  #RENALES
  pdf.cell(w=39, h=5, txt='Renales', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=renales, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo400X', border='R', align='L', ln=1, fill=0)

  #FILA 7 - BIOQUIMICO/TRANSITORIAS
  #BIOQUIMICO
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.cell(w=78, h=5, txt='EXAMEN BIOQUIMICO', border='LRBT', align='C', ln=0, fill=1)
  
  #TRANSITORIAS
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=39, h=5, txt='Celulas transitorias', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=transitorias, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo400X', border='R', align='L', ln=1, fill=0)

  #FILA 8 - PH/ESCAMOSAS
  #PH
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=30, h=5, txt='ph', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=48, h=5, txt=ph, border='R', align='C', ln=0, fill=0)

  #ESCAMOSAS
  pdf.cell(w=39, h=5, txt='Celulas escamosas', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=escamosas, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo400X', border='R', align='L', ln=1, fill=0)

  #FILA 9 - PROTEINAS/CILINDROS
  #PROTEINAS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=25, h=5, txt='Proteinas', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=40, h=5, txt=proteinas, border='', align='C', ln=0, fill=0)
  pdf.cell(w=13, h=5, txt='g/l', border='R', align='C', ln=0, fill=0)

  #CILINDROS
  pdf.cell(w=39, h=5, txt='Cilindros', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=cilindros, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='/campo100X', border='R', align='L', ln=1, fill=0)

  #FILA 10 - GLUCOSA/CRISTALES
  #GLUCOSA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=24, h=5, txt='Glucosa', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=40, h=5, txt=glucosa, border='', align='C', ln=0, fill=0)
  pdf.cell(w=14, h=5, txt='mmol/L', border='R', align='C', ln=0, fill=0)

  #CRISTALES
  pdf.cell(w=39, h=5, txt='Cristales', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=cristales, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='', border='R', align='L', ln=1, fill=0)

  #FILA 11 - CETONAS/BACTERIAS
  #CETONAS
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=25, h=5, txt='Cetonas', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=40, h=5, txt=cetonas, border='', align='C', ln=0, fill=0)
  pdf.cell(w=13, h=5, txt='', border='R', align='C', ln=0, fill=0)

  #BACTERIAS
  pdf.cell(w=39, h=5, txt='Bacterias', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=bacterias, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='', border='R', align='L', ln=1, fill=0)

  #FILA 12 - BILIRRUBINA/LIPIDOS
  #BILIRRUBINA
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=25, h=5, txt='Bilirrubinas', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=40, h=5, txt=bilirrubina, border='', align='C', ln=0, fill=0)
  pdf.cell(w=13, h=5, txt='', border='R', align='C', ln=0, fill=0)

  #LIPIDOS
  pdf.cell(w=39, h=5, txt='Lipidos', border='L', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=lipidos, border='', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='', border='R', align='L', ln=1, fill=0)

  #FILA 13 - SANGRE/OTROS
  #SANGRE
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.cell(w=25, h=5, txt='Sangre/Hg', border='BL', align='L', ln=0, fill=0)
  pdf.cell(w=40, h=5, txt=sangre, border='B', align='C', ln=0, fill=0)
  pdf.cell(w=13, h=5, txt='', border='RB', align='C', ln=0, fill=0)

  
  #OTROS
  pdf.cell(w=39, h=5, txt='Otros', border='BL', align='L', ln=0, fill=0)
  pdf.cell(w=35, h=5, txt=otros, border='B', align='C', ln=0, fill=0)
  pdf.cell(w=24, h=5, txt='', border='BR', align='L', ln=1, fill=0)

  if interpretacion != '':
    #FILA 14 - INTERPRETACION
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('Raleway', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=176, h=5, txt='Interpretacion:', border='RL ', align='L', ln=1, fill=0)

    #FILA 15 - INTERPRETACION CUADRO DE TEXTO
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('Raleway', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=176, h=5, txt=interpretacion, border='RBL', align='L', ln=1, fill=0)

  if comentarios != '':
    #FILA 14 - COMENTARIOS
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('Raleway', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=176, h=5, txt='Comentarios extras:', border='RL ', align='L', ln=1, fill=0)

    #FILA 15 - COMENTARIOS CUADRO DE TEXTO
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('Raleway', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=176, h=5, txt=comentarios, border='RBL', align='L', ln=1, fill=0)

  y1 = pdf.get_y()
  x1 = pdf.get_x()
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