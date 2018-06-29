import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 100)
year = ['2013.12', '2014.6', '2014.12', '2015.6', '2015.12', '2016.6', '2016.12', '2017.6', '2017.12', '2018.6']
fordY = [100, 101.7, 90, 88.68, 81, 80.4, 75.6, 66, 79.2, 69.6]
amazonY = [100, 82, 100, 109, 168.75, 175, 190, 250, 292, 410]
googleY = [100, 120, 104, 109, 150, 140, 160, 198, 215, 240]
pepsiY = [100, 112, 121, 117, 125, 127, 130, 114, 147, 126]
cardinalY = [100, 130, 132, 140, 141, 128, 118, 130, 100, 85]
disneyY = [100, 116, 124, 155, 140, 128, 140, 141, 149, 145]
adidasY = [100, 77, 61, 77, 99, 138, 165, 220, 187, 220]
interestY = [100, 102.4, 104.85, 107.37, 109.95, 112.58, 115, 118, 120.88, 123.78]

plt.plot(year, fordY, label='Ford')
plt.plot(year, amazonY, label='Amazon')
plt.plot(year, googleY, label='Google')
plt.plot(year, pepsiY, label='Pepsi')
plt.plot(year, cardinalY, label='Cardinal')
plt.plot(year, disneyY, label='Disney')
plt.plot(year, adidasY, label='Adidas')
plt.plot(year, interestY, 'k--', label='Commonweal Online 2.4% pa rate')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("If you put $100 in these companies, here what you'd have now")

plt.legend()

plt.show()
