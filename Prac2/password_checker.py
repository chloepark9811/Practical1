MIN_LENGTH = 2
MAX_LENGTH = 7
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("Please enter a password between", MIN_LENGTH, "and", MAX_LENGTH,".")
        password = input("> ")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0:
        return False
    if count_upper == 0:
        return False
    if count_digit == 0:
        return False
    if count_special == 0:
        return False


    print("You have {} lowercase characters, {} uppercase characters, {} digits and {} special characters.".format(count_lower,count_upper,count_digit,count_special))
    return True

main()