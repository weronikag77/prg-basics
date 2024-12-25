#Add to the set of numbers, the next number read from the keyboard 
#(store the numbers in the array)

class Statistics():
    def __init__(self):
        self.numbers = []
        self.min = 0
        self.max = 0
        self.mean = 0
        self.med = 0

    def add_number(self):
        number = int(input("Enter a number: "))
        self.numbers.append(number)

    
#Display all numbers separated by a space

    def display_numbers(self):
        print(*self.numbers, sep=" ")

#Determine the greatest number

    def max_number(self):
        self.max = max(self.numbers)

#Determine the smallest number

    def min_number(self):
        self.min = min(self.numbers)

#Calculate the arithmetic mean of numbers
    def arithmetic_mean(self):
        sum1 = sum(self.numbers)
        self.mean = sum1/len(self.numbers)

#Calculate of the median
    def median(self):
        self.numbers.sort()
        if len(self.numbers) % 2 == 1:
            self.med = self.numbers[len(self.numbers)//2]
        else:
            self.med = (self.numbers[len(self.numbers)//2] + self.numbers[len(self.numbers)//2 - 1])/2

#Print of calculated / determined statistical quantities 
    def display_stats(self):
        print(f"Biggest number: {self.max}")
        print(f"Smallest number: {self.min}")
        print(f"Arithmetic mean: {self.mean}")
        print(f"Median: {self.med}")
#(minimum, maximum, arithmetic mean, median)

def main():
    numbers = Statistics()
    numbers.add_number()
    numbers.add_number()
    numbers.add_number()
    numbers.add_number()
    numbers.add_number()
    numbers.max_number()
    numbers.min_number()
    numbers.arithmetic_mean()
    numbers.median()
    numbers.display_stats()

if __name__ =="__main__":
   main()