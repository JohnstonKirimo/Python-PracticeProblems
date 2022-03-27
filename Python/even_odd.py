"""
Given a range of integers, write a function to return
whether a given value is even or odd
"""
def my_even_odd(start, stop):

    for i in range(start, (stop+1)):
        if (i % 2) == 0:
            print(i, "even")
        else:
            print(i, "odd")
