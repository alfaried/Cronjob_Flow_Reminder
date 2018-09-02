import subprocess

# Return byte type : output, error
def executeBash(bashCommand):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()


# Return byte type : output, error
def addUser(username):
    bashCommand = 'sudo adduser ' + username
    return executeBash(bashCommand)


# Return byte type : output, error
def accessUser(username):
    bashCommand = 'sudo su - ' + username
    return executeBash(bashCommand)


if __name__ == "__main__":
    output, error = addUser('test')
    print('Creating user..')
    print(output)
    print(error)
    print('\n')

    output, error = accessUser('test')
    print('Accessing user..')
    print(output)
    print(error)
    print('\n')
