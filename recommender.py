####################################################################################################################
# Audiobook recommender system
# author: Igor Racca - K45DZH
####################################################################################################################

# debug mode
DEBUG = True

# defining rating class
class Rating:
	def __init__(self, rating, normalized, rated):
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
ratings = [[Rating(0,0, False)]*A for i in range(U)]

j = 0
# read inputs
for i in range(R):
	# reading recommendations from stdin
	u, a, r = map(int, input().split())
	if(u != j):
		j+=1
	# printDebug([u,j,a,r])
	ratings[j][a] = Rating(r,0, True)
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
		# printDebug('\ncomparing user %s and %s' % (i,k))
		if(k==i):
			# dealing with user similarity with himself
			similarities[i][k].u = k
			similarities[i][k].s = -2
			# print('User %s and %s are equal' % (i,k))
		else:		
			num, den1, den2 = 0,0,0
			for j in range(0, len(ratings[i])):
				# printDebug('ratings[i:%s][j:%s]:%s ratings[k:%s][j:%s]:%s' % (i,j,ratings[i][j].n,k,j,ratings[k][j].n))
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
			# printDebug('Similarity between user %s and %s=%s' % (i,k,s))
printDebug('')

for userSimilarities in similarities:
	# removing occurences of same user-user
	userSimilarities[:] = [x for x in userSimilarities if x.s != -2]
	# sorting by similarity (descending)
	userSimilarities.sort(key=lambda x: x.s, reverse=True)
	
printSimilarityDebug()



