"""
MedicAI is an initiative by Team MLXTREME for the Hackathon.
Medical Artificial Intelligence.
Assistive Technology for better Electronic Healthcare Facilities for a brighter tomorrow.

To get a demo, Run app.py and visit the link which comes up.

Regards,
Team MLXTREME

Instructions For Running :

View Instructions.md
MedicAIEnv\Scripts\activate
To deactivate base - conda.bat deactivate
cd WebsiteFiles/FlaskApp
python app.py


TODO :
Favicon
"""

import warnings
warnings.filterwarnings('ignore')
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from numpy import genfromtxt
import pandas as pd

# import Flask Library

from flask import Flask, render_template, request, url_for, send_from_directory, jsonify,render_template_string,Markup
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
from skimage import io
import warnings
from tensorflow import keras
from subprocess import call


from sklearn.preprocessing import StandardScaler
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

from sklearn.neighbors import KNeighborsClassifier
import warnings
from sklearn import metrics
CLASS_LABELS_Park = {0 : "healthy", 1: "parkinson"}
def ScaleData(data):
  scaler = StandardScaler()
  # transform data
  scaled = scaler.fit_transform(data)
  return scaled

SIZE= 128
def rgba2rgb( rgba, background=(255,255,255) ):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b, a = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

    a = np.asarray( a, dtype='float32' ) / 255.0

    R, G, B = background

    rgb[:,:,0] = r * a + (1.0 - a) * R
    rgb[:,:,1] = g * a + (1.0 - a) * G
    rgb[:,:,2] = b * a + (1.0 - a) * B

    return np.asarray( rgb, dtype='uint8' )


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def dispimgs(path,disp=0):
    # reading png image file
    im = plt.imread(path)
    if im.shape[-1]==4:
        im = rgba2rgb(im)
    im = cv2.resize(im,(SIZE,SIZE))
    im = rgb2gray(im)
    return im

def RunParkinsonInferences(imgPath):
  img = dispimgs(imgPath)
  imgres = ScaleData(img.reshape(1,-1))
  pred = model.predict(imgres)
  return pred[0],CLASS_LABELS_Park[pred[0]]


def predict_rf(a):
    """
    shape of a = (21,1)
    """
    filename = os.path.join(CurrDir,'rf_model.pkl')
    print(filename)
    # try:
    loaded_model = pickle.load(open(filename, 'rb'))
    predict = loaded_model.predict(a)
    print(predict)
    print("prediction done :)")
    return predict

def FetalInferences(FetalDetails):
    """
    baseline value,accelerations,fetal_movement,uterine_contractions,light_decelerations,severe_decelerations,
    prolongued_decelerations,abnormal_short_term_variability,mean_value_of_short_term_variability,
    percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,
    histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes,
    histogram_mode,histogram_mean,histogram_median,histogram_variance,histogram_tendency,fetal_health
    """
    DetailsArr = np.array(list(FetalDetails.values()))
    a= np.reshape(DetailsArr, (-1,DetailsArr.shape[0]))

    predict_rf1 = predict_rf(a)
    preds = predict_rf1[0]
    print(preds)
    return preds
    
LoginDict = dict()
RegisterDict = dict()

app = Flask(__name__, static_folder="assets")
ROOT_DIR = os.getcwd()
CurrDir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home1():
    return render_template('homepage.html')


@app.route('/index.html')
def home2():
    return render_template('homepage.html')


@app.route('/index')
def home3():
    return render_template('homepage.html')


@app.route('/home')
def home4():
    return render_template('homepage.html')


@app.route('/home.html')
def home():
    return render_template('homepage.html')


@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')




@app.route('/login', methods=['POST'])
def loginsuccess():
    LoginUserEmail = request.form['LoginUserEmail']
    LoginUserPassword = request.form['LoginUserPassword']
    try:
        LoginUserRememberMe = request.form['LoginUserRememberMe']
    except:
        LoginUserRememberMe = "off"

    # Creating Login Dictionaries
    LoginDict = {'LoginUserEmail': LoginUserEmail,
                 'LoginUserPassword': LoginUserPassword,
                 'LoginUserRememberMe': LoginUserRememberMe}
    print(LoginDict)
    return render_template('dashboardfinal.html')
    # return 'Hi You are now Logged in!!'
    # return render_template('success.html')



