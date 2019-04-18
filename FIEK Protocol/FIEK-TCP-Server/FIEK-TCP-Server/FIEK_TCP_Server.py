import socket 
import datetime
import sys
import os
import platform
import random
from random import choice
from _thread import *

def IPADRESA():
    z="IP Adresa e klientit eshte: "+ addr[0]
    socketKlienti.sendall(str.encode(str(z)))
def NUMRIIPORTIT():
    z="Klienti eshte duke perdorur portin "+ str(addr[1])
    socketKlienti.sendall(str.encode(z))
def BASHKETINGELLORE(a):
    nribashketingelloreve = 0
    bashk=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
    z=a.lower()
    for x in z:
        if x in bashk:
            nribashketingelloreve += 1
    a=('Teksti i pranuar permban %d bashketingellore'%nribashketingelloreve)
    socketKlienti.sendall(str.encode(a))
def PRINTIMI(a):
    socketKlienti.sendall(str.encode(a))
def EMRIIKOMPJUTERIT():
    z=socket.getfqdn(servername)
    socketKlienti.sendall(str.encode(z))
def KOHA():
    y = datetime.datetime.now()
    z=(y.strftime("%d")+'.'+y.strftime("%m")+'.'+y.strftime("%y")+' '+y.strftime("%I")+':'+y.strftime("%M")+':'+y.strftime("%S")+' '+y.strftime("%p"))
    socketKlienti.sendall(str.encode(z))
def LOJA():
    z='('
    sequence = [i for i in range(50)]
    for _ in range(7):
        selection = choice(sequence)
        z=z+str(selection)+' '
    z=z+')jane 7 numra te rastesishem nga 49.'
    socketKlienti.sendall(str.encode(z))
def FIBONACCI(n):
    a=0
    b=1
    for i in range(0, n):
        c=a
        a=b
        b=c+b
    return b
def KONVERTIMI(a,b):
    if(a=="KILOWATTOHORSEPOWER"):
        z=int(b)*1.34102209
    elif(a=="HORSEPOWERTOKILOWATT"):
        z=int(b)/1.34102209
    elif(a=="DEGREESTORADIANS"):
        z=int(b)*0.0174532925
    elif(a=="RADIANSTODEGREES"):
        z=int(b)/0.0174532925
    elif(a=="GALLONSTOLITERS"):
        z=int(b)*3.78541178
    elif(a=="LITERSTOGALLONS"):
        z=int(b)/3.78541178
    else:
        z="Nuk eshte shkruar mire kerkesa per konvertim."
    socketKlienti.sendall(str.encode(str(z)))
def VERSIONIIPYTHON():
    z=sys.version
    socketKlienti.sendall(str.encode(z))
def VERSIONIIOS():
    z=platform.machine()+"    "+platform.platform()+"    "+platform.node()+"    "+platform.processor()
    socketKlienti.sendall(str.encode(z))
def NOFUN():
    z='Nuk keni shenuar funksion valid.'
    socketKlienti.sendall(str.encode(str(z)))

def kerkesat(op):
    op = op.split()
    if(op[0]=="IPADRESA"):
        IPADRESA()
    elif(op[0]=="NUMRIIPORTIT"):
        NUMRIIPORTIT()
    elif(op[0]=="BASHKETINGELLORE"):
        BASHKETINGELLORE(op[1])
    elif(op[0]=="PRINTIMI"):
        PRINTIMI(op[1])
    elif(op[0]=="EMRIIKOMPJUTERIT"):
        EMRIIKOMPJUTERIT()
    elif(op[0]=="KOHA"):
        KOHA()
    elif(op[0]=="LOJA"):
        LOJA()
    elif(op[0]=="FIBONACCI"):
        a = FIBONACCI(op[1])
        socketKlienti.sendall(str.encode(str(a)))
    elif(op[0]=="KONVERTIMI"):
        KONVERTIMI(op[1], op[2])
    elif(op[0]=="VERSIONIIPYTHON"):
        VERSIONIIPYTHON()
    elif(op[0]=="VERSIONIIOS"):
        VERSIONIIOS()
    else:
        NOFUN()
def clientthread(socketKlienti):
    try:
        while True:
            opsioni = socketKlienti.recv(1024).decode()
            kerkesat(opsioni)
        socketKlienti.close()
    except:
        print("Error")

servername ='localhost'
serverport = 12000
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((servername, serverport))
print('================================================================================================')
print('Ky eshte programi FIEK-TCP Server.')
print('Serveri eshte duke punuar ne portin '+ str(serverport)+'. Ky port mund te ndryshohet nga klienti sipas nevojes.')
serversocket.listen()
print('Serveri eshte gati per te pranuar kerkesa.')
print('================================================================================================')

while True:
    try:
        socketKlienti, addr = serversocket.accept()
        print("Klienti i lidhur ne portin "+str(addr[1]))
        start_new_thread(clientthread, (socketKlienti, ))
    except:
        print("Error 2")

serversocket.close()