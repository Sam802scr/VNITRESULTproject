import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

plt.style.use('dark_background')

df = pd.read_csv('eee_CGPA.csv')

plt.hist(df['CGPA'],bins=15,color='orange',rwidth =0.95)

plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.title('Histogram Analysis of CGPA')
plt.xticks(np.arange(5,10,0.5))

plt.savefig('images/Histogram.png')