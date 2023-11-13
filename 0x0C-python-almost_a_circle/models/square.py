#!/usr/bin/python3
"""
Documentation goes here, Square is the child of Rectangle
"""
from .rectangle import Rectangle
class Square(Rectangle):
    """
        Square Class inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size,size,x,y,id)
        
    def size(self, value=None):
        if value == None:
            return self.width
        else:
            self.width = value
            self.height = value
    
    size = property(size,size)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
