"""
Justin Wu
Lab 9, Unit Testing
Feb 26, 2026
"""

import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    # Runs before every test
    def setUp(self):
        self.account = BankAccount("Justin", 100)

    # Test initialization
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    # Test deposit adds money
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    # Test withdraw subtracts money
    def test_withdraw(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    # Test withdrawing too much raises error
    def test_withdraw_over_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    # Test deposit negative amount raises error
    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    # Test withdraw negative amount raises error
    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-5)

    # Test multiple transactions
    def test_multiple_transactions(self):
        self.account.deposit(50)     # 150
        self.account.withdraw(20)    # 130
        self.account.deposit(30)     # 160
        self.account.withdraw(60)    # 100
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()
