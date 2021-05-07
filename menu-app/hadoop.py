import subprocess as sp

def hadoop_version():
    return sp.getoutput('hadoop version')

def hadoop_nn_format():
    return sp.getoutput('hadoop namenode -format')

def hadoop_nn_start():
    return sp.getoutput('hadoop-daemon.sh start namenode')

def hadoop_dn_start():
    return sp.getoutput('hadoop-daemon.sh start datanode')

def hadoop_report():
    return sp.getoutput('hadoop dfsadmin -report')

def hadoop_fs_list():
    return sp.getoutput('hadoop fs -ls /')