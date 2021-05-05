from flask import Flask
from flask import render_template

app = Flask('menu')
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('home.html')

app.run(debug=True)