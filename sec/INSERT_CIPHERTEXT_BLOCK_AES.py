#mostly taken from examples from output of pydoc Crypto.Cipher.AES
#tested with python v3.6
#also from https://pypi.python.org/pypi/pycrypto
#https://www.floyd.ch/?p=293
#https://pythonprogramming.net/encryption-and-decryption-in-python-code-example-with-explanation/
#http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
from Crypto.Cipher import AES
from Crypto import Random
import os, sys, time, random
from bitarray import bitarray

def encrypt_s (key, cipher_mode, mode_name):

    replay_input = "Give Eve $100"
    src_input = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"

    block_size = 16

    print("size of input is {}".format(len(src_input)))

    padding_src = '*'
    pad_src_input = src_input + (((16 - len(src_input)) % 16) * padding_src)
    pad_replay_src_input = replay_input + (((16 - len(replay_input)) % 16) * padding_src)

    padding_key = '*'
    pad_key = key + ((16 - len(key)) * padding_key)

    #create initialization vector, iv
    #randomized to ensure uniqueness
    iv = Random.new().read(AES.block_size)
    # creates cipher object using the key
    if (mode_name == 'CFB'):
        #s-bit definition
        cipher = AES.new(pad_key, cipher_mode, iv, segment_size = 128)
        enc_msg = iv + cipher.encrypt(pad_src_input)
        replay_enc_msg = iv + cipher.encrypt(pad_replay_src_input)
    else:
        cipher = AES.new(pad_key, cipher_mode, iv)
        enc_msg = iv + cipher.encrypt(pad_src_input)
        replay_enc_msg = iv + cipher.encrypt(pad_replay_src_input)

    return (enc_msg, replay_enc_msg)


def decrypt_s (enc_input, replay_enc_msg, key, cipher_mode, mode_name):

    iv = enc_input[:16]
    enc_output = replay_enc_msg[16:32] + enc_input[32:]

    padding = '*'
    pad_key = key + ((16 - len(key)) * padding)

    # creates cipher object using the key
    if (mode_name == 'CFB'):
        cipher = AES.new(pad_key, cipher_mode, iv, segment_size = 128)
    else:
        cipher = AES.new(pad_key, cipher_mode, iv)

    plain_output = cipher.decrypt(enc_output)

    #print (plain_output.decode('utf-8'))
    print (plain_output)


#create and test file encryption using AES / Python Crypto
cipher_mode = [ AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB ]
cipher_mode_name = ['ECB', 'CBC', 'CFB', 'OFB']
key = 'password'

j = 0
for i in cipher_mode:
    print ('Trying...{}'.format(cipher_mode_name[j]))
    #time.sleep(2)
    enc_msg, replay_enc_msg = encrypt_s(key, i, cipher_mode_name[j])
    decrypt_s(enc_msg, replay_enc_msg, key, i, cipher_mode_name[j])
    j += 1


#enc_msg = encrypt_s(key, AES.MODE_CBC)
