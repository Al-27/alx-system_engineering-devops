#!/usr/bin/python3
"""
Documentation goes here, Rectangle is the child of Base
"""
import base
class Rectangle(base.Base):
    """
        Rectancle Class Inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
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
        eq = ">"
        
        if var in "xy":
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
        return self.__width * self.__height
    
    def display(self):
        for i in range(0, self.__y):
            print()
        for i in range(0,self.__height):
            print(" "*self.__x + "#"*self.__width)
    
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{ self.__height}"
    
    def update(self, *args, **kwargs):
        if args:
            funcs = [None, "_Rectangle__width", "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
            i = 0
            for arg in args:
                if i == 0 : 
                    self.id = arg
                else:
                    self.__dict__[funcs[i]] = arg
                i += 1
        else:
            dicBas = "_Rectangle__"
            for key,val in kwargs.items():
                self.__dict__[f"{dicBas}{key}"] = val