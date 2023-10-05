from socket import *

def stringBuilder(command, number1, number2):
    str(number1)
    str(number2)
    resultString = command+';'+number1+';'+number2
    resultString.strip()
    return resultString
    

serverName = "localhost" #IPadressen
serverPort = 12000 #Port som serveren lytter på
clientSocket = socket(AF_INET, SOCK_STREAM) #definerer socket objekt. Her ipv4 og TCP
clientSocket.connect((serverName, serverPort)) #sender en forbindelses besked afsted til Ipadresse og den valgte port.
print(clientSocket.recv(1024))
commandToSend = ''

while commandToSend != 'quit'.strip():
    print('please chose a command')
    commandToSend = input('Input command: ') #skab sætning
    print('Give me the first number')
    first = input('first number: ')
    print('Give me the second number')
    second = input('second number: ')
    stringToSend = stringBuilder(commandToSend, first, second)
    clientSocket.send(stringToSend.encode())
    answer = clientSocket.recv(40).decode()
    print('The server responds: ', answer)
    print('write quit to close connection')




# while commandToSend != 'quit'.strip():
    
#     clientSocket.send(sentence.encode()) #gør besked til bytes og send det.
#     modifiedSentence = clientSocket.recv(1024) #Modtager max 1024 bytes fra serveren.
#     print('From server: ', modifiedSentence.decode())
#     sentence = input('Input sentence: ') 

clientSocket.send('quit'.encode()) #sørger for at sende en exit besked inden forbindelsen lukker.
clientSocket.close()