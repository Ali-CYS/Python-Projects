import hashlib # hashlib is used for hashing the password
import os      # here this is used for generating a random salt

def hash_password(input_password):       # a function defined to hash the password
    salt = os.urandom(16).hex()          # generates a random salt by using os.urandom
    # .hex () function converts the bytes to a hexadecimal string
    hashed = hashlib.sha256((salt+input_password).encode()).hexdigest() # hashes the password with the salt using SHA-256
    # .encode() converts the string to bytes, and .hexdigest() returns the hash as a hexadecimal string

    return salt,hashed # returns the salt and the hashed password

def store_hash(salt, hashed_password):            # a function to store the salt and hashed password in a file
    with open("passwords.txt", "a") as file:      #opens the file in append mode
        file.write(f"{salt}:{hashed_password}\n") # writes the salt && hashed password in the file separated by a colon
        file.close()

def verify_password(input_password):          # a function to verify the input password against the  stored hashes
    with open("passwords.txt", "r") as file:  # opens the file in read mode
        stored_hashes = file.readlines()      # readlines() reads all lines in the file
        
    for line in stored_hashes:  #for loop runs through each line in the file
        salt, hashed_password = line.strip().split(":")#splits the line into salt and hashed password as they are separated by a colon
        #strip() removes any whitespace characters
        if hashed_password == hashlib.sha256((salt+input_password).encode()).hexdigest(): # same function as in hash_password
            return True         # returns True if the hashed password matches the stored hash

    return False

# Main program to test the hashing and verification
password = input("Set your password: ")
salt, hashed_password = hash_password(password)
store_hash(salt, hashed_password)
print("Password hashed and stored.")

check = input("Enter password to verify: ")
if verify_password(check):
    print(" Password matched!")
else:
    print(" Incorrect password.")
