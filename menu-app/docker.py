import subprocess as sp

def doc_version():
    return sp.getoutput('docker version')

def docker_run(image,name):
    return sp.getoutput('docker run -dit --name {} {} '.format(name,image))

def docker_pull(image):
    return sp.getoutput('docker pull {}'.format(image))

def docker_ps():
    return sp.getoutput('docker ps')

def docker_ps_all():
    return sp.getoutput('docker ps -a')

def docker_images():
    return sp.getoutput('docker images')

def docker_start(name):
    return sp.getoutput('docker start {}'.format(name))

def docker_stop(name):
    return sp.getoutput('docker stop {}'.format(name))

def docker_rm(name):
    return sp.getoutput('docker rm {}'.format(name))

def docker_rm_all():
    return sp.getoutput('docker rm $(docker ps -aq)')

def docker_stop_all():
    return sp.getoutput('docker stop $(docker ps -aq)')