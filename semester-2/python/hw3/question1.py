'''
Two-line solution to Question 1
'''

#                                       Split most 2 times
#                                       ~~~~~~~~~~~
a, b, c = sorted(map(int, input().split(maxsplit=3)))
#         ~~~~~~ ~~~~~~~          ~~~~~~
#           |       |                |
#           |       |                +---> Whitespace by default
#           |       |
#           |       |
#           |       +---> int() all the elements in the iterator.
#           |
#           +---> Return the ascending sorted list without touch the original
#                 array.

print("fit" if a + b > c else "unfit")
#              ---------
#              Triangle determination
