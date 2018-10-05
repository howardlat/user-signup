from flask import Flask, request, redirect, render_template, url_for
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    if not username.isalnum() or len(username) <3 or len(username) > 20:
        error = "That's not a valid username"
        return redirect("/?error=" + error)  

    password = request.form['password']
    if not password.isalnum() or len(password) <3 or len(password) > 20:
        error = "That's not a valid password"
        return redirect("/?error=" + error)  

    verify = request.form['verify']
    if not verify.isalnum() or verify != password: 
        error = "Passwords don't match"
        return redirect("/?error=" + error) 


    email = request.form['email']
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    if not match:
        error = "Invalid email address"
        return redirect("/?error=" + error)

    else:
        return redirect('/welcome')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')
       
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()