#RegEx Excercise:
        #Creating a password checker

#At least 8 characters long
#contain any sort letters, numbers and symbols

#########################################################
# Has minimum 8 characters in length. Adjust it by modifying {8,}
# At least one uppercase English letter. You can remove this condition by removing (?=.*?[A-Z])
# At least one lowercase English letter.  You can remove this condition by removing (?=.*?[a-z])
# At least one digit. You can remove this condition by removing (?=.*?[0-9])
# At least one special character,  You can remove this condition by removing (?=.*?[#?!@$%^&*-])
#########################################################


import re

#Basic Checker, at least 8 chars including digits & Symbols, with no conditions of (at least one letter/digit or special)
password1 = re.compile(r"[A-Za-z0-9#?!@$%^&*-]{8,}\d") #Has to end with a number== \d, remove \d to remove restriction
password2 = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$") #More advanced restrictions
string1 = 'Iz113saq1' #will match pattern 1 not 2, because there's no characters
string2 = 'Iz@13saq' #will match pattern 2 not 1, because it doesn't end in a number


a = password2.fullmatch(string2)
print(a)