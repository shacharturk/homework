import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    condition = True
    s.connect(("localhost", 5050))
    while condition:
        s.sendall(input("guess code: ").encode())
        data = s.recv(1024).decode()
        print(data)
        if data == "your score is: ['B', 'B', 'B', 'B']":
            print("you have won!")
            s.close()
            condition = False
