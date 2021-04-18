"""
cd Dashboard
python app.py
"""

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')

@app.route('/model1res',methods=['POST'])
def uploadmodel1():
    f = request.files['file']
    return f.filename+" Uploaded"



@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)

if __name__ == "__main__":
    app.run(debug=True)