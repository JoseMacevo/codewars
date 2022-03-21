"""
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can
be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

En todo triángulo la suma de las longitudes de dos lados cualesquiera es siempre mayor a la longitud del lado restante.
"""


def is_triangle(a, b, c):  # Inequality triangles..
    """Determine if three sides of given lengths can form a valid triangle.
    Args:
       a (int): First side length
       b (int): Second side length
       c (int): Third side length

    Return:
         bool: True if the three sides given can form a valid triangle.
     """

    if a > 0 and b > 0 and c > 0:

        if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
            return True

        elif a == b == c:
            return True

        else:
            return False
    else:
        return False
