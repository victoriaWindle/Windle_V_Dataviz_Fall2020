import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
women = (41, 75, 123)
men = (66, 128, 192)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, men, bar_width,
alpha=opacity,
color='b',
label='Men')

rects2 = plt.bar(index + bar_width, women, bar_width,
alpha=opacity,
color='r',
label='Women')

plt.xlabel('Gender')
plt.ylabel('Medal Count')
plt.title('Medals for each Gender')
plt.xticks(index + bar_width, ('Bronze', 'Silver', 'Gold'))
plt.legend()

plt.tight_layout()
plt.show()


n_groups = 3
USA = (22, 64, 12)
Canada = (8, 15, 68)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, Canada, bar_width,
alpha=opacity,
color='r',
label='Canada')

rects2 = plt.bar(index + bar_width, USA, bar_width,
alpha=opacity,
color='b',
label='USA')

plt.xlabel('Country')
plt.ylabel('Medal Count')
plt.title('Count for each Country')
plt.xticks(index + bar_width, ('Bronze', 'Silver', 'Gold'))
plt.legend()

plt.tight_layout()
plt.show()


