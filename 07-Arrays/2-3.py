#total expenses for each category
#total expenses for each week
#total expenses for a month

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
sum_1 = 0
for i in range(0,4):
    sum_1 += monthly_expenses[i][0]

sum_2 = 0
for i in range(0,4):
    sum_2 += monthly_expenses[i][1]

sum_3 = 0
for i in range(0,4):
    sum_3 += monthly_expenses[i][2]

sum_week1 = 0
for i in range(0,3):
    sum_week1 += monthly_expenses[0][i]

sum_week2 = 0
for i in range(0,3):
    sum_week2 += monthly_expenses[1][i]

sum_week3 = 0
for i in range(0,3):
    sum_week3 += monthly_expenses[2][i]

sum_week4 = 0
for i in range(0,3):
    sum_week4 += monthly_expenses[3][i]

total_sum = sum_week1 + sum_week2 + sum_week3 + sum_week4

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum_1)
print('Transport:',sum_2)
print('Utilities:',sum_3)
print('Week 1:', sum_week1)
print('Week 2:',sum_week2)
print('Week 3:',sum_week3)
print('Week 4:',sum_week4)
print('---------------')
print('TOTAL:',total_sum)