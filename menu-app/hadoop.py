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

def hadoop_put(file_path, designation):
    return sp.getoutput('hadoop fs -put {} {}'.format(file_path,designation))

def hadoop_rm(file_path):
    return sp.getoutput('hadoop fs -rm {}'.format(file_path))

def hadoop_cat(file_path):
    return sp.getoutput('hadoop fs -cat {}'.format(file_path))

def hadoop_put_block_size(block_size, file_path, designation):
    return sp.getoutput('hadoop fs -Ddfs.block.size={} -put {} {} '.format(block_size,file_path,designation))

def hadoop_touch(file_name):
    return sp.getoutput('hadoop fs -touchz / {}'.format(file_name))