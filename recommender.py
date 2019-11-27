####################################################################################################################
# Audiobook recommender system
# author: Igor Racca - K45DZH
####################################################################################################################

# debug mode
DEBUG = True

# defining rating class
class Rating:
	def __init__(self, rating, normalized):
		self.r = rating
		self.n = normalized

# defining userSimilarity
class Similarity:
	def __init__(self, user, similarity):
		self.u = user
		self.s = similarity

# defining print function for debug mode
def printDebug(s):
	if DEBUG: print(s)

# printing ratings matrix #DEBUG
def printRatingsDebug():
	if DEBUG:
		for userRatings in ratings:
			for rating in userRatings:
				print(rating.r, end = '\t')
			print()
	print()

# printing normalized ratings matrix #DEBUG
def printNormalizedRatingsDebug():
	if DEBUG:
		for userRatings in ratings:
			for rating in userRatings:
				print(rating.n, end = '\t')
			print()
	print()

# printing similarity matrix #DEBUG
def printSimilarityDebug():
	if DEBUG:
		for userSimilarities in similarities:
			for similarity in userSimilarities:
				print('s[%s]:%s' % (similarity.u, similarity.s), end = '\t')
			print()
	print()

####################################################################################################################
# Main
####################################################################################################################

# reading R, U and A size (ratings, users and audiobooks)
R, U, A = map(int, input().split())

# initializang ratings matrix
ratings = [[Rating(0,0)]*A for i in range(U)]

j = 0
for i in range(R):
	# reading recommendations from stdin
	u, a, r = map(int, input().split())
	if(u != j):
		j+=1
	# printDebug([u,j,a,r])
	ratings[j][a] = Rating(r,0)
printRatingsDebug()

# normalize ratings
for i in range(0, len(ratings)):
	# calculate the row mean 
	rowMean = sum(x.r for x in ratings[i]) / sum(1 for x in ratings[i] if x.r != 0)
	# printDebug('rowMean: %s' % rowMean)
	for j in range(0, len(ratings[i])):
		if(ratings[i][j].r == 0):
			ratings[i][j].n = 0
		else:
			ratings[i][j].n = ratings[i][j].r - rowMean
printNormalizedRatingsDebug()

# # initializing user similary matrix
similarities = []

# printSimilarityDebug()	
	
		