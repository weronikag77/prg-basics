# Define in the class a method m1(s,n) that allows you to change the number of fans n 
# in sector s or add a new sector s with the given number of fans n. 
# Define in the class a method m2(s) that returns the sum of fans in the sectors listed in the string s. 
# Sample result:

#C({"A":120,"D":150,"G":90,"K":110})
#m1("G",130)
#m2("GD") returns 280
#m2("KEJ") returns 110

class C():
    def __init__(self):
        self.dictionary = {"A":120,"D":150,"G":90,"K":110}
        
    def m1(self, s, n):
        if s not in self.dictionary:
            self.dictionary[s] = n
        else:
            self.dictionary[s] += n

    def m2(self, s):
        sum = 0
        for key in self.dictionary:
            if key in s:
                sum += self.dictionary[key]
        print(sum)

def main():
    sector_num = C()
    sector_num.m1("M", 130)
    print(sector_num.dictionary)
    sector_num.m2("KEJ")

if __name__ =="__main__":
   main()
