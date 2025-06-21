# Finish the function below that takes a radius r as input 
# and make it return the circle area.

from math import pi

def circle_area(r):
    area = pi * r**2
    return area

print(circle_area(5))

# Write a function that takes a list radii as input 
# and returns a list of the corresponding circle areas.

def area_of_circlce(data):
    area = [circle_area(r) for r in data]
    return area

radius = [5, 6, 7, 8, 9, 10]

print(area_of_circlce(radius))

# Write a function described in the docstring below:
# Return a list with elements `True` for all piles longer than 
# or equal to 5m, `False` otherwise.

def is_pile_long(pile_lengths):
    true_lists = [True if i >= 5 else False for i in pile_lengths]
    return true_lists

piles = [4.51, 6.12, 4.15, 7.31, 5.01, 4.99, 5.00]

print(is_pile_long(piles))

# Finish the function below so it does as described in the docstring.
# '''Return distance between a point and a line defined by two points.
    
    # Args:
    #     x  : x-coordinate of point 
    #     y  : y-coordinate of point
    #     x1 : x-coordinate of point 1 defining the line
    #     y1 : y-coordinate of point 1 defining the line
    #     x2 : x-coordinate of point 2 defining the line
    #     y2 : y-coordinate of point 2 defining the line
        
    # Returns:
    #        The distance between the point and the line   
    # 
    # abs is used to get the numerical value 

from math import sqrt

def dist_point_to_line(x, y, x1, y1, x2, y2):

    return abs((x2-x1)*(y1-y)-(x1-x)*(y2-y1))/sqrt((x2-x1)**2 + (y2-y1)**2)

print(dist_point_to_line(2, 1, 5, 5, 1, 6))

# Given a line defined by two points and 
# , compute the distance to the points with 
# coordinates x_coords and y_coords below.

# Put the results into a list.

# # x- and y-coordinates of points
# You can either use a list comprehension or create a 
# traditional for-loop where results get appended 
# to the list in every loop.

x1,y1,x2,y2 = 2, 3, 8, 7
x_coords = [4.1, 22.2, 7.7, 62.2, 7.8, 1.1]
y_coords = [0.3, 51.2, 3.5, 12.6, 2.7, 9.8]

distance = [dist_point_to_line(x_coords[i],y_coords[i], x1, y1, x2, y2) for i in range(len(x_coords))]

print([round(dist,2) for dist in distance])

# Create a function that calculates the area of a simple 
# (non-self-intersecting) 
# polygon by using the so-called Shoelace Formula

def area_of_polygon(xv, yv, signed=False):

    a1 = [xv[i] * yv[i+1] for i in range(len(xv)-1)]
    a2 = [yv[i] * xv[i+1] for i in range(len(yv)-1)]

    if signed:
        return 1/2 * (sum(a1) - sum(a2))
    else:
        return 1/2 * abs(sum(a1) - sum(a2))
    
# Define the polygon vertices to test
xv = [3, 4, 7, 8, 8.5, 3]
yv = [5, 3, 0, 1, 3, 5]

result = area_of_polygon(xv,yv)

print(result)