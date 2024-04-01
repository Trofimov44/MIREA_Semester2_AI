import math
class biba:

    def __init__(self, x):
        self.x = x

    def cos(self):
        return math.cos(self.x)
    def sin(self):
        return math.sin(self.x)
    def tan(self):
        return math.tan(self.x)
    def asin(self):
        return math.asin(self.x)
    def acos(self):
        return math.acos(self.x)
    def radians(self):
        return math.radians(self.x)
    


rdf = biba(23)
print(rdf.cos())
print(rdf.radians())
