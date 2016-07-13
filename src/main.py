from sys import argv
import sentencer as sentencer
import density_algorithm as alg

script, input_file = argv

list_of_sentences = sentencer.break_into_sentences(input_file)

for i in range (len(list_of_sentences)):
	word_list = sentencer.tokenize_sentence(list_of_sentences[i])
	ID_list = sentencer.identify_words(word_list)
	#print(ID_list)
	alg.make_fragments(ID_list)


