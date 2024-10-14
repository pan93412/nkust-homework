import socket

multicast_addr = '224.1.2.3'
bind_addr = '0.0.0.0'
port = 9917
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((bind_addr, port))
while True:
    try:
        message, address = sock.recvfrom(64)
        print(f"Server received from {address}, message is {message.decode('utf-8')}")
    except (KeyboardInterrupt, SystemExit):
        break
    except Exception as e:
        print(e)

sock.close()
