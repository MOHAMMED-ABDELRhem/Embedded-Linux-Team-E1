#import the pi constant from the math module
from math import pi
# ask user to enter the radius 
r = float(input ("Input the radius of the circle : "))
#calculate the area of the circle (pi*r**2) Then concatenate the string and the value of the radius and area using the + operator and print the final string.
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))