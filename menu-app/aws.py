import subprocess as sp

def aws_keypair(name):
    return sp.getoutput('aws ec2 create-key-pair --key-name {}'.format(name))

def aws_sg(name,description):
    return sp.getoutput('aws ec2 create-security-group --group-name {} --description {}'.format(name,description))

def aws_instance(ami,type_,count,subnet,key,sgid):
    return sp.getoutput('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}'.format(ami,type_,count,subnet,sgid))

def aws_ebs_vol(zone,size):
    return sp.getoutput('aws ec2 create-volume --availability-zone {} --no-encrypted --size {}'.format(zone,size))

def aws_ebs_attach(instance_id,vol_id):
    return sp.getoutput('aws ec2 attach-volume --instance-id {} --volume-id {} --device xvdh'.format(instance_id,vol_id))

def aws_s3_bucket(name,region):
    return sp.getoutput('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(name,region,region))

def aws_s3_upload(bucket,name_dir,file_object):
    return sp.getoutput('aws s3api put-object --bucket {} --key {} --body {}'.format(bucket,name_dir,file_object))

    