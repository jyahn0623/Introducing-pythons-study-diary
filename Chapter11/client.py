import socket

server_address = ('localhost', 8009)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(4096)

print('At', server, 'said', data)
client.close()

# 서버와 bind()를 제외한 나머지 코드는 비슷.