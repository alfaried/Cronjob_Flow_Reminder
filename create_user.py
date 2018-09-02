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
    delUser('test')
    addUser('test')
    ssh_dir = '/home/test/.ssh'
    key_dir = '/home/test/.ssh/authorized_keys'

    os.makedirs(ssh_dir, mode=0777)
    os.chmod(path=ssh_dir, mode=700)

    os.makedirs(key_dir, mode=0777)
    os.chmod(path=key_dir, mode=600)
