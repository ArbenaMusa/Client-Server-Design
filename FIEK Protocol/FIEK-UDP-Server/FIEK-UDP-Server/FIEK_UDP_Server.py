import socket 
import datetime
import sys
import platform
import random
from random import choice

def IPADRESA():
    z="IP Adresa e klientit eshte: "+ address[0]
    serversocket.sendto(str.encode(z), address)
def NUMRIIPORTIT():
    z="Klienti eshte duke perdorur portin "+ str(address[1])
    serversocket.sendto(str.encode(z), address)
def BASHKETINGELLORE(a):
    nribashketingelloreve = 0
    bashk=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","z"]
    z=a.lower()
    for x in z:
        if x in bashk:
            nribashketingelloreve += 1
    a=('Teksti i pranuar permban %d bashketingellore'%nribashketingelloreve)
    serversocket.sendto(str.encode(a), address)
def PRINTIMI(a):
    serversocket.sendto(str.encode(a), address)
def EMRIIKLIENTIT():
    try:
        z="Emri i klientit eshte: "+socket.getfqdn(servername)
    except:
        z="Emri i klientit nuk mund te gjindet."
    serversocket.sendto(str.encode(z), address)
def KOHA():
    y = datetime.datetime.now()
    z=(y.strftime("%d")+'.'+y.strftime("%m")+'.'+y.strftime("%y")+' '+y.strftime("%I")+':'+y.strftime("%M")+':'+y.strftime("%S")+' '+y.strftime("%p"))
    serversocket.sendto(str.encode(z), address)
def LOJA():
    z='('
    sequence = [i for i in range(50)]
    for _ in range(7):
        selection = choice(sequence)
        z=z+str(selection)+' '
    z=z+')jane 7 numra te rastesishem nga 49.'
    serversocket.sendto(str.encode(z), address)
def FIBONACCI(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    serversocket.sendto(str.encode(str(a)), address)
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
    serversocket.sendto(str.encode(str(z)), address)
def VERSIONIIPYTHON():
    z=sys.version
    serversocket.sendto(str.encode(z), address)
def VERSIONIIOS():
    z=platform.machine()+"    "+platform.platform()+"    "+platform.node()+"    "+platform.processor()
    serversocket.sendto(str.encode(z), address)
def NOFUN():
    z=' '
    serversocket.sendto(str.encode(z), address)

def kerkesat(op):
    opi=op
    op = op.split()
    if(op[0]=="IPADRESA"):
        IPADRESA()
    elif(op[0]=="NUMRIIPORTIT"):
        NUMRIIPORTIT()
    elif(op[0]=="BASHKETINGELLORE"):
        BASHKETINGELLORE(opi[17:])
    elif(op[0]=="PRINTIMI"):
        PRINTIMI(opi[9:])
    elif(op[0]=="EMRIIKLIENTIT"):
        EMRIIKLIENTIT()
    elif(op[0]=="KOHA"):
        KOHA()
    elif(op[0]=="LOJA"):
        LOJA()
    elif(op[0]=="FIBONACCI"):
        FIBONACCI(int(op[1]))
    elif(op[0]=="KONVERTIMI"):
        KONVERTIMI(op[1], op[2])
    elif(op[0]=="VERSIONIIPYTHON"):
        VERSIONIIPYTHON()
    elif(op[0]=="VERSIONIIOS"):
        VERSIONIIOS()
    else:
        NOFUN()

servername ='localhost'
serverport = 12000
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((servername, serverport))
print('================================================================================================')
print('Ky eshte programi FIEK-TCP Server.')
print('Serveri eshte duke punuar ne portin '+ str(serverport)+'. Ky port mund te ndryshohet nga klienti sipas nevojes.')
print('Serveri eshte gati per te pranuar kerkesa.')
print('================================================================================================')

while True:
    try:
        while True:
            message, address = serversocket.recvfrom(128)
            kerkesat(message.decode())
    except:
         print("Error")