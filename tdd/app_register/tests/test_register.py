from app_register.src import register
import pytest
import io

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

#### Using Monkeypatch

def test_email_with_user_input_no_at_sign(monkeypatch):
    """Test if an email is missing @

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert register.get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    """Test if email has missing .

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adalatascom'))
    assert register.get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    """Test if email is correct

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin',io.StringIO('petra@adaltas.com'))
    assert register.get_email_from_input() == 'petra@adaltas.com'

def test_empty_username(monkeypatch):
    """Test if an username is missing empty

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO(" "))
    assert register.get_username_from_input() is None

def test_correct_username(monkeypatch):
    """Test if a username is correct

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("azert12344"))
    assert register.get_username_from_input() == "azert12344"

def test_short_password(monkeypatch):
    """Test if the pasword is too short

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("1234@aq"))
    assert register.get_password_from_input() is None

def test_password_without_special_character(monkeypatch):
    """Test if the pasword has not a special character

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("12341aqa"))
    assert register.get_password_from_input() is None

def test_password_without_character(monkeypatch):
    """Test if the pasword has no character

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("12341@12"))
    assert register.get_password_from_input() is None


def test_password_without_digits(monkeypatch):
    """Test if the pasword has no digits

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("azert@aq"))
    assert register.get_password_from_input() is None

def test_correct_password(monkeypatch):
    """Test if the pasword is correct

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("12345@aq"))
    assert register.get_password_from_input() == "12345@aq"

def test_wrong_password(monkeypatch):
    """Test a wrong password

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("azert@aq"))
    assert register.get_password_from_input() is None

def test_wrong_password1(monkeypatch):
    """Test a wrong password

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr('sys.stdin', io.StringIO("azert@aq"))
    assert register.get_password_from_input() is None