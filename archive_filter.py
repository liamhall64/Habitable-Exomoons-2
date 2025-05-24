# IMPORTS
import pandas as pd
import math

from astropy import constants as c

archive = pd.read_csv('exoplanets.csv')
archive = archive.fillna(0) # Fill NaN values with 0

# Filtering by radius
def filter_by_radius(archive, min_radius, max_radius):
    """
    Filters the archive for planets with a radius between min_radius and max_radius.
    """
    rad_filt = archive[(archive['pl_rade'] >= min_radius) & (archive['pl_rade'] <= max_radius)]
    return rad_filt

rad_filt = filter_by_radius(archive, 0.5, 2.0) # 0.5 and 2 Earth radii

#Conditions to meet specific criteria
disc = rad_filt['discoverymethod'].str.contains('Transit') # CONTAINS THE WORD 'transit' IN EACH ROW
con_A = rad_filt['tran_flag'] == 1 # EXACTLY EQUAL TO 1
con_B = rad_filt['ttv_flag'] == 1
con_C = rad_filt['pl_trandep'] != 0 # NOT EQUAL TO 0
con_D = rad_filt['pl_trandur'] != 0
con_E = rad_filt['pl_tranmid'] != 0

combined = disc | con_A | con_B | con_C | con_D | con_E # THIS IS THE COMBINATION OF ALL THE CONDITIONS WITH '|' BEING THE 'or' OPERATOR

method = rad_filt[combined]

print(rad_filt)
print(method)