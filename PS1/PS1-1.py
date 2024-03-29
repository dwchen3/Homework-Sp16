# CS196 homework problem set 1, file 1/3
#
# Most of these problems can be solved in a single line of code.
# Make sure to do *exactly* what the specifications tell you to!
# Also don't assume too much (if we said x is a number, don't assume
# you're only dealing with integers!)
#
# If the specification tells you to *print* a value, do it using:
#     print 'This is the output!'
# If the specification tells you to *return* a value, you should use:
#     return 'This is the output!'
# Do not confuse the two, or you will not receive credit for that problem!
#
# If you see the keyword "pass" anywhere, it's just a placeholder
# for your code. Failure to replace it with actual working code will
# earn you a not-"pass"ing grade!


# Hello, world!
#
# Input: None.
#
# Output:
#   Print exactly "Hello, world!" to the console. Do not return anything.
def hello_world():
    pass


# Identity
# 
# Input:
#   x - something (or more specifically, anything)
#
# Output:
#   Return x (the input). Do not print anything. In fact, we pretty much
#   just gave you the answer.
def identity(x):
    pass


# Increment
#
# Input:
#   x - an integer
#
# Output:
#   Return the value of x+1. Do not print anything.
def increment(x):
    pass


# It's opposite day... or is it?
#
# Input: 
#   b - a boolean
#
# Output:
#   Return True if b is False; return False if b is True. Do not print anything.
def opposite(b):
    pass


# I have the power!
#
# Input:
#   x - the base (a number)
#   y - the exponent (an integer)
#
# Output:
#   Return x raised to the power of y. Do not print anything.
def power(x, y):
    pass


# Can you repeat that?
# 
# Input:
#   x - a string
# 
# Output:
#   Print the value of x twice, *on a single line*! Do not return anything.
#   For example, if x is "hi", your code should print "hihi".
def repeat_that(x):
    pass


# Can you repeat that, again?
#
# Input:
#   x - a string
#
# Output:
#   Call the function you just defined, repeat_that, twice. The value of 
#   x should be printed 4 times, 2 times on each line.
def repeat_that_again(x):
    pass


# Order of operations
# This code is broken. Fix it so that it returns 15. *You may not delete
# any characters*!
#
# Input: None.
# 
# Output:
#   Return the integer 15. Do not print anything.
def give_me_15():
    return 2 + 3 * 3


# Is it even?
# Check whether the input value is an even integer.
# 
# Input: 
#   x - the number to check (an integer)
# 
# Output:
#   Return True if x is even, and False if x is odd. Do not print anything.
def is_it_even(x):
    pass


# Y U NO DECIMAL?!
# Something is horribly wrong. The code below should return 4.5, but
# for some reason it's off by 0.5! Fix the code, but *do not delete 
# any characters*.
#
# Input: None.
#
# Output:
#   Return 4.5. Do not print anything.
def y_u_no_decimal():
    return 9 / 2


# WHY WON'T IT COMPILE?!
# 
# Input: None.
#
# Output:
#   Return exactly the following string: I'm taking a class called "CS196"!
#   Do not print anything.
def quote_me():
    pass


# I can haz credits?
# 
# Input:
#   registered - whether you are registered for the course (a boolean)
#   score - an integer in the range [0, 100], zero if registered is False
#   override - whether you have a credit override (a boolean)
#
# Output:
#   Return True if you are registered for the class and have a score
#   of at least 60. Also return True if you have a credit override.
#   In all other cases, return False. Do not print anything.
def has_course_credit(registered, score, override):
    pass


# Pythagorean theorem
# Calculate the length of the hypotenuse of a right triangle
# given the lengths of the legs, a and b.
# 
# Input:
#   a - the length of the first leg (a float greater than 0)
#   b - the length of the second leg (a float greater than 0)
#
# Output:
#   Return the numeric value of the hypotenuse. Do not print anything.
def pythagorean(a, b):
    pass


# Fahrenheit to Celsius
# Wow, there's a lot of broken code today! Fix this function so that it
# correctly converts from Fahrenheit to Celsius. Hint: there are TWO
# bugs in the calculation.
#
# Input:
#   f - the temperature in Fahrenheit (a float)
#
# Output:
#   Return the temperature in Celsius. Do not print anything.
def fahrenheit_to_celsius(f):
    return 5 / 9 * f - 32


# Close enough
# This function is too strict! I'm telling you, 99% is good enough!
#
# Input:
#   a - a float
#   b - a float
#
# Output:
#   Return True if the difference between a and b is less than
#   or equal to 0.01, and False otherwise. Do not print anything.
#   Note that a may be larger than, smaller than, or equal to b.
#
# Hint:
#   The absolute value of a number x can be computed using abs(x)
def close_enough(a, b):
    return a == b


# Below are some test cases that we have written up for you!
# Feel free to add more to test your code! Though be warned, 
# our grading program will test more cases than this... so make
# sure your functions are correct!

# If you want to learn about this __name__ == "__main__",
# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    print "Running hello_world():"
    hello_world()
    print "Running repeat_that(\"double\"):"
    repeat_that("double")
    print "Running repeat_that_again(\"me\"):"
    repeat_that_again("me")

    print "identity(3) == " + repr(identity(3))
    print "identity('bob') == " + repr(identity('bob'))
    print "increment(195) == " + repr(increment(195))
    print "opposite(True) == " + repr(opposite(True))
    print "power(2.0, 10) == " + repr(power(2.0, 10))
    print "is_it_even(4) == " + repr(is_it_even(4))
    print "has_course_credit(True, 89, False) == " + repr(has_course_credit(True, 89, False))
    print "has_course_credit(False, 0, True) == " + repr(has_course_credit(False, 0, True))
    print "has_course_credit(False, 0, False) == " + repr(has_course_credit(False, 0, False))
    print "pythagorean(3.0, 4.0) == " + repr(pythagorean(3., 4.))
    print "fahrenheit_to_celsius(212.0) == " + repr(fahrenheit_to_celsius(212.))
    print "fahrenheit_to_celsius(-40.0) == " + repr(fahrenheit_to_celsius(-40.))
    print "close_enough(5.0, 5.00001) == " + repr(close_enough(5.0, 5.0001))
    print "close_enough(98.0, 100.0) == " + repr(close_enough(98., 100.))
