

from cryptography.fernet import Fernet


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()


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
    a = encrypt_message("encrypt this message")
    print(type(a))
    # print(type(str(a)))
    print(a)
    normal_string = a.decode("utf-8")
    print(normal_string)
    print(type(normal_string))
    bytesmessage = bytes(normal_string, 'utf-8')
    print(bytesmessage)
    print(type(bytesmessage))
    x = decrypt_message(a).decode('utf8')
    print(x)
    print(type(x))
    x = decrypt_message(bytesmessage).decode('utf8')
    print(x)
    print(type(x))
