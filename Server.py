import socket
import Extras


def recover_packet(lst):
    recovered_packet = Extras.bits_to_txt(bin(int(Extras.binaryLST_XOR(Extras.lst_to_binLST(lst[1:])), 2) ^ int(lst[0], 2)))
    print("#############################################################")
    print("The lost packet is: " + recovered_packet)
    print("#############################################################")
    UDPServer.sendto(recovered_packet, address)


localIP = "127.0.0.1" # Now is set for localhost can be change to any IP that we running the server on.
localPort = 12321
bufferSize = 1024
counter = 0
index = 0
msg = []

# Create a datagram socket

UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServer.bind((localIP, localPort))
print("**************************************************")
print("* UDP server up and listening on "+str(localIP)+":"+str(localPort)+" *")
print("**************************************************")

# Listen to incoming Datagrams

while True:

    bytesAddressPair = UDPServer.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    msg.append(message)

    # Sending a reply to client

    clientIP = "Client IP Address : {}".format(address)
    print(clientIP)
    print(message)
    print("---------------------------------------------------------------")
    UDPServer.sendto(message, address)

    index += 1
    counter += 1
    if counter == Extras.D + 1:
        print("Counter =  " + repr(Extras.D + 1) + " => Need to check if we lost packet!")
        if msg[len(msg) - 1][0:2] == "0b":
            print("Recovering Lost Packet :")
            recover_packet(msg[-Extras.D - 1:-1])
            counter = 1
        else:
            counter = 0
