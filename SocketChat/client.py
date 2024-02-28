# @Author: @IamRezaMousavi
# @Date:   2022-03-09 01:08:21
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-09 03:06:35

import socket
import threading


def main():
    ip = '127.0.0.1'
    port = 8731

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    def send():
        while True:
            message = input('[YOU] >>>')
            s.send(message.encode())

    def get():
        while True:
            print(f'\r[{ip}] >>>', s.recv(1024).decode())
            print('\r[YOU] >>>', end='')

    tSend = threading.Thread(target=send)
    tGet = threading.Thread(target=get)

    tSend.start()
    tGet.start()

    tSend.join()
    tGet.join()

    s.close()


if __name__ == '__main__':
    main()
