from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate', methods=['POST', 'GET'])
def validate():
    username = request.form['username']    
    if not username.isalpha() or len(username) <3 or len(username) > 20:
        error = "That's not a valid username"
        return error   

        
   
       
@app.route("/")
def index():
   return render_template('base.html')

app.run()