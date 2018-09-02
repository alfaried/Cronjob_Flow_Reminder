# Create a new user
sudo adduser test

# Create folder '.ssh'
sudo mkdir /home/test/.ssh
sudo chown test:test /home/test/.ssh
sudo chmod 700 /home/test/.ssh

# Create file 'authorized_keys'
sudo touch /home/test/.ssh/authorized_keys
sudo chown test:test /home/test/.ssh/authorized_keys
sudo chmod 600 /home/test/.ssh/authorized_keys

# Need to add the public key into the .ssh/authorized_keys file
sudo nano /home/test/.ssh/authorized_keys