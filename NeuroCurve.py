import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
NeuroCurveOG = pd.read_csv("TheChosenOne/alzheimers_disease_data.csv")
print(NeuroCurveOG.info())
print(NeuroCurveOG.describe())
print(NeuroCurveOG['BMI'].sum())