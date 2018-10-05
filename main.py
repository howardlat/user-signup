from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def validate():
    username = request.form['username']
    user_error = ""
    if " " in username or len(username) == 0 or len(username) <3 or len(username) > 20:
        user_error = "That's not a valid username"
    
    password = request.form['password']
    password_error = ""
    if " " in password or len(password) == 0 or len(password) <3 or len(password) > 20:
        password_error = "That's not a valid password"
        
    verify = request.form['verify']
    verify_error = ""
    if " " in verify or len(verify) == 0 or verify != password: 
        verify_error = "Passwords don't match"
        
    email = request.form['email']
    email_error = ""
    if @ not in email or and period not in email "":
        email_error = "Invalid email address"

    if user_error and password_error and verify_error and email_error:
        return render_template('welcome.html', username=username)
          
    else:
        return render_template('base.html',
        username=username,
        email=email,
        user_error=user_error,
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()