@app.route('/register', methods=['POST'])
def registersuccess():
    RegisterUserName = request.form['RegisterUserName']
    RegisterUserEmail = request.form['RegisterUserEmail']
    RegisterUserPassword = request.form['RegisterUserPassword']

    try:
        RegisterPolicy = request.form['RegisterPolicy']
    except:
        RegisterPolicy = "off"

    # Creating Login Dictionaries
    RegisterDict = {'RegisterUserName': RegisterUserName,
                    'RegisterUserEmail': RegisterUserEmail,
                    'RegisterUserPassword': RegisterUserPassword,
                    'RegisterPolicy': RegisterPolicy}
    print(RegisterDict)
    return render_template('register_success.html')
    # return 'Hi You are now Registered!!'
    # return render_template('success.html')


with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("Sunanda's Resume ChatBot")
trainer2 = ListTrainer(bott)
Training_List = [    "Hey",
        "Hi there!",
        "Hi",
        "Hi!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome.",
        "What is your name?", "My name is Resume ChatBot",
        "Who created you?", "Soumyadip",
        "Why is nutrition during pregnancy important?",
        "Eating well is one of the best things you can do during pregnancy. Good nutrition helps you handle the extra demands on your body as your pregnancy progresses. The goal is to balance getting enough nutrients to support the growth of your fetus and maintaining a healthy weight.",
        "How much should I eat during pregnancy?",
        "The popular saying is that pregnant women “eat for two,” but now we know that it’s dangerous to eat twice your usual amount of food during pregnancy. Instead of “eating for two,” think of it as eating twice as healthy.If you are pregnant with one fetus, you need an extra 340 calories per day starting in the second trimester (and a bit more in the third trimester). That's roughly the calorie count of a glass of skim milk and half a sandwich. Women carrying twins should consume about 600 extra calories a day, and women carrying triplets should take in 900 extra calories a day.",
        "Why should I take a prenatal vitamin?",
        "Vitamins and minerals play important roles in all of your body functions. Eating healthy foods and taking a prenatal vitamin every day should supply all the vitamins and minerals you need during pregnancy.",
        "How many prenatal vitamins should I take each day?",
        "Take only one serving of your prenatal supplement each day. Read the bottle to see how many pills make up one daily serving. If your obstetrician–gynecologist (ob-gyn) or other obstetric care provider thinks you need an extra amount of a vitamin or mineral, he or she may recommend it as a separate supplement.",
        "Can I take more prenatal vitamins to make up for a deficiency?",
        "No, do not take more than the recommended amount of your prenatal vitamin per day. Some multivitamin ingredients, such as vitamin A, can cause birth defects at higher doses.",
        "Why is iron important during pregnancy?",
        "Iron is used by your body to make the extra blood that you and your fetus need during pregnancy. Women who are not pregnant need 18 mg of iron per day. Pregnant women need more, 27 mg per day. This increased amount is found in most prenatal vitamins.",
        ]

"""

trainer2.train(Training_List)
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")
"""
@app.route('/MaternalHealthDy.html')
def getchatbot():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bott.get_response(userText))


@app.route('/CTdy.html')#,methods=['POST'])
def maternal():
    return render_template('/CTdy.html')

CurrDir = os.path.dirname(os.path.abspath(__file__))
"""
ModelPath = os.path.join(CurrDir, "Best_Model88")
Model = keras.models.load_model(ModelPath)
"""
warnings.filterwarnings("ignore")

