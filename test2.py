import hashlib

# Test code to show of SonarQube
# By: Peter Baker

username = input("Please enter your username")
password = input("Please enter your password")

m = hashlib.md5()
m.update(b"password")

print(m.hexdigest())