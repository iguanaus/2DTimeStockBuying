'''
2D stock Buying problem
By: John Peurifoy
done!!

The idea is that we will iterate through the columns, then linearly down the rows and store the best buy value, calculate what the trade prices will be at each node, and then see if that new trade price is greater than the old - if so store it.
Thus we will keep a running total of the best buy price to each position on the grid (note this takes n storage). We use this to find the trade times as we iterate through, and simply store the maximum
In order to store the location too, we simply each time we also store where that best buy price was (yea this is kinda a pain to code), and then we have the bestBuy point.
The best sell point actually can be stored in a singular location since we only care about the one and only BEST trade.

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
	#print "CurerntBestBuys: " + str(bestBuysFromEachRow)
	#for ele in values[0][0]:
	#	bestBuysFromEachRow.append(ele)#SHould be inf
	for i in xrange(0,len(values[0])):
		#print "CurerntBestBuys: " + str(bestBuysFromEachRow)
		#print "CurerntBestBuysLocs: " + str(bestBuyLocationsFromEachRow)
		#col = values[i]
		curBest = 10000000
		curBestBuyLoc = [0,0]
		for j in xrange(0,len(values)):
			ele = values[j][i]

			#print "Iterating ele: " + "i: " + str(i) + " j: " + str(j) + " : " + str(ele) + " : " + str(curBest)
			bestBuy= min([ele,bestBuysFromEachRow[j],curBest])
			#print "Bestbuy: " + str(bestBuy)
			#Okay now store these
			#if (bestBuy==ele):
			#elif (bestBuy ==bestBuysFromEachRow)
			#bestBuyLocationsFromEachRow[j]=[j,i]
			
			if (bestBuy ==ele):
				#print "It was here!"
				curBestBuyLoc = [j,i]
			elif(bestBuy==bestBuysFromEachRow[j]):
				#print "It was in the row!"
				curBestBuyLoc=bestBuyLocationsFromEachRow[j]
			elif(bestBuy==curBest):
				#print "It was in the col"
				curBestBuyLoc=curBestBuyLoc
			curBest = bestBuy
			bestBuysFromEachRow[j] = bestBuy
			bestBuyLocationsFromEachRow[j] = curBestBuyLoc
			tradePrice = ele-bestBuy
			if (tradePrice > bestTrade):
				#print "It is the best trade:" + str(curBestBuyLoc)
				bestTradeSell = [j,i]
				#bestTradeBuy = bestBuyLocationsFromEachRow[j]
				bestTrade = tradePrice
				bestTradeBuy = curBestBuyLoc
	print "Best Deal Made: " + str(bestTrade)
	print "Best Buy place: " + str(bestTradeBuy) + " : " + str(values[bestTradeBuy[0],bestTradeBuy[1]])

	print "Best Sell place: " + str(bestTradeSell) + " : " + str(values[bestTradeSell[0],bestTradeSell[1]])
	
	return

def genRandomMatrix(n,maxEle=10):
	#This creates a random n * n matrix and returns it
	sets = []
	for i in xrange(0,n):
		sets.append([])
		for j in xrange(0,n):
			sets[i].append(random.randint(1,maxEle))
	return sets
testArray =  array(genRandomMatrix(10000,100))
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