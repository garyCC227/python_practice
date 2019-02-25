import math


class Line(object):
    def __init__(self,coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return math.sqrt( (y2-y1)**2 + (x2-x1)**2)

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        result = ((y2-y1)/(x2-x1))
        print(type(result))
        return result



coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print (li.distance())
print (li.slope())

print ("Employee.__doc__:", Line.__doc__)
print ("Employee.__name__:", Line.__name__)
print ("Employee.__module__:", Line.__module__)
print ("Employee.__bases__:", Line.__bases__)
print ("Employee.__dict__:", Line.__dict__)

'''
#Problem 2
class Cylinder(object):
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius**2 *self.height

    def surface_area(self):
        return ((2*3.14*(self.radius)**2) + self.height * (2* 3.14 * self.radius))


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
'''
