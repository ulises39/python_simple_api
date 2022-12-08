from socket import *
from consume_api import *

server_address = 'localhost'
port = 9000

#Mandar a  erick.espejel@tribalworldwide.gt

def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        serverSocket.bind((server_address, port))
        serverSocket.listen()

        while(1):
            #El servidor espera hasta que se conecte un cliente
            (clientSocket, address) = serverSocket.accept()

            test_json = '{ "Hola": "Mundo" }'

            data_to_send  = "HTTP/1.1 200 OK\r\n" #En la respuesta incluimos el status 200
            data_to_send += "Content-Type: application/json; charset=utf-8\r\n\r\n" #Como es una API RESTful, la respuesta va en formato json
            # data_to_send += json.dumps(json.loads(test_json), indent=4) # Aquí iría la respuesta en json
            data_to_send += json.dumps(consume_api(25), indent=4) # Aquí iría la respuesta en json

            clientSocket.sendall(data_to_send.encode())
            clientSocket.shutdown(SHUT_WR)


    except KeyboardInterrupt:
        print('Apagando servidor')
    except Exception as ex:
        print('Error:')
        print(ex)

    serverSocket.close()

print('Servidor encendido en ' + server_address + ':' + str(port))
createServer()
