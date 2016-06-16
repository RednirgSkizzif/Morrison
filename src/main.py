from sys import argv
import sentencer as sentencer

script, input_file = argv

list_of_sentences = sentencer.break_into_sentences(input_file)

