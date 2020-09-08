import nltk
nltk.download('words')
english_words_list=nltk.corpus.words.words()


def encrypt (input,key):

    # alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    
    key=key%26

    for character in input:
        if character==" " or character=='!':
            continue
        if character.isupper():
            index=alphabet_upper.find(character)
            result+= alphabet_upper[index+key]
        else:
            index=alphabet.find(character)
            result+= alphabet[index+key]
    return result

def decrypt(input,key):
    # alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    
    key=key%26

    for character in input:
        
        if character==" " or character=='!':
            continue
        if character.isupper():
            index=alphabet_upper.find(character)
            result+= alphabet_upper[index-key]
        else:
            index=alphabet.find(character)
            result+= alphabet[index-key]    
    return result


def count_words(sentence):
    counter=0
    words=sentence.split()
    for i in words:
        if i in english_words_list:
            counter+=1
    return counter
    


if __name__ == "__main__":
    # assert encrypt('a',1)=='b'
    print(encrypt('a A!',35))
    print(decrypt('j J!',35))
    # print('success')
    # print(count_words('hi play work sde'))
    # print(words_list)