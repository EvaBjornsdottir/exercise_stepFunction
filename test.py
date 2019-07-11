KEY  = 7 #Specifiy a key
ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message):

    encrypted = " "
    msg = message.lower()
    for letter in msg:
        index = ALPHABETS.find(letter)
        if index == -1:
            print(letter)
            encrypted = encrypted + letter
        else:

            new_index = index + KEY
            character = ALPHABETS[new_index]
            if new_index > len(ALPHABETS):
                new_index = new_index % len(ALPHABETS)
            print(letter, index, new_index, character)
            encrypted = encrypted + character
        return encrypted
