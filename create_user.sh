# Delete current user
sudo userdel -r test

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

# Add the public key into the .ssh/authorized_keys file
sudo bash -c "echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuFnDJYM1KoZQT4YR5d3dDE59E1SiWf1sYiQC0CoEg/2mwWHTdu+m4NfPQWsLOazYy3h7F0xZKd64TOWy9jY/LrB4JWTVuTNajGysM/7bwehmeFkC8Nf4R50bg3IwnIoclt52pV259YP/NjVoyXWxkyRV7ATvFacY9nkBpYAF2eloukcdJR2OYn5GKs6aJfnKWNjuLgeQUtMZU9nqiSCNK6tPc7u6jZI7iQm9ev0hP3WEYwZGstO8HZFGofrk199n7tOhKCpIFn1e85pvtDilN160FFly7aNPGm9J4/A4wq6EWzEETUVKDl7fGaKMviLfiFCOgTzsq7VCvgFzUdrrr >> /home/test/.ssh/authorized_keys"
