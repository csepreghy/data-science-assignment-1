import numpy as np

# data is the datamatrix of the smoking dataset, e.g. as obtained by data = numpy.loadtxt('smoking.txt')
# should return a tuple containing average FEV1 of smokers and nonsmokers 

def meanFEV1(smoking_data):
  smokers, nonsmokers = split_smoking_data(smoking_data)

  smokers_FEV1 = smokers[:, 1]
  nonsmokers_FEV1 = nonsmokers[:, 1]

  smokers_avg_FEV1 = np.mean(smokers_FEV1)
  nonsmokers_avg_FEV1 = np.mean(nonsmokers_FEV1)

  return smokers_avg_FEV1, nonsmokers_avg_FEV1, smokers_FEV1, nonsmokers_FEV1


def split_smoking_data(smoking_data):
  smokers = []
  nonsmokers = []

  for person in smoking_data:
    if person[4] == 0:
      nonsmokers.append(person)
    elif person[4] == 1:
      smokers.append(person)

  smokers = np.array(smokers)
  nonsmokers = np.array(nonsmokers)

  return smokers, nonsmokers
