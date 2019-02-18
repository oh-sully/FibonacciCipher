#Returns the next fibonnaci number (begins at 1)
def fib():
    n2, n1 = 0, 1
    while True:
        yield n2
        n2, n1 = n1, (n2+n1)

def decode(codeWord, fib):
    
    fib_num = fib()
    next(fib_num)
    decodedWord = ""
    start = ord("A") #65
    end = ord("Z") #90
    interval = end - start + 1 #26
    for char in codeWord:
        shift = next(fib_num)
        if char.isupper():
            new_char = chr( start + (ord(char) - start + shift) % interval) 
        else:
            new_char =  chr( start + (ord(char.upper()) - start + shift) % interval).lower()
        decodedWord += new_char
    return decodedWord

def main(wordArr):

    decodedWords = [decode(word, fib) for word in wordArr]
    for i in range(len(decodedWords)):
        print('{0} = {1};'.format(wordArr[i], decodedWords[i]))

codedWords = ['SKU', 'SHIP', 'SHOPS', 'STORES', 'UNICORN']

if __name__ == "__main__":
    main(codedWords)