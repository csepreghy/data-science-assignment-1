import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

with open('smoking.txt', 'rb') as f:
  print(f.readlines())