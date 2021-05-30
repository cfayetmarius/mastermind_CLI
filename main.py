#hackaton 50 min mastermind game for school
import random, termcolor, sys, colorama, builtins
colorama.init()

class mlist:
	def __init__(self, lst):
		self.lst = lst
	def noerrindex(self,v) :
		try :
			return(self.lst.index(v))
		except :
			return(None)

def getcomb() :
	return(random.sample(['R','G','B','Y','W','M'],4))

def printboard(tryed) :
	for lign in tryed :
		print("|"+termcolor.colored("¤",lign[0])+"|"+termcolor.colored("¤",lign[1])+"|"+termcolor.colored("¤",lign[2])+"|"+termcolor.colored("¤",lign[3])+"|   "+termcolor.colored('°',lign[4])+termcolor.colored('°',lign[5])+termcolor.colored('°',lign[6])+termcolor.colored('°',lign[7])+'\n')
	print('_________')

def filltryed() :
	return([["white" for i in range(9)]for i in range(12)])


def main() :
	colordic = {'R':'red','Y':'yellow','B':"blue",'G':'green','W':'white','M':'magenta'}
	comb = getcomb()
	tryed = filltryed()
	print(comb)
	for i in range(12) :
		played = input(">What you want to play. Use only RGBYWM to play. (standing for red green blue yellow white magenta)\n4 LETTERS :") 
		if comb == list(played) :
			print('You won !\n')
			sys.exit() 
		found = ['green' for c in played if played.index(c)==mlist(comb).noerrindex(c)]+['blue' for c in played if c in comb and played.index(c) != mlist(comb).noerrindex(c)]
		for i in range(4-len(found)) :
			found.append('red')
		tryed[i] = list(colordic[c] for c in played)+found
		printboard(tryed)
	print("No attempts anymore, you lost ! The right comb was :",''.join(comb)) 

main()