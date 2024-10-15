###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = False # does the employee receive a bonus
bonus = 0.3 # 15%

if is_bonus == False:
    total_salary = basic_salary
else:
    total_salary = basic_salary + basic_salary*bonus

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')