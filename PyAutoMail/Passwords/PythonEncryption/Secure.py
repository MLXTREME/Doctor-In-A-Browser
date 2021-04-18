"""
python Passwords/PythonEncryption/Secure.py
"""

from cryptography.fernet import Fernet
import os

SecureDir = os.path.dirname(os.path.abspath(__file__))
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(os.path.join(SecureDir,"secret.key"), "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open(os.path.join(SecureDir,"secret.key"), "rb").read()


def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message
    # print(encrypted_message)


def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message
    # print(decrypted_message.decode())


if __name__ == "__main__":
    # generate_key()
    mess = "encrypt this message"
    print(mess,type(mess))
    a = encrypt_message(mess)
    print(a,type(a))
    normal_string = a.decode("utf-8")
    print(normal_string,type(normal_string))
    bytesmessage = bytes(normal_string, 'utf-8')
    print(bytesmessage,type(bytesmessage))
    x = decrypt_message(a).decode('utf8')
    print(x,type(x))
    x = decrypt_message(bytesmessage).decode('utf8')
    print(x,type(x))

