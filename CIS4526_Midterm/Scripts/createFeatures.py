import pandas as pd
import numpy as np
import os




def createFeatures(csv_file):
    df = pd.read_csv(csv_file)

    
# https://scikit-learn.org/stable/modules/cross_validation.html - CROSS_VALIDATION EVALUATING ESTIMATOR PERFORMANCE