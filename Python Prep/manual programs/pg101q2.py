class PasswordError(Exception):
    pass

def check_password(password):
    correct_password = "mysecretpassword"
    if password != correct_password:
        raise PasswordError("Incorrect password")

# Example usage
try:
    check_password("wrongpassword")
except PasswordError as e:
    print(e)
