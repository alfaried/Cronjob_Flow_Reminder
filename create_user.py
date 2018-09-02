import subprocess

def addUser(username):
    bashCommand = 'sudo adduser ' + username

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output, error

if __name__ == "__main__":
    output, error = addUser('test')
    print(output)
