# Try the first function named 'print'
print("hello, world")
print('hello')
#it works with double and single quote

# Ask user for their name
name = input("What is your name? ") #the space give a blank space after the question

# remove whitespace from a string
name = name.strip()

# and say hello to the name
print ("hello,", name)

"""
The pair of triple quotes is used to wrap many-line comment.
Or just put # at the beginnning of every line of comment.
"""
# Use 2 print functions, but over-write the default end="\n" into end="" to combine the output into 1 line
# Should learn to read Documentation of Python on website docs.python.org
# It shows print(*objects, sep=' ', end='\n', ...)
print("Hello, ", end='')
print(name)

# To demonstrate further that we have more control on the code, we can put any to end
print("hello, ", end='??!!')
print(name)

# We can over-write the default sep, too
print("hello,", name, sep='@**@')

#continue at Week 0 and timing 49:50
