# 1 Write a function called calculate_area that takes base and height as an input 
# and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def triangle_area(base, height):
    area=(1/2)*base*height
    return area

s=triangle_area(6,7)
print(s)
# 2 Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". 
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def triangle_or_rectangle_area(base, height, figure):
    if figure == 'triangle':
        area=(1/2)*base*height
    elif figure == 'rectangle':
        area=base*height
    else: print("We can not find area this figure") 
    return area

s=triangle_or_rectangle_area(6,7,'rectangle')
print(s)

# 3 Write a function called print_pattern that takes integer number as an argument and prints 
# following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(num):
    str = ''
    i = 0
    while i <= num:
        str = str + '*'
        i = i+1
        print(str)
    return num   

b=print_pattern(7) 
print(b)       