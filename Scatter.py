# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data into a pandas DataFrame. Using 'r' before the string handles backslashes correctly.
data = pd.read_csv(r'C:/Users/pc/Documents/Nitish093/ToyotaCorolla.csv')

# --- Box Plot ---
plt.title('Box Plot')

# Pass a list of the columns you want to plot to the boxplot function
plt.boxplot([data['Price'], data['HP'], data['KM']])

# Corrected function name from 'plt.xtictx' to 'plt.xticks' to set the x-axis tick labels
plt.xticks([1, 2, 3], ['Price', 'HP', 'KM'])

# Corrected function call from 'plt.show[]' to 'plt.show()'
plt.show()

# --- Scatter Plot ---
plt.title('Scatter Plot')

# Corrected function name from 'plt.Scatter' to 'plt.scatter' (case sensitive)
# Corrected column name typo from 'Prince' to 'Price'
plt.scatter(data['KM'], data['Price'])

plt.xlabel('KM')
plt.ylabel('Price')
plt.show()
