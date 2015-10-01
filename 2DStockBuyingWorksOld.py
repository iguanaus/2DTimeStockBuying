'''
2D stock Buying problem

The idea is that we will iterate through the columns, then linearly down the rows and store the best buy value, calculate what the trade prices will be at each node, and then see if that new trade price is greater than the old - if so store it.

'''
from numpy import *
import random

def makeSomeDollaDollaBills(values):
	print "Iterating: "
	print values
	#for row in values:
	#	print row
	#values = values.T
	#print values
			

	bestBuysFromEachRow = []
	bestBuyLocationsFromEachRow = []
	bestTrade = 0 #Should be inf
	bestTradeSell = [0,0]
	bestTradeBuy = [0,0]
	for i in xrange(0,len(values)):
		bestBuysFromEachRow.append(values[i][0])
		bestBuyLocationsFromEachRow.append([i,0])
	print "CurerntBestBuys: " + str(bestBuysFromEachRow)
	#for ele in values[0][0]:
	#	bestBuysFromEachRow.append(ele)#SHould be inf
	for i in xrange(0,len(values[0])):

		print "CurerntBestBuys: " + str(bestBuysFromEachRow)
		#col = values[i]
		curBest = 10000000
		for j in xrange(0,len(values)):
			ele = values[j][i]
			print "Iterating ele: " + str(ele) + " : " + str(curBest)
			bestBuy= min([ele,bestBuysFromEachRow[j],curBest])
			#Okay now store these
			bestBuysFromEachRow[j] = bestBuy
			#if (bestBuy==ele):
			#elif (bestBuy ==bestBuysFromEachRow)
			#bestBuyLocationsFromEachRow[j]=[j,i]
			curBest = bestBuy
			tradePrice = ele-bestBuy
			if (tradePrice > bestTrade):
				bestTradeSell = [j,i]
				bestTradeBuy = bestBuyLocationsFromEachRow[j]
				bestTrade = tradePrice
	print "Best Deal Made: " + str(bestTrade)
	print "Best Buy place: " + str(bestTradeBuy)

	print "Best Sell place: " + str(bestTradeSell)
	
	return

def genRandomMatrix(n,maxEle=10):
	#This creates a random n * n matrix and returns it
	sets = []
	for i in xrange(0,n):
		sets.append([])
		for j in xrange(0,n):
			sets[i].append(random.randint(1,maxEle))
	return sets
testArray =  array(genRandomMatrix(4,100))
makeSomeDollaDollaBills(testArray)
# #Yea I should really find a way to generate these
# array2 =  array([[1,2,3,4],
# 	           [2,3,4,5],
# 	           [2,3,4,2],
# 	           [3,23,4,5]])

# makeSomeDollaDollaBills(array2)

# array2 =  array([[1,2,3,4],
# 	           [2,3,4,5],
# 	           [2,3,4,2],
# 	           [3,23,4,5]])

# makeSomeDollaDollaBills(array2)

# array2 =  array([[1,2,3,4],
# 	           [2,3,4,5],
# 	           [2,3,4,2],
# 	           [3,23,4,5]])

# makeSomeDollaDollaBills(array2)

# array2 =  array([[1,2,3,4],
# 	           [2,3,4,5],
# 	           [2,3,4,2],
# 	           [3,23,4,5]])

# makeSomeDollaDollaBills(array2)

# array2 =  array([[5,2,3,1],
# 	           [2,3,4,2],
# 	           [2,3,4,2],
# 	           [3,3,4,5]])

# makeSomeDollaDollaBills(array2)