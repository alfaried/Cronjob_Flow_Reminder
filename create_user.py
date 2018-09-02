import os
import subprocess
from pathlib import Path

# Return output : tuple, error : default-None
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return output : tuple, error : default-None
def addUser(username):
    bashCommand = 'sudo adduser ' + username
    return executeBash(bashCommand)


# Return output : tuple, error : default-None
def delUser(username):
    bashCommand = 'sudo userdel -r ' + username
    return executeBash(bashCommand)


# Return output : tuple, error : default-None
def accessUser(username):
    bashCommand = 'sudo su - ' + username
    return executeBash(bashCommand)


if __name__ == "__main__":
    # Run test commands here
    # home = str(Path.home())
    output = addUser('test')
    output = output.decode('utf-8')
    print(output)
    print(type(output))
    # if output.decode('utf-8') == '':
    #     dir = '/home/test/.ssh'
    #     os.makedirs(dir)
