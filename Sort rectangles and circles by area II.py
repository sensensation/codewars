#https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/train/python
import math
def sort_by_area(seq):
   seq.sort(key=lambda x: x[0]*x[1] if (type(x) == tuple) else (math.pi*x**2))
   return print(seq)


sort_by_area([ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ])