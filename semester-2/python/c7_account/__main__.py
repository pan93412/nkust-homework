from decimal import Decimal
from account import Account


account = Account(Decimal("1000"))
account.withdraw(100)
print(account)
