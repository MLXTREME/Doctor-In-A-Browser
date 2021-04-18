"""
python Passwords/Save_Password_Main.py
"""
from PythonEncryption.Secure import generate_key,load_key,encrypt_message,decrypt_message
import json,os
from copy import deepcopy
"""
Email - teammlxtreme@gmail.com
Password - wearethebest69
"""
UserDetails = {"Email":"teammlxtreme@gmail.com","Password":"wearethebest69"}
FileName = "password_main.json"

SavePassDir = os.path.dirname(os.path.abspath(__file__))
SavePassFilePath = os.path.join(SavePassDir,FileName)

def write_user_details(FileName,UserDetails):
    HiddenUserDetails = deepcopy(UserDetails)
    password = HiddenUserDetails["Password"]
    HiddenUserDetails["Password"] = encrypt_message(password).decode("utf-8")
    # print(HiddenUserDetails)
    with open(SavePassFilePath, "w",encoding ='utf8') as f:
        json.dump(HiddenUserDetails,f)
    return True

def read_user_details(SavePassFilePath):
    with open(SavePassFilePath) as f:
        HiddenUserDetails = json.load(f)
        print(HiddenUserDetails)
        UserDetails = deepcopy(HiddenUserDetails)
    encrypted_password = bytes(UserDetails["Password"], 'utf-8')
    UserDetails["Password"] = decrypt_message(encrypted_password).decode('utf8')
    return UserDetails

def EncryptPassWord(password):
    encrypted_password = encrypt_message(password).decode("utf-8")
    return encrypted_password

def DecryptPassWord(password):
    encrypted_password = bytes(password, 'utf-8')
    decrypted_password = decrypt_message(encrypted_password).decode('utf8')
    return decrypted_password
    
    


if __name__=="__main__":
    """
    write_user_details(SavePassFilePath,UserDetails)
    print(read_user_details(SavePassFilePath))
    """
    word = "SomethingHere"
    enc = EncryptPassWord(word)
    print(enc)
    dec = DecryptPassWord(enc)
    print(dec)
