# import tkinter as tk
# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a') 

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper(): 

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower(): 

            c_index = ord(c) - ord('a') 

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted
# def encrypt(text,s):
#     result = ""
 
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
 
#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
 
#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)
 
#     return result

# def decrypt(text,s):
#     result = ""
 
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
 
#         # Decrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) - s+65) % 26 + 65)
 
#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) - s-97) % 26 + 97)
 
#     return result
 
#check the above function
# text = "ATTACKATONCE"
# s = 4


# def f():
#     def save():
#         a = t.get()
#         f = open(('readdata.txt'), 'w')
#         f.write(a)
#         f.close()
#         return

#     top = tk.Tk()
#     t = tk.StringVar()
#     e = tk.Entry(top, textvariable = t).pack()
#     b = tk.Button(top, text = 'Save as a file', command = save).pack()
#     top.mainloop()


# f()
# file = open('Users/asthapatwa/Downloads/kafka_2.12-3.4.0/python_assignment/files/readdata.txt', 'r')

# #To print the content of the whole file
# text = file.readline() 
# file.close()

# print ("Text  : " + text)
# ciper = cipher_encrypt(text,4)
# print ("Cipher: " + ciper)
# encr = open("encryptdata.txt",'w')
# encr.write(str(ciper))
# encr.close()

# decrypt = cipher_decrypt(ciper, 4)
# print("Decrypt: " + decrypt)
# F = open("decryptdata.txt",'w')
# F.write(str(decrypt))
# F.close()
