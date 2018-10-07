from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def validate():

    email = request.form['email']
    email_error = ""
    if "^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$" not in email and email != None:
        email_error = "Invalid email address"
                  
    password = request.form['password']
    password_error = ""
    if " " in password or len(password) == 0 or len(password) <3 or len(password) > 20:
        password_error = "That's not a valid password"

    verify = request.form['verify']
    verify_error = ""
    if " " in verify or len(verify) == 0 or verify != password: 
        verify_error = "Passwords don't match"

    username = request.form['username']
    user_error = ""
    if " " in username or len(username) == 0 or len(username) <3 or len(username) > 20:
        user_error = "That's not a valid username"

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('base.html',
        password_error=password_error,
        verify_error=verify_error,
        user_error=user_error,
        email_error=email_error)
          
            
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()