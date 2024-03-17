from cryptography.fernet import Fernet
import base64


class Crypto_Util():
    def __init__(self):
        pass


    def generate(self):
        key = Fernet.generate_key()
        with open("encrypt.key", 'wb') as key_file:
            key_file.write(key)


    def load_key(self):
        with open("encrypt.key", 'rb') as key_file:
            key = key_file.read()
        return key


    def encrypt_message(self, message):
        f = Fernet(self.load_key())
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()


    def decrypt_message(self, encrypted_message):
        f = Fernet(self.load_key())
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message