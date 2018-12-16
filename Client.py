import socket
import time
import Extras

serverAddressPort = ("127.0.0.1", 12321) # Now is set for local host can be change to any IP of the server.
bufferSize = 1024
count = 0

# Create a UDP socket at client side

UDPClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClient.settimeout(3)

# Send to server using UDP socket

msgFromClient = "Lorem Ipsum is simply dummy text of the printing and typesetting industry." \
                    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,when an unknown printer took a galley of type and scrambled it to make a type specimen book." \
                    "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged." \
                    "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
msg_lst = Extras.split_message(msgFromClient)
encrypted_msg = Extras.lst_to_binLST(msg_lst)

counter = 0
index = 0

while True:
    if counter == 0:
        xor_message = Extras.binaryLST_XOR(encrypted_msg[0:Extras.D])
        UDPClient.sendto(xor_message, serverAddressPort)
    else:
        if counter != Extras.D:
            UDPClient.sendto(msg_lst[index], serverAddressPort)
        index += 1
    counter += 1

    try:
        msgFromServer = UDPClient.recvfrom(bufferSize)
        msg = "Message from Server : {}".format(msgFromServer[0].decode('utf-8'))
        print(msg)
        print("---------------------------------------------------------------")
    except:
        print("---------------------------")
        print("|| TIMEOUT - Lost Packet ||")
        print("---------------------------")
    time.sleep(2)

    if counter == Extras.D + 1:
        counter = 0
    if index == (len(msg_lst) + 1):
        print("####################################")
        print("# The message has been fully sent! #")
        print("####################################")
        break

# sniff(iface="lo0", prn = lambda x: x.show(), store=0)
# cd scapy
# ./run_scapy

#        bytesToSend = str.encode(str(seq) + "\t" + msgFromClient[start:end])


