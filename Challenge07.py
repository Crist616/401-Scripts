#usr/var

#Cris
#17/11/2023
# Revision on 13/12/2023

from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key() 

def encrypt_file(key, in_filename, out_filename):
    fernet = Fernet(key)
    with open(in_filename, 'rb') as file:
        plaintext = file.read()
    ciphertext = fernet.encrypt(plaintext)
    with open(out_filename, 'wb') as file:
        file.write(ciphertext)
        
def decrypt_file(key, in_filename, out_filename):
    fernet = Fernet(key)
    with open(in_filename, 'rb') as file:
        ciphertext = file.read()
    plaintext = fernet.decrypt(ciphertext)
    with open(out_filename, 'wb') as file:
        file.write(plaintext)

def encrypt_folder(key, in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    for filename in os.listdir(in_folder):
        in_path = os.path.join(in_folder, filename)
        out_path = os.path.join(out_folder, filename + '.enc')
        
        encrypt_file(key, in_path, out_path)
        
def decrypt_folder(key, in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    for filename in os.listdir(in_folder):
        if filename.endswith('.enc'):
            in_path = os.path.join(in_folder, filename)
            out_path = os.path.join(out_folder, os.path.splitext(filename)[0])
            
            decrypt_file(key, in_path, out_path)
            
if __name__ == '__main__':
    key = generate_key()
    
    in_folder = '/data/input'
    out_folder = '/data/encrypted'
    
    encrypt_folder(key, in_folder, out_folder)
    
    decrypt_folder(key, out_folder, '/data/decrypted')



