#POLYGON AREA CALCULATOR ASSIGNMENT 4

class Rectangle:

    def __init__(self, wd, hg):
        self.width = wd
        self.height = hg

    def set_width(self, nwd):
        self.width = nwd

    def set_height(self, nhg):
        self.height = nhg

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50: return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

class Square(Rectangle):

    def __init__(self, sid):
        super().__init__(sid, sid)

    def set_side(self, nsid):
        super().set_width(nsid)
        super().set_height(nsid)

    def __str__(self):
        return 'Square(side={})'.format(self.width)
