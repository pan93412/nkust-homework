def checkSpeed(speed: int):
    if speed > 120:
        raise ValueError("速度過快")
    elif speed < 120:
        raise ValueError("速度過慢")

for n in [121,119,120]:
    try:
        checkSpeed(n)
    except Exception as e:
        print(f"{n} Error: {e}")
    else:
        print(f"{n} Pass")
