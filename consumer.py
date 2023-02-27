# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
from encrypt_decrypt import cipher_encrypt, cipher_decrypt
# Import sys module
import sys

# Import json module to serialize data
# import os

# Initialize consumer variable and set property for JSON decode
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode('utf-8'))

print("here")
# Read data from kafka
for message in consumer:
    print(message)
    
    ciper = cipher_encrypt(message[6],4)
    print ("Cipher: " + ciper)
    encr = open("encryptdata.txt",'w')
    encr.write(str(ciper))
    encr.close()

    decrypt = cipher_decrypt(ciper, 4)
    print("Decrypt: " + decrypt)
    F = open("decryptdata.txt",'w')
    F.write(str(decrypt))
    F.close()

# Terminate the script
sys.exit()