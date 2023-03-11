import socket

# Se crea el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se vincula el socket al puerto y dirección
server_address = ('localhost', 8888)
server_socket.bind(server_address)

# Se escucha por conexiones entrantes
server_socket.listen(1)

print('Esperando conexiones entrantes...')

while True:
    # Se espera por una conexión
    client_socket, client_address = server_socket.accept()
    print(f'Conexión entrante desde {client_address}')

    # Se recibe y se envía de vuelta un mensaje de prueba
    message = client_socket.recv(1024)
    print(f'Recibido: {message.decode()}')
    response = f'Hola, {message.decode()}'
    client_socket.send(response.encode())

    # Se cierra la conexión
    client_socket.close()

    print(f'Conexión desde {client_address} cerrada')
