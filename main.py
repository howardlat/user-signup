from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/username", methods=['Post'])
def username():
    username = request.form['username']
  
    if len(username) < 3 or len(username)> 20:
        return redirect ("/?error=")
           
        


@app.route("/")
def index():
    return render_template('base.html')

app.run()