#!/home/Install/anaconda/bin/python

#import EstNumJellyBeans as jelly
import thwJellyBeanCode as jelly

# Get a jelly bean estimator
estimator = jelly.NumJellyEstimator()

# Set the fraction of land being used for sugar, the world population,
# and the fraction of the population that loves pink.
land_frac = 0.1
ppl = 7e9
pink_frac = 0.18
estimator.set_land_frac_for_sugar(land_frac)
estimator.set_world_pop(ppl)
estimator.set_frac_ppl_loving_pink(pink_frac)

# Get the estimate of the number of jelly beans in the world,
# and report the result given the input.
est = estimator.compute_Njelly_est()

print "\nIt is estimated that when\n", land_frac*100, "percent\nof the land is"+\
      " used for sugar and\n", pink_frac*100, "percent of", int(ppl), \
      "people\nLOVE pink, then there are\n", est, "\nJelly Beans in the world."
