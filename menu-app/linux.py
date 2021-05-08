import subprocess as sp

def dir_create(name):
    return sp.getoutput('mkdir {}'.format(name))

def file_list():
    return sp.getoutput('ls')

def file_create(name):
    return sp.getoutput('touch {}'.format(name))

def user_add(name):
    return sp.getoutput('useradd {}'.format(name))

def passwd_change(user):
    return sp.getoutput('passwd {}'.format(user))

def ram_usage():
    return sp.getoutput('free -m')

def show_hd():
    return sp.getoutput('df -h')

def package_check(name):
    return sp.getoutput('rpm -q {}'.format(name))

def package_rm(name):
    return sp.getoutput('rpm -e {}'.format(name))

def ip():
    return sp.getoutput('ifconfig')

def java_process():
    return sp.getoutput('jps')

def cpu_info():
    return sp.getoutput('lscpu')

def running_processes():
    return sp.getoutput('ps -aux')

def uptime():
    return sp.getoutput('uptime')

def ram_clear():
    return sp.getoutput('echo 3 > /proc/sys/vm/drop_caches')

def yum_whatprovides(name):
    return sp.getoutput('yum whatprovides {}'.format(name))

def ping(ip):
    return sp.getoutput('ping -c 5 {}'.format(ip))

def useradd_command(command, username):
    return sp.getoutput('useradd -s {} {}'.format(command,username))