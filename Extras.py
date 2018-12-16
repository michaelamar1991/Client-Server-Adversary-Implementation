import binascii
from operator import xor

UDP_IP = "127.0.0.1" # IP of the server - now set on localhost can be changes to any IP address we want to run the server on.
UDP_PORT = 12321
D = 5 # The sequence number of the package that we will lost (For demonstration we choose packet to loose to make sure we will some some data then we can restore it with the restore function on the server side.).
n = 70 # The size of the splitted data without the sequence number and the UDP&IP headers.


def split_message(message):
    message = [message[i:i + n] for i in range(0, len(message), n)]
    for i in range(len(message)):
        message[i] = repr(i+1) + "\t" + message[i]
    return message


def txt_to_binary(text):
    return int(binascii.hexlify(text), 16)


def bits_to_txt(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int_to_bytes(n).decode(encoding, errors)


def int_to_bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def lst_to_binLST(list):
    return map(lambda x: bin(txt_to_binary(x)), list)


def binaryLST_XOR(list):
    return bin(reduce(xor, map(lambda x: int(x, 2), list)))
