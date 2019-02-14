import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

smoking_data = np.loadtxt('smoking.txt', delimiter="\t")

# age – a positive integer (years)
# FEV1 – a continuous valued measurement(liter)
# height – a continuous valued measurement(inches) 
# gender – binary(female: 0, male: 1)
# smoking status – binary(non-smoker: 0, smoker: 1) 
# weight – a continuous valued measurement(kg)

smokers = []
nonsmokers = []

for person in smoking_data:
  if person[4] == 0:
    nonsmokers.append(person)
  elif person[4] == 1:
    smokers.append(person)

print(np.array(smokers))
smokers = np.array(smokers)
nonsmokers = np.array(nonsmokers)

smokers_avg_FEV1 = np.mean(smokers[:,1])
nonsmokers_avg_FEV1 = np.mean(nonsmokers[:, 1])

print("Smokers' FEV1 score: ", str(smokers_avg_FEV1))
print("Non-smokers' FEV1 score: ", str(nonsmokers_avg_FEV1))

