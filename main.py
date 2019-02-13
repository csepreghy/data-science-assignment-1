import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

smoking_data = np.loadtxt('smoking.txt', delimiter="\t")
print(smoking_data)
