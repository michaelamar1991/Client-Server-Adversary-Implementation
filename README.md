# Client-Server-Adversary-Implementation
This is a Python implementation of simple web HTTP server that listens to specific port, a client that send chunks of data to the server and adversary that sniffing those packets. The adversary may prevent some packets from arrive at this destination so the client send XOR code of all the messages in the first packet and then if needs the server know to restore the lost packet using restore function from the XOR code.

To run the demonstration program just needed to clone the files to your computer and then run the files through terminal.
First run the server then the Sniffer and then run the Client.

1) Python Server.py
2) sudo Python Sniffer.py
3) Python Client.py

you will see the data transferred between the client and the server and can watch the sniffed data on the Sniffer terminal window.
