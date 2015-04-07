# class Position:
# 	def __init__(self,y,x):
# 		self.x = x
# 		self.y = y
# 	def increment(self):
# 		self.x = self.x+1

# def hasNext(col,i):
# 	pos = i
# 	if i+1 < len(col) and col[i+1] == 0:
# 		return False
# 	return True

def answer(document, searchTerms):
	wordMap = {} # hasmap to store searchTerms
	doc = document.split()
	end = 0     # end index of smallestWindow
	start = 0   # start index of smallestWindow
	startPt = 0 # pt to beginning of substring
	endPt = 0   # pt to ending of substring
	length = 1001   # use length to determiing which substring is shortest
	count = 0   # How many unique searchTerms have been found
	
	# Store all of the searchTerms into a hashmap
	# Key - the string, Value - number of occurences
	for x in range(len(searchTerms)):
		wordMap[searchTerms[x]] = 0

    # Iterate through the string to find shortest window by
    # using two pointers
	while startPt < len(doc):
		if endPt < len(doc):
		    # Increment endPt until all searchTerms are found at least 1
			if count != len(searchTerms):
			    # Increment the amount of occurence if found
				if doc[endPt] in wordMap:
					wordMap[doc[endPt]] = wordMap[doc[endPt]]+1
					# Increment count only if its the first occurence
					# of new searchTerm
					if wordMap[doc[endPt]] == 1:
						count = count + 1
				endPt = endPt + 1
		
		# Begin shorting the string if all searchTerms are found in one substring
		if count == len(searchTerms):
		    # Update the minimum window and range
			if endPt - startPt < length:
				length = endPt - startPt
				end = endPt
				start = startPt
			# If the word dropped is a searchTerm decrement its occurence
			if doc[startPt] in wordMap:
				wordMap[doc[startPt]] = wordMap[doc[startPt]] - 1
				# Decrement count only if the occurence of searchTerm is now 0 
				if wordMap[doc[startPt]] == 0:
					count = count - 1
			startPt = startPt + 1
		
		# If the endPt reached the end, continue incrementing only the startPt
		if endPt == len(doc) and count != len(searchTerms):
			startPt = startPt + 1
	
	# Create the minimum window string
	window = doc[start]
	for w in range(start+1,end):
		window = window + " " + doc[w]
	return window
	
document = "a b d c b a"
document = document.lower()
searchTerms = ["c","b","a"]
#searchTerms = ["words","with"]
window = answer(document,searchTerms)
print(window)