"""
python Passwords/Save_Password.py
"""

from PythonEncryption.Secure import generate_key,load_key,encrypt_message,decrypt_message
import json,os
from copy import deepcopy

UserDetails = {"Email":"youremail@gmail.com","Password":"yourpassword"}
FileName = "password_main.json"

SavePassDir = os.path.dirname(os.path.abspath(__file__))
SavePassFilePath = os.path.join(SavePassDir,FileName)

def write_user_details(SavePassFilePath=SavePassFilePath,UserDetails=UserDetails):
    HiddenUserDetails = deepcopy(UserDetails)
    password = HiddenUserDetails["Password"]
    HiddenUserDetails["Password"] = encrypt_message(password).decode("utf-8")
    # print(HiddenUserDetails)
    with open(SavePassFilePath, "w",encoding ='utf8') as f:
        json.dump(HiddenUserDetails,f)
    return True

def read_user_details(SavePassFilePath=SavePassFilePath):
    with open(SavePassFilePath) as f:
        HiddenUserDetails = json.load(f)
        # print(HiddenUserDetails)
        UserDetails = deepcopy(HiddenUserDetails)
    encrypted_password = bytes(UserDetails["Password"], 'utf-8')
    UserDetails["Password"] = decrypt_message(encrypted_password).decode('utf8')
    return UserDetails

if __name__=="__main__":
    write_user_details(SavePassFilePath,UserDetails)
    print(read_user_details(SavePassFilePath))
