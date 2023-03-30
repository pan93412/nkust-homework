from q9 import Account

class TestAccount:
    def test_init(self):
        Account(1234)

    def test_balance(self):
        assert Account(1234).balance() == 1234

    def test_despoit(self):
        account = Account(1234)
        account.despoit(100)

        assert account.balance() == 1234+100

    def test_withdraw(self):
        account = Account(1234)
        assert account.withdraw(100) == 100
        assert account.balance() == 1234-100

    def test_add_interest(self):
        account = Account(1000)
        account.add_interest(0.1)

        assert account.balance() == 1100
