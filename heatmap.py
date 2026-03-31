# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:36:27 2026

@author: pc
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("C:/Users/pc/Documents/Nitish093/ToyotaCorolla.csv")


x = data['KM']
y = data['Weight']
z = data['Price']

plt.tricontourf(x, y, z, levels=20, cmap="jet")
plt.colorbar(label="Price")

plt.xlabel("KM")
plt.ylabel("Weight")
plt.title("Contour Plot")

plt.show()

sns.heatmap(
    data[["Price", "KM", "Doors", "Weight"]].corr(),
    cmap="jet",
    annot=True
)

plt.title("Heatmap")
plt.show()

