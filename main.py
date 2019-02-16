import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

plt.style.use('dark_background')

# age – a positive integer (years)
# FEV1 – a continuous valued measurement(liter)
# height – a continuous valued measurement(inches) 
# gender – binary(female: 0, male: 1)
# smoking status – binary(non-smoker: 0, smoker: 1) 
# weight – a continuous valued measurement(kg)

# Exercise 1: 
# - Divide data into smokers and non-smokers
# - Calculate the mean FEV1 score for both group

smoking_data = np.loadtxt('smoking.txt', delimiter="\t")

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

# Exercise 2

data = [smokers[:,1], nonsmokers[:,1]]
labels = ['Smokers', 'Non-smokers']

dark_background = '#1C2024'

fig, ax = plt.subplots()
fig.patch.set_facecolor(dark_background)
ax.set_facecolor(dark_background)

bplot = ax.boxplot(data,
                     vert=True,
                     patch_artist=True,
                     labels=labels,
                     boxprops=dict(facecolor='#1861CC', color='#FFFFFF'),
                     capprops=dict(color='#FFFFFF'),
                     whiskerprops=dict(color='#ffffff'),
                     flierprops=dict(markeredgecolor='#FFFFFF'),
                     medianprops=dict(color='#FFFFFF')
)

colors = ['#F2B134', '#4FB99F']


for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
    print(patch)
    # patch.style()

ax.set_ylabel('FEV1 score')
ax.set_title('FEV1 scores for smokers\nand non-smokers')

plt.subplots_adjust(top=0.85)
plt.grid(True, color='#444444')
plt.show()



