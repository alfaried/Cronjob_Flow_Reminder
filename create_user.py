import os
import shlex, subprocess

# Return output : tuple, error : default-None
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return True is pk is added. ELSE raise Exception
def addPublicKey(username=None,public_key=None):
    if username == None or public_key == None:
        raise Exception('Please define a username and a public key')

    if 'ssh-rsa' not in public_key:
        public_key = 'ssh-rsa' + public_key

    pk_dir = '/home/' + username + '/.ssh/authorized_keys'
    # bashCommand_1 = 'sudo bash -c "echo \'# ' + username + ' public key\' >> ' + pk_dir + '"'
    # bashCommand_2 = 'sudo bash -c "echo \'' + public_key + '\' >> ' + pk_dir + '"'
    # bashCommand_1 = 'sudo bash -c "echo hi >> ' + pk_dir + '"'
    bashCommand_1 = 'sudo bash -c "echo hi >> /home/test/.ssh/authorized_keys"'

    try:
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


# ============================================================================ #
# ============================================================================ #
# ============================================================================ #


if __name__ == "__main__":
    # Run test commands here
    delUser('test')
    addUser('test','ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuFnDJYM1KoZQT4YR5d3dDE59E1SiWf1sYiQC0CoEg/2mwWHTdu+m4NfPQWsLOazYy3h7F0xZKd64TOWy9jY/LrB4JWTVuTNajGysM/7bwehmeFkC8Nf4R50bg3IwnIoclt52pV259YP/NjVoyXWxkyRV7ATvFacY9nkBpYAF2eloukcdJR2OYn5GKs6aJfnKWNjuLgeQUtMZU9nqiSCNK6tPc7u6jZI7iQm9ev0hP3WEYwZGstO8HZFGofrk199n7tOhKCpIFn1e85pvtDilN160FFly7aNPGm9J4/A4wq6EWzEETUVKDl7fGaKMviLfiFCOgTzsq7VCvgFzUdrrr')
