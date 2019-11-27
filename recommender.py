####################################################################################################################
# Audiobook recommender system
# author: Igor Racca - K45DZH
####################################################################################################################

# debug mode
DEBUG = True

# defining rating class
class Rating:
	def __init__(self, audiobook, rating):
		self.a = audiobook
		self.r = rating

# defining print function for debug mode
def printDebug(s):
	if DEBUG: print(s)

# printing ratings matrix #DEBUG
def printRatingsDebug():
	if DEBUG:
		for row in ratings:
			for val in row:
				print('a[%s]:%s' % (val.a, val.r), end = '\t')
			print()

####################################################################################################################
# Main
####################################################################################################################

# reading R, U and A size (ratings, users and audiobooks)
R, U, A = map(int, input().split())

# initializang list of user ratings
ratings = [[] for i in range(U)]

for i in range(R):
	# reading recommendations from stdin
	u, a, r = map(int, input().split())
	printDebug([u,a,r])
	# creating obj rating
	rating = Rating(a,r)
	# appending to the ratings list according to user u
	ratings[u].append(rating)

printRatingsDebug()

