# Program 4A3
# Katie Devinney
# Checks a string for "strong password" criteria

specialCharacters = '!&*%$'
digits = '0123456789'

hasSpecial = False
hasNumber = False

password = input("Enter a password: ")

for character in range(0, len(password)):
    if password[character] in specialCharacters:
        hasSpecial = True
    if password[character] in digits:
        hasNumber = True

if len(password) < 8:
    print("Password should be at least 8 characters.")

if not hasNumber and not hasSpecial:
    print("Your password needs at least one number and one special character.")
elif not hasSpecial and hasNumber:
    print("Your password needs at least one special character.")
elif not hasNumber and hasSpecial:
    print("Your password needs at least one number.")
else:
    print("Password looks great!")