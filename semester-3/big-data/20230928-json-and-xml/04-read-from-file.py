import json

if __name__ == '__main__':
    with open("03-write-to-file.txt", "r") as f:
        data = json.load(f)

        print(data)
        print(type(data))
