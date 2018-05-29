#O(n^2) time O(1) space solution with two for loops. Fails the Online Judge
def twoSum1(nums,target):
	for i,ival in enumerate(nums):#look up enumerate, and check out what python generators are
		for j,jval in enumerate(nums):
			if i!=j and (ival+jval)==target:
				return [i,j]#python's list literals are nice


#O(n) time and space solution using dictionary
def twoSum2(nums,target):
	dictionary = {}#look up python dictionaries. They are implemented using hashmaps, and store key value pairs
	for i,num in enumerate(nums):
		if (target-num) in dictionary:#does lookup in constant time
			return [dictionary[target-num],i]
		dictionary[num] = i #added to dictionary in constant time 

#I was gonna do one with sorting but the ones with sorting that I can think of can only be done in O(n*log(n)) time
#and O(n) space (I cant think of a way to do it without making a map from list entries to their indicies). I wouldn't bother
#coding it up because its just objectively worse than the last one. But if we know our input is sorted there's a clever
#solution

#Same problem when nums is sorted. O(n) time and O(1) space

def twoSumSorted(nums,target):
	lo = 0
	hi = len(target)-1
	while lo<hi:
	#loop invariant: if i<j such that nums[i]+nums[j]==target exists, then lo <= i<j <= hi
		if (nums[lo]+nums[hi]) == target:
			return [lo,hi]
		elif (nums[lo]+nums[hi])>target:
			#since nums[lo] is the least possible value in nums that can sum to target
			#nums[lo]+nums[hi] > target, so nums[i]+nums[hi]>target for all possible values of i
			#So, nums[hi] cant be a part of the sum, and we take it out of the range
			hi-=1
		else:#nums[lo]+nums[hi])>target:
			#same idea as above
			lo+=1
	
	
	


