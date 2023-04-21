import account
import unittest



"Testing code for account"

class account_tests(unittest.TestCase):
    
        
    def test_start_up(self):
        self.assertRaises(TypeError, account.Account)
        self.assertRaises(TypeError, account.Account, 1, 53)
    
    def test_deposit(self):
        self.assertEqual(account.Account("Nick").deposit(5), True)
        self.assertEqual(account.Account("Nick").deposit(0), False)
        self.assertEqual(account.Account("Nickd").deposit(-1), False)
    
    def test_withdraw(self):
        self.assertEqual(account.Account("Gerald").withdraw(6), False)
        self.assertEqual(account.Account("Gerald").withdraw(0), False)
        self.assertEqual(account.Account("G").withdraw(-1), False)

testy = account_tests()
testy.test_start_up()
testy.test_deposit()
testy.test_withdraw()

" Now Using PyTest "

def test_start():
    try:
        account.Account()
        assert False
    except:
        assert True
    
    try:
        account.Account("a", "b")
        assert False
    except:
        assert True

def test_dep():
    assert account.Account("Nick").deposit(5) == True
    jam = account.Account("Jammy")
    jam.deposit(5)
    assert jam.deposit(0) == False
    assert jam.deposit(-1) == False

def test_with():
    jam = account.Account("James")
    jam.deposit(10)
    jam.withdraw(1)
    assert jam.withdraw(0) == False
    assert jam.withdraw(-1) == False
    assert jam.withdraw(100) == False

test_start()
test_dep()
test_with()
    
