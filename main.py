import bcrypt

# Converting password into bytes
password = b'thisismypassword'

# Implementing password hashing + adding salt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# Accepting password from user
entered_password = input('Enter password to login: ')
entered_password = bytes(entered_password, encoding='utf-8')

# Comparing entered password with the original one
if bcrypt.checkpw(entered_password, hashed):
    print('Login successful')
else:
    print('Invalid password')
