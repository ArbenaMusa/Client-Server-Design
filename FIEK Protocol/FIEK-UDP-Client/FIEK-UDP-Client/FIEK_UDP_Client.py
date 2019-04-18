import socket

print('=====================================================================================================================')
print('Ky eshte programi FIEK-TCP Client.')
print('Klienti eshte gati per te komunikuar me serverin.')
print('=====================================================================================================================')
print('')

servername='localhost'
port=12000

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as clientsocket:
    while True:
        print('Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, VERSIONIIPYTHON, VERSIONIIOS)?')
        var=input().upper().encode()
        if var=='':
            break
        clientsocket.sendto(var, (servername, port))
        message, address= clientsocket.recvfrom(128)
        print(repr(message.decode()))
