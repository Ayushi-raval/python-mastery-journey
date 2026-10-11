"""
Python Introduction
Topics: Python overview, installation, syntax, comments, and variables
"""

# ------------------------------
# 1. Python Overview
# ------------------------------

# Python is a high-level, interpreted, and dynamically typed language.
# It is used for web development, data analysis, AI/ML, automation, and more.

print("Welcome to Python Basics!")
print("Python is simple, powerful, and beginner-friendly.")


# ------------------------------
# 2. Installation and Getting Started
# ------------------------------

# To install Python:
# 1. Visit https://www.python.org/
# 2. Download and install Python for your operating system.
# 3. Check the installed version using:
#    python --version
#
# To install a package:
#    pip install package-name
# Example:
#    pip install pandas

print("\nGetting Started:")
print("Hello World !!!")


# ------------------------------
# 3. What is Syntax?
# ------------------------------

# Syntax means the rules for writing valid Python code.
# Python uses indentation to define code blocks.

print("\nPython Syntax Example:")

for i in range(3):
    print("Number:", i)


# ------------------------------
# 4. Comments
# ------------------------------

# This is a single-line comment.
# Python ignores comments while running the program.

print("\nComments Example:")
print("This line will run.")  # Inline comment

# print("This line will NOT run because it is commented.")

"""
This is a multi-line comment.
It can explain a larger block of code.
"""


# ------------------------------
# 5. Variables
# ------------------------------

# Variables store information that can be used later in the program.

print("\nVariables Example:")

name = "Aayushi"          # String
age = 20                  # Integer
is_learning_python = True # Boolean

print("Name:", name)
print("Age:", age)
print("Learning Python:", is_learning_python)

# Variable naming rules:
# - Start with a letter or underscore
# - Use letters, numbers, and underscores
# - Do not start with a number
# - Variable names are case-sensitive

student_name = "Aayushi"  # Snake case, recommended in Python
StudentName = "Aayushi"   # Pascal case
studentName = "Aayushi"   # Camel case

print("\nVariable naming styles:")
print(student_name)
print(StudentName)
print(studentName)
