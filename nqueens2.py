def conflict(q1,q2):
	"""returns true if the two queens attack eachother"""
	return q1[0]==q2[0] or q1[1]==q2[1] or q1[0]+q1[1]==q2[0]+q2[1] or q1[0]-q1[1]==q2[0]-q2[1]


def get_queen_arrangement(queen_list,n,out):
	if len(queen_list)==n:
		out.append(list(queen_list))
	for i in range(n):
		has_conflict = False
		for queen in queen_list:
			if conflict(queen,(len(queen_list),i)):
				has_conflict=True
		if has_conflict:
			continue

		queen_list.append((len(queen_list),i))
		get_queen_arrangement(queen_list,n,out)
		queen_list.pop()

def get_queen_arrangement_count(n,queen_list=[]):
	if len(queen_list)==n:
		return 1
	out = 0
	for i in range(n):
		has_conflict=False
			
		for queen in queen_list:
			if conflict((len(queen_list),i),queen):
				has_conflict = True
		if has_conflict:
			continue
		queen_list.append((len(queen_list),i))
		out+=get_queen_arrangement_count(n,queen_list)
		queen_list.pop()

	return out


print("Configurations count for various values of n:\n")
for i in range(10):
	print("{}	{}".format(i,get_queen_arrangement_count(i)))

out = []
print("\nExample 8 queens configuration")
get_queen_arrangement([],8,out)
print(out[0])
