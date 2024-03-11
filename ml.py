# Google ML prerequisites

# # Defining Functions

# def fib(n):   # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n: 
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# f = fib

# print(f(100))

# def fib2(n):
#     """Return a list containing the Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n: 
#         result.append(a)
#         a, b = b, a+b
#     return result 

# f100 = fib2(100)
# print(f100)

# work in progress
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('Do you really want to quit?')

