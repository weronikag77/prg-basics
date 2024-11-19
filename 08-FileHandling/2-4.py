###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

with open(employees_file, "r") as file:
    with open(position_file, "w") as file2:
        for line in file:
            if job_title in line:
                file2.write(line)