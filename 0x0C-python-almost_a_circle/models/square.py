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
    
    def update(self, *args, **kwargs):
        """
            ...
        """
        if args: 
            i = 0
            for arg in args:
                if i == 0 : 
                    self.id = arg
                elif i == 1 :
                    self.size = arg     
                elif i == 2 :
                    self.x = arg
                else:
                    self.y = arg
                i += 1
        elif kwargs:
            dicBas = "_Rectangle__"
            for key,val in kwargs.items():
                if str(key) == "id" : 
                    self.id = val
                elif str(key) == "size" :
                    self.size = val
                elif str(key) == "x" :
                    self.x = val
                elif str(key) == "y":
                    self.y = val
    
    def to_dictionary(self):
        """
            ...
        """
        dict_ = {"id": self.id, "size": self.size, "x": self.x, "y":self.y}
        return dict_
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"