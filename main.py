import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats
from decimal import *
from matplotlib import rcParams
import matplotlib.font_manager

rcParams['font.sans-serif'] = ['Arial']




print([f.name for f in matplotlib.font_manager.fontManager.afmlist])

getcontext().prec = 26
getcontext().Emin = -9999999999999

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

smokers_FEV1 = smokers[:,1]
nonsmokers_FEV1 = nonsmokers[:,1]

print('number of smoker FEV1 scores ' + str(len(smokers_FEV1)))
print('number of non-smoker FEV1 scores ' + str(len(nonsmokers_FEV1)))
 
smokers_avg_FEV1 = np.mean(smokers_FEV1)
nonsmokers_avg_FEV1 = np.mean(nonsmokers_FEV1)

print("Smokers' FEV1 score: ", str(smokers_avg_FEV1))
print("Non-smokers' FEV1 score: ", str(nonsmokers_avg_FEV1))

# Exercise 2

data = [smokers_FEV1, nonsmokers_FEV1]
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

ax.set_ylabel('FEV1 score')
ax.set_title('FEV1 scores for smokers\nand non-smokers')
ax.legend((bplot['boxes']), ('Smokers', 'Non-smokers'),
          fontsize='medium', loc=2, facecolor='#282D33')

plt.subplots_adjust(top=0.85)
plt.grid(True, color='#444444')


# Exercise 3

variance_smokers = smokers_FEV1.var(ddof=1)
variance_nonsmokers = nonsmokers_FEV1.var(ddof=1)
print(variance_smokers)
print(variance_nonsmokers)

standard_deviation = np.sqrt((variance_smokers + variance_nonsmokers)/2)

print(standard_deviation)

# t = (smokers_FEV1.mean() - nonsmokers_FEV1.mean())/(standard_deviation*np.sqrt(2/N))

alpha = 0.05

t, p = stats.ttest_ind(smokers_FEV1, nonsmokers_FEV1, equal_var=False)

print('t is: ', t)
print('p is: ', p)

if p < alpha:
  print('Null hypothesis is rejected. The likeliness of it being true is: ' + str(p*100) + '%')

if p > alpha:
  print('Null hypothesis is acceoted.')

smokers_x = smokers[:,0]
smokers_y = smokers[:, 1]

nonsmokers_x = nonsmokers[:, 0]
nonsmokers_y = nonsmokers[:, 1]

fig, ax = plt.subplots()
fig.patch.set_facecolor(dark_background)
ax.set_facecolor(dark_background)

ax.set_ylabel('FEV1 score')
ax.set_xlabel('Age')
ax.set_title('FEV1 scores among different agegroups')

ax.scatter(nonsmokers_x, nonsmokers_y, linewidths=0.25, alpha=0.5, c='#4FB99F')
ax.scatter(smokers_x, smokers_y, linewidths=0.25, alpha=0.5, c='#F2B134')
plt.grid(True, color='#444444')

plt.legend(('Non-smokers', 'Smokers'), facecolor='#282D33')

plt.show()
