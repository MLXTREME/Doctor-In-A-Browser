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
    return render_template('dashboard.html')
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


if __name__ == "__main__":
    app.run(debug=True)
