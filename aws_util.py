import os
import boto3
import shlex, subprocess
from collections import defaultdict

# Return output : tuple, error : default-None
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return True is pk is added. ELSE raise Exception
def addPublicKey(username=None,public_key=None):
    if username == None or public_key == None:
        raise Exception('Please define a username and a public key')

    if 'ssh-rsa' not in public_key:
        public_key = 'ssh-rsa ' + public_key

    pk_dir = '/home/' + username + '/.ssh/authorized_keys'
    bashCommand = 'sudo bash -c "echo # ' + username + ' public key >> ' + pk_dir + '"'
    bashCommand_1 = 'sudo bash -c "echo ' + public_key + ' >> ' + pk_dir + '"'

    try:
        subprocess.Popen(shlex.split(bashCommand), stdout=subprocess.PIPE)
        subprocess.Popen(shlex.split(bashCommand_1), stdout=subprocess.PIPE)
    except:
        raise Exception('Unable to add public key for user ' + username)

    return True


# Return True is user is create. ELSE raise Exception
def addUser(username=None,public_key=None):
    if username == None:
        raise Exception('Please define a username for the new user')

    try:
        bashCommand = 'sudo adduser ' + username
        executeBash(bashCommand)
    except:
        raise Exception('User ' + username + ' already exists')

    # ========================= Create .ssh folder ========================== #

    bashCommand = 'sudo mkdir /home/' + username + '/.ssh'
    executeBash(bashCommand)

    bashCommand = 'sudo chown ' + username + ':' + username + ' /home/' + username + '/.ssh'
    executeBash(bashCommand)

    bashCommand = 'sudo chmod 700 /home/' + username + '/.ssh'
    executeBash(bashCommand)

    # ===================== Create authorized_keys file ===================== #

    bashCommand = 'sudo touch /home/' + username + '/.ssh/authorized_keys'
    executeBash(bashCommand)

    bashCommand = 'sudo chown ' + username + ':' + username + ' /home/' + username + '/.ssh/authorized_keys'
    executeBash(bashCommand)

    bashCommand = 'sudo chmod 600 /home/' + username + '/.ssh/authorized_keys'
    executeBash(bashCommand)

    # ============================ Add public key =========================== #

    if public_key != None:
        return addPublicKey(username,public_key)

    return True


# Return output : tuple, error : default-None
def delUser(username=None):
    if username == None:
        raise Exception('Please define a user to delete')

    bashCommand = 'sudo userdel -r ' + username
    return executeBash(bashCommand)


# Return public key : String
def generateKeyPair(username=None):
    if username == None:
        raise Exception('Please define a username')

    ec2 = boto3.client('ec2')
    try:
        response = ec2.create_key_pair(KeyName=username)
    except:
        results = delAWSKeyPair(username)
        if results['status']:
            response = ec2.create_key_pair(KeyName=username)
        else:
            raise Exception(results['message'])

    private_key = response['KeyMaterial']
    key_name = response['KeyName']

    file_path = os.path.join(os.getcwd(),key_name+'.pem')
    result = writeKeyPairFile(private_key,file_path)

    return {'key_name':key_name,'private_key':private_key,'public_key':getPublicKey(username,file_path).decode('utf-8').strip()}


# Return public key : String
def getPublicKey(username=None,file_name=None,file_path=None):
    if username == None and file_name == None and file_path == None:
        raise Exception('Please define a username, file name or a file path')

    file_name = username + '.pem' if username != None else file_name
    file_path = os.path.join(os.getcwd(),file_name) if file_name != None else file_path

    bashCommand = 'sudo ssh-keygen -y -f "' + file_path + '"'
    output,error = subprocess.Popen(shlex.split(bashCommand), stdout=subprocess.PIPE).communicate()

    return output


# Return True is successful delete. ELSE False
def delKeyPairFile(username=None,file_name=None,file_path=None,):
    if username == None and file_name == None and file_path == None:
        raise Exception('Please define a username, file name or a file path')

    file_name = username + '.pem' if username != None else file_name
    file_path = os.path.join(os.getcwd(),file_name) if file_name != None else file_path

    try:
        os.remove(file_path)
    except:
        return {'status':False,'message':file_path + ' does not exists'}

    return {'status':True,'message':None}


# Return True is successful write. ELSE False
def writeKeyPairFile(private_key=None,file_path=None):
    try:
        with open(file_path,'w') as file:
            file.write(private_key)
    except Exception as e:
        return {'status':False,'message':e.args[0]}

    return {'status':True,'message':None}


# Return True is successful delete. ELSE False
def delAWSKeyPair(username=None):
    if username == None:
        raise Exception('Please define a username')

    try:
        ec2 = boto3.client('ec2')
        response = ec2.delete_key_pair(KeyName=username)
    except Exception as e:
        return {'status':False,'message':e.args[0]}

    return {'status':True,'message':None}


# ============================================================================ #
# ============================================================================ #
# ============================================================================ #


if __name__ == "__main__":
    # Run test commands here
    # username = 'Test'
    # response = generateKeyPair(username)
    # print(response['public_key'])

    # response = generateKeyPair(username)
    # public_key = response['public_key']
    #
    # delUser(username)
    # response = addUser(username,public_key)
    # print(response)

    # Connect to EC2
    ec2 = boto3.resource('ec2')

    # Get information for all running instances
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']}])

    ec2info = defaultdict()
    for instance in running_instances:
        for tag in instance.tags:
            if 'Name'in tag['Key']:
                name = tag['Value']
        # Add instance info to a dictionary
        ec2info[instance.id] = {
            'Name': name,
            'Type': instance.instance_type,
            'State': instance.state['Name'],
            'Private IP': instance.private_ip_address,
            'Public IP': instance.public_ip_address,
            'Launch Time': instance.launch_time
            }

    attributes = ['Name', 'Type', 'State', 'Private IP', 'Public IP', 'Launch Time']
    for instance_id, instance in ec2info.items():
        for key in attributes:
            print("{0}: {1}".format(key, instance[key]))
        print("------")
