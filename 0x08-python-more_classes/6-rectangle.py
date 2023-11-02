#!/usr/bin/python3
class Rectangle:
    
    number_of_instances = 0
    
    def __init__(self, w=0, h=0):
        self.__width = w
        self.__height = h
        self.number_of_instances += 1
        
    def __del__(self):
        print("Bye rectangle...")
        self.number_of_instances -= 1
    
    def width(self, value=None):
        if value == None:
            return self.__width
         
        if isinstance(value,int) :
            self.__width = value
        elif value < 0 :
            raise ValueError("width must >= 0")
        else:
            raise TypeError("width must be an integer")
            
    def height(self, value=None):
        if value == None:
            return self.__height
        
        if isinstance(value,int) :
            self.__height = value
        elif value < 0 :
            raise ValueError("height must >= 0")
        else:
            raise TypeError("height must be an integer")
                 
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
    
    def __str__(self):
        w, h = self.__width ,self.__height
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ret
        else:
            for i in range(h):
                    ret += '#'*w + ( "\n" if i+1 < h else "")
        return ret
    
    def __repr__(self):
        w, h = self.__width ,self.__height
        return "Rectangle({}, {})".format(w, h)