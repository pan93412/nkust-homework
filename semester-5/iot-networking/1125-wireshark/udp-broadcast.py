import socket
import time


MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
MCAST_TTL = 2

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MCAST_TTL)

        while True:
            payload = "WireShark Class, 潘奕濬, C111156103"

            print(f"Sending {payload!r} at {time.strftime('%H:%M:%S')}")
            sock.sendto(payload.encode(), (MCAST_GRP, MCAST_PORT))
            time.sleep(1)


if __name__ == "__main__":
    main()
