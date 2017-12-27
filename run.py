import numpy
import sys
from lib import HellTriangle

print("Input your triangle array below then press enter! Example: [[6],[3,5],[9,7,1],[4,6,8,4]]")
triangle = input()
triangle = numpy.array(triangle)
hell_triangle = HellTriangle(triangle)
maximum_total = hell_triangle.find_maximum_total()

print("The maximum total, from top to bottom, is: " + str(maximum_total))
sys.exit("Press any key to exit...")