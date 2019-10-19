from flask import Flask, render_template, request

from DBConnection import DBConnection

app = Flask (__name__)

@app.route('/',methods=['GET'])
def login_page():
    return render_template('login_page.html')

@app.route('/home')
def home_page():
    return "In home page"

@app.route('/register',methods=['GET','POST'])
def registration_page():
    if request.method == "POST":
        dbConnect = DBConnection("NewDB.db")
        dbConnect.create_table('Mytable','name','userName','email','phoneNumber','country','state')
        dbConnect.update_values('Mytable', name=request.form.get('name'),username=request.form.get('username'),email=request.form.get('email'),
                                phoneNumber=request.form.get('phonenumber'),state=request.form.get('state'))
        dbConnect.close_connection()
    return render_template('registration_page.html')

if __name__=="__main__":
    app.run(debug=True)