def preprocessImg(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    return x


def RunInferences(imgPath, display=True):
    img = image.load_img(imgPath, grayscale=False, target_size=(64, 64))
    x = preprocessImg(img)
    custom = Model.predict(x)
    if display:
        displayImg = image.load_img(
            imgPath, grayscale=False, target_size=(256, 256))
        plt.imshow(displayImg)
        plt.xticks([])
        plt.yticks([])
        plt.show()

    a = custom[0]
    ind = np.argmax(a)
    print("Class Probabilities :", a)
    print('Prediction:', CLASS_LABELS[ind])
    pred = CLASS_LABELS[ind]
    proba = { CLASS_LABELS[0] : a[0],
             
            CLASS_LABELS[1] : a[1]
            }
    return proba,pred

CLASS_LABELS = {0: 'non-COVID', 1: 'COVID'}

CurrDir = os.path.dirname(os.path.abspath(__file__))

import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result



def dict_to_html_table(in_dict):
    tbl_fmt = '''
    <table class="rwd-table"> {}
    </table>'''

    row_fmt = '''
    <tr>
        <td>{}</td>
        <td>{}</td>
    </tr>'''
    return tbl_fmt.format(''.join(row_fmt.format(k, v) for k, v in in_dict.items()))

def read_file(fpath):
    with open(fpath) as f:
        return f.read()

@app.route('/CTdyResult',methods=['POST'])
def maternalresult():
    uploads_dir = os.path.join(CurrDir, 'uploads')
    """
    f = request.form['fname']
    l = request.form['lname']
    email = request.form['email']
    mobile = request.form['mobile']
    """
    filex = request.files['f']
    imgPath = os.path.join(uploads_dir,filex.filename)
    print(imgPath)
    filex.save(imgPath)
    
    proba,pred = RunInferences(imgPath, display=False)
    print(pred)
    Results_Dict = dict()
    Results_Dict["Predicted Class"]= pred
    Results_Dict["Class Probabilities"] = "Following Results"
    for each in proba:
        Results_Dict[each] = proba[each]
    # return Results_Dict
    Prediction_Results = Markup(dict_to_html_table(Results_Dict))
    send_the_email = True
    if send_the_email==True:
        mail_dir = os.path.join(CurrDir,"PyAutoMail")
        os.chdir(mail_dir)
        mail_file=os.path.join(CurrDir,"PyAutoMail","MailReplacerCert.py")
        call(["python", mail_file])
    return render_template("form_submit.html",Prediction_Results=Prediction_Results)
    filepath = os.path.join(CurrDir,"templates","form_submit.html")
    html_file = read_file(filepath)
    # return render_template_string({% extends 'form_submit.html' %},Prediction_Results=Prediction_Results)
    # return render_template("form_submit.html",Prediction_Results=Prediction_Results)
    # return f+" "+l+" with contacts "+email+" "+mobile+" uploaded "+ filex.filename


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets', 'favicons'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/HIV.html')
def hiv():
    return render_template('HIV.html')

@app.route('/maternalhealth.html')
def mh():
    return render_template('maternalhealth.html')

@app.route('/ChestxrayTB.html')
def chest():
    return render_template('ChestxrayTB.html')

@app.route('/whymedicai.html')
def why():
    return render_template('whymedicai.html')

@app.route('/Fetaldy.html')
def fetaldy():
    return render_template('Fetaldy.html')

@app.route('/fetaldyresult',methods=['POST'])
def fetaldyresult():
    columns = {'bv':0 ,'a':0, 'fm':0, 'uc':0, 'ld':0, 'sd':0,'pd':0,'astv':0,'mvstv':0,'ptwaltv':0,'mvltv':0,
               'hw':0,'hmin':0,'hmax':0,'hpeak':0,'hzero':0,'hmode':0,'hmean':0,'hmedian':0,'hvariance':0,'ht':0}
    for i in columns.keys():
        columns[i] =float(request.form[i])
    print(columns)
    x = FetalInferences(columns)
    Results_Dict = dict()
    Results_Dict["Predicted Value"]= x
    FetalCLASSLABELS = {
                        1:"Normal",
                        2:"Suspect",
                        3:"Pathological"
                        }
    Results_Dict["Predicted Class"] = FetalCLASSLABELS[x]
    Prediction_Results = Markup(dict_to_html_table(Results_Dict))
    return render_template("form_submit.html",Prediction_Results=Prediction_Results)
    return "Check Terminal"

'''
Parkinsons
'''

@app.route('/parkinsonsdy.html')
def park():
    return render_template('parkinsonsdy.html')
kNNModelPath = "kNNModel.p"
model = pickle.load( open( kNNModelPath , "rb" ) )
@app.route('/parkinsonResult',methods=['POST'])
def parkres():
    uploads_dir = os.path.join(CurrDir, 'uploads')
    filex = request.files['f']
    imgPath = os.path.join(uploads_dir,filex.filename)
    print(imgPath)
    filex.save(imgPath)
    
    CLASS_LABELS_Park = {0 : "healthy", 1: "parkinson"}
    
    print(RunParkinsonInferences(imgPath))
    pred, clsname= RunParkinsonInferences(imgPath)
    print(pred)
    Results_Dict = dict()
    Results_Dict["Predicted Class Value"]= pred
    Results_Dict["Predicted Class Label"]= clsname
    Prediction_Results = Markup(dict_to_html_table(Results_Dict))
    return render_template("form_submit.html",Prediction_Results=Prediction_Results)


if __name__ == "__main__":
    app.run(debug=True)
