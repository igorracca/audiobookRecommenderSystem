####################################################################################################################
# Audiobook recommender system
# author: Igor Racca - K45DZH
####################################################################################################################

# debug mode
DEBUG = False

# number of k-similar users 
K_NEIGHBORS = 2

# number of top audiobooks to be displayed in the output
TOP = 10

# defining rating class
class Rating:
	def __init__(self, audiobook, rating, normalized, rated):
		self.a = audiobook
		self.r = rating
		self.n = normalized
		self.t = rated

# defining userSimilarity
class Similarity:
	def __init__(self, user, similarity):
		self.u = user
		self.s = similarity

# defining print function for debug mode #DEBUG
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
ratings = [[Rating(0,0,0,False) for j in range(A)] for i in range(U)]

j = 0
# read inputs
for i in range(R):
	# reading recommendations from stdin
	u, a, r = map(int, input().split())
	if(u != j):
		j+=1
	# printDebug([u,j,a,r])
	ratings[j][a] = Rating(a, r, 0, True)
printRatingsDebug()

# normalize ratings
for i in range(0, len(ratings)):
	# calculate the row mean 
	rowMean = sum(x.r for x in ratings[i]) / sum(1 for x in ratings[i] if x.t == True)
	# printDebug('rowMean: %s' % rowMean)
	for j in range(0, len(ratings[i])):
		if(ratings[i][j].t == False):
			ratings[i][j].n = 0
		else:
			ratings[i][j].n = ratings[i][j].r - rowMean
printNormalizedRatingsDebug()

# initializing similarity matrix
similarities = [[Similarity(0,0) for j in range(U)] for i in range(U)]
# compute similarity between users (consine distance)
for i in range(0, len(ratings)):
	for k in range(i, len(ratings)):
		if(k==i):
			# dealing with same user-user 
			similarities[i][k].u = k
			similarities[i][k].s = -2
		else:		
			num, den1, den2 = 0,0,0
			for j in range(0, len(ratings[i])):
				# numerator is product of vector I and J 
				num += ratings[i][j].n * ratings[k][j].n
				# denominator is summation of square root of squared vector I and J 
				den1 += ratings[i][j].n**2
				den2 += ratings[k][j].n**2
			# square root
			den1 = den1 **(1/2)	
			den2 = den2 **(1/2)	
			den = den1 * den2
			if(den==0):
				s=0
			else:
				s = num/den
			# writing similarity for user i to k
			similarities[i][k].u = k	
			similarities[i][k].s = s
			# writing similarity for user k to i (same)
			similarities[k][i].u = i
			similarities[k][i].s = s

for userSimilarities in similarities:
	# removing occurences of same user-user
	userSimilarities[:] = [x for x in userSimilarities if x.s != -2]
	# sorting by similarity (descending)
	userSimilarities.sort(key=lambda x: x.s, reverse=True)
	
printSimilarityDebug()

for i in range(len(ratings)):
	for j in range(len(ratings[i])):
		if(ratings[i][j].t == False):
			num, den = 0,0 
			for k in range(0, K_NEIGHBORS):
				x = similarities[i][k].u
				num += similarities[i][k].s * ratings[x][j].r
				den += similarities[i][k].s
			if(den != 0):
				ratings[i][j].r = num/den
			ratings[i][j].a = j
printRatingsDebug()

for userRatings in ratings:
	# removing occurences of same user-user
	userRatings[:] = [x for x in userRatings if x.t == False]
	# sorting by similarity (descending)
	userRatings.sort(key=lambda x: x.r, reverse=True)
printRatingsDebug()

# print top10 audiobook recommendation per user
for i in range(0, len(ratings)):
	for j in range(0, TOP):
		if(j<TOP-1):
			print('%s' % (ratings[i][j].a), end = '\t')
		else:
			print('%s' % (ratings[i][j].a), end = '')
	if(i<len(ratings)-1):
		print()