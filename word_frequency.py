import string
from collections import Counter

def word_frequency(text):

    if(text == ""):
       
        return dict(Counter(text))

    lower_text = to_lower_case(text)
    new_text = strip_punctuation(lower_text)

    
    words = new_text.split()
    count = Counter(words)
    
    return dict(count)



#FUNCTION THAT CHANGE CHARACTERS TO LOWERCASE

def to_lower_case(text):
    lower_text = text.lower()
    return lower_text

# FUNCTION THAT CHANGES PUNCTUATION TO ""

def strip_punctuation(text):

   table = str.maketrans("","", string.punctuation)
   new_text = text.translate(table)
   return new_text




print(word_frequency("Hello... World?! Hello!!!"))





