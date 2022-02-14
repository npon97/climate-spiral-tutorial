import matplotlib.pyplot as plt
import pandas as pd

PATH_HADCRUT_MNTHLY_AVG = "/home/phippsy/Projects/ClimateAmbassador/\
visualizations/data/HadCRUT.4.6.0.0.monthly_ns_avg.tsv"

hadcrut = pd.read_csv(
    PATH_HADCRUT_MNTHLY_AVG,
    delim_whitespace=True,
    usecols=[0,1],
    header=None)

