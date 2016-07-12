"""
Created by: Dylan Frizzell
    Take in a txt file and output a list of sentence strings
"""

from sys import argv
import nltk as gram

script, input_file = argv



def break_into_sentences(textFile):
 #  "" "This function will take the textFile and output a list of each discrete sentence"""

    output_array = []
    working_file = open(textFile,'r')
   
    
    text = working_file.read()
    print(text)
    print(" ")
    characters = len(text)
    startingPoint=0
    for i in range (0,characters):
        if (text[i]=='.' or text[i]=='?' or text[i]=='!' or text[i]==';'):
            output_array.append(text[startingPoint:i+1])
            startingPoint=i+1
    working_file.close()
    return output_array

def tokenize_sentence(sentence):
#	"This function will assign a part of speech with each word in a sentence"
	tokens = gram.word_tokenize(sentence)
	return tokens

def identify_words(wordlist):
#	This function will take a list of words and output a 2XN array of those words coupled with their part of speech using nltk syntax
	word_types = gram.pos_tag(wordlist)
	return word_types


