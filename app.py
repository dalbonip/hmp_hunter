from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from report_maker import make_report

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


if __name__ == "__main__":
  app.run(debug=True)