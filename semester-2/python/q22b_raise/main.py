def checkZeroNumber(num: int):
    if num > 0:
        raise ValueError("數值大於 0")
    elif num < 0:
        raise ValueError("數值小於 0")

try:
    checkZeroNumber(0)
except Exception as e:
    print(f"0 Error: {e}")
else:
    print(f"0 Pass")

try:
    checkZeroNumber(1)
except Exception as e:
    print(f"1 Error: {e}")

try:
    checkZeroNumber(-1)
except Exception as e:
    print(f"-1 Error: {e}")
