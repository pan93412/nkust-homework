import json

d = {
    "名稱": "約翰",
    "年齡": 18,
}

if __name__ == "__main__":
    # 建立一個 file handle
    with open("text.txt", "w") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)
