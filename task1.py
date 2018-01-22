import math

class Point:
    """Represents a point in 2-D space."""



blank = Point()

#blank.x = 3
#blank.y = 4

def distance_between_two_points(x,y):
    distance = math.sqrt(x**2+y**2)
    print(distance)

distance_between_two_points(3,4)