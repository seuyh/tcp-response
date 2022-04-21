import socket
from re import match

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
mysocket.bind(('127.0.0.1', 9879))
mysocket.listen(5)
print('server is running, send data "quit" to stop')
close = 0
while not close:
    (client, (ip, port)) = mysocket.accept()
    print("new connection {address}".format(address=client))
    data = client.recv(buffer_size)
    client_data = data.decode()
    # это нужно так как получение данных с сервера обращает символ переноса строки \n в строку
    if client_data[-2:] == "\\n":
        client_data = client_data[:-2] + '\n'
    print(f'client_data: {client_data}')
    if match('\d{2}:\d{2}:\d{2}', client_data[8:17]):
        with open('log.txt', 'a') as f:
            f.write(client_data)
        if client_data[-3:-1] == '00':
            response = \
                f'спортсмен, нагрудный номер {client_data[:4]} прошёл отсечку {client_data[5:7]} в {client_data[8:17]}'
            print(response)
            client.send(bytes(response, 'utf-8'))
    elif client_data != 'quit':
        client.send(b"Unknown data format")
    if data.decode() == 'quit':
        close = 1
