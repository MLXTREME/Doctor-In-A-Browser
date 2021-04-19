"""
python bugfix.py
Tries to fix chatterbot bug
"""

import chatterbot
import os
import fnmatch

ModuleInitPath = chatterbot.__file__
ModulePath = os.path.dirname(ModuleInitPath)

def read_file(FilePath):
    with open(FilePath, "r") as f:
        return f.readlines()

def write_file(FilePath, txt):
    with open(FilePath, "w") as f:
        for row in txt:
            f.write(str(row) + '\n')
            



def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

target_file=find('*tagging.py', ModulePath)

print(target_file[0])
txt = read_file(target_file[0])
pos = 13
sub_txt = txt[:pos-1]
# del sub_txt[pos]
str_to_add = """
        if self.language.ISO_639_1.lower() == 'en':
            self.nlp = spacy.load('en_core_web_sm')
        else:
            self.nlp = spacy.load(self.language.ISO_639_1.lower())
"""
sub_txt.extend(str_to_add.split('\n'))
sub_txt.extend(txt[pos+1:])
write_file(target_file[0] , sub_txt)


