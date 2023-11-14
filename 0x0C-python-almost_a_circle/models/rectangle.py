#!/usr/bin/python3
"""
Documentation goes here, Rectangle is the child of Base 
"""
from .base import Base

class Rectangle(Base):
    """
        Rectancle Class Inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = self.width = width
        self.__height = self.height = height
        self.__x = x
        self.__y = y
        
    
    def width(self, value=None):
        if value == None:
            return self.__width
         
        if isinstance(value,int) :
            if value <= 0 :
                raise ValueError(Rectangle.errMsg("width",1))
            self.__width = value
        else:
            raise TypeError(Rectangle.errMsg("width"))
           
          
    def height(self, value=None):
        if value == None:
            return self.__height
        
        if isinstance(value,int) :
            if value <= 0 :
                raise ValueError(Rectangle.errMsg("height",1))
            self.__height = value
        else:
            raise TypeError(Rectangle.errMsg("height"))
        
        
    def x(self, value=None):
        if value == None:
            return self.__x
         
        if isinstance(value,int) :
            if value < 0 :
                raise ValueError(Rectangle.errMsg("x",1))
            self.__x = value
        else:
            raise TypeError(Rectangle.errMsg("x"))
     
            
    def y(self, value=None):
        if value == None:
            return self.__y
        
        if isinstance(value,int) :
            if value < 0 :
                raise ValueError(Rectangle.errMsg("y",1))
            self.__y = value
        else:
            raise TypeError(Rectangle.errMsg("y"))
     
    
    def errMsg(var, type=0):
        """
            ERRMSG
        """
        eq = ">"
        
        if "x" == var or "y" == var:
            eq = ">="
        
        if type :
            type = f"{var} must be {eq} 0" 
        else :
            type = f"{var} must be an integer" 
                
        return type
    
    width=property(width,width)
    height=property(height,height)
    x=property(x,x)
    y=property(y,y)
    
    def area(self):
        """
            ...
        """
        return self.__width * self.__height
    
    def display(self):
        """
            ...
        """
        for i in range(0, self.__y):
            print()
        for i in range(0,self.__height):
            print(" "*self.__x + "#"*self.__width)
    
    def __str__(self):
        """
            ...
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{ self.__height}"
    
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
                    self.width = arg                    
                elif i == 2 :
                    self.height = arg
                elif i == 3 :
                    self.x = arg
                else:
                    self.y = arg
                i += 1
        elif kwargs:
            dicBas = "_Rectangle__"
            for key,val in kwargs.items():
                if str(key) == "id" : 
                    self.id = val
                elif str(key) == "width" :
                    self.width = val                    
                elif str(key) == "height" :
                    self.height = val
                elif str(key) == "x" :
                    self.x = val
                elif str(key) == "y":
                    self.y = val
                    
    def to_dictionary(self):
        """
            ...
        """
        dict_ = {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y":self.y}
        return dict_