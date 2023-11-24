# Sample project with a solution
# Create a simple application for the Human Resource (HR) Manager of a company to enter details of a new employee, 
# edit details of employees, and delete certain details of resigned employees using functions. 
# This project is a completely function-oriented program with separate functions created for adding new employee details, 
# displaying employee details with edit details and calculating net salary for employees. 
# The program begins with calling the employee() function, which contains nested functions for various tasks. 
# These nested functions are called as per user requirements. The global variable count tracks for number of employees added.
# Note: We can improve this project and make it more interactive by using Object oriented approach.

# Solution

count = 0  # global variable to contain count of employees
def employee():  # outer function containing nested function
    def enter_new(en, dept, desig, bs, age, status): 
    # nested function to add new employee detail
        e_name = en
        department = dept
        designation = desig
        basic_salary = bs
        eage = age
        current_status = status
        global count
        count = count + 1
        display(e_name, department, designation, basic_salary, eage, current_status)

    def display(en, dept, desig, bs, age, cs):
    # nested function to display employee detail
        global count
        print("Total employees : ", count)
        print("*************The details entered are : ******************")
        print("The name of employee: ", en)
        print("The department of employee: ", dept)
        print("The designation of employee: ", desig)
        print("The basic salary of employee: ", bs)
        print("The age of employee: ", age)
        print("The current status of employee: ", cs)
        if cs=="Resigned":
            print("This record of resigned employee will be removed!!")
        else:
            calc_salary(bs)
            answer = input("Do you want to edit details?")
            if answer=="yes":
                edit_details()
            else:
                pass

    def edit_details():  # nested function edit employee detail
        print("Enter new details for this Employee")
        name = input("Enter Name : ")
        dept = input("Enter Department : ")
        desig = input("Enter Designation : ")
        bs = int(input("Enter Basic Salary : "))
        age = int(input("Enter Age : "))
        cs = input("Enter current Employee status : ")
        display(name, dept, desig, bs, age, cs)

    def calc_salary(salary): # nested function find net salary
        if (salary > 20000):
            tax = 0.15 * salary
            net_sal = salary - tax
            print("The net salary is", net_sal)
        else:
            net_sal = salary
            print("No Tax Deductions")
            print("The net salary is", net_sal)
   # call enter_new() inside employee() function to add new employee
    enter_new("John", "Marketing", "Assistant", 10000, 20, "Present")
    enter_new("Simon", "Production", "Manager", 30000, 35, "Present")
    enter_new("Piya", "Project Management", "Developer", 50000, 25, "Present")
    enter_new("Kylie", "Marketing", "Assistant", 20000, 20, "Resigned")
# Call employee() function to begin employee management for HR
employee()
