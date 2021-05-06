from flask import Flask
from flask import render_template

app = Flask('menu')
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/option/<y>')
def options(y):
    if y == 'hadoop':
        return render_template('/hadoop/hadoop.html')
    elif y == 'docker':
        return render_template('/docker/docker.html')
    elif y == 'aws':
        return render_template('/aws/aws.html')
    elif y == 'linux':
        return render_template('/linux/linux.html')
    else:
        return 'request not found'

app.run(debug=True)