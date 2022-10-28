class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height-2):
            s += "* "
            s += "  " * (self.width-2)
            s += "* \n"
        s += w
        return s

    def getPerimeter(self):
        return (self.height * 2) + (self.width * 2)

    def getArea(self):
        return (self.height * self.width)

class Square:
    def __init__(self, height):
        self.height = height
        self.width = self.height
    
    
    def __str__(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height-2):
            s += "* "
            s += "  " * (self.width-2)
            s += "* \n"
        s += w
        return s

    def getPerimeter(self):
        return (self.height * 4)

    def getArea(self):
        return (self.height * self.width)

def main():
    print("Rectangle Calculator")
    print()
    
    while True:
        choice = input("Rectangle or Square? (r/s): ").strip()
        if choice == "r":
            height = int(input("Height:         "))
            width = int(input("Width:          "))
            rectangle = Rectangle(height,width)
            print("Perimeter:    " , rectangle.getPerimeter())
            print("Area:         " , rectangle.getArea())
            print(rectangle.__str__)
        if choice == "s":
            length = int(input("Length:        "))
            square = Square(length)
            print("Perimeter:    " , square.getPerimeter())
            print("Area:         " , square.getArea())
            print(square.__str__)


        
        choice2 = input("Continue? (y/n): ")
        print()
        if choice2 != "y":
            print("Bye!")
            break
        
if __name__ == "__main__":
    main()
