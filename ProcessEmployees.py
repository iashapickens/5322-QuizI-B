'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import pandas as pd

# Load the employee data
file_path = 'employee_data.csv'
employee_data = pd.read_csv(file_path)

# Define the percentage increase in salary (for example, a 10% increase)
salary_increase_percentage = 0.10

# Initialize a variable to store the total increase in salary
total_increase = 0

# Create an empty dictionary to store the new salaries
new_salaries = {}

# Loop through each employee to calculate and display the salary details
for index, row in employee_data.iterrows():
    first_name = row['First Name']
    last_name = row['Last Name']
    full_name = f"{first_name} {last_name}"
    department = row['Department']
    title = row['Title']
    clearance = row['Clearance']
    current_salary = row['Salary']
    
    # Check if the employee fits the search criteria
    if department == 'Marketing' and title == 'CSR' and clearance == 'TS':
        # Calculate the new salary
        new_salary = current_salary * (1 + salary_increase_percentage)
        
        # Calculate the increase in salary
        increase_amount = new_salary - current_salary
        total_increase += increase_amount
        
        # Store the new salary in the dictionary
        new_salaries[full_name] = new_salary
        
        # Print current salary
        print(f"Employee Name: {full_name} Current Salary: ${current_salary:,.2f}")

print()
print('=========================================')
print()

# Iterate through the dictionary and print out the key and value
for name, new_salary in new_salaries.items():
    print(f"Employee Name: {name} New Salary: ${new_salary:,.2f}")

print()
print('=========================================')
print()

# Print out the total difference between the old salary and the new salary
print(f"Total increase in salary: ${total_increase:,.2f}")


