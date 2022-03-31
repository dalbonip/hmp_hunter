#!/usr/bin/python3
from crypt import methods
from flask import Flask, render_template, request, url_for
import os

from werkzeug.utils import secure_filename

from report_maker import make_report
from search import get_cve, get_version, read_data

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'clientes/'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
  return render_template('report.html')

@app.route('/atualizar')
def atualizar():
  make_report()
  return render_template('report.html')

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_csv():
  if request.method == 'POST':
    try:
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return '<h3><a href="/">Home</a><br>file uploaded successfully</h3>'
    except:
      return '<h3><a href="/">Home</a><br><br>file upload FAILURE</h3><p><h4>Você fez o upload corretamente de um csv com as especificações pedidas?</p></h4>'

@app.route('/search', methods = ['GET', 'POST'])
def search():
  if request.method == 'POST':
    lib = request.form['lib']
    version = request.form['version']

    try:
      args = read_data(lib,version)
      return render_template('index.html', args=args)
    except:
      return render_template('index.html', args=[f'{lib} {version} está seguro de acordo com as CVEs publicadas até o momento.'])

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True, host='0.0.0.0', port=port)