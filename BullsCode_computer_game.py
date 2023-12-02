from BullsCode_instantiation import BullsCode
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("localhost", 5050))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        while True:
            combination = BullsCode()
            condition = False
            for i in range(0, 10):
                guess = conn.recv(1024).decode()
                print(guess)
                #guess = str(input("please guess a four digits code: "))
                score = combination.check(guess)
                print(score)
                conn.send(f"your score is: {score}".encode())
                if score == ['B', 'B', 'B', 'B']:
                    condition = True
                    break
            if condition:
                conn.send(b"you have won!")
            else:
                conn.send(f"you have lost, this is the correct answer: {combination.get_answer()}".encode())
            conn.close()
