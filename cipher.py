plain_text=(input("enter any text"))
key_value=int(input("enter key value"))
for letter in plain_text:
    ascii_value=ord(letter)
    if ascii_value>=65 and ascii_value<=90:
        ascii_value=ascii_value+key_value
        if ascii_value>90:
            ascii_value=ascii_value-26
    elif ascii_value>=97 and ascii_value<=122:
        ascii_value=ascii_value+key_value
        if ascii_value>122:
            ascii_value=ascii_value-26  
    cipher_text=chr(ascii_value)
    print(cipher_text,end="")   