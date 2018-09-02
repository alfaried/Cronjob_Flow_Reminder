import os
import subprocess

# Return output : tuple, error : default-None
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return True is user is create. ELSE False
def addValidUser(username):
    try:
        bashCommand = 'sudo adduser ' + username
        executeBash(bashCommand)

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
    except:
        return False

    return True


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
    delUser('test')
    print(addValidUser('test'))
