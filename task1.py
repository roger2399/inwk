from math import *

class point:
      x = 0
      y = 0


def __init__(self,a,b):
       self.x=a
       self.y=b


def distance_between_points(obj1,obj2):
       distance_x=abs(obj1.x-obj2.x)
       distance_y=abs(obj1.y-obj2.y)
       distance = sqrt(distance_x**2+distance_y**2)
       return (distance)


object1 = point(20,40)
object2 = point(40,60)
print(distance_between_points(object1,object2))



#blank = Point()

