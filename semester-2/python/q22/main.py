x = [1, 2, 3]

try:
    print(f"{x[4]=}")
except IndexError:
    print("Index out of range")
else:
    print("No error")
finally:
    print("Finally")
