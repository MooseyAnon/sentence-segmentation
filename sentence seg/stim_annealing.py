from random import random
from sentence_seg import *


def switch(pat, pos):
	"""
	this func flips 0's and 1's in order to change where the sentence/word is segmented.

	the pattern is split at the index corrisponding with pos. The item at that location is then subtracted 

	from 1, i.e. (1-0 = 1; 1-1=0). And then it's joined back to the number either side of it. 

	ex: 
	pat = "0000"

	flip(pat, 2) 

	return 0010 where the word is split at 1

	"""
	return pat[:pos] + str(1 - int(pat[pos])) + pat[pos+1:]


 
def switch_n(pat, n):

	"""
	this func runs the flip aglo n number of times at a (psudo) random point in the pattern

	"""

	for i in range(n):
		pat = switch(pat, randint(0, len(pat)-1))
	return pat




def stim_anneal(pat, string, epochs, cool_rate):

	"""
	A stimulated annealing algo to minimise the evaluation score of the pattern
	"""
	temp = float(len(pat)) # arbitrary value for the tempreture. Should be decently high number 
	while temp > 0.5:
		best_pat, best = pat, evaluate(string, pat) # initialise first values for the 'best pattern' and 'best score'. These are the values to be measured against
		for i in range(epochs): # number of cycles we want the algo to go for
			guess = switch_n(pat, int(round(temp)))
			score = evaluate(string, guess)
			if score < best: # check if new score is lower than last best score (we want to minimise eval score)
				best_pat, best = guess, score # if new score is better, update 'best pattern' and 'best score'
			# need to add =~ esle if (E ^ (∆E/temp) > random.random(0.0, 1.0)

		score, pat = best, best_pat # update score and pattern for new cycle
		temp = temp / cool_rate # lower tempreture 

		print evaluate(string, pat), sen_seg(string, pat)
		print 
		print pat

