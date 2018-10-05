from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def validate():
    email = request.form['email']
    email_error = ""
    if len(email) > 0 and "@" and " " and "." not in email:
        email_error = "Invalid email address"

    verify = request.form['verify']
    verify_error = ""
    password = request.form['password']
    if " " in verify or len(verify) == 0 or verify != password: 
        verify_error = "Passwords don't match"

    password = request.form['password']
    verify = request.form['verify']
    password_error = ""
    if " " in password or len(password) == 0 or len(password) <3 or len(password) > 20 or password != verify:
        password_error = "That's not a valid password"

    
    username = request.form['username']
    user_error = ""
    if " " in username or len(username) == 0 or len(username) <3 or len(username) > 20:
        user_error = "That's not a valid username"
            
    
           
        return render_template('base.html',
        user_error=user_error,
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error)


    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

        
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()