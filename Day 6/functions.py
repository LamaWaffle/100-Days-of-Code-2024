# Functions are a way to group code together. There are built in functions and you can also create your own.
# For example, print() and len() are built in functions.

print("Hello")
len("Hello")

# To create our own function, we use the def keyword.
def my_function():
    print('Hello')
    print('Bye')

my_function()   # Since functions only run when they are called, we need to CALL them.



def my_num_range():
    for num in range(10):
        print(num)

my_num_range()