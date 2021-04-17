"""
cd Dashboard
python app.py
"""

from flask import *

app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')

@app.route('/model1res',methods=['POST'])
def uploadmodel1():
    f = request.files['file']
    return f.filename+" Uploaded"


if __name__ == "__main__":
    app.run(debug=True)