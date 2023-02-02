import hashlib

# Test code to show of SonarQube
# By: Peter Baker

username = input("Please enter your username")
password = input("Please enter your password")

print(f"Your username is " + username)
print(f"Your password is " + password)
m = hashlib.md5()
m.update(b"password")

print(m.hexdigest())