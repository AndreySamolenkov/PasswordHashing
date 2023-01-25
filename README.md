This is a Python script that uses the bcrypt library to hash a password and then compare it to a user-entered password.
The script first converts the original password into bytes and then hashes it using bcrypt's hashpw function, 
which takes the password and a randomly generated salt as arguments. 
The hashed password with the salt is then stored. When a user enters a password, 
it is converted to bytes and then compared to the original hashed password using bcrypt's checkpw function. 
If the comparison is successful, the script prints "Login successful". 
If the comparison fails, it prints "Invalid password".
