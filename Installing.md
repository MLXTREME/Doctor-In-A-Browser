virtualenv DocEnv
or run
python -m virtualenv DocEnv
DocEnv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python bugfix.py
python myapp.py
python app.py

https://stackoverflow.com/questions/66087475/chatterbot-error-oserror-e941-cant-find-model-en

###  BugFix
Make sure you actually have the right spacy model installed. For example, install en_core_web_sm with the python -m spacy download en_core_web_sm command in the terminal.

Next, fix this error:

File "C:\Users\USER\AppData\Local\Programs\Python\Python37\lib\site-packages\chatterbot\tagging.py", line 13, in __init__
    self.nlp = spacy.load(self.language.ISO_639_1.lower())
That is,

Open the C:\Users\USER\AppData\Local\Programs\Python\Python37\lib\site-packages\chatterbot\tagging.py file
Go to Line 13
Replace self.nlp = spacy.load(self.language.ISO_639_1.lower()) with
if self.language.ISO_639_1.lower() == 'en':
    self.nlp = spacy.load('en_core_web_sm')
else:
    self.nlp = spacy.load(self.language.ISO_639_1.lower())
You will need to add more conditions for other languages you need to support.
