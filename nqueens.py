board = [(i,j) for i in range(8) for j in range(8)]

def get_board_config(queen_rows,valid_spaces,n):
	if n==len(queen_rows):
		return queen_rows
	for i in range(n):
		candidate = (len(queen_rows),i)
		if candidate in valid_spaces:
			new_queen_rows = list(queen_rows)
			new_queen_rows.append(candidate)

			out = get_board_config(new_queen_rows,new_queen_update_valid(candidate[0],candidate[1],valid_spaces,n),n)
			if out is not None:
				return out
	return None


def new_queen_update_valid(row,col,board,n):
	new_board = set(board)
	#get all dem bishes in dat row
	for i in range(n):
		new_board.discard((row,i))
	#col
	for i in range(n):
		new_board.discard((i,col))
	#diag 1
	r = row
	c = col
	while r<n and c<n:
		new_board.discard((r,c))
		r+=1
		c+=1
	r = row
	c = col
	while r>=0 and c>=0:
		new_board.discard((r,c))
		r-=1
		c-=1
	#diag 2
	r = row
	c = col
	while r>=0 and c>=0 and r<n and c<n:
		new_board.discard((r,c))
		r+=1
		c-=1
	r = row
	c = col
	while r>=0 and c>=0 and r<n and c<n:
		new_board.discard((r,c))
		r-=1
		c+=1
	return new_board

print(get_board_config([],board,8))
