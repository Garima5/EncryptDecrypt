
import string
import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once 
    implementation of applyShifts is complete!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()



# Problem 1: Encryption

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic={'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h': 'h','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u',
         'v':'v','w':'w','x':'x','y':'y','z':'z','A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J','K':'K','L':'L','M':'M','N':'N','O':'O','P':'P',
         'Q':'Q','R':'R','S':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'Z'}     

    st1= 'abcdefghijklmnopqrstuvwxyz'
    st2= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for k in dic.keys():
    
        for i in range(0,len(list1)):
            n1=0
            if k in st1:
                if k==list1[i]:
                    n1=i+shift
                    if n1 >= len(list1):
                        l2=len(list1)-1-i
                        b=shift-l2
                        dic[k]=list1[b-1]
                        
                        break
                    else:
                        dic[k]=list1[i+shift]
                        
                        break
            elif k in st2:
                if k==list2[i]:
                    n1=i+shift
                    if n1 >= len(list2):
                        l2=len(list2)-1-i
                        b=shift-l2
                        dic[k]=list2[b-1]
                        
                        break
                    else:
                        dic[k]=list2[i+shift]
                        
                        break
            
    return dic

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
   
    string1=''
    b=coder
    i=0
    while i<len(text):
        
        if text[i]==" " or text[i]=="\n" or text[i] in string.digits or text[i] in string.punctuation:
            m=text[i]
            
            string1=string1+str(m)
            
            i=i+1
            
        else:

            m=b[text[i]]
            
            string1=string1+str(m)
           
            i=i+1

    return string1
    
     
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    
    m=applyCoder(text,buildCoder(shift) )
    return m
    
    
# Problem 2: Decryption

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    
    maxReal=0
    shift=0
    shiftcpy=0
    while shift<26:
        s=0
        m=applyShift(text, shift)
        
        list1=m.split(' ')
        
        for i in range(0,len(list1)):
            
            y=isWord(wordList, list1[i])
           
            if y==True:
               
                s=s+1

        if s>maxReal:
            maxReal=s
            shiftcpy=shift

        shift=shift+1

    return shiftcpy
        
    
    
    
def decryptStory():
    """
    Using the methods above,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
  
    r=loadWords()

    m1=getStoryString()
    
    p=findBestShift(r, m1)
    
    strans=applyShift(m1,p)
    return strans 
    

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    print s
    bestShift = findBestShift(wordList, s)
    print bestShift
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #s=decryptStory()
    #print s
