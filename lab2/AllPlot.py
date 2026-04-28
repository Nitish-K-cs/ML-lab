# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:36:27 2026
@author: pc
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
data = pd.read_csv("C:/Users/pc/Documents/Nitish093/ToyotaCorolla.csv")

# Select columns
x = data['KM']
y = data['Weight']   # fixed case (Weight instead of weight)
z = data['Price']

# =========================
# 1. 3D Surface Plot (Triangular)
# =========================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x, y, z, cmap='jet')

ax.set_title("3D Surface Plot")
ax.set_xlabel("KM")
ax.set_ylabel("Weight")
ax.set_zlabel("Price")

plt.show()

# =========================
# 2. Scatter Plot
# =========================
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("KM")
plt.ylabel("Weight")
plt.show()

# =========================
# 3. Box Plot
# =========================
plt.boxplot(data.select_dtypes(include=np.number))
plt.title("Box Plot")
plt.show()

# =========================
# 4. Heatmap
# =========================
sns.heatmap(
    data[["Price", "KM", "Doors", "Weight"]].corr(),
    cmap="jet",
    annot=True
)

plt.title("Heatmap")
plt.show()

# =========================
# 5. Contour Plot (for scattered data)
# =========================
plt.tricontourf(x, y, z, levels=20, cmap="jet")
plt.colorbar(label="Price")

plt.xlabel("KM")
plt.ylabel("Weight")
plt.title("Contour Plot")

plt.show()

# =========================
# 6. Regular Contour + 3D Surface (synthetic grid)
# =========================
x1 = np.linspace(-5, 5, 50)
y1 = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x1, y1)
Z = np.sin(X**2 + Y**2)

# Contour
plt.contour(X, Y, Z)
plt.title("Contour Plot (Synthetic)")
plt.show()

# 3D Surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.title("3D Surface Plot (Synthetic)")
plt.show()
