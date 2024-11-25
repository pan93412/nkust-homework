import socket
import ssl

ssl_ctx = ssl.SSLContext()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    ssl_sock = ssl_ctx.wrap_socket(s)
    ssl_sock.connect(
        ("140.133.78.64", 443)
    )

    # send HTTP/1.1 content
    ssl_sock.sendall(b'GET / HTTP/1.1\r\nHost: www.nkust.edu.tw\r\n\r\n')

    # receive response
    data = ssl_sock.recv(1024)
    print(data.decode())
