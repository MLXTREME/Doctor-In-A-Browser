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

# import Flask Library

from flask import Flask, render_template, request, url_for, send_from_directory, jsonify
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__, static_folder="assets")
ROOT_DIR = os.getcwd()

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

'''@app.route('/MaternalHealthDyabc.html')#,methods=['POST'])
def maternal():
    return render_template('/MaternalHealthDy.html')

@app.route('/maternalhealthresult',methods=['POST'])
def maternalresult():
    f = request.form['fname']
    l = request.form['lname']
    email = request.form['email']
    mobile = request.form['mobile']
    filex = request.files['f']

    return f+" "+l+" with contacts "+email+" "+mobile+" uploaded "+ filex.filename
'''

with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("Sunanda's Resume ChatBot")
trainer2 = ListTrainer(bott)
trainer2.train([    "Hey",
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
        ])
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")
@app.route('/MaternalHealthDy.html')
def getchatbot():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bott.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
