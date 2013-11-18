#!/Vendors/anaconda/bin/python

import sys
import EstNumJellyBeans as jelly

## This tests that the number of jelly beans is estimated correctly.
failed = []
passed = []

# Get a jelly bean estimator
estimator = jelly.NumJellyEstimator()

# Set the fraction of land for sugar and the world population.
frac = 0.1
ppl = 7e9
estimator.set_land_frac_for_sugar(frac)
estimator.set_world_pop(ppl)
# get the scaling constant for our information
val = estimator.get_scaling_const()

## ----- Test the basic funtion ----- ##
# We know that these number will return 0.1*7e9*scalingConst jelly beans
ref = int(frac*ppl*val)

# Get the estimate and check that it is the same as our reference.
test = 'basic_jelly_estimate'
est = estimator.compute_Njelly_est()
if (est == ref):
    passed.append(test)
else:
    failed.append(test)


# Print the results of our tests.
print "\n-----------------------------------------------------"
print " Passed", len(passed), "of", len(passed) + len(failed), "number of "\
      +"jelly beans estimator tests"
print "-----------------------------------------------------\n"
