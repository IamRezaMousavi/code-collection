# @Author: @IamRezaMousavi
# @Date:   2022-03-09 01:02:48
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-09 03:06:33

import socket
import threading


def main():
    ip = '127.0.0.1'
    port = 8731

    tSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tSocket.bind((ip, port))
    tSocket.listen(5)

    client, addr = tSocket.accept()
    print('Got connecting from', addr)

    def send():
        while True:
            message = input('[YOU] >>>')
            client.send(message.encode())

    def get():
        while True:
            print(f'\r[{addr[0]}] >>>', client.recv(1024).decode())
            print('\r[YOU] >>>', end='')

    tSend = threading.Thread(target=send)
    tGet = threading.Thread(target=get)

    tSend.start()
    tGet.start()

    tSend.join()
    tGet.join()

    client.close()


if __name__ == '__main__':
    main()
