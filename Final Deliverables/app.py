from flask import (Flask,
 render_template,
 request,
 redirect,
 url_for,
 session)
from flask_session import Session
from Module.predict import predict

import dbworks as db


app = Flask(__name__, static_url_path='/static')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@app.route('/Get_Started')
def getStarted():
    try:
        del session['user']
    except:
        pass
    return render_template('home.html')

@app.route('/uploadpage',methods = ['POST','GET'])
def uploadpage():
    if not session['user']:
        return render_template('Authentication.html', msg="Login First")
    if request.method == "POST":
        if request.form["type"]=="Upload":
            image = request.files['image']
            filesrc = './uploads/.predict.jpg'
            image.save(filesrc)
            best = predict(filesrc)
            if best == False:
                return render_template('debug.html',msg="Cannot able to Recognize, reupload with correct image")
            user = session.get('user',None)
            user[0] = list(user[0])
            user[0][4] = ','+str(best)+user[0][4]
            db.updateHistory(user[0])
            return render_template('Uploadphoto.html', bodyele = int(best))
    return render_template('Uploadphoto.html', bodyele = '-')

@app.route('/DeleteAccount', methods=['POST','GET'])
def deleteaccount():
    if request.method == "POST":
        user = session['user'][0][1]
        db.deleteAccount(user)
        return render_template('Authentication.html')
    return render_template('deleteacc.html')

@app.route('/Authentication', methods = ['POST','GET'])
def Authorize():

    if request.method == "POST":
        if request.form["type"] == "Login":
            username = request.form["email"]
            password = request.form["password"]
            user = db.retreiveUsers(username)
            if user == []:
                return render_template('Authentication.html', msg="User Doesnot Exist")
            if user[0][3] != password:
                return render_template('Authentication.html', msg="Incorrect Password")
            session['user'] = user;
            return redirect(url_for('uploadpage'))
        
        elif request.form["type"] == "Signup":
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            if password != request.form["cpassword"] and '' in [username,email,password]:
                return render_template('Authentication.html', msg="Invalid Data")
            if db.retreiveUsers(username) != []:
                return render_template('Authentication.html', msg="User Already Exist")
            ack = db.insertUser(username, email, password)
            if not ack:
                return render_template('Authentication.html', msg="Invalid Data")
            return render_template('Authentication.html', msg="Successfully Signed In")
        
    return render_template('Authentication.html')
