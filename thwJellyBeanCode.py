#!/home/Install/anaconda/bin/python

import sys

## This class estimates the number of jelly beans in the world using input data
#  determined to be correlated to this result.
# The number of jelly beans in the world is correlated to the fraction
# of land used for sugar, the world population, and the fraction of 
# people who like the color pink.
class NumJellyEstimator:

    ## Instantiating the class initializes some variables.
    def __init__(self):

        ## Fraction of land used for growing sugar
        self.fracLand4Sugar = 0.0
        ## World population
        self.worldPop = 0
        ## Scaling constant used in estimate
        self.scalingConst = 1e-1
        ## Fraction of people who love the color pink.
        self.fracPplLovingPink = 0.0


    ## Set the fraction of land used for sugar.
    def set_land_frac_for_sugar(self, frac):

        # Make sure we've got a float.
        assert type(frac) is float, \
            "Error: fraction of land set must be a float."

        # Check that the value is between zero and one.
        if ((frac <= 0.0) or (frac >= 1.0)):
            print "\nError: Fraction of land used for sugar must be between"\
                  +" 0.0 and 1.0.\n"
            sys.exit()

        # Store the fraction.
        self.fracLand4Sugar = frac


    ## Set the world population
    def set_world_pop(self, people):

        # THW: Add a test for type here
 
        # THW: Add a test for value here

        # Store the fraction.
        self.worldPop = people


    ## Set the fraction of people who love the color pink.
    def set_frac_ppl_loving_pink(self, frac):

        # THW: Add a test for type here

        # THW: Add a test for value here

        # Store the fraction.
        self.fracPplLovingPink = frac


    ## Return the scaling constant so the user can check it if they want.
    def get_scaling_const(self):

        return self.scalingConst


    ## Estimate the number of jelly beans in the world.
    # This is based on a previous understanding of the estimate that did not
    # take the color pink into account. Still supported for legacy reasons.
    def compute_Njelly_est(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar and world population"\
                  +"must be set before computing estimate.\n"
        return int(n)


    ## Estimate the number of jelly beans in the world using the new pink data.
    def compute_Njelly_pink_est(self):

        n = self.fracLand4Sugar * self.worldPop * self.scalingConst / \
            (1.0 - self.fracPplLovingPink)
        # If this value is zero, it means that some value didn't get set.
        if (n == 0.0):
            print "\nError: fraction of land for sugar, world population, and"\
                  +"fraction of people loving pink must be set before "\
                  +"computing estimate.\n"

        # THW: What other checks might be useful? What is a better way to do this?

        return int(n)


