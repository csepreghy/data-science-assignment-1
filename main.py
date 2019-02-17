import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from scipy import stats
from matplotlib import rcParams
import matplotlib.font_manager
import matplotlib.ticker as ticker

rcParams['font.sans-serif'] = ['Arial']

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

fig1, ax1 = plt.subplots()
fig1.patch.set_facecolor(dark_background)
ax1.set_facecolor(dark_background)

bplot = ax1.boxplot(data,
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

ax1.set_ylabel('FEV1 score')
ax1.set_title('FEV1 scores for smokers\nand non-smokers')
ax1.legend((bplot['boxes']), ('Smokers', 'Non-smokers'),
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

fig2, ax2 = plt.subplots()
fig2.patch.set_facecolor(dark_background)
ax2.set_facecolor(dark_background)

ax2.set_ylabel('FEV1 score')
ax2.set_xlabel('Age')
ax2.set_title('FEV1 scores among different agegroups')
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))

ax2.scatter(nonsmokers_x, nonsmokers_y, linewidths=0.25, alpha=0.5, c='#4FB99F')
ax2.scatter(smokers_x, smokers_y, linewidths=0.25, alpha=0.5, c='#F2B134')
ax2.grid(True, color='#444444')

ax2.legend(('Non-smokers', 'Smokers'), facecolor='#282D33')


# Exercise 5

fig3, ax3 = plt.subplots()
fig3.patch.set_facecolor(dark_background)
ax3.set_facecolor(dark_background)
ax3.grid(True, color='#444444')

ax3.hist(nonsmokers_x, int(np.max(nonsmokers_x) -
                           np.min(nonsmokers_x)), facecolor='#4FB99F')
ax3.hist(smokers_x, int(np.max(smokers_x) - np.min(smokers_x)), facecolor='#F2B134')
ax3.set_ylabel('Number of People')
ax3.set_xlabel('Age')
ax3.set_title('Numbeer of datapoints in different agegroups')
ax3.legend(('Non-smokers', 'Smokers'), facecolor='#282D33')
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))

plt.show()
