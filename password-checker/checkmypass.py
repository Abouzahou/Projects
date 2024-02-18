#Program check how secure your password is
#whether it was hacked or not
#requests module: allows us to request data from a website 
#will use pwned passwords API

#Hash Function: A function that generates a value of fixed length for each input it gets

import requests
import hashlib #needed for hashing password
import sys

#function to get the hash of the password and compare with known hashes
#if we type the normal password string then it will output an error
#because API only accepts a SHA-1 hash of the password
#API also uses K-anonymity
#K-anonymity: uses only the first 5 characters of the Hashed Password
#this way , the API will never know the full hashed password
#query_char will be the hashed password

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the API and try again')
    return response

def get_password_leaks_count(hashes, hash_to_check): #hash_to_check is the tail of the hashed password
    hashes = (line.split(':') for line in hashes.text.splitlines()) #we need splitlines to return each line as one element in list
    for h , count in hashes: # hashes has the hash and the textsplit Count, because we split the text recieved
        if h == hash_to_check: #h is = to the tail hashes returned from the API, so we compare it to our own hashed password tail
            return count
    return 0

def pwned_api_check(password):
    #Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #dividing the hash pass into two parts, grabing the 1st 5 characters
    first5_char , tail = sha1password[:5] , sha1password[5:]

    resp = request_api_data(first5_char)
    return get_password_leaks_count(resp, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times in the database, You should change your password immediately!')
        else:
            print(f'{password} was NOT found. You can keep it!')
    return 'done!'            


if  __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))