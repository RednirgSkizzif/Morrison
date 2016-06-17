"""
Created by: Dylan Frizzell
    Take in a txt file and output a list of sentence strings
"""

from sys import argv
import nltk

script, input_file = argv



def break_into_sentences(textFile):
    "This function will take the textFile and output a list of each discrete sentence"

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
    for x in range(0,len(output_array)):
        print(output_array[x])
        print("----------------------------------------")

    working_file.close()
    return output_array





