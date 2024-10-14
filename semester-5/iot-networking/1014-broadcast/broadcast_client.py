import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

PORT=5255
s.bind(('', PORT))

print('Listening for broadcast at', s.getsockname())

while True:
    try:
        data, address = s.recvfrom(65535)
        print(f"Received {len(data)} bytes from {address}. Data: ")
        print(data.decode('utf-8'))
        print("\n\n")
    except (KeyboardInterrupt, SystemExit):
        break
    except Exception as e:
        print(e)

s.close()
