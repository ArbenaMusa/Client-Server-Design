import socket

print('=====================================================================================================================')
print('Ky eshte programi FIEK-TCP Client.')
print('Klienti eshte gati per te komunikuar me serverin.')
print('=====================================================================================================================')
print('')
print("A doni te caktoni vete serverin dhe portin qe deshironi te perdorni?")
pergjigja=input().upper()
if(pergjigja=="PO"):
    print("Jep emrin e serverit:")
    servername=input().lower()
    print("Jep numerin e portit")
    p=input()
    port=int(p)
else:
    servername='localhost'
    port=12000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((servername,port))
    while True:
        print('Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKLIENTIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, VERSIONIIPYTHON, VERSIONIIOS)?')
        var=input().upper().encode()
        if var=='':
            break
        clientsocket.sendall(var)
        r=clientsocket.recv(128).decode()
        print(repr(r))
