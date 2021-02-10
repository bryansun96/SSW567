# -*- coding: utf-8 -*-
"""
Created on Mon Feb 9 13:44:00 2021

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: bryansun
"""

def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    a = float(a)
    b = float(b)
    c = float(c)

    # require that the input values be >= 0

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'


    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    res = ''
    if a == b == c:
        res = 'Equilateral'
    elif (a != b) and (b != c) and (a != b):
        res = 'Scalene'
    else:
        res = 'Isosceles'

    if ((a * a) + (b * b)) == (c * c) or \
        ((a * a) + (c * c)) == (b * b) or \
        ((c * c) + (b * b)) == (a * a):
        res += ' and Right'

    return res


def main():
    print('Please input a, b and c')
    a = float(input("The first slide is: "))
    b = float(input("The second slide is: "))
    c = float(input("The third slide is: "))
    print(f"The type of triangle is:{classifyTriangle(a,b,c)}")


if __name__ == '__main__':
    main()
