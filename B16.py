import string

ALPHABET = string.ascii_lowercase[:16] # set ALPHABET a to p 

LOWER_OFFSET = ord("a") # set a as base number 0
def b16_encoding(plain):
    enc = "" 
    for c in plain: # selecting each letter from plain text 
        binary = "{0:08b}".format(ord(c)) # converting into 8 bit binary formet ex :- 01100110
        enc += ALPHABET[int(binary[:4],2)] # concat into two part of binary number 0110 0110 and select first 4 letter  and conver that number into int(,2) here 2 for describe that numbers are in base 2 (binary) and after converting that number into a decimal add that index number alphabet in enc
        enc += ALPHABET[int(binary[4:],2)] # same process for other 4 bit 

    return enc # return the encrypted text 

def b16_decoding(encry_text):
    org_text = ""
    for i in range(0,len(encry_text),2): # use 2 char
        post1 = ALPHABET.index(encry_text[i])
        post2 = ALPHABET.index(encry_text[i+1])

        binary_val = (post1 << 4) | post2

        org_text += chr(binary_val)
    return org_text


while True:
    
    print("------------------------")
    print("[+] 1 :- Encoding      |")
    print("[+] 2 :- Decoding      |")
    print("[+] 3 Exit             |")
    print("------------------------")
    ch = int(input("Enter your Choice :- "))
    if ch == 1:
        text = input("[+] Enter your text for Encoding :- ")
        print(f"[+] Encoded Text :- {b16_encoding(text)}")
        print("--------------------------------------")
    elif ch == 2:
            Entext = input("[+] Enter your text for Decoding :- ").strip()
            print(f"[+] Decoded Text :- {b16_decoding(Entext)}")
            print("---------------------------------------")
    elif ch == 3:
         print("[+] Exiting ......")
    else:
         print("[!] Please Enter a valid choice :- ")

