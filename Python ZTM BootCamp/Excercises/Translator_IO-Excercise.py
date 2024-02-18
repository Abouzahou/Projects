#File_IO Excercise
#Building a Translator

#we will be building  a simple translator that can translate English to spanish.
#We will first be importing a translation library -  'translate' by Google.

#Script and test.txt files are available in the Excercise \ File_IO-Excercise Folders

""" 
from translate import Translator

translator = Translator(to_lang="es") #translates to spanish

try:
    with open('./test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode='w') as my_file2: #Creating a new file with the translation
            my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')
except IOError as err:
    print('IO error')     """