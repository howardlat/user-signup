from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']    
    if not username.isalpha() or len(username) <3 or len(username) > 20:
        error = "That's not a valid username"
        return render_template('base.html')  + error     
   
       
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('base.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()