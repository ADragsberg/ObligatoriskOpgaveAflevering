from socket import *
import random
import threading
# virker ikke helt endnu. Kan Kommandoerne går igennem men kan ikke få funktionerne til at virke ordentligt endnu.

def readClientString(clientString):
    if clientString != 'quit':
       splitString = clientString.split(';')
       command = splitString[0]
       match command:
           
        case 'Random':
              lowerLimit = int(splitString[1])
              upperLimit = int(splitString[2])
              result = random.randint(lowerLimit, upperLimit)
              return str(result)

        case 'Add':
               firstNumber = int(splitString[1])
               secondNumber = int(splitString[2])
               result = firstNumber + secondNumber
               return str(result)
        
        case 'Subtract':
               firstNumber = int(splitString[1])
               secondNumber = int(splitString[2])
               result = firstNumber - secondNumber
               return str(result)
        
# Lav en metode der konverterer nuerisk resultat til text

def handleClient(connectionSocket, addr):
    print(addr, 'connected')
    iceBreaker = 'Greetings, Chosen One. I will perform rudimentary operations on whatever integers you send me.'
    connectionSocket.send(iceBreaker.encode())

    sentence = connectionSocket.recv(1024).decode() #derp. 1024 bytes. Decode laver bytes om til string
    while sentence != 'quit': 
       result = str(readClientString(sentence))
       print(addr, 'asked for', sentence, 'and I answered', result)
       #  capitalizedSentence = sentence.upper() #derp. gør brugerens besked til uppercase
       #  print(sentence) #Jeg tilføjede selv at jeg kan læse hvad client sender til mig
       connectionSocket.send(result.encode()) #laver string om til bytes
       sentence = connectionSocket.recv(1024).decode() #derp. 1024 bytes. Decode laver bytes om til string
    print(addr, 'disconnected')
    connectionSocket.close()
    

serverPort = 12000 #Port der skal lyttes på
serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET definerer Ipv4. SOCK_STREAM definerer TCP
serverSocket.bind(('', serverPort)) # tom string (stringen er IPadressen). det at den er tom betyder der lyttes til alle MINE iadresser. og porten der lyttes til
serverSocket.listen(1) # starter med at lytte og sætter antallet af hvor mange der kan ligge i kø til serveren.
print('Server is ready to listen') 


while True: #always true
    connectionSocket, addr = serverSocket.accept() #Koden venter ved denne statement indtil en client connecter. betingelsesløs acceptering af forbindelse
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()