# raw-file: ch1_3.py
import json

if __name__ == "__main__":
    players = {
        "Stephen Curry": "Golden State Warriors",
        "Kevin Durant": "Golden State Warriors",
        "Lebron James": "Cleveland Cavaliers",
        "James Harden": "Houston Rockets",
        "Paul Gasol": "San Antonio Spurs",
    }
    json_obj1 = json.dumps(players)  # 未用排序將字典轉成 JSON 物件
    json_obj2 = json.dumps(players, sort_keys=True)  # 有用排序將字典轉成 JSON 物件
    print("未用排序將字典序列化為 JSON", json_obj1, sep="\t")
    print("使用排序將字典序列化為 JSON", json_obj2, sep="\t")
    print("有排序與未排序物件是否相同", json_obj1 == json_obj2, sep="\t")
    print("序列化完成的 JSON 在 Python 的資料類型 ", type(json_obj1), sep="\t")
