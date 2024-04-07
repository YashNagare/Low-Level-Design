# Interface Segmented / Segregation Principle 
# Interfaces should be such that client should not implement unnecessary functions they do not need


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


"""
This interface draws squares, circles, rectangles. class Circle, Square or Rectangle implementing the IShape 
interface must define the methods draw_square(), draw_rectangle(), draw_circle().
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_circle(self):
        pass

    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_circle(self):
        pass

    def draw_circle(self):
        pass

class Rectanle(IShape):
    def draw_square(self):
        pass

    def draw_circle(self):
        pass

    def draw_circle(self):
        pass

"""
It's quite funny looking at the code above. class Rectangle implements methods (draw_circle and draw_square) it has no use of, 
likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, draw_rectangle).
If we add another method to the IShape interface, like draw_triangle(),
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError

"""
To make our IShape interface conform to the ISP principle, we segregate the actions to different interfaces.
Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the IShape interface and implement their own draw behavior.
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

# We can then use the I -interfaces to create Shape specifics like Semi Circle, Right-Angled Triangle, Equilateral Triangle, Blunt-Edged Rectangle, etc.
