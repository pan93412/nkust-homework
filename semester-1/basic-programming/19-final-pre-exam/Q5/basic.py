'''Q5 (not really basic)

For some details, see README.md'''

def decrypt_chunk(c: int, n: int = 0) -> int:
    # 檢查 c 是否在我們在 README.md 推導出的範圍內
    if not 0 - c <= 7 * n <= 36 - c:
        # 如果不在範圍內，則拋出例外。
        raise ValueError("無法解密")

    # guessed_r 是我們猜測的 r
    guessed_r = (7 * n + c) / 4
    # 檢查 r 是不是個整數
    if guessed_r.is_integer():
        return int(guessed_r)

    # 不是的話，那 n 則不是我們要的答案。
    # 這裡用到 tail recursion 讓編譯器可以最佳化
    return decrypt_chunk(c, n + 1)


def decrypt(p: str) -> str:
    # 檢查密碼是不是數字
    if not p.isdigit():
        raise ValueError("密碼必須是數字")

    # "分割符號".join(迭代器)
    return "".join(
        # 這裡建立了一個迭代器，從 p 中取出每個字元 (為 c)
        # 先將其轉換成 int，然後解密，再轉回字串。
        str(decrypt_chunk(int(c)))
        for c in p
    )


# 這句話的意思是「如果這是以模組的方式載入 (import)，就不要執行」
if __name__ == "__main__":
    pwd = input("請輸入傳送密碼：")
    print(f"解密後的密碼是：{decrypt(pwd)}")
