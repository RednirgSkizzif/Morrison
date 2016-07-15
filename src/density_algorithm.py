
def make_fragments(N_by_two):
		fragment_list = []
		runner = []
		for i in range(0,len(N_by_two)):
			runner.append(N_by_two[i][0])
			#print(N_by_two[i][0])
			print(N_by_two[i][1])
			if (N_by_two[i][1] == 'NNS' or N_by_two[i][1]=='VBN'or N_by_two[i][1]=='VBP' or  N_by_two[i][1] == 'NNP' or N_by_two[i][1]=='CC' or N_by_two[i][1]==',' and len(runner)>1):
					fragment_list.append(runner)
					runner = []
		
		print("here is the final product:")
		print(fragment_list)
		return fragment_list
