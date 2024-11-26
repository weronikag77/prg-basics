# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total():
   sum = 0
   for i in range(0,5):
      sum += len(cinema_seats[i])
   return sum

print(seats_total())

def seats_available(seats):
   
   return ...

def seats_booked(seats):
   ...
   ...
   return ...