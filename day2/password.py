import re

def is_strong_password(password):
   
    password_pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.search(password_pattern, password))

passwords = ["Abcd1234", "Password", "StrongP@ss", "short1"]

for password in passwords:
    if is_strong_password(password):
        print(password + " is a strong password.")
    else:
        print(password + " is not a strong password.")

