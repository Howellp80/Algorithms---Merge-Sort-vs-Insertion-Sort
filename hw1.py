# Parker Howell
# cs325 - Homework 1


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random

#=================================================================
# Merge Sort
# Referenced from: https://en.wikipedia.org/wiki/Merge_sort
#=================================================================
def mergeSort(arr):
	if len(arr)>1:
		# split the array
		mid = len(arr) // 2
		lHalf = arr[:mid]
		rHalf = arr[mid:]

		# recursivly split the sub arrays
		mergeSort(lHalf)
		mergeSort(rHalf)

		i = j = k = 0
		# reconstruct array
		# while lHalf and rHalf are not empty
		while ((i < len(lHalf)) and (j < len(rHalf))):
			# fills in k with lesser of leading sub array values
			if lHalf[i] < rHalf[j]:
				arr[k]=lHalf[i]
				i += 1
			else:
				arr[k]=rHalf[j]
				j += 1
			k += 1

		# fill in array with remaining values of lHalf
		while i < len(lHalf):
			arr[k]=lHalf[i]
			i += 1
			k += 1

		# fill in array with remaining values of rHalf
		while j < len(rHalf):
			arr[k]=rHalf[j]
			j += 1
			k += 1



#=================================================================
# Insertion Sort
# Referenced from: https://en.wikipedia.org/wiki/Insertion_sort
#=================================================================
def insertionSort(arr):
	# for each index in
	for i in range(1, len(arr)):


		curVal = arr[i]
		pos = i

		while ((pos > 0) and (arr[pos-1] > curVal)):
			arr[pos] = arr[pos-1]
			pos -= 1

		arr[pos] = curVal




#=================================================================
# Main Program
#=================================================================
# Sizes of arrays to fill with random integers
arrSize = [0,2000,8000,32000,128000,512000,1024000,4096000]

# make a array for each value in arrSize
for i in arrSize:	

	arr = []
	# append randomly generated values between 1-1000 for each index up to i
	for index in range(i):
		arr.append(random.randint(1,1000))
	#print(arr)

	# time how long it takes to sort arr of size i with mergeSort
	mt1 = time.time()
	mergeSort(arr)
	mt2 = time.time()
	mT = mt2 - mt1

	# time how long it takes to sort arr of size i with insertionSort
	it1 = time.time()
	insertionSort(arr)
	it2 = time.time()
	iT = it2 - it1
	
	# print information of each iteration to console
	print ("Size i: "),
	print (i)
	print ("Merge Time: "),
	print (mT)
	print ("Insertion Time: "),
	print (iT)	
	print ("\n")



#testArr2 = [458,20,759,1,4,76,766,8548,4,76,83,746,210]
#mergeSort(testArr1)
#print(testArr1)
#testArr1 = [61,420,555,27,77,76,24,47,598,25,786,2147,10]
#insertionSort(testArr1)
#print(testArr1)

#insertionSort(testArr2)
#print(testArr2)
#testArr2 = [458,20,759,1,4,76,766,8548,4,76,83,746,210]
#mergeSort(testArr2)
#print(testArr2)