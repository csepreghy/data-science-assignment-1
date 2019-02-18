import numpy as np

# data is the datamatrix of the smoking dataset, e.g. as obtained by data = numpy.loadtxt('smoking.txt')
# should return a tuple containing average FEV1 of smokers and nonsmokers 
def meanFEV1(data):
  smokers = []
  nonsmokers = []

  for person in data:
    if person[4] == 0:
      nonsmokers.append(person)
    elif person[4] == 1:
      smokers.append(person)


  smokers = np.array(smokers)
  nonsmokers = np.array(nonsmokers)

  smokers_FEV1 = smokers[:, 1]
  nonsmokers_FEV1 = nonsmokers[:, 1]

  print('number of smoker FEV1 scores ' + str(len(smokers_FEV1)))
  print('number of non-smoker FEV1 scores ' + str(len(nonsmokers_FEV1)))

  smokers_avg_FEV1 = np.mean(smokers_FEV1)
  nonsmokers_avg_FEV1 = np.mean(nonsmokers_FEV1)

  return smokers_avg_FEV1, nonsmokers_avg_FEV1
