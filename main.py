from flask import Flask,render_template,request,url_for,flash,redirect
#from regform import RegistrationForm
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
# AS simeple as possbile flask google oAuth 2.0
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta

# decorator for routes that should be accessible only by logged in users
from auth_decorator import login_required

# dotenv setup
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
obj = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'portfolio'

app.config['SECRET_KEY'] = '123456'

app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='668015713436-sv29riq0ndieo9njjriqck57s775l60i.apps.googleusercontent.com',
    client_secret='v_KRhwxqJde5MgfWXmVotz2P',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)




class Portfolio(FlaskForm):
    fname = StringField('fname', validators=[DataRequired(), Length(min=2, max=20)])
    lname = StringField('lname', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('address', validators=[DataRequired(), Length(min=2, max=20)])
    dob = StringField('dob', validators=[DataRequired(), Length(min=2, max=20)])
    cname = StringField('cname', validators=[DataRequired(), Length(min=2, max=20)])
    branch = StringField('branch', validators=[DataRequired(), Length(min=2, max=20)])
    year = StringField('year ', validators=[DataRequired(), Length(min=2, max=20)])
    links = StringField('links', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('button')
class Achieve(FlaskForm):
    activity = StringField('activity', validators=[DataRequired(), Length(min=2, max=20)])
    course = StringField('course', validators=[DataRequired(), Length(min=2, max=20)])
    time = StringField('time', validators=[DataRequired(), Length(min=2, max=20)])
    sem = StringField('sem', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('button')

class Goals(FlaskForm):
    sgoals = StringField('sgoals', validators=[DataRequired(), Length(min=2, max=20)])
    lgoals = StringField('lgoals', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('button')
    
class Acadamics(FlaskForm):
    board= StringField('board', validators=[DataRequired(), Length(min=2, max=20)])
    college = StringField('college', validators=[DataRequired(), Length(min=2, max=20)])
    marks = StringField('hmarks', validators=[DataRequired(), Length(min=2, max=20)])
    hboard= StringField('hboard', validators=[DataRequired(), Length(min=2, max=20)])
    hcollege = StringField('hcollege', validators=[DataRequired(), Length(min=2, max=20)])
    hmarks = StringField('hmarks', validators=[DataRequired(), Length(min=2, max=20)])
    skill = StringField('skill', validators=[DataRequired(), Length(min=2, max=20)])
    level = StringField('level', validators=[DataRequired(), Length(min=2, max=20)])
    category = StringField('category', validators=[DataRequired(), Length(min=2, max=20)])
    
    ptitle = StringField('ptitle', validators=[DataRequired(), Length(min=2, max=20)])
    desc = StringField('desc', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('button2')

class Coact(FlaskForm):
    activity = StringField('Activity', validators=[DataRequired(), Length(min=2, max=20)])
    sem= StringField('sem', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('button')

@app.route('/home')
@login_required
def home():
    email = dict(session)['profile']['email']
    #return f'Hello, you are logge in as {email}!'
    return render_template('home.html',title='home',email=email)
@app.route('/portfolio')
@login_required
def portfolio():
    cur = obj.connection.cursor()
    email = dict(session)['profile']['email']
    cur.execute("USE portfolio")	
    constantKey = 123
    cur.execute("SELECT * FROM details where email = %s AND constantKey= %s ",(email, constantKey))
    data=cur.fetchall()
    cur.execute("SELECT * FROM acadamics where email = %s AND constantKey= %s ",(email, constantKey))
    data2=cur.fetchall()
    cur.execute("SELECT * FROM achieve where email = %s AND constantKey= %s ",(email, constantKey))
    data3=cur.fetchall()
    cur.execute("SELECT * FROM coact where email = %s AND constantKey= %s ",(email, constantKey))
    data4=cur.fetchall()
    cur.execute("SELECT * FROM goals where email = %s AND constantKey= %s ",(email, constantKey))
    data5=cur.fetchall()
    obj.connection.commit()
    cur.close()

    return render_template('index.html',title='home', data=data,data2=data2,data3=data3,data4=data4,data5=data5)
@app.route('/personal',methods=['GET','POST'])
@login_required
def personal():
    forms = Portfolio()
    if request.method == 'POST':
        
            
        fname = request.form['fname']
        lname = request.form['lname']
        city = request.form['city']
        address = request.form['address']
        email= request.form['email']
        dob = request.form['dob']
        cname = request.form['cname']
        branch= request.form['branch']
        year = request.form['year']
        links = request.form['links'] 
        constantKey = 123

        cur = obj.connection.cursor()
        cur.execute("USE portfolio;")
        cur.execute("INSERT INTO details(fname, lname,city,address,email,dob,constantKey,cname,branch,year,links) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s )",
        (fname, lname,city,address,email,dob,constantKey,cname,branch,year,links))
            
        obj.connection.commit()
        print("HelooooooooooooHello")
        cur.close()
		
        return render_template('personal.html',title='MAIN PAGE',form=forms)	
    return render_template('personal.html',title='MAIN PAGE',form=forms)
@app.route('/achieve',methods=['GET','POST'])
@login_required
def achievements():
    forms = Achieve()

    if request.method == 'POST':
        email = dict(session)['profile']['email']
        
            
        activity = request.form['activity']
        course = request.form['course']
        time = request.form['time']
        sem = request.form['sem']
        #email= request.form['email']
        
        constantKey = 123

        cur = obj.connection.cursor()
        cur.execute("USE portfolio;")
        cur.execute("INSERT INTO achieve(activity,course,time,sem,email,constantKey) VALUES(%s, %s,%s,%s,%s,%s )",
        (activity, course,time,sem,email,constantKey))
            
        obj.connection.commit()
        
        cur.close()
        return render_template('achieve.html',form=forms)
    return render_template('achieve.html',form=forms)
@app.route('/goals',methods=['GET','POST'])
@login_required
def goals():
    forms= Goals()
    if request.method == 'POST':
        email = dict(session)['profile']['email']
        sgoals = request.form['sgoals']
        lgoals = request.form['lgoals']
        constantKey = 123

        cur = obj.connection.cursor()
        cur.execute("USE portfolio;")
        cur.execute("INSERT INTO goals(email,sgoals,lgoals,constantKey) VALUES(%s, %s,%s,%s )",
        (email,sgoals,lgoals,constantKey))
            
        obj.connection.commit()
        
        cur.close()

        return render_template('goals.html',form=forms)


    return render_template('goals.html',form=forms)


@app.route('/acadamics',methods=['GET','POST'])
@login_required
def acadamics():

    forms = Acadamics()
    if request.method == 'POST':
        email = dict(session)['profile']['email']
        board = request.form['board']
        college = request.form['college']
        marks = request.form['marks']
        hboards = request.form['hboard']
        hcollege = request.form['hcollege']
        hmarks = request.form['hmarks']
        skill = request.form['skill']
        level = request.form['level']
        category = request.form['category']
        
        ptitle = request.form['ptitle']
        desc = request.form['desc']
        constantKey = 123

        cur = obj.connection.cursor()
        cur.execute("USE portfolio;")
        cur.execute("INSERT INTO acadamics(email,board,college,marks,hboards,hcollege,hmarks,constantKey,skills,level,category,ptitle,description) VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )",
        (email,board,college,marks,hboards,hcollege,hmarks,constantKey,skill,level,category,ptitle,desc))
            
        obj.connection.commit()
        
        cur.close()
        return render_template('acadamics.html',form=forms)   


    return render_template('acadamics.html',form=forms)    
@app.route('/coact',methods=['GET','POST'])
@login_required
def coacts():
    forms= Coact()
    if request.method == 'POST':
        email = dict(session)['profile']['email']
        activity = request.form['activity']
        sem = request.form['sem']
        constantKey = 123

        cur = obj.connection.cursor()
        cur.execute("USE portfolio;")
        cur.execute("INSERT INTO coact(email,activity,sem,constantKey) VALUES(%s, %s,%s,%s )",
        (email,activity,sem,constantKey))
            
        obj.connection.commit()
        
        cur.close()

        return render_template('coact.html',form=forms)


    return render_template('coact.html',form=forms)    
@app.route('/')
def main():
    return render_template('main.html')
@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/home')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')




if __name__=='__main__':
	app.run(debug=True)    