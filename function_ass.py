"""
25-05-2023 assignment
Write a python program for student registration portal that will ask user to register and give matric
 number to the student.
NOTE:
- Your code should be able to generate matric number for the student.
- if admin did not enter "end", admin should be able to keep registering students;
- at the end of the registration process, your code should be able to fetch the student details and matric number
- your code should be able to print all matric numbers of students registered.
"""


    # SOLUTION by JUNAID, S. O."

import random

student_info = []

def registration():
    name = input("Enter your First name ")
    names = input("Enter your Last name ")
    age = input("Enter your age ")
    gender = input("Enter your gender ")
    discipline = input("Enter your discipline ")
    level = input("Enter your level ")
    state = input("Enter your state ")
    tribe = input("Enter your tribe ")
    nationality = input("Enter your nationality ")
    degree = input("Enter your degree ")
    matric_num = random.randint(230100, 230500)
    student_info.append([name, names, age, matric_num])
    quit = input("Enter 'end' to quit or any other key to continue ").lower()
    while quit != "end": # as long as the user did not enter "end" the program will continue to register users...
        registration()
        break
    else:
        print(student_info)

registration()