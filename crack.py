import hashlib

flag = 0

pass_hash = input("enter md5 hash: ")
wordlist = input("enter file name: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("no file found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == pass_hash:
        print("password has been found.")
        print(f"password is {word}")

        flag = 1
        break

if flag == 0:
    print("password / passphrase is not in the list.")