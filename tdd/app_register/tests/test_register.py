from app_register.src import register

def test_username():
    """Test function for the username
    """
    # Testing the empty case
    assert register.register('','toto@gmail.com','1234@aze') == False
    # Testing the space case
    assert register.register('rr rr','toto@gmail.com','1234@aze') == False

def test_email():   
    """Test function for the email
    """
    # Testing the email without @
    assert register.register('username','totogmail.com','1234@aze') == False
    # Testing the email without .
    assert register.register('username','toto@gmailcom','1234@aze') == False

def test_password():
    """Test function for the password
    """
    # Testing the case with less than 8 characters
    assert register.register('username','toto@gmail.com','1234@az') == False
    # TEsting the case with missing digits
    assert register.register('username','toto@gmail.com','abcd@azd') == False
    # Testing the case with missing characters
    assert register.register('username','toto@gmail.com','1234@123') == False
    # TEsting the case with missing special character
    assert register.register('username','toto@gmail.com','12341123') == False
