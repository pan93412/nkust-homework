import os
import socket


def main():
    hostname = os.environ.get("HOSTNAME", "0.0.0.0")
    port = int(os.environ.get("PORT", 80))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((hostname, port))

        s.sendall(b"GET / HTTP/1.1\r\nHost:127.0.0.1\r\n\r\n")

        server_response = str(s.recv(1024), "utf-8")
        print(f"Server response:\n{server_response}")


if __name__ == "__main__":
    main()
