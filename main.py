from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/error", methods=['POST'])
def error():
    username = request.form['username']
    
    if not username.isalpha():
        error = "That's not a valid username"
    elif len(username) <3 or len(username) > 20:
        return redirect("/?error=" + error)
        

       
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error)

app.run()