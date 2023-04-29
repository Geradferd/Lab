import account
import unittest



"Testing code for account"


" Now Using PyTest "

def test_init():
    """
    makes sure that a TypeError will happen when you have 0 or more
    than 2 arguments

    Returns
    -------
    None.

    """
    jay = account.Account("Jay")
    assert jay.get_name() == "Jay"
    assert jay.get_balance() == 0
    
    try:
        account.Account
        assert False
    except:
        assert True
    
    try:
        account.Account("a", "b")
        assert False
    except:
        assert True

def test_deposit():
    """
    Checks for if a number can be added to the balance,
    if False is returned when entering 0 or less

    Returns
    -------
    None.

    """
    assert account.Account("Nick").deposit(5) == True
    jam = account.Account("Jammy")
    jam.deposit(5)
    assert jam.deposit(0) == False
    assert jam.deposit(-1) == False
    assert jam.deposit(1) == True
    assert jam.get_balance() == 6

def test_withdraw():
    """
    Checks if false will be returned when you try and withraw 0, a negative
    number or more than what your balance is

    Returns
    -------
    None.

    """
    jam = account.Account("James")
    jam.deposit(10)
    assert jam.withdraw(1) == True
    assert jam.withdraw(0) == False
    assert jam.withdraw(-1) == False
    assert jam.withdraw(100) == False
    assert jam.get_balance() == 9

test_init()
test_deposit()
test_withdraw()
    
