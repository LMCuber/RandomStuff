import string


def decipher(code):
    chars = string.ascii_lowercase
    for i in range(26):
        s = ""
        for char in code:
            space = False
            try:
                index = chars.index(char) + i
                chars[index]
            except ValueError:
                s += " "
                space = True
            except IndexError:
                index -= len(chars)
            if not space:
                s += chars[index]
        print(s)
            
            
decipher()  # input
