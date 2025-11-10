#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(x,y,z):
    semiperimeter = (x+y+z)/2
    return semiperimeter
x = semiPerimeter(2,4,1)
print(x)
#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(w,x,y,z):
    w = w*((w-x)*(w-y)*(w-z))
    return w
x = multiplyDifferences(5, 2, 4, 1)
print(x)
#multiplyDifferences(140,12,34,34)
#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    area = math.sqrt(multiplyDifferences(s,a,b,c))
    return area
x = herons(3,4,5)
print(x)
#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(n):
    number = n*2
    return number
x = denominator(5)
print(x)

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a,b):
    first = a*(-1)
    add = (first - b)
    sub = (first + b)
    return add , sub
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(c,d,e):
    together = (c*e)*4
    sub =  (d*d)-together
    return sub

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    quad = (plusMinus(b/denominator(a),math.sqrt(mainCalc(a,b,c))/denominator(a)))
    return quad
