import bcrypt

plain_text_password = "Magic123"

def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode("utf-8")
    salt = bcrypt.gensalt()
    bcrypted_password = bcrypt.hashpw(password_bytes, salt)
    return (bcrypted_password).decode("utf-8")



def check_password(plain_text_password, hash_password):
    password_bytes = plain_text_password.encode("utf-8")
    hash_password_bytes = hash_passwords.encode("utf-8")
    if bcrypt.checkpw(password_bytes, hash_password_bytes):
        print("Password is correct")
    else:
        print("Password is correct")


user_name =input("What is your name")
password = input("What is your password ")
h_password = hash_password(password)
print(f"Your hashed password is:{h_password}")
