import os
import subprocess
from pathlib import Path

# Return output : byte, error : default-None
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return output : byte, error : default-None
def addUser(username):
    bashCommand = 'sudo adduser ' + username
    return executeBash(bashCommand)


# Return output : byte, error : default-None
def delUser(username):
    bashCommand = 'sudo userdel -r ' + username
    return executeBash(bashCommand)


# Return output : byte, error : default-None
def accessUser(username):
    bashCommand = 'sudo su - ' + username
    return executeBash(bashCommand)


if __name__ == "__main__":
    # Run test commands here
    # home = str(Path.home())
    output = addUser('test')

    if output.decode('utf-8') == '':
        dir = '/home/test/.ssh'
        os.makedirs(dir)
