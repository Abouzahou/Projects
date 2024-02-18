import sys 
#imports the module from the python Library Dir for use in the script
sys.path.append('C:/Users/Hunter/AppData/Local/Programs/Python/Python312/Lib/site-packages')

from translate import Translator

translator = Translator(to_lang="es") #translates to spanish

try:
    with open('./test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-es.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')
except IOError as err:
    print('IO error')    