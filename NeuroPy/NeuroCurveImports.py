import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv

NeuroCurveOG = pd.read_csv("CSV/alzheimers_disease_data.csv")
usableCSV = pd.read_csv('CSV/output_CSVs/processed.csv')