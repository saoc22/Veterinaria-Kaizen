from fpdf import FPDF
import subprocess
import sys
# -*- coding: utf-8 -*-

def generar_citologia(valores):

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

  #FILA 1 - METODO DE MUESTREO
  textoMuestreo = ""
  txt_paf = "X" if valores['paf'] == 'y' else " "
  txt_acaf = "X" if valores['acaf'] == 'y' else " "
  txt_impr = "X" if valores['impro'] == 'y' else " "
  txt_rasp = "X" if valores['raspado'] == 'y' else " "
  txt_hiso = "X" if valores['hisopado'] == 'y' else " "
  
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=42, h=5, txt='Metodo de muestreo:', border='LRBT', align='L', ln=0, fill=1)
  pdf.cell(w=20, h=5, txt='PAF/PAD', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=6, h=5, txt=txt_paf, border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=24, h=5, txt='ACAF/ACAD', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=6, h=5, txt=txt_acaf, border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=20, h=5, txt='Impronta', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=6, h=5, txt=txt_impr, border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=20, h=5, txt='Hisopado', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=6, h=5, txt=txt_hiso, border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=20, h=5, txt='Raspado', border='LRBT', align='C', ln=0, fill=1)
  pdf.cell(w=6, h=5, txt=txt_rasp, border='LRBT', align='C', ln=1, fill=1)

  #FILA 2 - DESCRIPCION MACROSCOPICA:
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=176, h=5, txt='Descripcion macroscópica:', border='LRBT', align='L', ln=1, fill=1)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=176, h=5, txt=valores['macros'], border='LRBT', align='L', fill=0)
  
  #FILA 3 - DESCRIPCION MICROSCOPICA:
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=176, h=5, txt='Descripcion microscópica:', border='LRBT', align='L', ln=1, fill=1)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=176, h=5, txt=valores['micros'], border='LRBT', align='L', fill=0)
  
  #FILA 4 - Interpretacion:
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=176, h=5, txt='Interpretacion:', border='LRBT', align='L', ln=1, fill=1)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_fill_color(255, 255, 255)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=176, h=5, txt=valores['inter'], border='LRBT', align='L', fill=1)
  
  #FILA 5 - Diagnostico:
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('RalewayB', '', 10)
  pdf.set_text_color(255, 255, 255)
  pdf.set_fill_color(4, 22, 49)
  pdf.cell(w=176, h=5, txt='Diagnostico:', border='LRBT', align='L', ln=1, fill=1)
  y1 = pdf.get_y()
  pdf.set_xy(x1+6, y1)
  pdf.set_font('Raleway', '', 10)
  pdf.set_fill_color(255, 255, 255)
  pdf.set_text_color(0, 0, 0)
  pdf.multi_cell(w=176, h=5, txt=valores['diag'], border='LRBT', align='L', fill=1)
  
  if valores['comen'] != '':
    #FILA 6 - Comentario:
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('RalewayB', '', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_fill_color(4, 22, 49)
    pdf.cell(w=176, h=5, txt='Comentario:', border='LRBT', align='L', ln=1, fill=1)
    y1 = pdf.get_y()
    pdf.set_xy(x1+6, y1)
    pdf.set_font('Raleway', '', 10)
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(w=176, h=5, txt=valores['comen'], border='LRBT', align='L', fill=1)
  
  #FIRMA
  y1 = pdf.get_y()
  x1 = pdf.get_x()
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