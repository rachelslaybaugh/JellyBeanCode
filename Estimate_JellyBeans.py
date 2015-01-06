# This script estimates the number of jelly beans in the world using input data determined to be correlated to this result.

#The number of jelly beans in the world is correlated to the fraction of land used for sugar, the world population, and the fraction of people who like the color pink.


# Set the fraction of land being used for sugar, the world population,
# and the fraction of the population that loves pink.
''' TO DO:
(1) Write assertions to check that these values are reasonable
(2) Make sure these values are the correct type
'''

fracLand4Sugar = 0.1        # Fraction of land used for growing sugar
worldPop = 7e9              # World population
scalingConst = 1e-1         # Scaling constant used in estimate
fracPplLovingPink = 0.18    # Fraction of people who love the color pink.



# Get the estimate of the number of jelly beans in the world,
# and report the result given the input.
''' TO DO:
(3) Write this equation into a function
(4) Write an assertion to check that all of the needed values have been defined
'''

est = fracLand4Sugar * worldPop * scalingConst / (1.0 - fracPplLovingPink)

print "\nIt is estimated that when\n", fracLand4Sugar*100, "percent\nof the land is used for sugar and\n", fracPplLovingPink*100, "percent of", worldPop, "people\nLOVE pink, then there are\n", est, "\nJelly Beans in the world."



''' TO DO:
(5) Write a script that creates a three plot figure:
    (Subplot 1) Number of jelly beans against population size
    (Subplot 2) Number of jelly beans against fraction of land used for sugar
    (Subplot 3) Number of jelly beans against fraction of pink lovers

Hint: Create a one-dimensional numpy array of equally spaced values with:
array_name = numpy.arange(start_value, end_value, step_size)
'''
