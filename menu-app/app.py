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
    elif x=='7':
        return render_template('hadoop/op-input.html',x='7', input=2, input1=['FILE PATH IN LOCAL SYSTEM','DESIGNATION IN HDFS CLUSTER'], input2=['path','designation'], title='Details')
    elif x=='8':
        return render_template('hadoop/op-input.html',x='8', input=1, input1=['FILE PATH IN HDFS CLUSTER'], input2=['path'], title='Details')
    elif x=='9':
        return render_template('hadoop/op-input.html',x='9', input=1, input1=['FILE PATH IN HDFS CLUSTER'], input2=['path'], title='Details')
    elif x=='10':
        return render_template('hadoop/op-input.html',x='10', input=3, input1=['BLOCK SIZE','FILE PATH IN LOCAL SYSTEM','DESIGNATION IN HDFS CLUSTER'], input2=['block','path','designation'], title='Details')
    elif x=='11':
        return render_template('hadoop/op-input.html',x='11', input=1, input1=['FILE NAME'], input2=['name'], title='Details')


@app.route('/hadoop-dynamic-op', methods=['GET'])
def hadoop_dynamic():
    x = request.args.get('x')
    if x=='7':
        path = request.args.get('path')
        desig = request.args.get('designation')
        output = hadoop_put(path, desig)
        return render_template('hadoop/default-op.html', op=output, title='OUTPUT')
    elif x=='8':
        path = request.args.get('path')
        output = hadoop_rm(path)
        return render_template('hadoop/default-op.html', op=output, title='OUTPUT')
    elif x=='9':
        path = request.args.get('path')
        output = hadoop_cat(path)
        return render_template('hadoop/default-op.html', op=output, title='OUTPUT')
    elif x=='10':
        block = request.args.get('block')
        path = request.args.get('path')
        desig = request.args.get('designation')
        output = hadoop_put_block_size(block, path, desig)
        return render_template('hadoop/default-op.html', op=output, title='OUTPUT')
    elif x=='11':
        name = request.args.get('name')
        output = hadoop_touch(name)
        return render_template('hadoop/default-op.html', op=output, title='OUTPUT')

app.run(debug=True)