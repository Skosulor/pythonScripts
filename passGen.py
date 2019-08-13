import pyperclip
from getpass import getpass
from sys import argv

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
symbols2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789.@!?#$/\+"
symbolsLen = len(symbols)
passLen = 15

try:
    script, arg1, arg2, arg3 = argv;
except ValueError:
    noarg = True;

def fit(offset, limit):
    while(offset >= limit):
        offset -= limit
    return offset

if len(argv)>= 2 and argv[1] != "-l":
    domain = argv[1]
else:
    domain = input("Domain: ")
if len(argv) >=3 and argv[2] != "-l":
    key = argv[2];
else:
    key = getpass("Key: ")
domLen = len(domain)
keyLen = len(key)
sumLen = domLen + keyLen

domOffset = 0
for i in domain:
    domOffset += symbols2.find(i)

keyOffset = 0
for t in key:
    keyOffset += symbols2.find(t)

offset = fit(keyOffset + domOffset,symbolsLen)
passString = ''
for x in range(passLen):
    passString += symbols[offset]

    offset += symbols2.find(key[fit(x,keyLen)])
    if(offset >= symbolsLen):
        offset -= symbolsLen
if "-l" in argv:
    print(passString)
pyperclip.copy(passString)
