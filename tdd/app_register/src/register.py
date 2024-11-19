import re

def register(username: str, email: str, password:str)->bool:
    """Function that tests the validity of the username, email and password

    Args:
        username (str): It must not have empty spaces or being empty
        email (str): It must contain @ and .
        password (str): It must be 8 character long, at least 1 number, at least 1 letter and at least 1 special character

    Returns:
        bool: Returns True if all the checks are passed, False otherwise
    """
    # Setting the default case
    check_username = True
    check_email = True
    check_password = True

    # Checking the username
    if (username == '') or (' ' in username):
        check_username = False

    # Checking the email
    # Regex to check both @ and .
    pattern = r"@.*\."

    if not re.search(pattern, email):
        check_email = False

    # Checking the password
    if len(password)<8:
        check_password = False

    # Checking that we have the required complexity
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"


    if check_password and not re.match(pattern, password):
        check_password = False

    # The output is simply the multiplication of 3 booleans: if one is false, it is all false
    return check_username * check_email * check_password
