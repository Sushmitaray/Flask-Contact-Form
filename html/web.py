from flask import Flask , render_template, request,flash
from flask_mail import Mail
import json


with open('config.json','r')as c:
  params=json.load(c)["param"]

app = Flask(__name__)
app.secret_key="dont tell anyone"
app.config.update(
  MAIL_SERVER='smtp.gmail.com',
  MAIL_PORT='465',
  MAIL_USE_SSL=True,
  MAIL_USERNAME=params['gmail-user'],
  MAIL_PASSWORD=params['gmail-password']
)
mail=Mail(app)
@app.route("/",methods=['GET','POST'])
def index():
  if(request.method=='POST'):
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    email=request.form.get('email')
    password=request.form.get('password')
    phone=request.form.get('phone')
    mail.send_message('New entry',
      sender=email,
      recipients=[params['gmail-user']], body='Firstname='+firstname +'\n'+'Lastname='+lastname +'\n'+'Email='+email +'\n'+'Phone='+phone) 
    flash("Successfully Registered")
    return render_template('FORM.html')
  return render_template('FORM.html')
if __name__=='__main__':
    app.run(debug=True) 