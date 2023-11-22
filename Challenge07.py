#usr/var

#Cris
#17/11/2023

from cryptography.fernet import Fernet

def encrypt_file(filepath, key):
    with open(filepath, 'rb') as file:
        file_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    with open(filepath, 'rb') as file:
        file_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("Encrypted message:", encrypted_message)

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message.decode())

mode = input("Select mode (1=encrypt file, 2=decrypt file, 3=encrypt message, 4=decrypt message): ")

key = Fernet.generate_key()

if mode == '1':
    filepath = input("Enter filepath to encrypt: ")
    encrypt_file(filepath, key)
elif mode == '2':
    filepath = input("Enter filepath to decrypt: ")
    decrypt_file(filepath, key)
elif mode == '3':
    message = input("Enter message to encrypt: ")
    encrypt_message(message, key)
elif mode == '4':
    encrypted_message = input("Enter message to decrypt: ")
    decrypt_message(encrypted_message, key)


    # Encrypt /home/test folder recursively 
$folder = "/home/test"
$password = Read-Host -Prompt "Enter encryption password" -AsSecureString
Encrypt-Folder $folder -Password $password -Recurse

    # Decrypt /home/test folder recursively
$folder = "/home/test" 
$password = Read-Host -Prompt "Enter decryption password" -AsSecureString
Decrypt-Folder $folder -Password $password -Recurse

function Encrypt-Folder {
  param(
    [string]$folder,
    [SecureString]$password,
    [switch]$recurse
  )
  
    # Encryption  using $password 
}

function Decrypt-Folder {
 param(
    [string]$folder,
    [SecureString]$password,
    [switch]$recurse
  )

    # Decryption logic using $password
}
