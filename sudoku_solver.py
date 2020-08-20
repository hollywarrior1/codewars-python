#sudoku solver

def puzzle_column(puzzle):
	puz_column = [[0]*9 for i in range(0, 9)]
	for i in range(0, 9):
		for j in range(0, 9):
			puz_column[i][j] = puzzle[j][i]
	return puz_column

def puzzle_cube(puzzle):
	k = 0
	m = 0
	puz_cube = [[0]*9 for i in range(0, 9)]
	for i in range(0, 9):
		if i<3:
			k = 0
		elif i<6:
			k = 3
		else:
			k = 6

		if i==0 or i==3 or i==6:
			m = 0
		elif i==1 or i==4 or i==7:
			m = 3
		else:
			m = 6
		
		for j in range(0, 9):
			
			if i<3:
				if j<3:
					puz_cube[i][j] = puzzle[k][m]
					m+=1
				elif j<6:
					puz_cube[i][j] = puzzle[k+1][m-3]
					m+=1
				else:
					puz_cube[i][j] = puzzle[k+2][m-6]
					m+=1
			
			elif i<6:
				if j<3:
					puz_cube[i][j] = puzzle[k][m]
					m+=1
				elif j<6:
					puz_cube[i][j] = puzzle[k+1][m-3]
					m+=1
				else:
					puz_cube[i][j] = puzzle[k+2][m-6]
					m+=1
			
			else:
				if j<3:
					puz_cube[i][j] = puzzle[k][m]
					m+=1
				elif j<6:
					puz_cube[i][j] = puzzle[k+1][m-3]
					m+=1
				else:
					puz_cube[i][j] = puzzle[k+2][m-6]
					m+=1
	return puz_cube

		

def sudoku(puzzle):
	
	str1 = '123456789'
	for i in range(0, 9):
		for j in range(0, 9):
			if puzzle[i][j] == 0:
				puzzle[i][j] = ' '
			else:
				puzzle[i][j] = str(puzzle[i][j])
	
	puz_cube = puzzle_cube(puzzle)
	puz_column = puzzle_column(puzzle)

	while True:
		spaces = 0
		for i in range(0, 9):
			for j in range(0, 9):

				if puzzle[i][j] == ' ':
					spaces+=1

				if i<3 and j<3:
					n = 0
				elif i<3 and j<6:
					n = 1
				elif i<3 and j<9:
					n = 2
				elif i<6 and j<3:
					n = 3
				elif i<6 and j<6:
					n = 4
				elif i<6 and j<9:
					n = 5
				elif i<9 and j<3:
					n = 6
				elif i<9 and j<6:
					n = 7
				elif i<9 and j<9:
					n = 8

				if puzzle[i][j] == ' ':
					char = ''
					for k in range(0, 9):
						if (str1[k] not in puzzle[i]) and (str1[k] not in puz_column[j]) and (str1[k] not in puz_cube[n]):
							char+=str1[k]
						if len(char)==2:
							char = ''
							break
					if len(char) == 1:
						puzzle[i][j] = char
						puz_column[j][i] = char

						if (i == 0) or (i == 3) or (i == 6):
							if (j == 0) or (j == 3) or (j == 6):
								puz_cube[n][0] = char
							elif (j == 1) or (j == 4) or (j == 7):
								puz_cube[n][1] = char
							elif (j == 2) or (j == 5) or (j == 8):
								puz_cube[n][2] = char

						elif (i == 1) or (i == 4) or (i == 7):
							if (j == 0) or (j == 3) or (j == 6):
								puz_cube[n][3] = char
							elif (j == 1) or (j == 4) or (j == 7):
								puz_cube[n][4] = char
							elif (j == 2) or (j == 5) or (j == 8):
								puz_cube[n][5] = char

						elif (i == 2) or (i == 5) or (i == 8):
							if (j == 0) or (j == 3) or (j == 6):
								puz_cube[n][6] = char
							elif (j == 1) or (j == 4) or (j == 7):
								puz_cube[n][7] = char
							elif (j == 2) or (j == 5) or (j == 8):
								puz_cube[n][8] = char

		if spaces == 0:
			break

	for i in range(0, 9):
		for j in range(0, 9):
			puzzle[i][j] = int(puzzle[i][j])
	return puzzle


import numpy as np


puz1 = [[5,4,8,6,0,3,0,9,0],
		[9,1,0,2,0,5,8,6,3],
		[2,0,0,0,8,0,4,5,7],
		[0,0,0,4,0,0,0,1,0],
		[7,6,5,9,1,0,0,0,0],
		[0,8,0,5,0,0,0,0,0],
		[0,5,3,7,9,0,1,4,2],
		[6,0,0,0,0,0,7,8,0],
		[1,7,0,0,0,0,0,0,5]]

puzzzle = sudoku(puz1)
print(np.matrix(puzzzle))