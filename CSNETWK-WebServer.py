'''
    ABENOJA, Amelia Joyce L.
    SANG, Nathan Immanuel C.

    CSNETWK - S16

    Laboratory Avtivity 05 - Web Server Programming
    16 November 2023

    Reference:
    - Socket Programming HOWTO:
    https://docs.python.org/3/howto/sockets.html?fbclid=IwAR0i2Kf3loa6hoS2muuKawR_rkyddLFnT4MMGtjfyZEKGvshoGVhSozfn8E
'''


from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server socket: ', serverSocket)
# Fill in end


while True:
    # Establish the connection
    print('CSNETWK Web Server is ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(4026)
        print('Message: ', message)
        # Fill in end

        filename = message.split()[1]
        f = open(filename[1:], 'rb')
        outputdata = f.read()

        # Fill in start
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('\nHTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
        #Fill in end

        # Send the content of the requested file to the client
        connectionSocket.sendall(outputdata)
       
        connectionSocket.send("\r\n".encode('utf-8'))
        connectionSocket.close()
    
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.sendall('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.sendall('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
        print('404 Not Found')
        # Fill in end
       
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end


    serverSocket.close()
    sys.exit()  #Terminate the program after sending the corresponding data