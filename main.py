from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/error")
def error():
    username = request.form['username']
    if not username.isalpha() or len(username) <3 or len(username) > 20:
        error = "That's not a valid username"
        return redirect(url_for("/") + error)
    else:
        return render_template('base.html')
   
       
@app.route("/")
def index():
   return render_template('base.html')

app.run()