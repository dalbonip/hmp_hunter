import os
import re
import pandas as pd
from search_db_for_lib import look_for_lib
from datetime import date, datetime
from pytz import timezone


directory = "clientes"

def make_report():
  data_e_hora_atuais = datetime.now()
  fuso_horario = timezone('America/Sao_Paulo')
  data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
  data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')


  f = open("templates/report.html",  "w")
  f.write("")
  f.close()

  f = open("templates/report.html",  "r+")
  f.write("<div>")
  f.write("{% extends 'base.html' %}")
  f.write("{% block head %}")
  f.write("{% endblock %}")
  f.write("{% block body %}")
  f.write('<div class="content">')
  f.write('<br><h1>CVEs Report</h1><br>')
  f.write('<div><button onClick="window.location.href=`/atualizar`">Atualizar report</button>&nbsp&nbsp<button onClick="window.print()">Print to file</button>&nbsp&nbsp<button onClick="window.location.href=`/upload`">Add cliente</button></a></h3><br><br></div>')
  f.write(f'<teste class="normal">atualizado pela última vez em: {data_e_hora_sao_paulo_em_texto} (UTC -3/Brasília)</teste>')


  for filename in os.listdir(directory):
    if filename[-4:] == ".csv":
      f.write("<div>")
      csvtoread = directory +"/"+ filename
      dataframe = pd.read_csv(csvtoread)
      f.write(f"<div><br><br><br><br><br><h2><p> >_ Cliente: {filename[:-4].capitalize()} </p></h2></div>")
      # print(dataframe)
      for r in range(len(dataframe)):
        lib = dataframe.iat[r,0]
        ver = dataframe.iat[r,1]
        retorno = look_for_lib(lib,ver)
        if retorno != 404 and retorno != None :
          retorno_final = list(dict.fromkeys(retorno))
          #f.write(f"<br><br><div><h4>&nbsp;&nbsp;&nbsp;&nbsp;{filename[:-4]}:</h4></div>")
          f.write(f'<br><div><h4>[+] {filename[:-4].capitalize()} <teste class="normal">-</teste> <a>{lib} {ver} </a><teste class="normal">is vulnerable to<teste> <a>{len(retorno_final)} CVE(s)<teste class="normal">!</teste></a><br></h4></div>')

          for vuln in retorno_final:
            f.write('<cvee class="greeny">')
            final = vuln.replace(' : ','</cvee><a> : </a><teste class="normal">')
            src_str1  = re.compile(lib, re.IGNORECASE)
            src_str2  = re.compile("(( |v)(\d+)\.(\d+)\.?(\d+)\.?(\d+)?\.?(\d+)?( |\.)?)")
            final = src_str1.sub(f'<cvee class="greeny"> {lib} </cvee>',final)
            final = src_str2.sub(f'<cvee class="greeny"> {ver} </cvee>',final)
            f.write(f'<div><p>{final}</teste></p></div>')
            f.write("</div>")
        else:
          f.write("</div>")
        f.write("<br>")
      f.write("<br><br><br><br><hr>")
    else:
      continue

  f.write("</div>")
  f.write("{% endblock %}")
  f.close()