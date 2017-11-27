#Python's list objects are implemented using ArrayLists, but you could create another list class
#with all of the functionality of Python list using a singlely linked list

#Lets write a linked list class that does this using our ListNode class
#This is gonna kind of suck to have to write, but it'll probably make you more comfortable dealing
#with linked lists

class ListNode:
	def __init__(self,val):
		self.val = val
		self.nxt = None 

class LinkedList:
	def __init__(self):
		#construct an empty linked list.
		#Try and see how many attributes you're going to need

	def __str__(self):
		#return a string representation of your list. Try and do this one
		#early so you can use it to debug the rest. __str__ is a special
		#python function, it can be invoked like this: str(lis), instead of
		#just lis.__str__(). Also, print(lis) will work when you implement this

	def append(self,val):
		#add val to the end of the list

	def length(self):
		#return number of elements in list

	def set(self,i,val):
		#set the ith value of our list to val. Should work for 0<=i<(length of list)

	def insert(self,i,val):
		#insert the item val in the index i
		#eg x = [1,2,3,4,5]
		#x.insert(2,9)
		#x now equals [1,2,9,3,4,5]
		#Should work for 0<=i<=(length of list)

	def remove(self,i):
		#remove the value at the i'th index
		#should work for 0<=i<(length of list)

	def get(self,i):
		#return the value stored at index i. Return None if i>=(length of list)

	def extend(self,other_list):
		#append all of the contents of other list to the end of the list in order


#Also, try these LeetCode problems: 206, 237, 83, 21, and 234
#Circle back to 2 also when you get time
