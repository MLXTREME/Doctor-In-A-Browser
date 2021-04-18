"""
python PyAutoMail/AutoReplacer.py
"""

from AutoMailer import *
import os,shutil
import re


def readHTML(FilePath):
    with open(FilePath, "r") as f:
        return f.readlines()


def writeHTML(FilePath, txt):
    with open(FilePath, "w") as f:
        for row in txt:
            if not str(row).strip() == "":
                f.write(str(row) + '\n')


def addtoHTMLFile(txt, pos, str_to_add, fpath):
    sub_txt = txt[:pos]
    sub_txt.extend(str_to_add.split('\n'))
    sub_txt.extend(txt[pos:])
    writeHTML(fpath, sub_txt)
    # return sub_txt


def findLineNumber(main_lst, search_string):
    """
    x = re.search("<!--Add The Box Here-->", txt)
    """
    Lines = []
    for i, each in enumerate(main_lst):
        if re.search(search_string, each):
            Lines.append(i)
            # yield i

    return Lines


def logger(line):
    with open('log.txt', 'a+') as f:
        f.write(str(line)+"\n")
"""
<!--Covid Test Predictions :<br>Test Results : Negative<br>Desription : XYZ<br>Comments : ABC<br><br> -->
"""

def rewriteHTMLTemplate(TestDetails,fpath):
    title = TestDetails["Title"]
    str_to_add = title + " - " +"<br>"
    del TestDetails["Title"]
    for each_key in TestDetails.keys():
        each_val = TestDetails[each_key]
        str_to_add = str_to_add + each_key + " : " + each_val +"<br>"
    txt = readHTML(fpath)
    linesadded = findLineNumber(txt, "<!--Add The Box Here-->")
    addtoHTMLFile(txt, pos=linesadded[-1]+1, str_to_add=str_to_add,fpath=fpath)
    return 1

if __name__ == "__main__":
    """
    TemplateName = "MLXTREME_Template_Stripo.html"
    TemplateFolder = "Templates"
    UserDetails = read_user_details()

    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    MailDetails = {
                    "Subject": "New Mail Sent using Python",
                    "To":      ['damikdhar@gmail.com','njrfarhandasilva10@gmail.com','nirmalya14misra@gmail.com','swaymsdennings@gmail.com'],
                    "Body" :   read_file(TemplatePath),
                    "AttachmentPath" : "PyAutoMail/AutoMailer.py"
                    }
    send_email_attach(MailDetails)
    """
    TemplateName = "AutoMail_Content_JINJA.html"
    TemplateFolder = "Templates"
    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    TempPath = os.path.join(ROOT_DIR,TemplateFolder, "temp.html")
    shutil.copy(TemplatePath,TempPath)
    string_res = """Covid Test Predictions :<br>Test Results : Negative<br>Desription : XYZ<br>Comments : ABC<br><br></p></td>"""
    TestDetails = {
                    "Title" : "Covid Test Predictions",
                    "Test Results" : "Positive",
                    "Desription" : "Level 1 - Advised Usage of Medical Treatment with Proper Consultation with a Doctor",
                    "Comments" : "Immediate Vaccination May Help in Recovery."
                    }
    rewriteHTMLTemplate(TestDetails,fpath=TempPath)
    # os.remove(TempPath)
    
    
