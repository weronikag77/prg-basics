
# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, "r") as file:
   for line in file:
      if job_title in line:
        print(line, end="")