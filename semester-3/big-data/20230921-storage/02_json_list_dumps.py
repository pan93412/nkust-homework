# raw-file: ch1_1.py
import json

if __name__ == "__main__":
    list_numbers = [5, 10, 20, 1]  # 串列資料
    tuple_numbers = (1, 5, 10, 9)  # 元組資料
    json_data1 = json.dumps(list_numbers)  # 將串列資料轉成 JSON 資料
    json_data2 = json.dumps(tuple_numbers)  # 將串列資料轉成 JSON 資料
    print(f"串列轉換成 JSON 的陣列: {json_data1=}")
    print(f"元組轉換成 JSON 的陣列: {json_data2=}")
    print(f"JSON 陣列在 Python 的資料類型: {type(json_data1)}")
