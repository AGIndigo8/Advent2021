#%
import numpy
from numpy import linalg as LA
import math
def get_points(data):
  #data x1,y1 -> x2,y2
  str_points = data.split('->')
  #x,y becomes tuple(x,y)
  str_points = [pt.split(',') for pt in str_points]
  return [numpy.array((int(pt[0]),int(pt[1]))) for pt in str_points]

class Line:
    #check to see if it is horizontal or vertical.
    def orthos_bool(self):
        return (
         self.p0[1]==self.p1[1],
         self.p0[0]==self.p1[0]
        )

    def __init__(self, points):
        self.p0=points[0]
        self.p1=points[1]
        self.vector = self.p1 - self.p0
        self.vector = self.vector / LA.norm(self.vector)
        if not any(self.orthos_bool()):
            self.vector = self.vector * math.sqrt(2)

    def __iter__(self):
        self.current_pt = self.p0 - self.vector
        self.next_end = False
        return self

    def __next__(self):
        self.current_pt += self.vector
        if(self.next_end): raise StopIteration
        if numpy.array_equal(self.current_pt, self.p1) :
            self.next_end = True
        return self.current_pt

with open("data.txt") as f:
  data_lines = f.readlines()

field = numpy.zeros((1000,1000))
lines = [Line(get_points(pt)) for pt in data_lines]
for line in lines:
    for pt in line:
        field[int(pt[0]), int(pt[1])] +=1
ans = 0
for pt in numpy.nditer(field):
    if pt>=2:
        ans +=1
print(ans)
