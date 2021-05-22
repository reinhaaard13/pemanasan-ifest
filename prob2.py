def main():
    itr = int(input())
    texts =[]
    for _ in range(itr):
        text = input()
        texts.append(text)

    for text in texts:
        print(encrypt_text(text))

def encrypt_text(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "zyxwvutsrqponmlkjihgfedcba"

    A = False # flag for ()
    B = False # flag for ''

    result = ""

    for letter in text:
        if letter == "(":
            A = True
            result += letter
        elif letter == "'":
            B = True if A == True and B == False else False
            result += letter
        elif letter == ")":
            A = False
            B = False
            result += letter
        elif A == True and B == True:
            result += letter
        elif letter.lower() in alphabet:
            A = False
            B = False
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter 
    return result

if __name__ == "__main__":
    main()