from math import sqrt

class Cell:
	def __init__(self):
		self.Color = 'white'

	def GetColor(self):
		return self.Color

	def PaintCell(self, color):
		self.Color = color

class Matrix:
	def __init__(self, rows, columns):
		self.Rows = rows
		self.Columns = columns
		self.Values = []
		for i in range(rows):
			a=[0]*columns
			self.Values.append(a)
		for i in range(rows):
			for j in range(columns):
				self.Values[i][j] = Cell()

#Cells: Number of matrix's cells.
def CreateMatrix(Cells):
	
	#Generate the number of rows and columns
	#so matrix can be similar as possible to a square matrix	

	root = int(sqrt(Cells))
	l = list(range(1,root+1))
	l.reverse()
	for i in l:
		if((Cells%i)==0):
			rows=i
			break
	columns = Cells / rows
	
	matrix = Matrix(rows,columns)
	return matrix;

#Parameters: matrix, list of colors, and how many cells has to be painted in each color
def CheckMatrix(matrix, colors, number_color):
	painted = number_color	
	
	for item in painted:
		item = 0
	
	rows = matriz.rows
	columns = matriz.columns
	
	for i in range(rows):
		for j in range(columns):
			cont=0
			for color in colors:
				if matriz.Cells[i][j].GetColor() == color:
					painted[cont]=painted[cont] + 1
				
				cont=cont+1
	
	#Check	
	#Controlar si la cantidad de celdas pintadas por color coinciden
	#con las cantidades solicitadas
	success=True
	cont=0
	for item in painted:
		if painted[cont] != number_color[cont]:
			success=False
			break
		
		cont=cont+1
	
	return success

