from random import randint




def sen_seg(astr, pattern):
	"""takes a string, a pattern and returns a split string based on pattern """ 

	word_list = []
	last = 0

	for ch in range(len(pattern)):
		if pattern[ch] == '1':
			word_list.append(astr[last:ch+1])
			last = ch+1 
	word_list.append(astr[last:])
	return word_list


def evaluate(astr, pattern):

	words = sen_seg(astr, pattern)
	t_size = len(words)
	lex = len(' '.join(list(set(words))))
	return lex  + t_size




st = 'thisisatesttextthatneedstobesplitthisisatesttextthatneedstobesplit'


pat = "00010110001000100010000101010000100010110001000100010000101010000"




