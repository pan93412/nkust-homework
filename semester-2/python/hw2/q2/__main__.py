from .decryptor import Decryptor


y = input() # 讀取輸入的密文Y
decryptor = Decryptor(y)
x = decryptor.decrypt()
print(x)
