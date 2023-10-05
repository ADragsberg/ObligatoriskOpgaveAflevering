from socket import *
import json

def stringBuilder(command, number1, number2):
    str(number1)
    str(number2)
    resultString = command+';'+number1+';'+number2
    resultString.strip()
    return resultString
    
def convertStringToJsonObject(stringToConvert):
    
    splitString = stringToConvert.split(';')
    jsonBuild = {"method": splitString[0], "tal1": splitString[1], "tal2": splitString[2]}
    return json.dumps(jsonBuild)

def answerTranslator(answerObjectString):
    answerObject = json.loads(answerObjectString)
    answer = answerObject["answer"]
    return answer

    

quitCommand = convertStringToJsonObject(stringBuilder('quit','0','0'))

serverName = "localhost" #IPadressen
serverPort = 12000 #Port som serveren lytter på
clientSocket = socket(AF_INET, SOCK_STREAM) #definerer socket objekt. Her ipv4 og TCP
clientSocket.connect((serverName, serverPort)) #sender en forbindelses besked afsted til Ipadresse og den valgte port.
print(clientSocket.recv(1024))
commandToSend = ''

while commandToSend != 'quit'.strip():
    print('please chose a command')
    commandToSend = input('Input command: ')
    if (commandToSend != 'quit'):
        print('Give me the first number')
        first = input('first number: ')
        print('Give me the second number')
        second = input('second number: ')
        stringToSend = convertStringToJsonObject(stringBuilder(commandToSend, first, second))
        clientSocket.send(stringToSend.encode())
        answer = clientSocket.recv(1024).decode()
        print('The server responds: ', answerTranslator(answer))
        print('write quit to close connection')

clientSocket.send(quitCommand.encode()) #sørger for at sende en exit besked inden forbindelsen lukker.
clientSocket.close()
print('connection has been closed')












# while commandToSend != 'quit'.strip():
    
#     clientSocket.send(sentence.encode()) #gør besked til bytes og send det.
#     modifiedSentence = clientSocket.recv(1024) #Modtager max 1024 bytes fra serveren.
#     print('From server: ', modifiedSentence.decode())
#     sentence = input('Input sentence: ') 
