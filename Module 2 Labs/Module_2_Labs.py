# SSgt Daniel Hayward. All labs from Module 2 20/09/21 - 21/09/21

# 2.1.1.6 LAB: The print() function
#use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string
print("Hello, Python!") 
#having done that, use the print() function again, but this time print your first name
print("Daniel")

# 2.1.1.18 LAB: The print() function
# Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor
# Programming***Essentials***in...Python
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# 2.1.1.19 LAB: Formatting the output
# minimize the number of print() function invocations by inserting the \n sequence into the strings
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")
# make the arrow twice as large (but keep the proportions)
print("         *")
print("        * *")
print("       *   *")
print("      *     *")
print("     *       *")
print("    *         *")
print("   *           *")
print("  *             *")
print(" *****       *****")
print("     *       *")
print("     *       *")
print("     *       *")
print("     *       *")
print("     *       *")
print("     *********\n")
# duplicate the arrow, placing both arrows side by side;
# note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print("  *****  "*2)

# 2.2.1.11 LAB: Python literals - strings
# Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.
# "I'm"
# ""learning""
# """Python"""
print('"I\'m"\n\"\"learning""\n\"\"\"Python"\"\"')

# 2.4.1.7 LAB: Variables
# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.
# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
john = 3
mary = 5
adam = 6
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma
print(john, mary, adam, sep=",")
# now create a new variable named total_apples equal to addition of the three former variables
total_apples = (john+mary+adam)
# print the value stored in total_apples to the console
print(total_apples)
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them
# (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples
print ("Total number of apples:", total_apples)

# 2.4.1.9 LAB: Variables: a simple converter
# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
# miles to kilometers
# kilometers to miles
# Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code
kilometers = 12.25
miles = 7.38
miles_to_kilometers = (miles*1.61)
kilometers_to_miles = (kilometers/1.61)
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 2.4.1.10 LAB: Operators and expressions
# Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y.
# Your task is to complete the code in order to evaluate the following expression:
#3x^3 - 2x^2 + 3x - 1
#The result should be assigned to y.
# Test Data
# Sample input
# x = 0
# x = 1
# x = -1
x =  0
x = float(x)
y = (3*(x**3)-2*(x**2)+(3*x)-1)
print("y =", y)
x =  1
x = float(x)
y = (3*(x**3)-2*(x**2)+(3*x)-1)
print("y =", y)
x =  -1
x = float(x)
y = (3*(x**3)-2*(x**2)+(3*x)-1)
print("y =", y)

# 2.5.1.2 LAB: Comments
# this program computes the number of seconds in a given number of hours
# this program has been written two days ago
# The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate 
# (yes, sometimes removing a comment can make the code more readable), and change variable names where you think this will improve code comprehension.
a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour
print("Hours: ", a) #printing the number of hours
print("Seconds in 2 hours: ", a * seconds) # printing the number of seconds in a given number of hours
print ("Goodbye") #printing Goodbye
a = 3 # number of hours
print("Seconds in 3 hours:", a * seconds) #this is the end of the program that computes the number of seconds in 3 hour

# 2.6.1.9 LAB: Simple input and output
#Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
#The results have to be printed to the console.
#You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
#Test your code - does it produce the results you expect?
#We won't show you any test data - that would be too simple.
var_a = float(input("Variable A:"))# input a float value for variable a here
var_b = float(input("Variable B:"))# input a float value for variable b here

print (var_a + var_b)# output the result of addition here
print (var_a - var_b)# output the result of subtraction here
print (var_a * var_b)# output the result of multiplication here
print (var_a / var_b)# output the result of division here

print("\nThat's all, folks!")

#2.6.1.10 LAB: Operators and expressions
# Your task is to complete the code in order to evaluate the following expression:
# PICTURE OF EQUATION
# The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind.
# Don't hesitate to use as many parentheses as you need.
# You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.
x = float(input("Enter value for x: "))
y = 1/((x+1/(x+1/(x+1/x))))
print("y =", y)

#2.6.1.11 LAB: Operators and expressions
#Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large).
#The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
#For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
#Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
print ((hour+(mins + dura)//60)%24, (mins + dura) % 60, sep=":")