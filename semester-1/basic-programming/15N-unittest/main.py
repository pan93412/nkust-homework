# 這是一個用來在考試前進行 Unit Test 和 E2E Test 的範例

def main():
    m = map(lambda m: int(input(f"輸入數字 {m}：")), range(1, 4))

    print(f"1000")
    print(12, 24, 36)
    print(1000)
    print(sum(m))

if __name__ == "__main__":
    main()
