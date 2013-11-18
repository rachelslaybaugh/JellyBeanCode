#!/Vendors/anaconda/bin/python

import sys

## This class estimates the number of jelly beans in the world using input data
#  determined to be correlated to this result.
class NumJellyEstimator:

    ## Instantiating the class initializes some variables.
    def __init__(self):

        # The number of jelly beans in the world is correlated to the fraction
        # of land used for sugar and the world population.
        ## Fraction of land used for growing sugar
        self.fracLand4Sugar = 0.0
        ## World population
        self.worldPop = 0
        ## Scaling constant used in estimate
        self.scalingConst = 1e-1


    ## Set the fraction of land used for sugar.
    def set_land_frac_for_sugar(self, frac):

        # Make sure we've got a float.
        frac = float(frac) 

        # Check that the value is between zero and one.
        if ((frac <= 0.0) or (frac >= 1.0)):
            print "\nError: Fraction of land used for sugar must be between"\
                  +" 0 and 1.\n"
            sys.exit()

        # Store the fraction.
        self.fracLand4Sugar = frac


    ## Set the world population
    def set_world_pop(self, people):

        # Make sure we've got an int.
        people = int(people)

        # Check that the value is between zero and 1e20.
        if ((people <= 0) or (people >= 1e20)):
            print "\nError: World population must be between 0 and 1e20.\n"
            sys.exit()

        # Store the fraction.
        self.worldPop = people


    ## Return the scaling constant so the user can check it if they want.
    def get_scaling_const(self):

        return self.scalingConst


    ## Estimate the number of jelly beans in the world.
    def compute_Njelly_est(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar and world population"\
                  +"must be set before computing estimate.\n"
        return int(n)


