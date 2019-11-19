class rectangle:
    def __init__(self, width, height):
        self.__width = int(width)
        self.__height = int(height)

    def area(self):
        return self.__height * self.__width

    def getwidth(self):
        return self.__width

    def getheight(self):
        return self.__height


n = int(input("Enter the number of rectangle : "))

lst = []

for i in range(0, n):
    lst.append(rectangle((input("Width : ")), (input("Height : "))))

lst = sorted(lst, key=rectangle.area)

print(lst[0].getwidth(), lst[0].getheight(), "Least area rectangle")
print(lst[len(lst)-1].getwidth(), lst[len(let)-1].getheight(), "Most area rectangle")
