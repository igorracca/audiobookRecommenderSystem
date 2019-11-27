####################################################################################################################
# Audiobook recommender system
# author: Igor Racca - K45DZH
####################################################################################################################

# debug mode
DEBUG = True

# defining vehicle class
class Vehicle:
	def __init__(self, id, w, h, priority):
		self.id = id
		self.w = w
		self.h = h
		self.priority = priority

# defining print function for debug mode
def printDebug(s):
	if DEBUG: print(s)

# printing ratings matrix #DEBUG
def printRatingsDebug():
	if DEBUG:
		for row in ratings:
			for val in row:
				print(val, end = '\t')
			print()

####################################################################################################################
# Main
####################################################################################################################

# reading R, U and A size (ratings, users and audiobooks)
R, U, A = map(int, input().split())

# initializang ratings matrix
ratings = [[0]*A for i in range(U)]

j = 0
for i in range(R):
	# reading recommendations from stdin
	u, a, r = map(int, input().split())
	if(u != j):
		j+=1
	# printDebug([u,j,a,r])
	ratings[j][a] = r

printRatingsDebug()