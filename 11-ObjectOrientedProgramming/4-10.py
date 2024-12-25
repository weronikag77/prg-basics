# Define a C class that allows you to create an object. 
# Provide the list of coordinates of points at the time of creating the object. 
# In the class C, define a method m(n) that returns true when at least n points are in 
# the first quadrant of the coordinate system (both point coordinates are greater than 0), 
# or false otherwise. Sample result:

#C([[2,3],[1,8],[-6,4],[3,-7]])
#m(2) returns True
#m(3) returns False

class C():
    def __init__(self, array):
        self.count = 0
        self.list = array
    def m(self, n):
        for i in range(len(self.list)):
            if self.list[i][0] > 0 and self.list[i][1] > 0:
                self.count += 1
        if self.count >= n:
            print(True)
        else:
            print(False)
        
def main():
    set1 = C([[2,3],[1,8],[-6,4],[3,-7]])
    set1.m(3)

if __name__ =="__main__":
   main()
