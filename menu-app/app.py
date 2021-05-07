from flask import Flask
from flask import render_template
from flask import request
from hadoop import *

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

@app.route('/hadoop-output', methods=['GET'])
def hadoop_output():
    x = request.args.get('option')
    if x=='1':
        output = hadoop_version()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
    elif x=='2':
        output = hadoop_nn_format()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
    elif x=='3':
        output = hadoop_nn_start()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
    elif x=='4':
        output = hadoop_dn_start()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
    elif x=='5':
        output = hadoop_report()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
    elif x=='6':
        output = hadoop_fs_list()
        return render_template('hadoop/default-op.html', op=output, title='HADOOP OUTPUT')
        

app.run(debug=True)